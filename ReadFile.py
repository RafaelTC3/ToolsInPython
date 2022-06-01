import pandas as pd
import datetime


# from pyspark.sql import SparkSession
# from pyspark.sql.functions import lit


def replace_csv_value(csv_file_path: str, column_name: str, new_column_value: str):
    start = datetime.datetime.now()
    path = csv_file_path.split(".csv")

    csv = pd.read_csv(
        csv_file_path, delimiter="|", dtype=str
    )
    csv[column_name] = new_column_value
    csv.to_csv(
        f"{path[0]}_column_renamed.csv",
        sep="|",
        index=None,
        header=True,
    )
    end = datetime.datetime.now()
    total_time = end - start

    print(f"Time elapsed with pandas: {total_time}")

# def replace_csv_value_spark(csv_file_path: str, column_name: str, new_column_value: str):
#    ps = SparkSession.builder.getOrCreate()
#    start = datetime.datetime.now()
#    path = csv_file_path.split(".csv")
#    csv = (
#        ps.read.options(header=True, delimiter="|")
#        .csv(csv_file_path)
#        .fillna("")
#    )
#    csv2 = csv.withColumn(column_name, lit(new_column_value))
# csv2.show(truncate=False)
#    csv2.write.mode("overwrite").csv(
#        f"{path[0]}_column_renamed_spark.csv"
#    )
#    end = datetime.datetime.now()
#    total_time = end - start

#   print(f"Time elapsed with spark: {total_time}")
