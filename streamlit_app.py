

#Gathering the PostgreSQL database
import psycopg2
import pandas as pd
import numpy as np
import requests #for aws authenticaion
#import json
from bs4 import BeautifulSoup

from haystack import document_stores
import streamlit as st
#from copy import deepcopy

#CONNECT to postgre DB

try:
    # create connection and cursor
    conn = psycopg2.connect(dbname=st.secrets["postgres_database"],
                            user=st.secrets["postgres_username"],
                            password=st.secrets["postgres_password"], 
                            host=st.secrets["postgres_address"], 
                            port=st.secrets["postgres_port"], 
                            sslmode='require')
    print('connected successfully')
    st.write('sucessfully contencted to case database')
except:
    print("can't connect to db")
    st.write('failed to connect to case database')
#get the SQL Column Names

cur = conn.cursor()
page = 1
#####################################################################
#######Openseaerch Connection#############################
########################################3
from haystack.document_stores import InMemoryDocumentStore
from haystack.document_stores import OpenSearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline

document_store = OpenSearchDocumentStore(host= st.secrets["opensearch_address"], username= st.secrets["opensearch_username"], password= st.secrets["opensearch_password"], port=443) 
retriever = BM25Retriever(document_store=document_store)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

pipe = ExtractiveQAPipeline(reader, retriever)

 prompt_=st.text_area("Enter your query here",placeholder="""Q:What is the density of seawater?""")
prediction = pipe.run(
    query=prompt_,
    params={
        "Retriever": {"top_k": 10},
        "Reader": {"top_k": 5}
    }
)

st.write(prediction)
from haystack.utils import print_answers

query_output= print_answers(
    prediction,
    details="minimum" ## Choose from `minimum`, `medium`, and `all`
)

st.write(query_output)
