# CloudDrove Module Catalog

Every Terraform module CloudDrove maintains, across 6 clouds, including every submodule.

**160 modules** and **93 submodules** = **253 addressable units**. 3,971,558 Terraform Registry downloads.

Generated 2026-09-01T12:29:13Z by `scripts/generate_catalog.py`. Do not edit by hand.

## Summary

| Cloud | Organisation | Modules | Submodules | Registry downloads |
|-------|--------------|--------:|-----------:|-------------------:|
| AWS | [clouddrove](https://github.com/clouddrove) | 80 | 29 | 3,793,118 |
| Azure | [terraform-az-modules](https://github.com/terraform-az-modules) | 47 | 2 | 88,878 |
| Google Cloud | [terraform-gcloud-modules](https://github.com/terraform-gcloud-modules) | 3 | 0 | 0 |
| DigitalOcean | [terraform-do-modules](https://github.com/terraform-do-modules) | 17 | 0 | 89,193 |
| Hetzner Cloud | [terraform-hc-modules](https://github.com/terraform-hc-modules) | 7 | 16 | 369 |
| Cloudflare | [terraform-cf-modules](https://github.com/terraform-cf-modules) | 6 | 46 | 0 |
| **Total** | | **160** | **93** | **3,971,558** |

## AWS

Organisation [clouddrove](https://github.com/clouddrove) - provider `aws` - 80 modules, 29 submodules.

| Module | Source | Version | Downloads | Submodules |
|--------|--------|---------|----------:|------------|
| [labels](https://github.com/clouddrove/terraform-aws-labels) | `clouddrove/labels/aws` | 1.3.1 | 1,790,836 | - |
| [kms](https://github.com/clouddrove/terraform-aws-kms) | `clouddrove/kms/aws` | 1.3.4 | 798,988 | - |
| [api-gateway](https://github.com/clouddrove/terraform-aws-api-gateway) | `clouddrove/api-gateway/aws` | 1.6.1 | 85,397 | - |
| [iam-role](https://github.com/clouddrove/terraform-aws-iam-role) | `clouddrove/iam-role/aws` | 1.4.0 | 80,315 | `aws_github_oidc_role` |
| [route53-record](https://github.com/clouddrove/terraform-aws-route53-record) | `clouddrove/route53-record/aws` | 1.0.2 | 78,136 | - |
| [vpc](https://github.com/clouddrove/terraform-aws-vpc) | `clouddrove/vpc/aws` | 2.0.5 | 66,190 | - |
| [subnet](https://github.com/clouddrove/terraform-aws-subnet) | `clouddrove/subnet/aws` | 2.0.3 | 65,918 | - |
| [elasticache](https://github.com/clouddrove/terraform-aws-elasticache) | `clouddrove/elasticache/aws` | 2.1.4 | 60,477 | - |
| [security-group](https://github.com/clouddrove/terraform-aws-security-group) | `clouddrove/security-group/aws` | 2.0.3 | 55,326 | - |
| [ses](https://github.com/clouddrove/terraform-aws-ses) | `clouddrove/ses/aws` | 1.3.4 | 47,905 | - |
| [s3](https://github.com/clouddrove/terraform-aws-s3) | `clouddrove/s3/aws` | 2.0.1 | 41,113 | - |
| [cloudwatch-alarms](https://github.com/clouddrove/terraform-aws-cloudwatch-alarms) | `clouddrove/cloudwatch-alarms/aws` | 1.3.3 | 40,948 | - |
| [ec2](https://github.com/clouddrove/terraform-aws-ec2) | `clouddrove/ec2/aws` | 2.1.1 | 26,199 | - |
| [sns](https://github.com/clouddrove/terraform-aws-sns) | `clouddrove/sns/aws` | 1.3.1 | 25,590 | - |
| [lambda](https://github.com/clouddrove/terraform-aws-lambda) | `clouddrove/lambda/aws` | 1.3.3 | 23,952 | - |
| [acm](https://github.com/clouddrove/terraform-aws-acm) | `clouddrove/acm/aws` | 1.4.3 | 23,806 | - |
| [keypair](https://github.com/clouddrove/terraform-aws-keypair) | `clouddrove/keypair/aws` | 1.3.4 | 19,420 | - |
| [ecr](https://github.com/clouddrove/terraform-aws-ecr) | `clouddrove/ecr/aws` | 1.3.3 | 19,225 | - |
| [elasticsearch](https://github.com/clouddrove/terraform-aws-elasticsearch) | `clouddrove/elasticsearch/aws` | 1.0.2 | 18,610 | - |
| [eks](https://github.com/clouddrove/terraform-aws-eks) | `clouddrove/eks/aws` | 1.4.8 | 18,339 | - |
| [cross-account-role](https://github.com/clouddrove/terraform-aws-cross-account-role) | `clouddrove/cross-account-role/aws` | 0.15.1 | 17,938 | - |
| [cloudwatch-event-rule](https://github.com/clouddrove/terraform-aws-cloudwatch-event-rule) | `clouddrove/cloudwatch-event-rule/aws` | 1.0.3 | 17,668 | - |
| [route53](https://github.com/clouddrove/terraform-aws-route53) | `clouddrove/route53/aws` | 1.0.4 | 17,631 | - |
| [sftp](https://github.com/clouddrove/terraform-aws-sftp) | `clouddrove/sftp/aws` | 1.3.4 | 17,460 | - |
| [secrets-manager](https://github.com/clouddrove/terraform-aws-secrets-manager) | `clouddrove/secrets-manager/aws` | 2.0.1 | 17,386 | - |
| [cognito](https://github.com/clouddrove/terraform-aws-cognito) | `clouddrove/cognito/aws` | 1.0.2 | 15,470 | - |
| [client-vpn](https://github.com/clouddrove/terraform-aws-client-vpn) | `clouddrove/client-vpn/aws` | 1.0.10 | 15,421 | - |
| [alb](https://github.com/clouddrove/terraform-aws-alb) | `clouddrove/alb/aws` | 2.0.1 | 14,260 | - |
| [waf](https://github.com/clouddrove/terraform-aws-waf) | `clouddrove/waf/aws` | 2.1.3 | 13,902 | - |
| [cloudtrail](https://github.com/clouddrove/terraform-aws-cloudtrail) | `clouddrove/cloudtrail/aws` | 1.4.4 | 13,759 | - |
| [vpc-peering](https://github.com/clouddrove/terraform-aws-vpc-peering) | `clouddrove/vpc-peering/aws` | 1.3.1 | 13,094 | - |
| [sqs](https://github.com/clouddrove/terraform-aws-sqs) | `clouddrove/sqs/aws` | 1.3.1 | 13,040 | - |
| [aurora](https://github.com/clouddrove/terraform-aws-aurora) | `clouddrove/aurora/aws` | 2.0.0 | 12,693 | - |
| [iam-user](https://github.com/clouddrove/terraform-aws-iam-user) | `clouddrove/iam-user/aws` | 1.3.2 | 11,684 | - |
| [efs](https://github.com/clouddrove/terraform-aws-efs) | `clouddrove/efs/aws` | 2.0.1 | 10,370 | - |
| [eks-addons](https://github.com/clouddrove/terraform-aws-eks-addons) | `clouddrove/eks-addons/aws` | 0.4.0 | 9,831 | `irsa` |
| [dynamodb](https://github.com/clouddrove/terraform-aws-dynamodb) | `clouddrove/dynamodb/aws` | 1.0.2 | 9,252 | - |
| [cloudfront](https://github.com/clouddrove/terraform-aws-cloudfront) | `clouddrove/cloudfront/aws` | 1.2.0 | 9,138 | - |
| [multi-account-peering](https://github.com/clouddrove/terraform-aws-multi-account-peering) | `clouddrove/multi-account-peering/aws` | 1.1.1 | 9,055 | - |
| [transit-gateway](https://github.com/clouddrove/terraform-aws-transit-gateway) | `clouddrove/transit-gateway/aws` | 2.0.1 | 9,037 | - |
| [security-hub](https://github.com/clouddrove/terraform-aws-security-hub) | `clouddrove/security-hub/aws` | 1.0.3 | 8,712 | - |
| [vpn](https://github.com/clouddrove/terraform-aws-vpn) | `clouddrove/vpn/aws` | 2.0.1 | 8,276 | - |
| [ec2-autoscaling](https://github.com/clouddrove/terraform-aws-ec2-autoscaling) | `clouddrove/ec2-autoscaling/aws` | 1.5.0 | 7,939 | - |
| [lightsail](https://github.com/clouddrove/terraform-aws-lightsail) | `clouddrove/lightsail/aws` | 1.3.2 | 7,748 | - |
| [lambda-site-monitor](https://github.com/clouddrove/terraform-aws-lambda-site-monitor) | `clouddrove/lambda-site-monitor/aws` | 1.0.2 | 7,316 | - |
| [mysql](https://github.com/clouddrove/terraform-aws-mysql) | `clouddrove/mysql/aws` | 1.3.3 | 7,225 | - |
| [active-directory](https://github.com/clouddrove/terraform-aws-active-directory) | `clouddrove/active-directory/aws` | 1.0.4 | 6,948 | - |
| [macie](https://github.com/clouddrove/terraform-aws-macie) | `clouddrove/macie/aws` | 1.0.2 | 6,317 | - |
| [eventbridge](https://github.com/clouddrove/terraform-aws-eventbridge) | `clouddrove/eventbridge/aws` | 1.0.2 | 6,190 | - |
| [pritunl](https://github.com/clouddrove/terraform-aws-pritunl) | `clouddrove/pritunl/aws` | 1.3.1 | 6,101 | - |
| [mfa](https://github.com/clouddrove/terraform-aws-mfa) | `clouddrove/mfa/aws` | 1.0.2 | 6,040 | - |
| [secure-baseline](https://github.com/clouddrove/terraform-aws-secure-baseline) | `clouddrove/secure-baseline/aws` | 1.3.1 | 5,671 | `alarm`, `analyzer`, `cloudtrail`, `config`, `ebs`, `guardduty`, `iam`, `inspector`, `security_hub`, `shield` |
| [cloudwatch-dashboard](https://github.com/clouddrove/terraform-aws-cloudwatch-dashboard) | `clouddrove/cloudwatch-dashboard/aws` | 1.0.1 | 5,517 | - |
| [cloudtrail-slack-notification](https://github.com/clouddrove/terraform-aws-cloudtrail-slack-notification) | `clouddrove/cloudtrail-slack-notification/aws` | 1.0.2 | 4,673 | - |
| [documentdb](https://github.com/clouddrove/terraform-aws-documentdb) | `clouddrove/documentdb/aws` | 1.0.2 | 4,552 | - |
| [cost-billing-alarm](https://github.com/clouddrove/terraform-aws-cost-billing-alarm) | `clouddrove/cost-billing-alarm/aws` | 1.0.3 | 4,316 | - |
| [backup](https://github.com/clouddrove/terraform-aws-backup) | `clouddrove/backup/aws` | 1.3.2 | 3,942 | - |
| [cloudwatch-synthetics](https://github.com/clouddrove/terraform-aws-cloudwatch-synthetics) | `clouddrove/cloudwatch-synthetics/aws` | 1.3.2 | 3,613 | - |
| [amplify](https://github.com/clouddrove/terraform-aws-amplify) | `clouddrove/amplify/aws` | 1.4.2 | 3,448 | - |
| [workspace](https://github.com/clouddrove/terraform-aws-workspace) | `clouddrove/workspace/aws` | 1.0.2 | 3,301 | - |
| [iam](https://github.com/clouddrove/terraform-aws-iam) | `clouddrove/iam/aws` | 4.11.0 | 3,292 | `iam-account`, `iam-assumable-role`, `iam-assumable-role-with-oidc`, `iam-assumable-role-with-saml`, `iam-assumable-roles`, `iam-assumable-roles-with-saml`, `iam-eks-role`, `iam-group-with-assumable-roles-policy`, `iam-group-with-policies`, `iam-policy`, `iam-read-only-policy`, `iam-user` |
| [athena](https://github.com/clouddrove/terraform-aws-athena) | `clouddrove/athena/aws` | 1.0.1 | 3,290 | - |
| [lifecycle-manager](https://github.com/clouddrove/terraform-aws-lifecycle-manager) | `clouddrove/lifecycle-manager/aws` | 1.0.2 | 2,995 | - |
| [msk](https://github.com/clouddrove/terraform-aws-msk) | `clouddrove/msk/aws` | 1.3.0 | 2,698 | - |
| [control-tower](https://github.com/clouddrove/terraform-aws-control-tower) | `clouddrove/control-tower/aws` | 0.0.5 | 2,476 | - |
| [ecs](https://github.com/clouddrove/terraform-aws-ecs) | `clouddrove/ecs/aws` | 1.0.2 | 2,029 | `auto-scaling`, `ecs`, `service`, `task-definition` |
| [eks-lb-controller](https://github.com/clouddrove/terraform-aws-eks-lb-controller) | `clouddrove/eks-lb-controller/aws` | 0.5.1 | 1,457 | - |
| [cloudtrail-baseline](https://github.com/clouddrove/terraform-aws-cloudtrail-baseline) | `clouddrove/cloudtrail-baseline/aws` | 1.0.2 | 1,086 | - |
| [bastion](https://github.com/clouddrove/terraform-aws-bastion) | `clouddrove/bastion/aws` | 1.0.1 | 944 | - |
| [karpenter](https://github.com/clouddrove/terraform-aws-karpenter) | `clouddrove/karpenter/aws` | 1.0.2 | 179 | - |
| [health-notifier](https://github.com/clouddrove/terraform-aws-health-notifier) | `clouddrove/health-notifier/aws` | 0.0.1 | 25 | - |
| [global-accelerator](https://github.com/clouddrove/terraform-aws-global-accelerator) | `clouddrove/global-accelerator/aws` | 1.4.1 | 23 | - |
| [autoscaling](https://github.com/clouddrove/terraform-aws-autoscaling) | _unpublished_ | v1.0.0 | 0 | - |
| [bedrock](https://github.com/clouddrove/terraform-aws-bedrock) | _unpublished_ | v1.0.0 | 0 | - |
| [mq](https://github.com/clouddrove/terraform-aws-mq) | _unpublished_ | v0.0.3 | 0 | - |
| [redshift](https://github.com/clouddrove/terraform-aws-redshift) | _unpublished_ | v0.1.1 | 0 | - |
| [reference-architecture](https://github.com/clouddrove/terraform-aws-reference-architecture) | _unpublished_ | v1.0.0 | 0 | - |
| [s3-multiaccount-replication](https://github.com/clouddrove/terraform-aws-s3-multiaccount-replication) | _unpublished_ | v1.0.2 | 0 | - |
| [serverless-jenkins](https://github.com/clouddrove/terraform-aws-serverless-jenkins) | _unpublished_ | - | 0 | `jenkins_platform` |
| [sftp-workflow](https://github.com/clouddrove/terraform-aws-sftp-workflow) | _unpublished_ | v1.0.1 | 0 | - |

## Azure

Organisation [terraform-az-modules](https://github.com/terraform-az-modules) - provider `azurerm` - 47 modules, 2 submodules.

| Module | Source | Version | Downloads | Submodules |
|--------|--------|---------|----------:|------------|
| [tags](https://github.com/terraform-az-modules/terraform-azurerm-tags) | `terraform-az-modules/tags/azurerm` | 1.0.2 | 19,913 | - |
| [resource-group](https://github.com/terraform-az-modules/terraform-azurerm-resource-group) | `terraform-az-modules/resource-group/azurerm` | 1.0.4 | 14,341 | - |
| [vnet](https://github.com/terraform-az-modules/terraform-azurerm-vnet) | `terraform-az-modules/vnet/azurerm` | 1.0.4 | 11,495 | - |
| [subnet](https://github.com/terraform-az-modules/terraform-azurerm-subnet) | `terraform-az-modules/subnet/azurerm` | 1.0.3 | 10,114 | `nat_gateway`, `route_table` |
| [log-analytics](https://github.com/terraform-az-modules/terraform-azurerm-log-analytics) | `terraform-az-modules/log-analytics/azurerm` | 2.1.0 | 8,231 | - |
| [private-dns](https://github.com/terraform-az-modules/terraform-azurerm-private-dns) | `terraform-az-modules/private-dns/azurerm` | 1.0.8 | 6,384 | - |
| [key-vault](https://github.com/terraform-az-modules/terraform-azurerm-key-vault) | `terraform-az-modules/key-vault/azurerm` | 3.2.0 | 6,043 | - |
| [nsg](https://github.com/terraform-az-modules/terraform-azurerm-nsg) | `terraform-az-modules/nsg/azurerm` | 1.0.7 | 2,123 | - |
| [storage](https://github.com/terraform-az-modules/terraform-azurerm-storage) | `terraform-az-modules/storage/azurerm` | 4.0.0 | 1,424 | - |
| [aks](https://github.com/terraform-az-modules/terraform-azurerm-aks) | `terraform-az-modules/aks/azurerm` | 1.0.7 | 1,108 | - |
| [acr](https://github.com/terraform-az-modules/terraform-azurerm-acr) | `terraform-az-modules/acr/azurerm` | 4.0.1 | 1,041 | - |
| [application-insights](https://github.com/terraform-az-modules/terraform-azurerm-application-insights) | `terraform-az-modules/application-insights/azurerm` | 1.0.2 | 899 | - |
| [vnet-peering](https://github.com/terraform-az-modules/terraform-azurerm-vnet-peering) | `terraform-az-modules/vnet-peering/azurerm` | 2.0.0 | 854 | - |
| [virtual-machine](https://github.com/terraform-az-modules/terraform-azurerm-virtual-machine) | `terraform-az-modules/virtual-machine/azurerm` | 1.3.0 | 714 | - |
| [flexible-postgresql](https://github.com/terraform-az-modules/terraform-azurerm-flexible-postgresql) | `terraform-az-modules/flexible-postgresql/azurerm` | 1.0.7 | 687 | - |
| [cognitive](https://github.com/terraform-az-modules/terraform-azurerm-cognitive) | `terraform-az-modules/cognitive/azurerm` | 5.0.0 | 568 | - |
| [application-gateway](https://github.com/terraform-az-modules/terraform-azurerm-application-gateway) | `terraform-az-modules/application-gateway/azurerm` | 3.0.0 | 561 | - |
| [vpn](https://github.com/terraform-az-modules/terraform-azurerm-vpn) | `terraform-az-modules/vpn/azurerm` | 2.0.0 | 366 | - |
| [dns](https://github.com/terraform-az-modules/terraform-azurerm-dns) | `terraform-az-modules/dns/azurerm` | 1.0.1 | 363 | - |
| [waf](https://github.com/terraform-az-modules/terraform-azurerm-waf) | `terraform-az-modules/waf/azurerm` | 3.0.0 | 186 | - |
| [redis-cache](https://github.com/terraform-az-modules/terraform-azurerm-redis-cache) | `terraform-az-modules/redis-cache/azurerm` | 1.1.0 | 184 | - |
| [service-bus](https://github.com/terraform-az-modules/terraform-azurerm-service-bus) | `terraform-az-modules/service-bus/azurerm` | 2.0.0 | 145 | - |
| [communication-service](https://github.com/terraform-az-modules/terraform-azurerm-communication-service) | `terraform-az-modules/communication-service/azurerm` | 2.0.1 | 142 | - |
| [app-service](https://github.com/terraform-az-modules/terraform-azurerm-app-service) | `terraform-az-modules/app-service/azurerm` | 1.0.1 | 131 | - |
| [mssql-db](https://github.com/terraform-az-modules/terraform-azurerm-mssql-db) | `terraform-az-modules/mssql-db/azurerm` | 2.1.0 | 130 | - |
| [static-web-app](https://github.com/terraform-az-modules/terraform-azurerm-static-web-app) | `terraform-az-modules/static-web-app/azurerm` | 1.0.0 | 124 | - |
| [data-factory](https://github.com/terraform-az-modules/terraform-azurerm-data-factory) | `terraform-az-modules/data-factory/azurerm` | 3.1.0 | 102 | - |
| [load-balancer](https://github.com/terraform-az-modules/terraform-azurerm-load-balancer) | `terraform-az-modules/load-balancer/azurerm` | 4.0.0 | 92 | - |
| [databricks](https://github.com/terraform-az-modules/terraform-azurerm-databricks) | `terraform-az-modules/databricks/azurerm` | 1.0.5 | 67 | - |
| [vmss-agent](https://github.com/terraform-az-modules/terraform-azurerm-vmss-agent) | `terraform-az-modules/vmss-agent/azurerm` | 1.0.2 | 62 | - |
| [sql-managed-instance](https://github.com/terraform-az-modules/terraform-azurerm-sql-managed-instance) | `terraform-az-modules/sql-managed-instance/azurerm` | 3.0.0 | 57 | - |
| [private-dns-resolver](https://github.com/terraform-az-modules/terraform-azurerm-private-dns-resolver) | `terraform-az-modules/private-dns-resolver/azurerm` | 1.0.4 | 51 | - |
| [eventhub](https://github.com/terraform-az-modules/terraform-azurerm-eventhub) | `terraform-az-modules/eventhub/azurerm` | 3.1.0 | 42 | - |
| [firewall](https://github.com/terraform-az-modules/terraform-azurerm-firewall) | `terraform-az-modules/firewall/azurerm` | 1.0.1 | 32 | - |
| [sentinel](https://github.com/terraform-az-modules/terraform-azurerm-sentinel) | `terraform-az-modules/sentinel/azurerm` | 3.0.1 | 27 | - |
| [functions-app](https://github.com/terraform-az-modules/terraform-azurerm-functions-app) | `terraform-az-modules/functions-app/azurerm` | 2.0.0 | 21 | - |
| [logic-app](https://github.com/terraform-az-modules/terraform-azurerm-logic-app) | `terraform-az-modules/logic-app/azurerm` | 2.0.0 | 16 | - |
| [flexible-mysql](https://github.com/terraform-az-modules/terraform-azurerm-flexible-mysql) | `terraform-az-modules/flexible-mysql/azurerm` | 1.0.1 | 15 | - |
| [cosmos-db](https://github.com/terraform-az-modules/terraform-azurerm-cosmos-db) | `terraform-az-modules/cosmos-db/azurerm` | 2.0.1 | 12 | - |
| [service-principle](https://github.com/terraform-az-modules/terraform-azurerm-service-principle) | `terraform-az-modules/service-principle/azurerm` | 1.0.0 | 11 | - |
| [api-management](https://github.com/terraform-az-modules/terraform-azurerm-api-management) | _unpublished_ | - | 0 | - |
| [app-service-plan](https://github.com/terraform-az-modules/terraform-azurerm-app-service-plan) | _unpublished_ | - | 0 | - |
| [bastion](https://github.com/terraform-az-modules/terraform-azurerm-bastion) | _unpublished_ | - | 0 | - |
| [diagnostic-settings](https://github.com/terraform-az-modules/terraform-azurerm-diagnostic-settings) | _unpublished_ | - | 0 | - |
| [managed-devops-pool](https://github.com/terraform-az-modules/terraform-azurerm-managed-devops-pool) | _unpublished_ | - | 0 | - |
| [nat-gateway](https://github.com/terraform-az-modules/terraform-azurerm-nat-gateway) | _unpublished_ | - | 0 | - |
| [private-endpoint](https://github.com/terraform-az-modules/terraform-azurerm-private-endpoint) | _unpublished_ | - | 0 | - |

## Google Cloud

Organisation [terraform-gcloud-modules](https://github.com/terraform-gcloud-modules) - provider `gcp` - 3 modules, 0 submodules.

| Module | Source | Version | Downloads | Submodules |
|--------|--------|---------|----------:|------------|
| [labels](https://github.com/terraform-gcloud-modules/terraform-gcp-labels) | _unpublished_ | v0.0.1 | 0 | - |
| [subnet](https://github.com/terraform-gcloud-modules/terraform-gcp-subnet) | _unpublished_ | v0.0.1 | 0 | - |
| [vpc](https://github.com/terraform-gcloud-modules/terraform-gcp-vpc) | _unpublished_ | v0.0.1 | 0 | - |

## DigitalOcean

Organisation [terraform-do-modules](https://github.com/terraform-do-modules) - provider `digitalocean` - 17 modules, 0 submodules.

| Module | Source | Version | Downloads | Submodules |
|--------|--------|---------|----------:|------------|
| [labels](https://github.com/terraform-do-modules/terraform-digitalocean-labels) | `terraform-do-modules/labels/digitalocean` | 1.0.7 | 44,501 | - |
| [vpc](https://github.com/terraform-do-modules/terraform-digitalocean-vpc) | `terraform-do-modules/vpc/digitalocean` | 1.0.0 | 11,921 | - |
| [spaces](https://github.com/terraform-do-modules/terraform-digitalocean-spaces) | `terraform-do-modules/spaces/digitalocean` | 1.0.7 | 8,726 | - |
| [database](https://github.com/terraform-do-modules/terraform-digitalocean-database) | `terraform-do-modules/database/digitalocean` | 1.0.7 | 7,982 | - |
| [droplet](https://github.com/terraform-do-modules/terraform-digitalocean-droplet) | `terraform-do-modules/droplet/digitalocean` | 1.0.6 | 4,522 | - |
| [kubernetes](https://github.com/terraform-do-modules/terraform-digitalocean-kubernetes) | `terraform-do-modules/kubernetes/digitalocean` | 1.1.9 | 3,405 | - |
| [firewall](https://github.com/terraform-do-modules/terraform-digitalocean-firewall) | `terraform-do-modules/firewall/digitalocean` | 1.0.5 | 1,460 | - |
| [certificate](https://github.com/terraform-do-modules/terraform-digitalocean-certificate) | `terraform-do-modules/certificate/digitalocean` | 1.0.4 | 1,236 | - |
| [container-registry](https://github.com/terraform-do-modules/terraform-digitalocean-container-registry) | `terraform-do-modules/container-registry/digitalocean` | 1.0.7 | 1,136 | - |
| [domain](https://github.com/terraform-do-modules/terraform-digitalocean-domain) | `terraform-do-modules/domain/digitalocean` | 1.0.6 | 945 | - |
| [ssh-key](https://github.com/terraform-do-modules/terraform-digitalocean-ssh-key) | `terraform-do-modules/ssh-key/digitalocean` | 1.0.7 | 905 | - |
| [app](https://github.com/terraform-do-modules/terraform-digitalocean-app) | `terraform-do-modules/app/digitalocean` | 1.0.9 | 755 | - |
| [cdn](https://github.com/terraform-do-modules/terraform-digitalocean-cdn) | `terraform-do-modules/cdn/digitalocean` | 1.0.7 | 635 | - |
| [load-balancer](https://github.com/terraform-do-modules/terraform-digitalocean-load-balancer) | `terraform-do-modules/load-balancer/digitalocean` | 1.0.7 | 553 | - |
| [monitoring](https://github.com/terraform-do-modules/terraform-digitalocean-monitoring) | `terraform-do-modules/monitoring/digitalocean` | 1.0.5 | 511 | - |
| [components](https://github.com/terraform-do-modules/terraform-digitalocean-components) | _unpublished_ | v1.0.3 | 0 | - |
| [nfs](https://github.com/terraform-do-modules/terraform-digitalocean-nfs) | _unpublished_ | v1.0.2 | 0 | - |

## Hetzner Cloud

Organisation [terraform-hc-modules](https://github.com/terraform-hc-modules) - provider `hcloud` - 7 modules, 16 submodules.

| Module | Source | Version | Downloads | Submodules |
|--------|--------|---------|----------:|------------|
| [compute](https://github.com/terraform-hc-modules/terraform-hcloud-compute) | `terraform-hc-modules/compute/hcloud` | 0.3.1 | 97 | `placement-group`, `server`, `snapshot`, `ssh-key`, `volume` |
| [network](https://github.com/terraform-hc-modules/terraform-hcloud-network) | `terraform-hc-modules/network/hcloud` | 0.3.1 | 96 | `firewall`, `load-balancer`, `vpc` |
| [labels](https://github.com/terraform-hc-modules/terraform-hcloud-labels) | `terraform-hc-modules/labels/hcloud` | 0.3.5 | 56 | - |
| [certificate](https://github.com/terraform-hc-modules/terraform-hcloud-certificate) | `terraform-hc-modules/certificate/hcloud` | 0.3.0 | 34 | `managed`, `uploaded` |
| [ip](https://github.com/terraform-hc-modules/terraform-hcloud-ip) | `terraform-hc-modules/ip/hcloud` | 0.3.0 | 31 | `floating-ip`, `primary-ip`, `rdns` |
| [dns](https://github.com/terraform-hc-modules/terraform-hcloud-dns) | `terraform-hc-modules/dns/hcloud` | 0.4.0 | 30 | `records`, `zone` |
| [storage-box](https://github.com/terraform-hc-modules/terraform-hcloud-storage-box) | `terraform-hc-modules/storage-box/hcloud` | 1.1.0 | 25 | `storage-box` |

## Cloudflare

Organisation [terraform-cf-modules](https://github.com/terraform-cf-modules) - provider `cloudflare` - 6 modules, 46 submodules.

| Module | Source | Version | Downloads | Submodules |
|--------|--------|---------|----------:|------------|
| [account](https://github.com/terraform-cf-modules/terraform-cloudflare-account) | _unpublished_ | - | 0 | `api-token`, `dns-settings`, `logpush`, `member`, `notification`, `secrets-store`, `sharing` |
| [network](https://github.com/terraform-cf-modules/terraform-cloudflare-network) | _unpublished_ | - | 0 | `addressing`, `load-balancer`, `magic-transit`, `magic-wan`, `monitor`, `monitoring`, `pool`, `spectrum` |
| [security](https://github.com/terraform-cf-modules/terraform-cloudflare-security) | _unpublished_ | - | 0 | `api-shield`, `bot-management`, `firewall-legacy`, `list`, `page-shield`, `rate-limit`, `ruleset`, `turnstile` |
| [workers](https://github.com/terraform-cf-modules/terraform-cloudflare-workers) | _unpublished_ | - | 0 | `cron`, `d1`, `hyperdrive`, `kv`, `pages`, `queue`, `r2`, `route`, `script` |
| [zero-trust](https://github.com/terraform-cf-modules/terraform-cloudflare-zero-trust) | _unpublished_ | - | 0 | `access-app`, `access-policy`, `device-posture`, `dlp`, `gateway-policy`, `identity`, `service-token`, `tunnel` |
| [zone](https://github.com/terraform-cf-modules/terraform-cloudflare-zone) | _unpublished_ | - | 0 | `cache`, `custom-hostname`, `dns-record`, `dnssec`, `settings`, `ssl` |

## Ansible Roles

27 repositories.

| Name | Description |
|------|-------------|
| [commands](https://github.com/clouddrove/ansible-commands) | This repository is used to understand how to use ansible commands. |
| [role-certbot](https://github.com/clouddrove/ansible-role-certbot) | This ansible role is used to install certbot SSL on linux. |
| [role-common](https://github.com/clouddrove/ansible-role-common) | This ansible role install common packages for Debian. |
| [role-docker](https://github.com/clouddrove/ansible-role-docker) | his ansible role install docker at Debian and Centos. |
| [role-docker-basic-node-exporter](https://github.com/clouddrove/ansible-role-docker-basic-node-exporter) | This ansible role is used to setup Basic node exporter with docker. |
| [role-docker-caddy](https://github.com/clouddrove/ansible-role-docker-caddy) | This ansible role is used to install Caddy with docker on server. |
| [role-docker-elastichq](https://github.com/clouddrove/ansible-role-docker-elastichq) | This ansible role is used to install Elastichq  with docker on linux |
| [role-docker-elasticsearch](https://github.com/clouddrove/ansible-role-docker-elasticsearch) | This ansible role is used to install Elasticsearch Server with docker on linux. |
| [role-docker-elasticsearch-node-exporter](https://github.com/clouddrove/ansible-role-docker-elasticsearch-node-exporter) | This ansible role is used to setup Elasticsearch node exporter with docker. |
| [role-docker-jenkins](https://github.com/clouddrove/ansible-role-docker-jenkins) | This ansible role is used to install Jenkins with docker on server. |
| [role-docker-jenkins-node-exporter](https://github.com/clouddrove/ansible-role-docker-jenkins-node-exporter) | This ansible role is used to setup Jenkins node exporter with docker. |
| [role-docker-mysql-node-exporter](https://github.com/clouddrove/ansible-role-docker-mysql-node-exporter) | This ansible role is used to setup MySQL node exporter with docker. |
| [role-docker-nginx](https://github.com/clouddrove/ansible-role-docker-nginx) | This ansible role is used to install Nginx Server with docker on linux |
| [role-docker-nginx-node-exporter](https://github.com/clouddrove/ansible-role-docker-nginx-node-exporter) | This ansible role is used to setup Nginx node exporter with docker. |
| [role-docker-php](https://github.com/clouddrove/ansible-role-docker-php) | This ansible ro used to install PHP with docker on linux. |
| [role-docker-php-node-exporter](https://github.com/clouddrove/ansible-role-docker-php-node-exporter) | This ansible role is used to setup Php node exporter with docker. |
| [role-docker-pritunl](https://github.com/clouddrove/ansible-role-docker-pritunl) | This ansible role is used to install Pritunl and Mongodb with docker on server. |
| [role-docker-rabbitmq-node-exporter](https://github.com/clouddrove/ansible-role-docker-rabbitmq-node-exporter) | This ansible role is used to setup Rabbitmq node exporter with docker. |
| [role-docker-redis](https://github.com/clouddrove/ansible-role-docker-redis) | This ansible role is used to setup Redis server with docker on Debian. |
| [role-docker-redis-node-exporter](https://github.com/clouddrove/ansible-role-docker-redis-node-exporter) | This ansible role is used to setup Redis node exporter with docker. |
| [role-mount-efs](https://github.com/clouddrove/ansible-role-mount-efs) | This ansible role is used for installing & Mounting AWS EFS on Debian. |
| [role-mysql](https://github.com/clouddrove/ansible-role-mysql) | This ansible role install mysql server for Debian. |
| [role-nginx](https://github.com/clouddrove/ansible-role-nginx) | This ansible role is used to install Nginx Server on linux. |
| [role-php](https://github.com/clouddrove/ansible-role-php) | This ansible role is used to install PHP server on Debian. |
| [role-s3-sftp](https://github.com/clouddrove/ansible-role-s3-sftp) | This Ansible role sets up SFTP with S3 Bucket. |
| [role-slack-ssh-notifier](https://github.com/clouddrove/ansible-role-slack-ssh-notifier) | This ansible role is used to install Slack SSH notifier on server. |
| [role-user](https://github.com/clouddrove/ansible-role-user) | This ansible role is used to create users on server. |
