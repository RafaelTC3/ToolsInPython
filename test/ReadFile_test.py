import os
import pytest
import pandas
import ReadFile


def test_replace_csv_value_pandas():
    print(os.getcwd())
    ReadFile.replace_csv_value("rsc/test.csv", "birth_date", "99/99/9999")
    df = pandas.read_csv("rsc/test_column_renamed.csv", delimiter="|", dtype=str)
    birth_date = df["birth_date"].values[0]
    assert str(birth_date) == "99/99/9999"  # add assertion here


#   def test_replace_csv_value_pyspark(self):
#       ReadFile.replace_csv_value_spark("rsc/test.csv", "birth_date", "00/00/0000")
#       ps = pyspark.sql.SparkSession.builder.getOrCreate()
#       df = ps.read.options(header=True, delimiter="|").csv("rsc/test_column_renamed_spark.csv").fillna("")
#       birth_date = df["birth_date"][0]
#       self.assertEqual(str(birth_date), "00/00/0000")  # add assertion here