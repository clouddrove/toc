package main

import (
	"context"
	"fmt"
	"bytes"
	"strings"
	"strconv"
	"io/ioutil"
	"github.com/google/go-github/github"
	"golang.org/x/oauth2"
)

func fetchAllUserMigrations() ([]*github.Repository) {
	ctx := context.Background()
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: "875bc57877f615dd985481c9ffe7f1148b7ee14e"},
	)
	tc := oauth2.NewClient(ctx, ts)
	client := github.NewClient(tc)
	var allRepos []*github.Repository
	opt := &github.RepositoryListByOrgOptions{
		ListOptions: github.ListOptions{PerPage: 50},
		Type: "all",
	}
	for {
		repos, resp, err := client.Repositories.ListByOrg(ctx, "clouddrove", opt)
		if err != nil {
		}
		allRepos = append(allRepos, repos...)
		if resp.NextPage == 0 {
			break
		}
		opt.Page = resp.NextPage
	}
	return allRepos
}

func main() {
	var buffer bytes.Buffer
	migrations := fetchAllUserMigrations()
	buffer.WriteString("# TOC of All Clouddrove Packages and Tools\n\n")
	buffer.WriteString("This repo is a useful way to discover all [Clouddrove](https://clouddrove.com) developed and maintained repositories. It is mainly designed for clients of Clouddrove.\n\n")
	var terraform_packages = "" 
	var ansible_packages = "" 
	var tool_packages = "" 
	var terraform_num = 1 
	var ansible_num = 1 
	var tool_num = 1 
	for _, m := range migrations {
		if(strings.HasPrefix(m.GetName(), "terraform-")){
			terraform_packages = terraform_packages + strconv.Itoa(terraform_num) + ". **["+m.GetName()+"]("+m.GetHTMLURL()+")"
			if(m.GetDescription() != ""){
				terraform_packages = terraform_packages + ":** "+m.GetDescription()+"\n"
			} else{
				terraform_packages = terraform_packages + "**\n"
			}
			terraform_num = terraform_num + 1
		} else if(strings.HasPrefix(m.GetName(), "ansible-")){
			ansible_packages = ansible_packages + strconv.Itoa(ansible_num) + ". **["+m.GetName()+"]("+m.GetHTMLURL()+")"
			if(m.GetDescription() != ""){
				ansible_packages = ansible_packages + ":** "+m.GetDescription()+"\n"
			} else{
				ansible_packages = ansible_packages + "**\n"
			}
			ansible_num = ansible_num + 1
		} else if(m.GetName() == "genie" || m.GetName() == "aladdin" || m.GetName() == "slack-ssh-notifier"){
			tool_packages = tool_packages + strconv.Itoa(tool_num) + ". **["+m.GetName()+"]("+m.GetHTMLURL()+")"
			if(m.GetDescription() != ""){
				tool_packages = tool_packages + ":** "+m.GetDescription()+"\n"
			} else{
				tool_packages = tool_packages + "**\n"
			}
			tool_num = tool_num + 1
		}
	}
	if(terraform_packages != ""){
		buffer.WriteString(fmt.Sprintf("## Terraform Packages\n\nThese are the Terraform packages which currently Clouddrove have\n\n%s\n",terraform_packages))
	}
	if(ansible_packages != ""){
		buffer.WriteString(fmt.Sprintf("## Ansible Packages\n\nThese are the Ansible packages which currently Clouddrove have\n\n%s\n",ansible_packages))
	}
	if(tool_packages != ""){
		buffer.WriteString(fmt.Sprintf("## Clouddrove Internal Tools\n\nThese are some internal tools which currently Clouddrove have\n\n%s\n",tool_packages))
	}
	err := ioutil.WriteFile("README.md", buffer.Bytes(), 0644)
	if(err != nil){
		fmt.Println(err)
	}
}