import requests
import pandas as pd
from pandas import json_normalize
import yaml

def yaml_cred(item_name, cred_path):
    """Read YAML config file"""
    with open(cred_path) as file: 
        documents = yaml.full_load(file)
        for item, doc in documents.items():
            if item == item_name:
                return doc

FMP_DOMAIN = 'https://financialmodelingprep.com'
TOKEN = 'YOUR_API_KEY'

