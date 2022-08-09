# Databricks notebook source
# MAGIC %md
# MAGIC # Import libraries

# COMMAND ----------

import pandas as pd
import os

# COMMAND ----------

pd.read_excel("Loyalty.xls")

# COMMAND ----------

os.getcwd()

# COMMAND ----------

# MAGIC %md
# MAGIC # Get data

# COMMAND ----------

# Define the working directory
working_directory = ""

# COMMAND ----------

# Get the delta table file path
file_path = ""

# Read delta table as spark dataframe
df = spark.read.format("delta").load(file_path)

# COMMAND ----------

# Get the delta table directory

# List all elements in the delta directory
dbutils.fs.ls(delta_directory)

# COMMAND ----------


