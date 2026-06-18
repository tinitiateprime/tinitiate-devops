# AWS DevOps for Data Engineers and AI Platforms

A practical, enterprise-focused AWS DevOps course for data engineers, platform engineers, AI platform teams, and production support engineers.

## Quick Links

- [Course Modules](#course-modules)
- [GitHub Actions AWS Examples](docs/github-actions-aws-examples.md)
- [Capstone Project](capstone-project/119-enterprise-data-platform-capstone.md)
- [Capstone Solution Guide](capstone-project/120-capstone-solution-guide.md)

---

## Course Modules

| Module | Lessons | Focus |
| --- | ---: | --- |
| [Module 01 - Enterprise AWS Foundations](#module-01---enterprise-aws-foundations) | 7 | Enterprise AWS structure, accounts, organizations, landing zones, and team responsibilities |
| [Module 02 - IAM and Access Management](#module-02---iam-and-access-management) | 11 | IAM users, groups, roles, policies, SSO, cross-account access, and least privilege |
| [Module 03 - AWS Networking](#module-03---aws-networking) | 11 | VPCs, subnets, routing, gateways, security boundaries, endpoints, and troubleshooting |
| [Module 04 - Storage and Data Platforms](#module-04---storage-and-data-platforms) | 9 | S3, encryption, lifecycle, access patterns, and data lake architecture |
| [Module 05 - PostgreSQL Administration](#module-05---postgresql-administration) | 12 | RDS PostgreSQL administration, indexing, tuning, backup, replication, and support |
| [Module 06 - Messaging and Eventing](#module-06---messaging-and-eventing) | 6 | SNS, SQS, EventBridge, Step Functions, and event-driven design |
| [Module 07 - Infrastructure as Code](#module-07---infrastructure-as-code) | 12 | Terraform, state, modules, workspaces, backends, CI/CD, and CDK comparison |
| [Module 08 - AWS Data Engineering Platform](#module-08---aws-data-engineering-platform) | 12 | Glue, crawlers, catalog, PySpark, data quality, validation, and platform patterns |
| [Module 09 - CI/CD and Deployments](#module-09---cicd-and-deployments) | 9 | Git, GitHub, pull requests, GitHub Actions, deployments, and release management |
| [Module 10 - Security and Governance](#module-10---security-and-governance) | 11 | Governance, RBAC, ABAC, Secrets Manager, KMS, CloudTrail, Config, and compliance |
| [Module 11 - Monitoring and Operations](#module-11---monitoring-and-operations) | 9 | CloudWatch logs, metrics, dashboards, alarms, runbooks, incidents, RCA, and on-call |
| [Module 12 - Production Support Scenarios](#module-12---production-support-scenarios) | 9 | Hands-on production support scenarios and troubleshooting patterns |
| [Capstone Project](#capstone-project) | 2 | End-to-end enterprise data platform project and complete solution guide |

---

## How To Use This Repository

1. Start with Module 01 if you are new to enterprise AWS.
2. Use the README as the home page and module index.
3. Open each lesson from the module list below.
4. Use the navigation links at the top of each lesson to go Home, Previous, or Next.
5. Complete the capstone after finishing the core modules.

---

## GitHub Actions and Project Assets

| Resource | Purpose |
| --- | --- |
| [GitHub Actions for AWS Deployments](docs/github-actions-aws-examples.md) | S3, Lambda, Glue, crawler, and Athena deployment workflows |
| [Sample Claims Data](data/claims_sample.csv) | Capstone input data |
| [Lambda Starter Code](lambda/app.py) | Capstone Lambda function |
| [Glue Starter Job](glue/jobs/claims_transform.py) | Capstone ETL job |
| [Athena Validation SQL](sql/athena_validation.sql) | Capstone validation queries |
| [Architecture Notes](docs/architecture-notes.md) | Capstone architecture notes |

---

## Detailed Lesson Index

## Module 01 - Enterprise AWS Foundations

Enterprise AWS structure, accounts, organizations, landing zones, and team responsibilities

<details open>
<summary>Show lessons</summary>

- [01-how-enterprise-aws-works.md](module-01-enterprise-aws-foundations/01-how-enterprise-aws-works.md) - How Enterprise Aws Works
- [02-multi-account-strategy.md](module-01-enterprise-aws-foundations/02-multi-account-strategy.md) - Multi Account Strategy
- [03-aws-organizations.md](module-01-enterprise-aws-foundations/03-aws-organizations.md) - Aws Organizations
- [04-landing-zones.md](module-01-enterprise-aws-foundations/04-landing-zones.md) - Landing Zones
- [05-shared-services-account.md](module-01-enterprise-aws-foundations/05-shared-services-account.md) - Shared Services Account
- [06-govcloud-fundamentals.md](module-01-enterprise-aws-foundations/06-govcloud-fundamentals.md) - Govcloud Fundamentals
- [07-enterprise-teams-and-responsibilities.md](module-01-enterprise-aws-foundations/07-enterprise-teams-and-responsibilities.md) - Enterprise Teams And Responsibilities

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 02 - IAM and Access Management

IAM users, groups, roles, policies, SSO, cross-account access, and least privilege

<details open>
<summary>Show lessons</summary>

- [08-iam-overview.md](module-02-iam-and-access-management/08-iam-overview.md) - Iam Overview
- [09-iam-users.md](module-02-iam-and-access-management/09-iam-users.md) - Iam Users
- [10-iam-groups.md](module-02-iam-and-access-management/10-iam-groups.md) - Iam Groups
- [11-iam-roles.md](module-02-iam-and-access-management/11-iam-roles.md) - Iam Roles
- [12-iam-policies.md](module-02-iam-and-access-management/12-iam-policies.md) - Iam Policies
- [13-trust-relationships.md](module-02-iam-and-access-management/13-trust-relationships.md) - Trust Relationships
- [14-service-accounts.md](module-02-iam-and-access-management/14-service-accounts.md) - Service Accounts
- [15-cross-account-access.md](module-02-iam-and-access-management/15-cross-account-access.md) - Cross Account Access
- [16-federation-and-sso.md](module-02-iam-and-access-management/16-federation-and-sso.md) - Federation And Sso
- [17-least-privilege-principle.md](module-02-iam-and-access-management/17-least-privilege-principle.md) - Least Privilege Principle
- [18-iam-best-practices.md](module-02-iam-and-access-management/18-iam-best-practices.md) - Iam Best Practices

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 03 - AWS Networking

VPCs, subnets, routing, gateways, security boundaries, endpoints, and troubleshooting

<details open>
<summary>Show lessons</summary>

- [19-vpc-fundamentals.md](module-03-aws-networking/19-vpc-fundamentals.md) - Vpc Fundamentals
- [20-subnets.md](module-03-aws-networking/20-subnets.md) - Subnets
- [21-route-tables.md](module-03-aws-networking/21-route-tables.md) - Route Tables
- [22-internet-gateway.md](module-03-aws-networking/22-internet-gateway.md) - Internet Gateway
- [23-nat-gateway.md](module-03-aws-networking/23-nat-gateway.md) - Nat Gateway
- [24-security-groups.md](module-03-aws-networking/24-security-groups.md) - Security Groups
- [25-network-acls.md](module-03-aws-networking/25-network-acls.md) - Network Acls
- [26-vpc-endpoints.md](module-03-aws-networking/26-vpc-endpoints.md) - Vpc Endpoints
- [27-private-link.md](module-03-aws-networking/27-private-link.md) - Private Link
- [28-hybrid-connectivity.md](module-03-aws-networking/28-hybrid-connectivity.md) - Hybrid Connectivity
- [29-network-troubleshooting.md](module-03-aws-networking/29-network-troubleshooting.md) - Network Troubleshooting

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 04 - Storage and Data Platforms

S3, encryption, lifecycle, access patterns, and data lake architecture

<details open>
<summary>Show lessons</summary>

- [30-s3-fundamentals.md](module-04-storage-and-data-platforms/30-s3-fundamentals.md) - S3 Fundamentals
- [31-s3-security.md](module-04-storage-and-data-platforms/31-s3-security.md) - S3 Security
- [32-s3-versioning.md](module-04-storage-and-data-platforms/32-s3-versioning.md) - S3 Versioning
- [33-s3-lifecycle-policies.md](module-04-storage-and-data-platforms/33-s3-lifecycle-policies.md) - S3 Lifecycle Policies
- [34-s3-encryption.md](module-04-storage-and-data-platforms/34-s3-encryption.md) - S3 Encryption
- [35-s3-access-patterns.md](module-04-storage-and-data-platforms/35-s3-access-patterns.md) - S3 Access Patterns
- [36-data-lake-architecture.md](module-04-storage-and-data-platforms/36-data-lake-architecture.md) - Data Lake Architecture
- [37-bronze-silver-gold-architecture.md](module-04-storage-and-data-platforms/37-bronze-silver-gold-architecture.md) - Bronze Silver Gold Architecture
- [38-data-sharing-patterns.md](module-04-storage-and-data-platforms/38-data-sharing-patterns.md) - Data Sharing Patterns

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 05 - PostgreSQL Administration

RDS PostgreSQL administration, indexing, tuning, backup, replication, and support

<details open>
<summary>Show lessons</summary>

- [39-rds-postgresql-fundamentals.md](module-05-postgresql-administration/39-rds-postgresql-fundamentals.md) - Rds Postgresql Fundamentals
- [40-postgresql-architecture.md](module-05-postgresql-administration/40-postgresql-architecture.md) - Postgresql Architecture
- [41-postgresql-users-and-roles.md](module-05-postgresql-administration/41-postgresql-users-and-roles.md) - Postgresql Users And Roles
- [42-postgresql-schemas.md](module-05-postgresql-administration/42-postgresql-schemas.md) - Postgresql Schemas
- [43-postgresql-indexing.md](module-05-postgresql-administration/43-postgresql-indexing.md) - Postgresql Indexing
- [44-explain-analyze.md](module-05-postgresql-administration/44-explain-analyze.md) - Explain Analyze
- [45-query-optimization.md](module-05-postgresql-administration/45-query-optimization.md) - Query Optimization
- [46-vacuum-and-autovacuum.md](module-05-postgresql-administration/46-vacuum-and-autovacuum.md) - Vacuum And Autovacuum
- [47-postgresql-monitoring.md](module-05-postgresql-administration/47-postgresql-monitoring.md) - Postgresql Monitoring
- [48-postgresql-backup-and-recovery.md](module-05-postgresql-administration/48-postgresql-backup-and-recovery.md) - Postgresql Backup And Recovery
- [49-postgresql-replication.md](module-05-postgresql-administration/49-postgresql-replication.md) - Postgresql Replication
- [50-postgresql-production-support.md](module-05-postgresql-administration/50-postgresql-production-support.md) - Postgresql Production Support

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 06 - Messaging and Eventing

SNS, SQS, EventBridge, Step Functions, and event-driven design

<details open>
<summary>Show lessons</summary>

- [51-sns-fundamentals.md](module-06-messaging-and-eventing/51-sns-fundamentals.md) - Sns Fundamentals
- [52-sqs-fundamentals.md](module-06-messaging-and-eventing/52-sqs-fundamentals.md) - Sqs Fundamentals
- [53-eventbridge.md](module-06-messaging-and-eventing/53-eventbridge.md) - Eventbridge
- [54-step-functions.md](module-06-messaging-and-eventing/54-step-functions.md) - Step Functions
- [55-event-driven-architecture.md](module-06-messaging-and-eventing/55-event-driven-architecture.md) - Event Driven Architecture
- [56-messaging-best-practices.md](module-06-messaging-and-eventing/56-messaging-best-practices.md) - Messaging Best Practices

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 07 - Infrastructure as Code

Terraform, state, modules, workspaces, backends, CI/CD, and CDK comparison

<details open>
<summary>Show lessons</summary>

- [57-terraform-fundamentals.md](module-07-infrastructure-as-code/57-terraform-fundamentals.md) - Terraform Fundamentals
- [58-terraform-providers.md](module-07-infrastructure-as-code/58-terraform-providers.md) - Terraform Providers
- [59-terraform-resources.md](module-07-infrastructure-as-code/59-terraform-resources.md) - Terraform Resources
- [60-terraform-variables.md](module-07-infrastructure-as-code/60-terraform-variables.md) - Terraform Variables
- [61-terraform-state.md](module-07-infrastructure-as-code/61-terraform-state.md) - Terraform State
- [62-terraform-modules.md](module-07-infrastructure-as-code/62-terraform-modules.md) - Terraform Modules
- [63-terraform-workspaces.md](module-07-infrastructure-as-code/63-terraform-workspaces.md) - Terraform Workspaces
- [64-terraform-backends.md](module-07-infrastructure-as-code/64-terraform-backends.md) - Terraform Backends
- [65-terraform-ci-cd.md](module-07-infrastructure-as-code/65-terraform-ci-cd.md) - Terraform Ci Cd
- [66-cdk-fundamentals.md](module-07-infrastructure-as-code/66-cdk-fundamentals.md) - Cdk Fundamentals
- [67-cdk-python.md](module-07-infrastructure-as-code/67-cdk-python.md) - Cdk Python
- [68-cdk-vs-terraform.md](module-07-infrastructure-as-code/68-cdk-vs-terraform.md) - Cdk Vs Terraform

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 08 - AWS Data Engineering Platform

Glue, crawlers, catalog, PySpark, data quality, validation, and platform patterns

<details open>
<summary>Show lessons</summary>

- [69-glue-fundamentals.md](module-08-aws-data-engineering-platform/69-glue-fundamentals.md) - Glue Fundamentals
- [70-glue-crawlers.md](module-08-aws-data-engineering-platform/70-glue-crawlers.md) - Glue Crawlers
- [71-glue-catalog.md](module-08-aws-data-engineering-platform/71-glue-catalog.md) - Glue Catalog
- [72-glue-jobs.md](module-08-aws-data-engineering-platform/72-glue-jobs.md) - Glue Jobs
- [73-glue-workflows.md](module-08-aws-data-engineering-platform/73-glue-workflows.md) - Glue Workflows
- [74-glue-triggers.md](module-08-aws-data-engineering-platform/74-glue-triggers.md) - Glue Triggers
- [75-pyspark-fundamentals.md](module-08-aws-data-engineering-platform/75-pyspark-fundamentals.md) - Pyspark Fundamentals
- [76-pyspark-transformations.md](module-08-aws-data-engineering-platform/76-pyspark-transformations.md) - Pyspark Transformations
- [77-pyspark-performance-tuning.md](module-08-aws-data-engineering-platform/77-pyspark-performance-tuning.md) - Pyspark Performance Tuning
- [78-data-quality-frameworks.md](module-08-aws-data-engineering-platform/78-data-quality-frameworks.md) - Data Quality Frameworks
- [79-data-validation.md](module-08-aws-data-engineering-platform/79-data-validation.md) - Data Validation
- [80-enterprise-data-platform-patterns.md](module-08-aws-data-engineering-platform/80-enterprise-data-platform-patterns.md) - Enterprise Data Platform Patterns

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 09 - CI/CD and Deployments

Git, GitHub, pull requests, GitHub Actions, deployments, and release management

<details open>
<summary>Show lessons</summary>

- [81-git-fundamentals.md](module-09-ci-cd-and-deployments/81-git-fundamentals.md) - Git Fundamentals
- [82-github-fundamentals.md](module-09-ci-cd-and-deployments/82-github-fundamentals.md) - Github Fundamentals
- [83-branching-strategies.md](module-09-ci-cd-and-deployments/83-branching-strategies.md) - Branching Strategies
- [84-pull-requests.md](module-09-ci-cd-and-deployments/84-pull-requests.md) - Pull Requests
- [85-github-actions.md](module-09-ci-cd-and-deployments/85-github-actions.md) - Github Actions
- [86-deploying-glue-jobs.md](module-09-ci-cd-and-deployments/86-deploying-glue-jobs.md) - Deploying Glue Jobs
- [87-deploying-lambda-functions.md](module-09-ci-cd-and-deployments/87-deploying-lambda-functions.md) - Deploying Lambda Functions
- [88-deploying-data-platform-components.md](module-09-ci-cd-and-deployments/88-deploying-data-platform-components.md) - Deploying Data Platform Components
- [89-release-management.md](module-09-ci-cd-and-deployments/89-release-management.md) - Release Management

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 10 - Security and Governance

Governance, RBAC, ABAC, Secrets Manager, KMS, CloudTrail, Config, and compliance

<details open>
<summary>Show lessons</summary>

- [90-data-governance.md](module-10-security-and-governance/90-data-governance.md) - Data Governance
- [91-rbac.md](module-10-security-and-governance/91-rbac.md) - Rbac
- [92-abac.md](module-10-security-and-governance/92-abac.md) - Abac
- [93-secrets-manager.md](module-10-security-and-governance/93-secrets-manager.md) - Secrets Manager
- [94-kms.md](module-10-security-and-governance/94-kms.md) - Kms
- [95-cloudtrail.md](module-10-security-and-governance/95-cloudtrail.md) - Cloudtrail
- [96-aws-config.md](module-10-security-and-governance/96-aws-config.md) - Aws Config
- [97-security-hub.md](module-10-security-and-governance/97-security-hub.md) - Security Hub
- [98-guardduty.md](module-10-security-and-governance/98-guardduty.md) - Guardduty
- [99-compliance-and-auditing.md](module-10-security-and-governance/99-compliance-and-auditing.md) - Compliance And Auditing
- [100-fedramp-and-govcloud.md](module-10-security-and-governance/100-fedramp-and-govcloud.md) - Fedramp And Govcloud

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 11 - Monitoring and Operations

CloudWatch logs, metrics, dashboards, alarms, runbooks, incidents, RCA, and on-call

<details open>
<summary>Show lessons</summary>

- [101-cloudwatch-fundamentals.md](module-11-monitoring-and-operations/101-cloudwatch-fundamentals.md) - Cloudwatch Fundamentals
- [102-cloudwatch-logs.md](module-11-monitoring-and-operations/102-cloudwatch-logs.md) - Cloudwatch Logs
- [103-cloudwatch-metrics.md](module-11-monitoring-and-operations/103-cloudwatch-metrics.md) - Cloudwatch Metrics
- [104-cloudwatch-dashboards.md](module-11-monitoring-and-operations/104-cloudwatch-dashboards.md) - Cloudwatch Dashboards
- [105-cloudwatch-alarms.md](module-11-monitoring-and-operations/105-cloudwatch-alarms.md) - Cloudwatch Alarms
- [106-operational-runbooks.md](module-11-monitoring-and-operations/106-operational-runbooks.md) - Operational Runbooks
- [107-incident-management.md](module-11-monitoring-and-operations/107-incident-management.md) - Incident Management
- [108-root-cause-analysis.md](module-11-monitoring-and-operations/108-root-cause-analysis.md) - Root Cause Analysis
- [109-on-call-support.md](module-11-monitoring-and-operations/109-on-call-support.md) - On Call Support

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Module 12 - Production Support Scenarios

Hands-on production support scenarios and troubleshooting patterns

<details open>
<summary>Show lessons</summary>

- [110-glue-job-failures.md](module-12-production-support-scenarios/110-glue-job-failures.md) - Glue Job Failures
- [111-s3-access-denied.md](module-12-production-support-scenarios/111-s3-access-denied.md) - S3 Access Denied
- [112-postgresql-performance-issues.md](module-12-production-support-scenarios/112-postgresql-performance-issues.md) - Postgresql Performance Issues
- [113-iam-troubleshooting.md](module-12-production-support-scenarios/113-iam-troubleshooting.md) - Iam Troubleshooting
- [114-network-connectivity-issues.md](module-12-production-support-scenarios/114-network-connectivity-issues.md) - Network Connectivity Issues
- [115-data-quality-incidents.md](module-12-production-support-scenarios/115-data-quality-incidents.md) - Data Quality Incidents
- [116-production-outages.md](module-12-production-support-scenarios/116-production-outages.md) - Production Outages
- [117-disaster-recovery.md](module-12-production-support-scenarios/117-disaster-recovery.md) - Disaster Recovery
- [118-production-support-best-practices.md](module-12-production-support-scenarios/118-production-support-best-practices.md) - Production Support Best Practices

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

## Capstone Project

End-to-end enterprise data platform project and complete solution guide

<details open>
<summary>Show lessons</summary>

- [119-enterprise-data-platform-capstone.md](capstone-project/119-enterprise-data-platform-capstone.md) - Enterprise Data Platform Capstone
- [120-capstone-solution-guide.md](capstone-project/120-capstone-solution-guide.md) - Capstone Solution Guide

</details>

[Back to top](#aws-devops-for-data-engineers-and-ai-platforms)

---

