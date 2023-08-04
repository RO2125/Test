# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 16:05:46 2023

@author: RO2125
"""

import os
import pandas as pd
import numpy as np

so_weekly=pd.read_csv(r'C:\Users\RO2125\Downloads\Daily_Amazon_Inventory.csv',parse_dates=(['Date']))
so_weekly.dtypes
nc=pd.read_excel(r'C:\Users\RO2125\OneDrive - Zebra Technologies\Documents\my_projects\Philips\AMAZON_RELEASE\Data\sell_out_analysis\12nc.xlsx', sheet_name='12NC')
nc.head()
nc=nc[['12nc','mkey','sku','country']]
nc.head()
nc.shape
nc=nc.drop_duplicates()

so_weekly.columns

so_12nc=pd.merge(nc,so_weekly,on=(['sku','country']),how='left')
so_12nc.head()
so_12nc=so_12nc[['12nc','Date','Ordered units Total']]
so_12nc=so_12nc.groupby(['12nc','Date']).sum().reset_index()
so_12nc.head()
so_12nc.to_csv(r'C:\Users\RO2125\Downloads\so_12nc.csv')
