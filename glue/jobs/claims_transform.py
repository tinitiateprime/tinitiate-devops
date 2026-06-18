import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, to_date


args = getResolvedOptions(
    sys.argv,
    [
        "JOB_NAME",
        "INPUT_PATH",
        "OUTPUT_PATH",
    ],
)

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

claims_df = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv(args["INPUT_PATH"])
)

curated_df = (
    claims_df.select(
        col("claim_id").cast("string"),
        col("member_id").cast("string"),
        col("provider_id").cast("string"),
        to_date(col("claim_date"), "yyyy-MM-dd").alias("claim_date"),
        col("claim_amount").cast("double"),
        col("claim_status").cast("string"),
        col("diagnosis_code").cast("string"),
    )
    .dropDuplicates(["claim_id"])
)

curated_df.write.mode("overwrite").parquet(args["OUTPUT_PATH"])

job.commit()
