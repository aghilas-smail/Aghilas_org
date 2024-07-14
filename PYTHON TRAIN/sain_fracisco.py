import bq_helper
from bq_helper import BigQueryHelper
# https://www.kaggle.com/sohier/introduction-to-the-bq-helper-package
sf = bq_helper.BigQueryHelper(active_project="bigquery-public-data",
                                   dataset_name="san_francisco")


bq_assistant = BigQueryHelper("bigquery-public-data", "san_francisco")
bq_assistant.list_tables()