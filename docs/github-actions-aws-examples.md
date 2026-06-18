---

[Home](../README.md) | [Course Modules](../README.md#course-modules)

---

# GitHub Actions for AWS Deployments

These workflows show how to deploy common AWS resources from GitHub Actions.

## Required GitHub Variable

Create this repository variable:

```text
AWS_GITHUB_ACTIONS_ROLE_ARN
```

Example value:

```text
arn:aws:iam::123456789012:role/github-actions-aws-deploy-role
```

The workflows use GitHub OIDC, so you do not need to store long-lived AWS access keys in GitHub.

---

## Workflows Added

| Workflow | Purpose |
| --- | --- |
| `.github/workflows/aws-s3-create.yml` | Create an S3 bucket and optional folder-style prefix |
| `.github/workflows/aws-lambda-deploy.yml` | Package code from GitHub and create or update Lambda |
| `.github/workflows/aws-glue-job-deploy.yml` | Upload a Glue script to S3 and create or update a Glue job |
| `.github/workflows/aws-athena-crawler-table.yml` | Create a Glue database, crawler, and example Athena table |

---

## 1. S3 Bucket Creation

Run workflow:

```text
AWS - Create S3 Bucket and Prefix
```

Inputs:

* `bucket_name`: globally unique S3 bucket name
* `aws_region`: AWS region
* `s3_prefix`: optional folder-style prefix such as `bronze/raw/`
* `block_public_access`: keep this enabled for normal enterprise buckets

Example:

```text
bucket_name = tinitiate-data-platform-dev
aws_region  = us-east-1
s3_prefix   = bronze/raw/
```

Important note: S3 does not have real folders. A folder is represented by an object key prefix.

---

## 2. GitHub to Lambda Code Deployment

Run workflow:

```text
AWS - Deploy Lambda From GitHub
```

Expected repo layout:

```text
lambda/
|-- app.py
`-- requirements.txt
```

Example `app.py`:

```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from GitHub Actions"
    }
```

Inputs:

* `function_name`: Lambda function name
* `lambda_source_dir`: repo folder to zip and deploy
* `runtime`: used when creating a new function
* `handler`: used when creating a new function
* `lambda_role_arn`: Lambda execution role used when creating a new function

---

## 3. GitHub to Glue Job Deployment

Run workflow:

```text
AWS - Deploy Glue Job From GitHub
```

Expected repo layout:

```text
glue/
`-- jobs/
    `-- sample_job.py
```

Inputs:

* `job_name`: Glue job name
* `glue_script_path`: local script path in GitHub
* `script_s3_bucket`: bucket where Glue scripts are uploaded
* `script_s3_prefix`: S3 prefix for Glue scripts
* `input_path`: S3 path read by the Glue job
* `output_path`: S3 path written by the Glue job
* `glue_role_arn`: IAM role used by the Glue job

The workflow uploads the script to S3, then creates or updates the Glue job.

---

## 4. GitHub to Athena Crawler and Table

Run workflow:

```text
AWS - Create Glue Crawler and Athena Table
```

Athena uses the AWS Glue Data Catalog for databases and tables.

Inputs:

* `database_name`: Glue database name
* `table_name`: Glue table name queried by Athena
* `data_s3_location`: S3 data path such as `s3://bucket/gold/sales/`
* `crawler_name`: Glue crawler name
* `crawler_role_arn`: IAM role used by the crawler
* `create_example_table`: creates a simple Parquet table definition

The crawler can infer schema from S3 data. The example table is useful for class demos, but production tables should match the actual dataset schema.

---

## Minimum AWS Permissions

The GitHub Actions deployment role needs permissions for the services you plan to deploy.

For class demos, the role commonly needs access to:

* S3: create buckets, put objects, configure encryption, configure public access block
* Lambda: create functions, update function code, read function status
* Glue: create databases, create crawlers, update crawlers, create jobs, update jobs, create tables, update tables
* IAM: pass only approved execution roles to Lambda and Glue

In production, scope permissions to specific resources and environments.

---

[Home](../README.md) | [Course Modules](../README.md#course-modules)

