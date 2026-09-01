#!/usr/bin/env python3
"""
Build the CloudDrove module catalog.

Scans every CloudDrove GitHub organisation, enumerates each Terraform module
repository *and its submodules*, enriches with Terraform Registry download
counts, and writes four artifacts:

    catalog.json   complete machine readable data
    llms.txt       compact index for LLMs (llmstxt.org convention)
    llms-full.txt  expanded index including every submodule
    MODULES.md     full human catalog

Only the standard library is used. Authentication comes from GITHUB_TOKEN.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

GITHUB_API = "https://api.github.com"
REGISTRY_API = "https://registry.terraform.io/v1/modules"

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB")

# Organisation -> (display name, provider slug used on the Terraform Registry).
# provider is None for collections that are not published as Terraform modules.
ORGS = [
    ("clouddrove", "AWS", "aws", "terraform-aws-"),
    ("terraform-az-modules", "Azure", "azurerm", "terraform-azurerm-"),
    ("terraform-gcloud-modules", "Google Cloud", "gcp", "terraform-gcp-"),
    ("terraform-do-modules", "DigitalOcean", "digitalocean", "terraform-digitalocean-"),
    ("terraform-hc-modules", "Hetzner Cloud", "hcloud", "terraform-hcloud-"),
    ("terraform-cf-modules", "Cloudflare", "cloudflare", "terraform-cloudflare-"),
]

# Non-Terraform collections, kept so this catalog is a superset of the old TOC.
EXTRA_COLLECTIONS = [
    ("clouddrove", "Ansible Roles", "ansible-"),
]


def api(url: str, retries: int = 3):
    """GET a JSON document, tolerating rate limits and transient failures."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "clouddrove-toc",
    }
    if TOKEN and "registry.terraform.io" not in url:
        headers["Authorization"] = f"Bearer {TOKEN}"

    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 429):  # rate limited
                reset = exc.headers.get("X-RateLimit-Reset")
                if reset and attempt < retries - 1:
                    wait = max(0, int(reset) - int(time.time())) + 2
                    print(f"  rate limited, sleeping {wait}s", file=sys.stderr)
                    time.sleep(min(wait, 120))
                    continue
            if exc.code in (404, 409):  # missing or empty repository
                return None
            if attempt == retries - 1:
                print(f"  HTTP {exc.code} for {url}", file=sys.stderr)
                return None
        except Exception as exc:  # noqa: BLE001 - network is best effort
            if attempt == retries - 1:
                print(f"  {type(exc).__name__} for {url}", file=sys.stderr)
                return None
        time.sleep(1 + attempt * 2)
    return None


def list_repos(org: str) -> list[dict]:
    repos, page = [], 1
    while True:
        batch = api(f"{GITHUB_API}/orgs/{org}/repos?per_page=100&page={page}")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return [r for r in repos if not r.get("archived") and not r.get("disabled")]


def submodules_of(org: str, repo: str, branch: str) -> list[str]:
    """Directory names under modules/ , which the registry exposes as submodules."""
    tree = api(f"{GITHUB_API}/repos/{org}/{repo}/git/trees/{branch}?recursive=1")
    if not tree or "tree" not in tree:
        return []
    found = set()
    for node in tree["tree"]:
        path = node.get("path", "")
        if path.startswith("modules/") and node.get("type") == "tree":
            parts = path.split("/")
            if len(parts) == 2 and parts[1] and parts[1] != "example":
                found.add(parts[1])
    return sorted(found)


def latest_release(org: str, repo: str) -> str | None:
    rel = api(f"{GITHUB_API}/repos/{org}/{repo}/releases/latest")
    if rel and rel.get("tag_name"):
        return rel["tag_name"]
    tags = api(f"{GITHUB_API}/repos/{org}/{repo}/tags?per_page=1")
    if tags:
        return tags[0].get("name")
    return None


def registry_index(namespace: str) -> dict[str, dict]:
    """Map module name -> registry record for one namespace."""
    out, offset = {}, 0
    while True:
        data = api(f"{REGISTRY_API}?namespace={namespace}&limit=100&offset={offset}")
        if not data or not data.get("modules"):
            break
        for m in data["modules"]:
            out[f"{m['name']}/{m['provider']}"] = m
        meta = data.get("meta", {})
        if "next_offset" not in meta:
            break
        offset = meta["next_offset"]
    return out


def registry_address(org: str, repo: str, prefix: str, provider: str) -> str | None:
    if not repo.startswith(prefix):
        return None
    return f"{org}/{repo[len(prefix):]}/{provider}"


def build() -> dict:
    catalog = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "clouds": [],
        "collections": [],
        "totals": {},
    }

    total_modules = total_submodules = total_downloads = 0

    for org, cloud, provider, prefix in ORGS:
        print(f"scanning {org} ...", file=sys.stderr)
        repos = [r for r in list_repos(org) if r["name"].startswith(prefix)]
        reg = registry_index(org)

        def enrich(repo: dict) -> dict:
            name = repo["name"]
            subs = submodules_of(org, name, repo.get("default_branch") or "main")
            addr = registry_address(org, name, prefix, provider)
            key = f"{name[len(prefix):]}/{provider}" if name.startswith(prefix) else None
            rec = reg.get(key) if key else None
            return {
                "repo": name,
                "name": name[len(prefix):],
                "url": repo["html_url"],
                "description": (repo.get("description") or "").strip(),
                "registry": addr,
                "registry_url": f"https://registry.terraform.io/modules/{addr}" if addr else None,
                "published": bool(rec),
                "version": (rec or {}).get("version") or latest_release(org, name),
                "downloads": (rec or {}).get("downloads", 0),
                "stars": repo.get("stargazers_count", 0),
                "forks": repo.get("forks_count", 0),
                "topics": repo.get("topics", []),
                "submodules": [
                    {
                        "name": s,
                        "source": f"{addr}//modules/{s}" if addr else None,
                        "url": f"{repo['html_url']}/tree/{repo.get('default_branch') or 'main'}/modules/{s}",
                    }
                    for s in subs
                ],
            }

        with ThreadPoolExecutor(max_workers=8) as pool:
            modules = list(pool.map(enrich, repos))

        modules.sort(key=lambda m: (-m["downloads"], m["name"]))
        subs = sum(len(m["submodules"]) for m in modules)
        dls = sum(m["downloads"] for m in modules)
        total_modules += len(modules)
        total_submodules += subs
        total_downloads += dls

        catalog["clouds"].append(
            {
                "cloud": cloud,
                "org": org,
                "org_url": f"https://github.com/{org}",
                "provider": provider,
                "repo_prefix": prefix,
                "module_count": len(modules),
                "submodule_count": subs,
                "downloads": dls,
                "modules": modules,
            }
        )

    for org, label, prefix in EXTRA_COLLECTIONS:
        print(f"scanning {org} for {label} ...", file=sys.stderr)
        repos = [r for r in list_repos(org) if r["name"].startswith(prefix)]
        items = sorted(
            (
                {
                    "repo": r["name"],
                    "name": r["name"][len(prefix):],
                    "url": r["html_url"],
                    "description": (r.get("description") or "").strip(),
                    "stars": r.get("stargazers_count", 0),
                }
                for r in repos
            ),
            key=lambda x: x["name"],
        )
        catalog["collections"].append(
            {"label": label, "org": org, "count": len(items), "items": items}
        )

    catalog["totals"] = {
        "clouds": len(catalog["clouds"]),
        "modules": total_modules,
        "submodules": total_submodules,
        "addressable_units": total_modules + total_submodules,
        "registry_downloads": total_downloads,
        "collections": sum(c["count"] for c in catalog["collections"]),
    }
    return catalog


# --------------------------------------------------------------------------
# Renderers
# --------------------------------------------------------------------------

def num(n: int) -> str:
    return f"{n:,}"


def render_modules_md(cat: dict) -> str:
    t = cat["totals"]
    out = [
        "# CloudDrove Module Catalog",
        "",
        f"Every Terraform module CloudDrove maintains, across {t['clouds']} clouds, "
        f"including every submodule.",
        "",
        f"**{num(t['modules'])} modules** and **{num(t['submodules'])} submodules** "
        f"= **{num(t['addressable_units'])} addressable units**. "
        f"{num(t['registry_downloads'])} Terraform Registry downloads.",
        "",
        f"Generated {cat['generated_at']} by `scripts/generate_catalog.py`. Do not edit by hand.",
        "",
        "## Summary",
        "",
        "| Cloud | Organisation | Modules | Submodules | Registry downloads |",
        "|-------|--------------|--------:|-----------:|-------------------:|",
    ]
    for c in cat["clouds"]:
        out.append(
            f"| {c['cloud']} | [{c['org']}]({c['org_url']}) | {num(c['module_count'])} "
            f"| {num(c['submodule_count'])} | {num(c['downloads'])} |"
        )
    out.append(
        f"| **Total** | | **{num(t['modules'])}** | **{num(t['submodules'])}** "
        f"| **{num(t['registry_downloads'])}** |"
    )
    out.append("")

    for c in cat["clouds"]:
        out += [
            f"## {c['cloud']}",
            "",
            f"Organisation [{c['org']}]({c['org_url']}) - provider `{c['provider']}` - "
            f"{num(c['module_count'])} modules, {num(c['submodule_count'])} submodules.",
            "",
        ]
        if not c["modules"]:
            out += ["_No modules yet._", ""]
            continue
        out += [
            "| Module | Source | Version | Downloads | Submodules |",
            "|--------|--------|---------|----------:|------------|",
        ]
        for m in c["modules"]:
            src = f"`{m['registry']}`" if m["published"] else "_unpublished_"
            subs = ", ".join(f"`{s['name']}`" for s in m["submodules"]) or "-"
            ver = m["version"] or "-"
            out.append(
                f"| [{m['name']}]({m['url']}) | {src} | {ver} "
                f"| {num(m['downloads'])} | {subs} |"
            )
        out.append("")

    for coll in cat["collections"]:
        out += [f"## {coll['label']}", "", f"{coll['count']} repositories.", "",
                "| Name | Description |", "|------|-------------|"]
        for i in coll["items"]:
            out.append(f"| [{i['name']}]({i['url']}) | {i['description']} |")
        out.append("")

    return "\n".join(out)


def render_llms_txt(cat: dict) -> str:
    """Compact index, llmstxt.org convention."""
    t = cat["totals"]
    out = [
        "# CloudDrove Terraform Modules",
        "",
        f"> {num(t['modules'])} open source Terraform modules and {num(t['submodules'])} "
        f"submodules maintained by CloudDrove across {t['clouds']} clouds "
        "(AWS, Azure, Google Cloud, DigitalOcean, Hetzner Cloud, Cloudflare). "
        "All are published on the Terraform Registry and usable by anyone.",
        "",
        "Modules are addressed as `<namespace>/<name>/<provider>`. Submodules use the "
        "double slash form `<namespace>/<name>/<provider>//modules/<submodule>`.",
        "",
        f"Generated {cat['generated_at']}.",
        "",
        "## Catalog",
        "",
        "- [Full catalog with every submodule](https://github.com/clouddrove/toc/blob/master/MODULES.md): human readable tables",
        "- [Machine readable catalog](https://github.com/clouddrove/toc/blob/master/catalog.json): complete JSON",
        "- [Expanded index](https://github.com/clouddrove/toc/blob/master/llms-full.txt): every module and submodule inline",
        "",
    ]
    for c in cat["clouds"]:
        if not c["modules"]:
            continue
        out.append(f"## {c['cloud']}")
        out.append("")
        for m in c["modules"]:
            desc = m["description"] or f"Terraform module for {m['name']}"
            n = len(m["submodules"])
            extra = f" ({n} submodule{'s' if n != 1 else ''})" if n else ""
            if m["published"]:
                out.append(f"- [{m['registry']}]({m['registry_url']}): {desc}{extra}")
            else:
                # Not on the registry yet: point at the repository so it is still usable.
                out.append(
                    f"- [{m['repo']}]({m['url']}): {desc}{extra} "
                    "[not yet on the Terraform Registry]"
                )
        out.append("")
    return "\n".join(out)


def render_llms_full_txt(cat: dict) -> str:
    """Expanded index: every module and every submodule as its own line."""
    t = cat["totals"]
    out = [
        "# CloudDrove Terraform Modules (full index)",
        "",
        f"> Every addressable Terraform module and submodule CloudDrove maintains: "
        f"{num(t['modules'])} modules and {num(t['submodules'])} submodules, "
        f"{num(t['addressable_units'])} total. Each line is a usable Terraform "
        "`source` value.",
        "",
        f"Generated {cat['generated_at']}.",
        "",
        "## Usage",
        "",
        "```hcl",
        'module "example" {',
        '  source  = "<source value from below>"',
        '  version = "<version from below>"',
        "}",
        "```",
        "",
    ]
    for c in cat["clouds"]:
        if not c["modules"]:
            continue
        out += [f"## {c['cloud']} ({c['org']})", ""]
        for m in c["modules"]:
            desc = m["description"] or f"Terraform module for {m['name']}"
            git_source = f"git::{m['url']}.git"
            out.append(f"### {m['registry'] or m['repo']}")
            out.append("")
            out.append(f"{desc}")
            out.append("")
            if m["published"]:
                out.append(f"- source: `{m['registry']}`")
                out.append(f"- version: `{m['version'] or 'unreleased'}`")
            else:
                out.append(f"- source: `{git_source}` (not yet on the Terraform Registry)")
                out.append(f"- version: `{m['version'] or 'unreleased'}`")
            out.append(f"- repository: {m['url']}")
            if m["submodules"]:
                out.append("- submodules:")
                for s in m["submodules"]:
                    src = s["source"] or f"{git_source}//modules/{s['name']}"
                    out.append(f"  - `{src}`")
            out.append("")
    return "\n".join(out)


def render_readme(cat: dict) -> str:
    """Front door. Shows the modules themselves, not just counts."""
    t = cat["totals"]
    out = [
        "<p align='center'>",
        "  <img width='1024' alt='CloudDrove Banner' "
        "src='https://clouddrove.s3.ca-central-1.amazonaws.com/Logo/banner.png' />",
        "</p>",
        "",
        "<h1 align='center'>TOC of All CloudDrove Modules</h1>",
        "",
        "<p align='center' style='font-size: 1.2rem;'>",
        "  This repo is a useful way to discover all "
        "<a href='https://clouddrove.com'>CloudDrove</a> developed and maintained modules,",
        "  across every cloud, including every submodule.",
        "</p>",
        "",
        "<p align='center'>",
        f"  <img src='https://img.shields.io/badge/modules-{t['modules']}-blue' alt='Modules' />",
        f"  <img src='https://img.shields.io/badge/submodules-{t['submodules']}-blue' alt='Submodules' />",
        f"  <img src='https://img.shields.io/badge/clouds-{t['clouds']}-blue' alt='Clouds' />",
        f"  <img src='https://img.shields.io/badge/downloads-{t['registry_downloads'] // 1000}k-brightgreen' alt='Downloads' />",
        "</p>",
        "",
        "<hr>",
        "",
        f"**{num(t['modules'])} modules** and **{num(t['submodules'])} submodules** across "
        f"**{t['clouds']} clouds**, which is **{num(t['addressable_units'])} separately "
        f"addressable Terraform sources**, with {num(t['registry_downloads'])} registry downloads.",
        "",
        "| Cloud | Organisation | Modules | Submodules | Downloads |",
        "|-------|--------------|--------:|-----------:|----------:|",
    ]
    for c in cat["clouds"]:
        anchor = c["cloud"].lower().replace(" ", "-")
        out.append(
            f"| [{c['cloud']}](#{anchor}) | [{c['org']}]({c['org_url']}) "
            f"| {num(c['module_count'])} | {num(c['submodule_count'])} | {num(c['downloads'])} |"
        )
    out += [
        f"| **Total** | | **{num(t['modules'])}** | **{num(t['submodules'])}** "
        f"| **{num(t['registry_downloads'])}** |",
        "",
        "For AI assistants: [llms.txt](llms.txt) (compact index), "
        "[llms-full.txt](llms-full.txt) (every source string), "
        "[catalog.json](catalog.json) (structured data).",
        "",
        "<hr>",
        "",
    ]

    for c in cat["clouds"]:
        out += [
            f"## {c['cloud']}",
            "",
            f"CloudDrove offers the below Terraform {c['cloud']} modules in "
            f"[{c['org']}]({c['org_url']}), provider `{c['provider']}`:",
            "",
        ]
        if not c["modules"]:
            out += ["_No modules yet._", "", "<hr>", ""]
            continue
        out += [
            "Sr No. | Module | Description | Source | Version | Submodules | Downloads | Star",
            "--- | --- | --- | --- | --- | --- | --- | ---",
        ]
        for i, m in enumerate(c["modules"], 1):
            desc = (m["description"] or "").replace("|", "/") or "-"
            src = f"`{m['registry']}`" if m["published"] else "_unpublished_"
            ver = (
                f"[{m['version']}]({m['url']}/releases)" if m["version"] else "-"
            )
            if m["submodules"]:
                subs = "<br>".join(f"`{s['name']}`" for s in m["submodules"])
            else:
                subs = "-"
            out.append(
                f"| {i}. | **[{m['repo']}]({m['url']})** | {desc} | {src} | {ver} "
                f"| {subs} | {num(m['downloads'])} | {m['stars'] or ''}"
            )
        out += ["", "<hr>", ""]

    for coll in cat["collections"]:
        out += [
            f"## {coll['label']}",
            "",
            f"CloudDrove offers the below {coll['label'].lower()} ({coll['count']}):",
            "",
            "Sr No. | Name | Description | Star",
            "--- | --- | --- | ---",
        ]
        for i, it in enumerate(coll["items"], 1):
            d = (it["description"] or "").replace("|", "/") or "-"
            out.append(f"| {i}. | **[{it['repo']}]({it['url']})** | {d} | {it['stars'] or ''}")
        out += ["", "<hr>", ""]

    out += [
        "## How this is built",
        "",
        "`scripts/generate_catalog.py` scans every CloudDrove organisation through the GitHub API, "
        "reads each repository tree to enumerate `modules/` submodules, and enriches with Terraform "
        "Registry download counts. It runs nightly through "
        "[`.github/workflows/catalog.yml`](.github/workflows/catalog.yml), using only the standard "
        "library and the built-in `GITHUB_TOKEN`.",
        "",
        "```bash",
        "GITHUB_TOKEN=$(gh auth token) python3 scripts/generate_catalog.py",
        "```",
        "",
        f"Generated {cat['generated_at']}. This file is generated, so do not edit it by hand.",
        "",
        "## Feedback",
        "",
        "Report issues or request modules on "
        "[clouddrove/toc](https://github.com/clouddrove/toc/issues), or write to "
        "[business@clouddrove.com](mailto:business@clouddrove.com).",
        "",
        "## About us",
        "",
        "At [CloudDrove](https://clouddrove.com), we build reliable, secure and cost efficient "
        "cloud native solutions. Join our "
        "[Slack community](https://www.launchpass.com/devops-talks).",
    ]
    return "\n".join(out)


def main() -> int:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cat = build()

    with open(os.path.join(root, "catalog.json"), "w") as fh:
        json.dump(cat, fh, indent=2, sort_keys=False)
        fh.write("\n")
    for name, body in (
        ("README.md", render_readme(cat)),
        ("llms.txt", render_llms_txt(cat)),
        ("llms-full.txt", render_llms_full_txt(cat)),
    ):
        with open(os.path.join(root, name), "w") as fh:
            fh.write(body.rstrip() + "\n")

    t = cat["totals"]
    print(
        f"wrote catalog: {t['modules']} modules, {t['submodules']} submodules, "
        f"{t['addressable_units']} addressable units, "
        f"{t['registry_downloads']:,} downloads",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
