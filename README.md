<h1 align='center'>TOC of All CloudDrove Packages and Tools</h1><p align='center' style='font-size: 1.2rem;''> This repo is a useful way to discover all <a href='https://clouddrove.com'>CloudDrove</a> developed and maintained repositories. It is mainly designed for clients of CloudDrove. </p>	<p align='center'>	<a href='https://facebook.com/sharer/sharer.php?u=https://github.com/clouddrove/toc'>	  <img title='Share on Facebook' src='https://user-images.githubusercontent.com/50652676/62817743-4f64cb80-bb59-11e9-90c7-b057252ded50.png' />	</a>	<a href='https://www.linkedin.com/shareArticle?mini=true&title=TOC+of+All+CloudDrove+Packages+and+Tools&url=https://github.com/clouddrove/toc'>	  <img title='Share on LinkedIn' src='https://user-images.githubusercontent.com/50652676/62817742-4e339e80-bb59-11e9-87b9-a1f68cae1049.png' />	</a>	<a href='https://twitter.com/intent/tweet/?text=TOC+of+All+CloudDrove+Packages+and+Tools&url=https://github.com/clouddrove/toc'>	  <img title='Share on Twitter' src='https://user-images.githubusercontent.com/50652676/62817740-4c69db00-bb59-11e9-8a79-3580fbbf6d5c.png' />	</a>	</p>	<hr>

## Terraform Packages

CloudDrove offers the below terraform modules:

1. **[terraform-github-users](https://github.com/clouddrove/terraform-github-users):** Terraform module to manage github users.
2. **[terraform-aws-production-access-role](https://github.com/clouddrove/terraform-aws-production-access-role):** This terraform module is used for creating an IAM Role which can give permission to another AWS account for accessing it's inventory.
3. **[terraform-aws-cross-account-role](https://github.com/clouddrove/terraform-aws-cross-account-role):** This terraform module is used to create an IAM Role to access another AWS account inventory.
4. **[terraform-aws-public-subnet](https://github.com/clouddrove/terraform-aws-public-subnet):** Terraform module for public subnets provisioning.
5. **[terraform-aws-ecr](https://github.com/clouddrove/terraform-aws-ecr):** This terraform module is used to create ECR on AWS.
6. **[terraform-aws-ebs-volume](https://github.com/clouddrove/terraform-aws-ebs-volume):** Terraform module to get EBS volume resource on AWS.
7. **[terraform-aws-elasticache](https://github.com/clouddrove/terraform-aws-elasticache):** Terraform module to create Elasticache Cluster and replica for Redis and Memcache.
8. **[terraform-aws-elasticache-redis-cluster](https://github.com/clouddrove/terraform-aws-elasticache-redis-cluster):** This terraform module creates Elasticache multiple replica for Redis on AWS.
9. **[terraform-digitalocean-k8s](https://github.com/clouddrove/terraform-digitalocean-k8s):** A terraform module for managing and creating a Kubernetes cluster on digital ocean.
10. **[terraform-aws-vpn](https://github.com/clouddrove/terraform-aws-vpn):** Terraform module is used to create VPN resource on AWS for network connectivity.
11. **[terraform-aws-cloudfront-cdn](https://github.com/clouddrove/terraform-aws-cloudfront-cdn):** Terraform module provisions CloudFront CDN resource on AWS.
12. **[terraform-aws-logging](https://github.com/clouddrove/terraform-aws-logging):** Terraform module to enable logging on AWS.
13. **[terraform-aws-nuke](https://github.com/clouddrove/terraform-aws-nuke):** This module is used to cleanup the AWS account inventory.
14. **[terraform-aws-sns](https://github.com/clouddrove/terraform-aws-sns):** Terraform module is used to setup SNS service to manage notifications on application.
15. **[terraform-aws-bastion](https://github.com/clouddrove/terraform-aws-bastion):** Terraform module to deploy bastion host on AWS.
16. **[terraform-aws-autoscaling](https://github.com/clouddrove/terraform-aws-autoscaling):** Terraform module to provision Auto Scaling Group and Launch Template on AWS.
17. **[terraform-aws-eks](https://github.com/clouddrove/terraform-aws-eks):** Terraform module will be created Autoscaling, Workers, EKS.
18. **[terraform-aws-transit-gateway](https://github.com/clouddrove/terraform-aws-transit-gateway):** Terraform module to create Transit gateway resource on AWS.
19. **[terraform-aws-vpn-transit-gateway](https://github.com/clouddrove/terraform-aws-vpn-transit-gateway):** Terraform module to create Transit gateway for VPN resource on AWS.
20. **[terraform-aws-consul](https://github.com/clouddrove/terraform-aws-consul):** Terraform module to create Consul server cluster on EC2.
21. **[terraform-aws-efs](https://github.com/clouddrove/terraform-aws-efs):** Terraform module to create or deploy EFS on AWS.
22. **[terraform-aws-elastic-beanstalk](https://github.com/clouddrove/terraform-aws-elastic-beanstalk):** Terraform module to deploy Elastic Beanstalk resource on AWS.
23. **[terraform-aws-iam-role](https://github.com/clouddrove/terraform-aws-iam-role):** Terraform module to create Iam role resource on AWS.
24. **[terraform-aws-baseline](https://github.com/clouddrove/terraform-aws-baseline):** Internal repo for testing terraform modules.
25. **[terraform-aws-s3](https://github.com/clouddrove/terraform-aws-s3):** Terraform module to create default S3 bucket with logging and encryption type specific features.
26. **[terraform-aws-acm](https://github.com/clouddrove/terraform-aws-acm):** This terraform module is used for requesting or importing SSL/TLS certificate with validation.
27. **[terraform-labels](https://github.com/clouddrove/terraform-labels):** This terraform module is designed to generate consistent label names and tags for resources. You can use terraform-labels to implement a strict naming convention.
28. **[terraform-aws-vpc](https://github.com/clouddrove/terraform-aws-vpc):** Terraform module to create VPC resource on AWS.
29. **[terraform-aws-subnet](https://github.com/clouddrove/terraform-aws-subnet):** Terraform module to create public, private and public-private subnet with network acl, route table, Elastic IP, nat gateway, flow log.
30. **[terraform-aws-keypair](https://github.com/clouddrove/terraform-aws-keypair):** Terraform module for generating or importing an SSH public key file into AWS.
31. **[terraform-aws-security-group](https://github.com/clouddrove/terraform-aws-security-group):** This terraform module creates set of Security Group and Security Group Rules resources in various combinations.
32. **[terraform-aws-ec2](https://github.com/clouddrove/terraform-aws-ec2):** Terraform module to create an EC2 resource on AWS with Elastic IP Addresses and Elastic Block Store.
33. **[terraform-aws-cloudtrail](https://github.com/clouddrove/terraform-aws-cloudtrail):** Terraform module to provision an AWS CloudTrail and an encrypted S3 bucket with versioning to store CloudTrail logs
34. **[terraform-aws-lambda](https://github.com/clouddrove/terraform-aws-lambda):**  Terraform module to create Lambda resource on AWS for create lambda function. 
35. **[terraform-aws-alb](https://github.com/clouddrove/terraform-aws-alb):** This terraform module is used to create ALB on AWS.
36. **[terraform-aws-kms](https://github.com/clouddrove/terraform-aws-kms):** This terraform module creates a KMS Customer Master Key (CMK) and its alias.
37. **[terraform-aws-aurora](https://github.com/clouddrove/terraform-aws-aurora):** Terraform module which creates RDS Aurora database resources on AWS and can create different type of databases. Currently it supports Postgres and MySQL.
38. **[terraform-aws-cloudwatch-alarms](https://github.com/clouddrove/terraform-aws-cloudwatch-alarms):** Terraform module creates Cloudwatch Alarm on AWS for monitoriing AWS services.
39. **[terraform-aws-ses](https://github.com/clouddrove/terraform-aws-ses):** Terraform module to create an SES Identity with SES IAM user on AWS.
40. **[terraform-aws-sqs](https://github.com/clouddrove/terraform-aws-sqs):** Terraform module to create SQS resource on AWS for managing queue.
41. **[terraform-aws-vpc-peering](https://github.com/clouddrove/terraform-aws-vpc-peering):** Terraform module to connect two VPC's on AWS.
42. **[terraform-aws-multi-account-peering](https://github.com/clouddrove/terraform-aws-multi-account-peering):** Terraform module to connect two VPC’s from different AWS account.
43. **[terraform-aws-sftp](https://github.com/clouddrove/terraform-aws-sftp):** This terraform module is used to create sftp on AWS for S3.
44. **[terraform-aws-route53](https://github.com/clouddrove/terraform-aws-route53):** Terraform module to create Route53 resource on AWS for zone and record set. 
45. **[terraform-aws-api-gateway](https://github.com/clouddrove/terraform-aws-api-gateway):** Terraform module to create Route53 resource on AWS for create api gateway with it's basic elements.
46. **[terraform-aws-elasticsearch](https://github.com/clouddrove/terraform-aws-elasticsearch):** Terraform module to create an Elasticsearch resource on AWS. 
47. **[terraform-aws-iam-user](https://github.com/clouddrove/terraform-aws-iam-user):** Terraform module to create Iam user resource on AWS.
48. **[terraform-aws-route53-record](https://github.com/clouddrove/terraform-aws-route53-record):** Terraform module to create Route53 table record set resource on AWS. 
49. **[terraform-aws-snapshot](https://github.com/clouddrove/terraform-aws-snapshot):** Terraform module to create Lambda resource on AWS for create and delete snapshot backups through lambda function.
50. **[terraform-aws-cloudwatch-event-rule](https://github.com/clouddrove/terraform-aws-cloudwatch-event-rule):** Terraform module to create cloudwatch event rule on AWS.
51. **[terraform-lambda-api-gateway](https://github.com/clouddrove/terraform-lambda-api-gateway):** Provides an HTTP Method Integration for an API Gateway Integration.
52. **[terraform-aws-cloudtrail-slack-notification](https://github.com/clouddrove/terraform-aws-cloudtrail-slack-notification):** Terraform module to create Lambda resource on AWS for sending notification when anything done from console in AWS. 
53. **[terraform-aws-lambda-proxy-api-gateway](https://github.com/clouddrove/terraform-aws-lambda-proxy-api-gateway):** Terraform module to create Api Gateway resource on AWS for trigger lambda function.
54. **[terraform-aws-route53-resolver](https://github.com/clouddrove/terraform-aws-route53-resolver):** Terraform module to create Route53 table record set resource on AWS.
55. **[terraform-aws-iam-baseline](https://github.com/clouddrove/terraform-aws-iam-baseline):** Terraform Module Create default IAM roles for managing AWS account.
56. **[terraform-aws-cloudtrail-baseline](https://github.com/clouddrove/terraform-aws-cloudtrail-baseline):** Terraform module to create an cloudtrail resource on AWS with S3 encryption with KMS key
57. **[terraform-aws-alarm](https://github.com/clouddrove/terraform-aws-alarm):** Terraform module to create an Cloudwatch Alarm.
58. **[terraform-aws-config-baseline](https://github.com/clouddrove/terraform-aws-config-baseline):** Terraform module to create an AWS Config resource on AWS with S3, IAM user, Recoder and Roles.
59. **[terraform-aws-secure-baseline](https://github.com/clouddrove/terraform-aws-secure-baseline):** Terraform module to create an Secure Basline, inclued module is alarm baseline, config baseline, and clouddtrail baseline.
60. **[terraform-aws-config](https://github.com/clouddrove/terraform-aws-config):** Provides an AWS Config Rule.
61. **[terraform-aws-snapshot-baseline](https://github.com/clouddrove/terraform-aws-snapshot-baseline):** Terraform module to create Lambda resource on AWS for creating backup and clear Snapshots and AMIs of instances in AWS.
62. **[terraform-digitalocean-ssh-key](https://github.com/clouddrove/terraform-digitalocean-ssh-key):** Provides a DigitalOcean SSH key resource to allow you to manage SSH keys for Droplet access.
63. **[terraform-digitalocean-labels](https://github.com/clouddrove/terraform-digitalocean-labels):**   This terraform module is designed to generate consistent label names and tags for resources. You can use terraform-labels to implement a strict naming convention.
64. **[terraform-digitalocean-vpc](https://github.com/clouddrove/terraform-digitalocean-vpc):**  VPCs are virtual networks containing resources that can communicate with each other in full isolation, using private IP addresses
65. **[terraform-digitalocean-droplet](https://github.com/clouddrove/terraform-digitalocean-droplet):** Provides a DigitalOcean Droplet resource. This can be used to create, modify, and delete Droplets.
66. **[terraform-digitalocean-firewall](https://github.com/clouddrove/terraform-digitalocean-firewall):** Provides a DigitalOcean Cloud Firewall resource. This can be used to create, modify, and delete Firewalls.
67. **[terraform-digitalocean-certificate](https://github.com/clouddrove/terraform-digitalocean-certificate):** Provides a DigitalOcean Certificate resource that allows you to manage certificates.
68. **[terraform-aws-guardduty](https://github.com/clouddrove/terraform-aws-guardduty):** Provides a resource to manage a GuardDuty member. To accept invitations in member accounts.
69. **[terraform-aws-aurora-serverless](https://github.com/clouddrove/terraform-aws-aurora-serverless):** Manages a RDS Aurora Cluster. 
70. **[terraform-aws-teevity](https://github.com/clouddrove/terraform-aws-teevity):** This terraform module is used for create needed resources like Iam user, S3 and others which used to connect AWS account with Teevity tool to monitor our bills.
71. **[terraform-aws-ecs](https://github.com/clouddrove/terraform-aws-ecs):** Terraform module to create ECS on AWS.
72. **[terraform-aws-inspector](https://github.com/clouddrove/terraform-aws-inspector):** Terraform module to create Inspector on AWS for monitoring instances.
73. **[terraform-digitalocean-cdn](https://github.com/clouddrove/terraform-digitalocean-cdn):** Provides a DigitalOcean CDN Endpoint resource for use with Spaces.
74. **[terraform-azure-virtual-network](https://github.com/clouddrove/terraform-azure-virtual-network):** This is Terraform Azure Virutal Network module.
75. **[terraform-azure-resource-group](https://github.com/clouddrove/terraform-azure-resource-group):** Terraform module for Azure resource group.
76. **[terraform-azure-labels](https://github.com/clouddrove/terraform-azure-labels):** Terraform module for Azure labels.
77. **[terraform-azure-subnet](https://github.com/clouddrove/terraform-azure-subnet):** Terraform module for Azure subnet.
78. **[terraform-azure-security-group](https://github.com/clouddrove/terraform-azure-security-group):** Terraform module for Azure security group.
79. **[terraform-aws-iam-access-analyzer](https://github.com/clouddrove/terraform-aws-iam-access-analyzer):** Terraform module to create IAM Access Analyzer on AWS for monitoring policies.
80. **[terraform-azure-virtual-machine](https://github.com/clouddrove/terraform-azure-virtual-machine):** Terraform module for Azure virtual machine.
81. **[terraform-cloud](https://github.com/clouddrove/terraform-cloud):** Terraform Cloud is an application that helps teams use Terraform together
82. **[terraform-aws-rabbitmq](https://github.com/clouddrove/terraform-aws-rabbitmq):** This terraform module is used to create RabbitMQ on AWS.
83. **[terraform-aws-alb-multi-targetgroup](https://github.com/clouddrove/terraform-aws-alb-multi-targetgroup):** Provides a Target Group resource for use with Load Balancer resources.
84. **[terraform-aws-waf-regional](https://github.com/clouddrove/terraform-aws-waf-regional):** This is terraform repository for AWS WAF (Web Application Firewall) Regional.
85. **[terraform-aws-slack-alerts](https://github.com/clouddrove/terraform-aws-slack-alerts):** Terraform module to setup tool for send slack alerts via sns for cloudwatch alarms, Elasticbeanstalk, elasticache, autoscaling and other things.

## Ansible Packages

CloudDrove offers the below ansible roles:

1. **[ansible-commands](https://github.com/clouddrove/ansible-commands):** This repository is used to understand how to use ansible commands.
2. **[ansible-role-docker](https://github.com/clouddrove/ansible-role-docker):** his ansible role install docker at Debian and Centos.
3. **[ansible-role-common](https://github.com/clouddrove/ansible-role-common):** This ansible role install common packages for Debian.
4. **[ansible-role-redis](https://github.com/clouddrove/ansible-role-redis):** This ansible role is used to install Redis server on Debian.
5. **[ansible-role-keys](https://github.com/clouddrove/ansible-role-keys):** Ansible role to manage keys.
6. **[ansible-role-php](https://github.com/clouddrove/ansible-role-php):** This ansible role is used to install PHP server on Debian.
7. **[ansible-role-jenkins-agent](https://github.com/clouddrove/ansible-role-jenkins-agent):** This ansible role is used to install Jenkins Agent on Debian.
8. **[ansible-role-docker-php](https://github.com/clouddrove/ansible-role-docker-php):** This ansible ro used to install PHP with docker on linux.
9. **[ansible-role-docker-nginx](https://github.com/clouddrove/ansible-role-docker-nginx):** This ansible role is used to install Nginx Server with docker on linux
10. **[ansible-role-docker-redis](https://github.com/clouddrove/ansible-role-docker-redis):** This ansible role is used to setup Redis server with docker on Debian.
11. **[ansible-role-docker-mysql](https://github.com/clouddrove/ansible-role-docker-mysql):** This ansible role is used for formation of MySQL server with docker on Debian.
12. **[ansible-role-mongo-cluster](https://github.com/clouddrove/ansible-role-mongo-cluster):** This ansible role is used to setup Mongo cluster on Debian.
13. **[ansible-role-docker-mongo-cluster](https://github.com/clouddrove/ansible-role-docker-mongo-cluster):** This ansible role is used to setup Mongo cluster with docker on Debian.
14. **[ansible-role-solr](https://github.com/clouddrove/ansible-role-solr):** Ansible role to run setup solr  using docker.
15. **[ansible-role-logz-io](https://github.com/clouddrove/ansible-role-logz-io):** This ansible role is used to install logz.io tool dependency on Debian.
16. **[ansible-role-nginx](https://github.com/clouddrove/ansible-role-nginx):** This ansible role is used to install Nginx Server on linux.
17. **[ansible-role-mount-efs](https://github.com/clouddrove/ansible-role-mount-efs):** This ansible role is used for installing & Mounting AWS EFS on Debian.
18. **[ansible-role-user](https://github.com/clouddrove/ansible-role-user):** This ansible role is used to create users on server.
19. **[ansible-role-redash](https://github.com/clouddrove/ansible-role-redash):** This ansible role is used for the installation of Redash tool on Debian.
20. **[ansible-role-gitlab-runner](https://github.com/clouddrove/ansible-role-gitlab-runner):** ansible role is used for installing gitlab runner.
21. **[ansible-role-docker-superset](https://github.com/clouddrove/ansible-role-docker-superset):** This ansible role is used for installing Superset tool with docker on Debian.
22. **[ansible-role-docker-metabase](https://github.com/clouddrove/ansible-role-docker-metabase):** This ansible role is used for installing Metabase tool with docker on Debian.
23. **[ansible-role-docker-compose](https://github.com/clouddrove/ansible-role-docker-compose):** This ansible role is used to install docker-compose on linux
24. **[ansible-role-mysql](https://github.com/clouddrove/ansible-role-mysql):** This ansible role install mysql server for Debian.
25. **[ansible-role-docker-jenkins](https://github.com/clouddrove/ansible-role-docker-jenkins):** This ansible role is used to install Jenkins with docker on server.
26. **[ansible-role-slack-ssh-notifier](https://github.com/clouddrove/ansible-role-slack-ssh-notifier):** This ansible role is used to install Slack SSH notifier on server.
27. **[ansible-role-docker-caddy](https://github.com/clouddrove/ansible-role-docker-caddy):** This ansible role is used to install Caddy with docker on server.
28. **[ansible-role-docker-pritunl](https://github.com/clouddrove/ansible-role-docker-pritunl):** This ansible role is used to install Pritunl and Mongodb with docker on server. 
29. **[ansible-role-vault](https://github.com/clouddrove/ansible-role-vault):** Ansible role for setup Hashicorp Vault
30. **[ansible-role-docker-elasticsearch](https://github.com/clouddrove/ansible-role-docker-elasticsearch):**   This ansible role is used to install Elasticsearch Server with docker on linux.
31. **[ansible-role-docker-elastichq](https://github.com/clouddrove/ansible-role-docker-elastichq):** This ansible role is used to install Elastichq  with docker on linux
32. **[ansible-role-docker-wowza](https://github.com/clouddrove/ansible-role-docker-wowza):** This ansible role is used to install Wowza streaming engine with docker on linux.
33. **[ansible-role-docker-vault](https://github.com/clouddrove/ansible-role-docker-vault):** This ansible role is used to install vault  with docker on linux.
34. **[ansible-role-docker-rabbitmq](https://github.com/clouddrove/ansible-role-docker-rabbitmq):** This ansible role is used to setup rabbitmq with docker on Debian.
35. **[ansible-role-certbot](https://github.com/clouddrove/ansible-role-certbot):** This ansible role is used to install certbot SSL on linux.
36. **[ansible-role-k8s-common](https://github.com/clouddrove/ansible-role-k8s-common):** This ansible role is used to install k8s common.
37. **[ansible-role-wordpress](https://github.com/clouddrove/ansible-role-wordpress):** Automated Installation and Configuring Wordpress on Linux.
38. **[ansible-role-magento2](https://github.com/clouddrove/ansible-role-magento2):** Automated Installation and Configuring Magento2 on Linux.
39. **[ansible-role-docker-redis-node-exporter](https://github.com/clouddrove/ansible-role-docker-redis-node-exporter):** This ansible role is used to setup Redis node exporter with docker.
40. **[ansible-role-docker-elasticsearch-node-exporter](https://github.com/clouddrove/ansible-role-docker-elasticsearch-node-exporter):** This ansible role is used to setup Elasticsearch node exporter with docker.
41. **[ansible-role-docker-rabbitmq-node-exporter](https://github.com/clouddrove/ansible-role-docker-rabbitmq-node-exporter):** This ansible role is used to setup Rabbitmq node exporter with docker.
42. **[ansible-role-docker-monitoring](https://github.com/clouddrove/ansible-role-docker-monitoring):** This ansible role is used to install prometheus, grafana and alertmanager with docker on linux.
43. **[ansible-role-docker-nginx-node-exporter](https://github.com/clouddrove/ansible-role-docker-nginx-node-exporter):** This ansible role is used to setup Nginx node exporter with docker.
44. **[ansible-role-docker-basic-node-exporter](https://github.com/clouddrove/ansible-role-docker-basic-node-exporter):** This ansible role is used to setup Basic node exporter with docker.
45. **[ansible-role-docker-php-node-exporter](https://github.com/clouddrove/ansible-role-docker-php-node-exporter):** This ansible role is used to setup Php node exporter with docker.
46. **[ansible-role-docker-varnish](https://github.com/clouddrove/ansible-role-docker-varnish):** This ansible role is used to setup Varnish with docker.
47. **[ansible-role-docker-jenkins-node-exporter](https://github.com/clouddrove/ansible-role-docker-jenkins-node-exporter):** This ansible role is used to setup Jenkins node exporter with docker.
48. **[ansible-role-docker-exporter](https://github.com/clouddrove/ansible-role-docker-exporter):** This ansible role is used to setup Docker node exporter with docker.
49. **[ansible-role-docker-mysql-node-exporter](https://github.com/clouddrove/ansible-role-docker-mysql-node-exporter):** This ansible role is used to setup MySQL node exporter with docker.
50. **[ansible-role-docker-nginx-proxy](https://github.com/clouddrove/ansible-role-docker-nginx-proxy):** This ansible role is used to install Nginx Server with docker on linux.
51. **[ansible-role-aws-inspector-agent](https://github.com/clouddrove/ansible-role-aws-inspector-agent):** This ansible role is used to install ansible-role-aws-inspector-agent
52. **[ansible-role-apache-airflow](https://github.com/clouddrove/ansible-role-apache-airflow):** This ansible role is used to install ansible-role-apache-airflow
53. **[ansible-role-clamav](https://github.com/clouddrove/ansible-role-clamav):** This ansible role is used to install ansible-role-clamav
54. **[ansible-role-os-hardning](https://github.com/clouddrove/ansible-role-os-hardning):** This ansible role is used to install ansible-role-os-hardning
55. **[ansible-role-devops](https://github.com/clouddrove/ansible-role-devops):** This ansible role setup devops repo on jenkins.
56. **[ansible-role-newrelic](https://github.com/clouddrove/ansible-role-newrelic):** This ansible role is used to installansible-role-newrelic

## Docker Packages

CloudDrove offers the below docker packages:

1. **[docker-terraform](https://github.com/clouddrove/docker-terraform):** Running terraform using docker for better CI/CD.
2. **[docker-images](https://github.com/clouddrove/docker-images)**
3. **[docker-elasticsearch](https://github.com/clouddrove/docker-elasticsearch)**

## CloudDrove Internal Tools

CloudDrove offers the below internal tools:

1. **[genie](https://github.com/clouddrove/genie):** This repository is a collection of Makefiles to facilitate some task easily like dynamic readme, terraform and git related.
2. **[slack-ssh-notifier](https://github.com/clouddrove/slack-ssh-notifier):** This repository is used to send Slack notification when any user logged in on the server.
3. **[aladdin](https://github.com/clouddrove/aladdin):** This repository is a collection of packages which can be installed directly by a single command on Debian(Linux) and Darwin(Mac) bases.

## Feedback

If you come accross a bug or have any feedback, please log it in our [issue tracker](https://github.com/clouddrove/toc/issues), or feel free to drop us an email at [hello@clouddrove.com](mailto:hello@clouddrove.com).

If you have found it worth your time, go ahead and give us a * on [our GitHub](https://github.com/clouddrove/toc)!

## About us

At [CloudDrove](https://clouddrove.com), we offer expert guidance, implementation support and services to help organisations accelerate their journey to the cloud. Our services include docker and container orchestration, cloud migration and adoption, infrastructure automation, application modernisation and remediation, and performance engineering.

<p align='center'>We are <b> The Cloud Experts!</b></p><hr /><p align='center'>We ❤️  <a href='https://github.com/clouddrove'>Open Source</a> and you can check out <a href='https://github.com/clouddrove'>our other modules</a> to get help with your new Cloud ideas.</p>

