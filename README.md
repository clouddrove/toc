# TOC of All CloudDrove Packages and Tools

This repo is a useful way to discover all [CloudDrove](https://clouddrove.com) developed and maintained repositories. It is mainly designed for clients of CloudDrove.

## Terraform Packages

These are the Terraform packages which currently Clouddrove have

1. **[terraform-github-users](https://github.com/clouddrove/terraform-github-users)**
2. **[terraform-aws-vpc](https://github.com/clouddrove/terraform-aws-vpc):** Terraform module to create autoscaling ,workers,eks-clusters.
3. **[terraform-aws-security-group-rules](https://github.com/clouddrove/terraform-aws-security-group-rules)**
4. **[terraform-aws-acm](https://github.com/clouddrove/terraform-aws-acm):** This terraform module is used to request or import SSL/TLS certificate with validation
5. **[terraform-aws-keypair](https://github.com/clouddrove/terraform-aws-keypair):** Terraform module for generating or importing an SSH public key file into AWS.
6. **[terraform-aws-production-access-role](https://github.com/clouddrove/terraform-aws-production-access-role)**
7. **[terraform-aws-cross-account-role](https://github.com/clouddrove/terraform-aws-cross-account-role)**
8. **[terraform-aws-route-table](https://github.com/clouddrove/terraform-aws-route-table)**
9. **[terraform-aws-public-subnet](https://github.com/clouddrove/terraform-aws-public-subnet):** Terraform module for public subnets provisioning
10. **[terraform-labels](https://github.com/clouddrove/terraform-labels):** Terraform module designed to generate consistent label names and tags for resources. Use terraform-labels to implement a strict naming convention.
11. **[terraform-aws-ecr](https://github.com/clouddrove/terraform-aws-ecr)**
12. **[terraform-aws-s3](https://github.com/clouddrove/terraform-aws-s3):** Terraform module to create default s3 bucket, s3 bucket with logging, s3bucket with encryption and s3 bucket for hosting static website
13. **[terraform-aws-vpc-peering](https://github.com/clouddrove/terraform-aws-vpc-peering):** Terraform module to create a peering connection between two VPCs.
14. **[terraform-aws-ebs-volume](https://github.com/clouddrove/terraform-aws-ebs-volume)**
15. **[terraform-aws-cloudtrail](https://github.com/clouddrove/terraform-aws-cloudtrail):** Terraform module to provision an AWS CloudTrail and an encrypted S3 bucket with versioning to store CloudTrail logs
16. **[terraform-aws-cloudtrail-s3-bucket](https://github.com/clouddrove/terraform-aws-cloudtrail-s3-bucket):** S3 bucket with built in IAM policy to allow CloudTrail logs
17. **[terraform-aws-s3-log-storage](https://github.com/clouddrove/terraform-aws-s3-log-storage):** This module creates an S3 bucket suitable for receiving logs from other AWS services such as S3, CloudFront, and CloudTrail
18. **[terraform-aws-security-group](https://github.com/clouddrove/terraform-aws-security-group):** Terraform module creates set of Security Group and Security Group Rules resources in various combinations.
19. **[terraform-aws-ec2](https://github.com/clouddrove/terraform-aws-ec2):** Terraform module to create an EC2 with Elastic IP Addresses and Elastic Block Store.
20. **[terraform-aws-alb](https://github.com/clouddrove/terraform-aws-alb)**
21. **[terraform-aws-aurora](https://github.com/clouddrove/terraform-aws-aurora):** Terraform module which creates RDS Aurora resources on AWS.
22. **[terraform-aws-elasticache-redis](https://github.com/clouddrove/terraform-aws-elasticache-redis)**
23. **[terraform-aws-elasticache-redis-cluster](https://github.com/clouddrove/terraform-aws-elasticache-redis-cluster)**
24. **[terraform-aws-acm-import-certficate](https://github.com/clouddrove/terraform-aws-acm-import-certficate)**
25. **[terraform-digitalocean](https://github.com/clouddrove/terraform-digitalocean)**
26. **[terraform-digitalocean-k8s](https://github.com/clouddrove/terraform-digitalocean-k8s):** A terraform module for managing and creating a Kubernetes cluster on digital ocean
27. **[terraform-aws-ses](https://github.com/clouddrove/terraform-aws-ses):** Terraform module to create an SES Identity with SES user and proper policy.
28. **[terraform-aws-vpn](https://github.com/clouddrove/terraform-aws-vpn)**
29. **[terraform-aws-cloudfront-cdn](https://github.com/clouddrove/terraform-aws-cloudfront-cdn)**
30. **[terraform-aws-logging](https://github.com/clouddrove/terraform-aws-logging):** Terraform module to enable logging
31. **[terraform-aws-nuke](https://github.com/clouddrove/terraform-aws-nuke):** Nuke module to cleanup the AWS account 
32. **[terraform-aws-subnet](https://github.com/clouddrove/terraform-aws-subnet):** Terraform module to create public, private  subnet with network acl, route table, Elastic IP, nat gateway, flow log.
33. **[terraform-aws-sns](https://github.com/clouddrove/terraform-aws-sns)**
34. **[terraform-aws-bastion](https://github.com/clouddrove/terraform-aws-bastion):** Terraform module to deploy bastion host on aws 
35. **[terraform-aws-eks](https://github.com/clouddrove/terraform-aws-eks):** Terraform module for provisioning an EKS cluster
36. **[terraform-aws-eks-workers](https://github.com/clouddrove/terraform-aws-eks-workers):** Terraform module to provision an AWS AutoScaling Group, IAM Role, and Security Group for EKS Workers
37. **[terraform-aws-autoscaling](https://github.com/clouddrove/terraform-aws-autoscaling):** Terraform module to provision Auto Scaling Group and Launch Template on AWS
38. **[terraform-aws-kms](https://github.com/clouddrove/terraform-aws-kms):** Terraform module which creates a KMS Customer Master Key (CMK) and its alias.
39. **[terraform-aws-0-11-baseline](https://github.com/clouddrove/terraform-aws-0-11-baseline)**
40. **[terraform-aws-eks-cluster](https://github.com/clouddrove/terraform-aws-eks-cluster):** Terraform module will be created Autoscaling, Workers, EKS Clusters.
41. **[terraform-aws-transit-gateway](https://github.com/clouddrove/terraform-aws-transit-gateway)**
42. **[terraform-aws-vpn-transit-gateway](https://github.com/clouddrove/terraform-aws-vpn-transit-gateway)**
43. **[terraform-aws-consul](https://github.com/clouddrove/terraform-aws-consul):** Consul server cluster on EC2
44. **[terraform-aws-sqs](https://github.com/clouddrove/terraform-aws-sqs)**
45. **[terraform-aws-efs](https://github.com/clouddrove/terraform-aws-efs):** EFS Filesystem
46. **[terraform-aws-cloudwatch-alarms](https://github.com/clouddrove/terraform-aws-cloudwatch-alarms)**
47. **[terraform-aws-elastic-beanstalk](https://github.com/clouddrove/terraform-aws-elastic-beanstalk):**  Elastic Beanstalk allows you to deploy and manage applications in the AWS cloud without worrying about the infrastructure that runs those applications.
48. **[terraform-aws-iam](https://github.com/clouddrove/terraform-aws-iam)**

## Ansible Packages

These are the Ansible packages which currently Clouddrove have

1. **[ansible-commands](https://github.com/clouddrove/ansible-commands):** Ansible Commands
2. **[ansible-role-docker](https://github.com/clouddrove/ansible-role-docker):** Ansible Role - Docker
3. **[ansible-role-common](https://github.com/clouddrove/ansible-role-common):** Ansible role for installing comman packages for ubuntu
4. **[ansible-role-redis](https://github.com/clouddrove/ansible-role-redis)**
5. **[ansible-role-keys](https://github.com/clouddrove/ansible-role-keys):** Ansible role to manage keys
6. **[ansible-role-php](https://github.com/clouddrove/ansible-role-php)**
7. **[ansible-role-jenkins-agent](https://github.com/clouddrove/ansible-role-jenkins-agent)**
8. **[ansible-role-docker-php](https://github.com/clouddrove/ansible-role-docker-php)**
9. **[ansible-role-docker-nginx](https://github.com/clouddrove/ansible-role-docker-nginx)**
10. **[ansible-role-docker-redis](https://github.com/clouddrove/ansible-role-docker-redis)**
11. **[ansible-role-docker-mysql](https://github.com/clouddrove/ansible-role-docker-mysql)**
12. **[ansible-role-mongo-cluster](https://github.com/clouddrove/ansible-role-mongo-cluster)**
13. **[ansible-role-docker-mongo-cluster](https://github.com/clouddrove/ansible-role-docker-mongo-cluster)**
14. **[ansible-role-solr](https://github.com/clouddrove/ansible-role-solr)**
15. **[ansible-role-logz-io](https://github.com/clouddrove/ansible-role-logz-io)**
16. **[ansible-role-nginx](https://github.com/clouddrove/ansible-role-nginx)**
17. **[ansible-role-mount-efs](https://github.com/clouddrove/ansible-role-mount-efs):** Ansible role for installing & Mounting AWS EFS on Debian
18. **[ansible-role-user](https://github.com/clouddrove/ansible-role-user)**
19. **[ansible-role-redash](https://github.com/clouddrove/ansible-role-redash):** Ansible role for redash with docker
20. **[ansible-modules](https://github.com/clouddrove/ansible-modules):** Repo contains all ansible modules 
21. **[ansible-role-gitlab-runner](https://github.com/clouddrove/ansible-role-gitlab-runner)**
22. **[ansible-role-docker-superset](https://github.com/clouddrove/ansible-role-docker-superset)**
23. **[ansible-role-docker-metabase](https://github.com/clouddrove/ansible-role-docker-metabase)**

## Docker Packages

These are the Docker packages which currently	Clouddrove have

1. **[docker-elasticsearch](https://github.com/clouddrove/docker-elasticsearch)**
2. **[docker-terraform](https://github.com/clouddrove/docker-terraform):** Running terraform using docker for better CI/CD
3. **[docker-pritunl](https://github.com/clouddrove/docker-pritunl):** Virtualize your private networks across datacenters

## Clouddrove Internal Tools

These are some internal tools which currently Clouddrove have

1. **[genie](https://github.com/clouddrove/genie)**
2. **[aladdin](https://github.com/clouddrove/aladdin)**
3. **[slack-ssh-notifier](https://github.com/clouddrove/slack-ssh-notifier):** Slack notifier of SSH login

