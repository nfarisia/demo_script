# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read the dataset as a Pandas dataframe in memory
# Note: here, we only read the first 100K rows. Other sampling options are available
dataset_customers_stacked_prepared = dataiku.Dataset("customers_stacked_prepared")
df = dataset_customers_stacked_prepared.get_dataframe(limit=100000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Get some simple descriptive statistics
pdu.audit(df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df["campaign"].value_counts()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dataset_orders = dataiku.Dataset("orders_by_customer")
df_orders = dataset_orders.get_dataframe(limit=100000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_joined = df.merge(df_orders,left_on="customerID",right_on="customer_id")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
pd.pivot_table(df_joined.reset_index(),
  index='index',
  columns='campaign',
  values=['total']).plot.hist(normed=True,subplots=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
customers_enriched = dataiku.Dataset("customers_enriched")
customers_enriched.write_with_schema(df_joined)