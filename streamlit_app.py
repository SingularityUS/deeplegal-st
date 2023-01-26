

#Gathering the PostgreSQL database
import psycopg2
import pandas as pd
import numpy as np
#import requests
#import json
from bs4 import BeautifulSoup

from haystack import document_stores
import streamlit as st
#from copy import deepcopy

#CONNECT to postgre DB

try:
    # create connection and cursor
    conn = psycopg2.connect(dbname=st.secrets[postgres_database],
                            user=st.secrets[postgres_username],
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
