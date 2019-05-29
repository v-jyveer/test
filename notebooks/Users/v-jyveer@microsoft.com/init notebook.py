# Databricks notebook source
dbutils.fs.mkdirs("dbfs:/databricks/scripts/globalinit")

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts/globalinit/postgresql-install.sh"))

# COMMAND ----------

dbutils.fs.put("dbfs:/databricks/scripts/globalinit/postgresql-install.sh" ,"""
#!/bin/bash

echo "hello" >> /hello.txt
""", True)

# COMMAND ----------

# MAGIC %sh head /dbfs/databricks/scripts/globalinit/postgresql-install.sh

# COMMAND ----------

dbutils.fs.put("/databricks/scripts/globalinit/postgresql-install.sh","""
#!/bin/bash
wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar http://central.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar
wget --quiet -O /mnt/jars/driver-daemon/postgresql-42.2.2.jar http://central.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar""", True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts/"))

# COMMAND ----------

dbutils.fs.ls ("dbfs:/cluster-logs/")
