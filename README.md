<p align='center'>
  <img width='1000' alt='CloudDrove Banner' src='https://clouddrove.s3.ca-central-1.amazonaws.com/img/clouddrove-github-cover.png' />
</p>

<h1 align='center'>CloudDrove Module Catalog</h1>
<p align='center'><em>Every open source Terraform module CloudDrove maintains, in one index, for humans and for AI.</em></p>

<p align='center'>
  <img src='https://img.shields.io/badge/modules-207-blue' alt='Modules' />
  <img src='https://img.shields.io/badge/submodules-93-blue' alt='Submodules' />
  <img src='https://img.shields.io/badge/clouds-6-blue' alt='Clouds' />
  <img src='https://img.shields.io/badge/registry%20downloads-3971k-brightgreen' alt='Downloads' />
</p>

---

## At a glance

**207 modules** and **93 submodules** across **6 clouds**, which is **300 separately addressable Terraform sources**. 3,971,558 Terraform Registry downloads to date.

| Cloud | Organisation | Modules | Submodules | Registry downloads |
|-------|--------------|--------:|-----------:|-------------------:|
| AWS | [clouddrove](https://github.com/clouddrove) | 105 | 29 | 3,793,118 |
| Azure | [terraform-az-modules](https://github.com/terraform-az-modules) | 50 | 2 | 88,878 |
| Google Cloud | [terraform-gcloud-modules](https://github.com/terraform-gcloud-modules) | 22 | 0 | 0 |
| DigitalOcean | [terraform-do-modules](https://github.com/terraform-do-modules) | 17 | 0 | 89,193 |
| Hetzner Cloud | [terraform-hc-modules](https://github.com/terraform-hc-modules) | 7 | 16 | 369 |
| Cloudflare | [terraform-cf-modules](https://github.com/terraform-cf-modules) | 6 | 46 | 0 |
| **Total** | | **207** | **93** | **3,971,558** |

Submodules are not extras. They are separately addressable modules published from the same repository, so the real surface area is the addressable-units number, not the repository count.

---

## Where to look

| You are | Read this |
|---------|-----------|
| A human browsing | **[MODULES.md](MODULES.md)** - full tables, every module and submodule |
| An AI assistant | **[llms.txt](llms.txt)** - compact index, [llms-full.txt](llms-full.txt) - every source string |
| A script or tool | **[catalog.json](catalog.json)** - complete structured data |

---

## For AI assistants

This repository follows the [llms.txt](https://llmstxt.org/) convention.

- [`llms.txt`](llms.txt) is the compact index: one line per module with its registry address.
- [`llms-full.txt`](llms-full.txt) expands every module *and every submodule* into a usable Terraform `source` string.
- [`catalog.json`](catalog.json) is the same data structured, with download counts, versions, stars and topics.

Module addresses take the form `<namespace>/<name>/<provider>`. Submodules use the double slash form:

```hcl
module "kv" {
  source  = "terraform-cf-modules/workers/cloudflare//modules/kv"
  version = "~> 0.1"
}
```

---

## Organisations

| Cloud | Organisation | Provider |
|-------|--------------|----------|
| AWS | [clouddrove](https://github.com/clouddrove) | `aws` |
| Azure | [terraform-az-modules](https://github.com/terraform-az-modules) | `azurerm` |
| Google Cloud | [terraform-gcloud-modules](https://github.com/terraform-gcloud-modules) | `gcp` |
| DigitalOcean | [terraform-do-modules](https://github.com/terraform-do-modules) | `digitalocean` |
| Hetzner Cloud | [terraform-hc-modules](https://github.com/terraform-hc-modules) | `hcloud` |
| Cloudflare | [terraform-cf-modules](https://github.com/terraform-cf-modules) | `cloudflare` |

---

## How this is built

`scripts/generate_catalog.py` scans every organisation through the GitHub API, reads each repository tree to enumerate `modules/` submodules, enriches with Terraform Registry download counts, and writes all four artifacts. It runs nightly through [`.github/workflows/catalog.yml`](.github/workflows/catalog.yml) and uses only the standard library and the built-in `GITHUB_TOKEN`.

Run it yourself:

```bash
GITHUB_TOKEN=$(gh auth token) python3 scripts/generate_catalog.py
```

Generated 2026-09-01T12:26:22Z. Every file in this repository except the script and the workflow is generated, so do not edit them by hand.

---

## Feedback

Open an issue on [clouddrove/toc](https://github.com/clouddrove/toc/issues), or reach us at [business@clouddrove.com](mailto:business@clouddrove.com).

Maintained by [CloudDrove](https://clouddrove.com).
