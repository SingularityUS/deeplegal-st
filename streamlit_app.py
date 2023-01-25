!pip install --upgrade pip
!pip install farm-haystack
!pip install opensearch-py
!pip install requests-aws4auth
!pip install tqdm
!pip install streamlit

import logging

logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("haystack").setLevel(logging.INFO)

#Gathering the PostgreSQL database
import psycopg2
import pandas as pd
import numpy as np
import requests
import json
from bs4 import BeautifulSoup

from haystack import document_stores
import streamlit as st
from copy import deepcopy

#CONNECT to postgre DB

try:
    # create connection and cursor
    conn = psycopg2.connect(dbname=st.secrets[postgres_database],
                            user=st.secrets[postgres_port],
                            password=st.secrets[postgres_password], 
                            host=st.secrets[postgres_address], 
                            port=st.secrets[postgres_port], 
                            sslmode='require')
    print('connected successfully')
    st.write('sucessfully contencted to case database')
except:
    print("can't connect to db")
    st.write('failed to connect to case database')
#get the SQL Column Names

cur = conn.cursor()
page = 1
