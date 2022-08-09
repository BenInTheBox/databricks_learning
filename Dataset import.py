# Databricks notebook source
# MAGIC %md
# MAGIC # Lib installation and import

# COMMAND ----------

!pip install xlrd
!pip install dbutils

# COMMAND ----------

import urllib
import pandas as pd
import dbutils

# COMMAND ----------

# MAGIC %md
# MAGIC # Data loading

# COMMAND ----------

row_data = pd.read_excel('Loyalty.xls')


# COMMAND ----------

display(row_data)
display(row_data.describe())
#dbutils.data.summarize(row_data)

# COMMAND ----------

# MAGIC %md
# MAGIC # Write in delta table

# COMMAND ----------


