---

[Home](../README.md) | [Course Modules](../README.md#course-modules) | [Next](02-multi-account-strategy.md)

---

# How Enterprise AWS Works

## Learning Objectives

By the end of this chapter, students will be able to:

* Explain how personal AWS accounts differ from enterprise AWS environments
* Describe why organizations use multiple AWS accounts
* Explain AWS Organizations and Organizational Units (OUs)
* Understand the AWS Shared Responsibility Model
* Recognize common enterprise data platform architecture patterns
* Identify the responsibilities of platform, security, DevOps, data engineering, and AI teams

---

## Opening Discussion

### Instructor Question

Ask students:

```text
How many AWS accounts have you worked with?
```

Most students will answer:

```text
1 AWS account
```

Usually this means:

* Personal Free Tier account
* Sandbox account
* Learning account

Now ask:

```text
What if a company has 2,000 engineers, 300 applications, 50 databases,
and petabytes of data?
```

Would everything run in a single AWS account?

The answer is no.

Enterprise AWS environments are fundamentally different from personal AWS environments.

---

## Why This Topic Matters

Many engineers know individual AWS services but struggle in interviews because they do not understand enterprise cloud operations.

Students may know services such as:

* S3
* Lambda
* Glue
* EC2

But they may not yet know:

* AWS Organizations
* Shared services
* Landing zones
* Account strategy
* Security boundaries

These topics are critical in real-world enterprise AWS environments.

---

## Personal AWS vs Enterprise AWS

### Personal AWS Environment

Typical structure:

```text
AWS Account
|
|-- S3 Bucket
|-- Lambda
|-- EC2
`-- RDS
```

Characteristics:

* Single account
* Single owner
* Minimal security requirements
* Lower cost
* Simple management

### Enterprise AWS Environment

Typical structure:

```text
AWS Organization
|
|-- Production
|-- Development
|-- QA
|-- Security
|-- Shared Services
`-- Sandbox
```

Characteristics:

* Hundreds or thousands of accounts
* Thousands of resources
* Multiple engineering teams
* Compliance requirements
* Governance controls

---

## Real-World Scenario

Imagine a healthcare company.

Departments:

* Data Engineering
* AI Team
* Finance
* Human Resources
* Application Development
* Security
* DevOps

Applications:

* Customer Portal
* Claims Processing
* Data Lake
* Analytics Platform
* AI Recommendation Engine

Would you place all these workloads inside one AWS account?

No.

Doing so would create:

* Security risks
* Operational complexity
* Cost tracking problems
* Compliance challenges

---

## AWS Organizations

AWS Organizations is a service used to centrally manage multiple AWS accounts.

Think of AWS Organizations as:

```text
Corporate headquarters
```

Each AWS account can represent a:

```text
Business unit, workload, environment, or team
```

Example structure:

```text
Root
|
|-- Production OU
|   |-- Data Platform
|   |-- AI Platform
|   `-- Applications
|
|-- NonProd OU
|   |-- Development
|   `-- QA
|
|-- Security OU
`-- Shared Services OU
```

Benefits:

* Central governance
* Consolidated billing
* Security controls
* Standardization

---

## Organizational Units

An Organizational Unit, or OU, is a logical grouping of AWS accounts.

Example:

```text
Production OU
```

Contains:

```text
Data Platform Prod
Application Prod
AI Prod
```

Security policies can be applied to the entire OU.

---

## Enterprise Data Platform Example

A typical enterprise data platform may look like this:

```text
SAP
Salesforce
Oracle
Flat Files
APIs
      |
      v
S3 Bronze
      |
      v
AWS Glue
      |
      v
S3 Silver
      |
      v
S3 Gold
      |
      v
Athena
Databricks
PostgreSQL
Power BI
```

Notice that the platform is not a single service.

It is a collection of:

* Storage
* Processing
* Governance
* Monitoring
* Security

---

## Shared Responsibility Model

AWS secures:

* Physical data centers
* Networking infrastructure
* Hardware
* Hypervisors

Customers secure:

* IAM
* Data
* Databases
* Encryption
* Applications

### Example

A company stores sensitive customer data in S3.

AWS responsibility:

* Protect the physical servers and managed infrastructure.

Customer responsibility:

* Configure bucket permissions correctly.
* Enable encryption.
* Control access.

If the bucket becomes public, AWS is not responsible for the misconfiguration.

The customer is.

---

## Typical Enterprise Teams

### Platform Engineering Team

Responsible for:

* AWS accounts
* IAM
* Terraform
* Networking
* Shared infrastructure

### Data Engineering Team

Responsible for:

* Glue
* Spark
* ETL
* Data quality

### AI Team

Responsible for:

* Model development
* Feature engineering
* Training pipelines

### Security Team

Responsible for:

* Compliance
* Access reviews
* Vulnerability management

### DevOps Team

Responsible for:

* CI/CD
* Monitoring
* Automation

---

## Environment Strategy

Most organizations separate workloads by environment.

Example:

```text
DEV
QA
UAT
PROD
```

Benefits:

* Testing before production
* Reduced risk
* Controlled deployments

---

## Cost Management

Example monthly costs:

```text
Data Platform = $40,000
AI Team       = $25,000
Applications  = $60,000
```

Separate accounts make cost allocation and chargeback easier.

---

## AWS Services Commonly Used

Data platform:

* S3
* Glue
* Athena
* PostgreSQL
* CloudWatch

DevOps:

* Terraform
* CodePipeline
* GitHub Actions

Security:

* IAM
* CloudTrail
* AWS Config

Networking:

* VPC
* Security groups
* NAT gateway

---

## Hands-On Lab

### Lab 1: Explore a Basic AWS Account

Create or open an AWS account.

Explore:

* IAM
* S3
* EC2
* CloudWatch

### Lab 2: Design an Enterprise Architecture Diagram

Include:

* Sources
* Storage
* Processing
* Analytics

---

## GovCloud Considerations

GovCloud environments often require alignment with:

* FedRAMP
* FISMA
* NIST controls

Additional controls may include:

* Enhanced auditing
* Restricted networking
* Strong IAM governance

---

## Production Best Practices

Always:

* Use MFA
* Enable CloudTrail
* Follow least privilege
* Separate environments
* Use Infrastructure as Code

Never:

* Use the root account for daily work
* Hardcode credentials
* Deploy directly to production without review

---

## Interview Questions

1. What is AWS Organizations?
2. Why do enterprises use multiple AWS accounts?
3. What is an Organizational Unit?
4. Explain the AWS Shared Responsibility Model.
5. Why should DEV and PROD environments be separated?

---

## Student Assignment

Design an enterprise AWS architecture for a healthcare company with:

* Data Engineering Team
* AI Team
* Analytics Team
* Security Team

Create:

* Account structure
* Environment strategy
* Data platform architecture

## Teaching Examples

### Example 1: Healthcare Multi-Account Setup

A healthcare company separates workloads into different AWS accounts:

* `security-prod` for CloudTrail, GuardDuty, and audit logs
* `shared-services-prod` for networking, CI/CD, and common tooling
* `data-platform-dev`, `data-platform-qa`, and `data-platform-prod` for data pipelines
* `analytics-prod` for reporting users and BI tools

This makes it easier to control access, track cost, and protect sensitive data.

### Example 2: Interview Explanation

Instead of saying, "We use AWS accounts," explain that enterprises use accounts as security, billing, and operational boundaries. DEV and PROD are separated so a test change cannot accidentally affect production data.

---

## Summary
Enterprise AWS is not only about learning individual services.

It is about understanding:

* Governance
* Security
* Multi-account strategy
* Shared responsibility
* Enterprise operations

These concepts form the foundation for everything that follows in IAM, networking, Terraform, DevOps, and data platforms.

---

[Home](../README.md) | [Course Modules](../README.md#course-modules) | [Next](02-multi-account-strategy.md)

