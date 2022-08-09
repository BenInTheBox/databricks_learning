# Databricks notebook source
from src.player_class import Tank
from src.player import Player

# COMMAND ----------

player1: Player = Tank('Bob')

# COMMAND ----------

player1.print_stats()

# COMMAND ----------

player1.level_up()

player1.print_stats()

# COMMAND ----------


