# Databricks notebook source
# MAGIC %md
# MAGIC # Lib installation and import

# COMMAND ----------

!pip install xlrd

# COMMAND ----------

import urllib
import numpy as np
import pandas as pd
import pyspark
import pyspark.pandas as pspd

# COMMAND ----------

# MAGIC %md
# MAGIC # Data loading

# COMMAND ----------

row_data: pd.DataFrame = pd.read_excel('Loyalty.xls')
row_data: pspd.DataFrame = pspd.DataFrame(row_data)

# COMMAND ----------

dbutils.data.summarize(row_data)

# COMMAND ----------

# MAGIC %md
# MAGIC # Write in delta table

# COMMAND ----------

row_data: pyspark.sql.dataframe.DataFrame = row_data.to_spark()
#row_data: pyspark.sql.dataframe.DataFrame = spark.createDataFrame(row_data) 


# COMMAND ----------

wprking_dir = "UNKNOWN"

# COMMAND ----------

row_data.write.format("delta").mode("overwrite").save(working_dir)

# COMMAND ----------

import os
os.getcwd()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------


