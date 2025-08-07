import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

class DatabaseClient:
    def __init__(self, uri: str):
        self._client = MongoClient(uri, server_api=ServerApi("1"))

    def get_client(self):
        return self._client

db_client = DatabaseClient(uri=st.secrets.mongo.database_url)