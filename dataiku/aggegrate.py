# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
orders = dataiku.Dataset("orders")
orders_df = orders.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

orders_by_customer_df = orders_df.assign(total=orders_df.tshirt_price*orders_df.tshirt_quantity
       ).groupby(by="customer_id"
                ).agg({"pages_visited":"mean",
                       "total":"sum"}).reset_index()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
orders_by_customer_df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
orders_by_customer = dataiku.Dataset("orders_by_customer")
orders_by_customer.write_with_schema(orders_by_customer_df)