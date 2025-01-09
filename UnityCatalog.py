# Databricks notebook source
# MAGIC %sql
# MAGIC show catalogs

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog if not exists first_catalog;
# MAGIC use catalog first_catalog;
# MAGIC create schema if not exists bronze;
# MAGIC create schema if not exists silver;
# MAGIC create schema if not exists gold;
# MAGIC create schema if not exists dev;
# MAGIC
# MAGIC use schema dev;
# MAGIC create table if not exists people
# MAGIC (
# MAGIC   id bigint primary key not null generated always as identity,
# MAGIC   name varchar(50),
# MAGIC   gender varchar(10)
# MAGIC );
# MAGIC
# MAGIC Insert into people (name, gender)
# MAGIC -- VALUES ('Joe', 'male');
# MAGIC VALUES ('Jane', 'female');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from people
