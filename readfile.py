import pandas as pd
import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit


def replace_csv_value():
    start = datetime.datetime.now()
    csv = pd.read_csv(
        "", delimiter="|", dtype=str
    )
    csv["columnName"] = ""
    csv.to_csv(
        "",
        sep="|",
        index=None,
        header=True,
    )
    end = datetime.datetime.now()
    total_time = end - start

    print(f"Time elapsed with pandas: {total_time}")


def replace_csv_value_spark():
    ps = SparkSession.builder.getOrCreate()
    start = datetime.datetime.now()
    csv = (
        ps.read.options(header=True, delimiter="|")
        .csv("")
        .fillna("")
    )
    csv2 = csv.withColumn("columnName", lit(""))
    # csv2.show(truncate=False)
    csv2.write.mode("overwrite").csv(
        ""
    )
    end = datetime.datetime.now()
    total_time = end - start

    print(f"Time elapsed with spark: {total_time}")
