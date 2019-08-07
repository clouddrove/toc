# TOC of All CloudDrove Packages and Tools

This repo is a useful way to discover all [CloudDrove](https://clouddrove.com) developed and maintained repositories. It is mainly designed for clients of CloudDrove.

## Terraform Packages

CloudDrove offers the below terraform modules:

1. **[terraform-github-users](https://github.com/clouddrove/terraform-github-users):** Terraform module to manage github users 
2. **[terraform-aws-vpc](https://github.com/clouddrove/terraform-aws-vpc):** Terraform module to create VPC resource on AWS.
3. **[terraform-aws-acm](https://github.com/clouddrove/terraform-aws-acm):** This terraform module is used for requesting or importing SSL/TLS certificate with validation.
4. **[terraform-aws-keypair](https://github.com/clouddrove/terraform-aws-keypair):** Terraform module for generating or importing an SSH public key file into AWS.
5. **[terraform-aws-production-access-role](https://github.com/clouddrove/terraform-aws-production-access-role):** This terraform module is used for creating an IAM Role which can give permission to another AWS account for accessing it's inventory.
6. **[terraform-aws-cross-account-role](https://github.com/clouddrove/terraform-aws-cross-account-role):** This terraform module is used to create an IAM Role to access another AWS account inventory.
7. **[terraform-aws-public-subnet](https://github.com/clouddrove/terraform-aws-public-subnet):** Terraform module for public subnets provisioning
8. **[terraform-labels](https://github.com/clouddrove/terraform-labels):** This terraform module is designed to generate consistent label names and tags for resources. You can use terraform-labels to implement a strict naming convention.
9. **[terraform-aws-ecr](https://github.com/clouddrove/terraform-aws-ecr):** This terraform module is used to create ECR on AWS for store docker images.
10. **[terraform-aws-s3](https://github.com/clouddrove/terraform-aws-s3):** Terraform module to create default S3 bucket with logging and encryption type specific features.
11. **[terraform-aws-vpc-peering](https://github.com/clouddrove/terraform-aws-vpc-peering):** Terraform module to connect two VPC's on AWS.
12. **[terraform-aws-ebs-volume](https://github.com/clouddrove/terraform-aws-ebs-volume):** Terraform module to get EBS volume resource on AWS.
13. **[terraform-aws-cloudtrail](https://github.com/clouddrove/terraform-aws-cloudtrail):** Terraform module to provision an AWS CloudTrail and an encrypted S3 bucket with versioning to store CloudTrail logs
14. **[terraform-aws-security-group](https://github.com/clouddrove/terraform-aws-security-group):** This terraform module creates set of Security Group and Security Group Rules resources in various combinations.
15. **[terraform-aws-ec2](https://github.com/clouddrove/terraform-aws-ec2):** Terraform module to create an EC2 resource on AWS with Elastic IP Addresses and Elastic Block Store.
16. **[terraform-aws-alb](https://github.com/clouddrove/terraform-aws-alb):** This terraform module is used to create ALB on AWS.
17. **[terraform-aws-aurora](https://github.com/clouddrove/terraform-aws-aurora):** Terraform module which creates RDS Aurora database resources on AWS and can create different type of databases. Currently it supports Postgres and MySQL.
18. **[terraform-aws-elasticache-redis](https://github.com/clouddrove/terraform-aws-elasticache-redis):** This terraform module creates Elasticache standalone server for Redis on AWS.
19. **[terraform-aws-elasticache-redis-cluster](https://github.com/clouddrove/terraform-aws-elasticache-redis-cluster):** This terraform module creates Elasticache multiple replica for Redis on AWS.
20. **[terraform-digitalocean](https://github.com/clouddrove/terraform-digitalocean):** Terraform module to manage Digital Ocean Account 
21. **[terraform-digitalocean-k8s](https://github.com/clouddrove/terraform-digitalocean-k8s):** A terraform module for managing and creating a Kubernetes cluster on digital ocean.
22. **[terraform-aws-ses](https://github.com/clouddrove/terraform-aws-ses):** Terraform module to create an SES Identity with SES IAM user on AWS.
23. **[terraform-aws-vpn](https://github.com/clouddrove/terraform-aws-vpn):** Terraform module is used to create VPN resource on AWS for network connectivity.
24. **[terraform-aws-cloudfront-cdn](https://github.com/clouddrove/terraform-aws-cloudfront-cdn):** Terraform module provisions CloudFront CDN resource on AWS.
25. **[terraform-aws-logging](https://github.com/clouddrove/terraform-aws-logging):** Terraform module to enable logging on AWS.
26. **[terraform-aws-nuke](https://github.com/clouddrove/terraform-aws-nuke):** This module is used to cleanup the AWS account inventory.
27. **[terraform-aws-subnet](https://github.com/clouddrove/terraform-aws-subnet):** Terraform module to create public, private and public-private subnet with network acl, route table, Elastic IP, nat gateway, flow log.
28. **[terraform-aws-sns](https://github.com/clouddrove/terraform-aws-sns):** Terraform module is used to setup SNS service to manage notifications on application.
29. **[terraform-aws-bastion](https://github.com/clouddrove/terraform-aws-bastion):** Terraform module to deploy bastion host on AWS.
30. **[terraform-aws-eks](https://github.com/clouddrove/terraform-aws-eks):** Terraform module for provisioning an EKS cluster
31. **[terraform-aws-eks-workers](https://github.com/clouddrove/terraform-aws-eks-workers):** Terraform module to provision an AWS AutoScaling Group, IAM Role, and Security Group for EKS Workers.
32. **[terraform-aws-autoscaling](https://github.com/clouddrove/terraform-aws-autoscaling):** Terraform module to provision Auto Scaling Group and Launch Template on AWS.
33. **[terraform-aws-kms](https://github.com/clouddrove/terraform-aws-kms):** This terraform module creates a KMS Customer Master Key (CMK) and its alias.
34. **[terraform-aws-0-11-baseline](https://github.com/clouddrove/terraform-aws-0-11-baseline):** This module creates baseline like VPC, EC2, Subnet etc with terraform 0.11.
35. **[terraform-aws-eks-cluster](https://github.com/clouddrove/terraform-aws-eks-cluster):** Terraform module will be created Autoscaling, Workers, EKS Clusters.
36. **[terraform-aws-transit-gateway](https://github.com/clouddrove/terraform-aws-transit-gateway):** Terraform module to create Transit gateway resource on AWS.
37. **[terraform-aws-vpn-transit-gateway](https://github.com/clouddrove/terraform-aws-vpn-transit-gateway):** Terraform module to create Transit gateway for VPN resource on AWS.
38. **[terraform-aws-consul](https://github.com/clouddrove/terraform-aws-consul):** Terraform module to create Consul server cluster on EC2.
39. **[terraform-aws-sqs](https://github.com/clouddrove/terraform-aws-sqs):** Terraform module to create SQS resource on AWS for managing queue.
40. **[terraform-aws-efs](https://github.com/clouddrove/terraform-aws-efs):** Terraform module to create or deploy EFS on AWS.
41. **[terraform-aws-cloudwatch-alarms](https://github.com/clouddrove/terraform-aws-cloudwatch-alarms):** Terraform module creates Cloudwatch Alarm on AWS for monitoriing AWS services.
42. **[terraform-aws-elastic-beanstalk](https://github.com/clouddrove/terraform-aws-elastic-beanstalk):** Terraform module to deploy Elastic Beanstalk resource on AWS.
43. **[terraform-aws-iam](https://github.com/clouddrove/terraform-aws-iam):** Terraform module to create IAM role resource on AWS.
44. **[terraform-aws-baseline](https://github.com/clouddrove/terraform-aws-baseline):** Internal repo for testing terraform modules 

## Ansible Packages

CloudDrove offers the below ansible roles:

1. **[ansible-commands](https://github.com/clouddrove/ansible-commands):** This repository is used to understand how to use ansible commands.
2. **[ansible-role-docker](https://github.com/clouddrove/ansible-role-docker):** This ansible role installs docker at Debian.
3. **[ansible-role-common](https://github.com/clouddrove/ansible-role-common):** This ansible role installs common packages for Debian.
4. **[ansible-role-redis](https://github.com/clouddrove/ansible-role-redis):** This ansible role is used to install Redis server on Debian.
5. **[ansible-role-keys](https://github.com/clouddrove/ansible-role-keys):** Ansible role to manage keys
6. **[ansible-role-php](https://github.com/clouddrove/ansible-role-php):** This ansible role is used to install PHP server on Debian.
7. **[ansible-role-jenkins-agent](https://github.com/clouddrove/ansible-role-jenkins-agent):** This ansible role is used to install Jenkins Agent on Debian.
8. **[ansible-role-docker-php](https://github.com/clouddrove/ansible-role-docker-php):** This ansible ro used to install PHP with docker on Debian.
9. **[ansible-role-docker-nginx](https://github.com/clouddrove/ansible-role-docker-nginx):** This ansible role is used for the installation of Nginx server with docker on Debian.
10. **[ansible-role-docker-redis](https://github.com/clouddrove/ansible-role-docker-redis):** This ansible role is used to setup Redis server with docker on Debian.
11. **[ansible-role-docker-mysql](https://github.com/clouddrove/ansible-role-docker-mysql):** This ansible role is used for formation of MySQL server with docker on Debian.
12. **[ansible-role-mongo-cluster](https://github.com/clouddrove/ansible-role-mongo-cluster):** This ansible role is used to setup Mongo cluster on Debian.
13. **[ansible-role-docker-mongo-cluster](https://github.com/clouddrove/ansible-role-docker-mongo-cluster):** This ansible role is used to setup Mongo cluster with docker on Debian.
14. **[ansible-role-solr](https://github.com/clouddrove/ansible-role-solr):** Ansible role to run setup solr  using docker 
15. **[ansible-role-logz-io](https://github.com/clouddrove/ansible-role-logz-io):** This ansible role is used to install logz.io tool dependency on Debian.
16. **[ansible-role-nginx](https://github.com/clouddrove/ansible-role-nginx):** This ansible role is used to setup Redis server with docker on Debian.
17. **[ansible-role-mount-efs](https://github.com/clouddrove/ansible-role-mount-efs):** This ansible role is used for installing & Mounting AWS EFS on Debian.
18. **[ansible-role-user](https://github.com/clouddrove/ansible-role-user):** This ansible role is used to create users on server.
19. **[ansible-role-redash](https://github.com/clouddrove/ansible-role-redash):** This ansible role is used for the installation of Redash tool on Debian.
20. **[ansible-modules](https://github.com/clouddrove/ansible-modules):** This repo contains all ansible modules.
21. **[ansible-role-gitlab-runner](https://github.com/clouddrove/ansible-role-gitlab-runner):** ansible role is used for installing gitlab runner
22. **[ansible-role-docker-superset](https://github.com/clouddrove/ansible-role-docker-superset):** This ansible role is used for installing Superset tool with docker on Debian.
23. **[ansible-role-docker-metabase](https://github.com/clouddrove/ansible-role-docker-metabase):** This ansible role is used for installing Metabase tool with docker on Debian.

## Docker Packages

CloudDrove offers the below docker packages:

1. **[docker-elasticsearch](https://github.com/clouddrove/docker-elasticsearch):** Need . to be .  removed 
2. **[docker-terraform](https://github.com/clouddrove/docker-terraform):** Running terraform using docker for better CI/CD
3. **[docker-pritunl](https://github.com/clouddrove/docker-pritunl):** Virtualize your private networks across datacenters

## CloudDrove Internal Tools

CloudDrove offers the below internal tools:

1. **[genie](https://github.com/clouddrove/genie):** This repository is a collection of Makefiles to facilitate some task easily like dynamic readme, terraform and git related.
2. **[slack-ssh-notifier](https://github.com/clouddrove/slack-ssh-notifier):** This repository is used to send Slack notification when any user logs in on the server.
3. **[aladdin](https://github.com/clouddrove/aladdin):** This repository is a collection of packages which can be installed directly by a single command on Debian(Linux) and Darwin(Mac) bases.

