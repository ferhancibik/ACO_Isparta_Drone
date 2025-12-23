import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_api_key():
    if hasattr(st, 'secrets') and 'GOOGLE_MAPS_API_KEY' in st.secrets:
        return st.secrets['GOOGLE_MAPS_API_KEY']
    return os.getenv('GOOGLE_MAPS_API_KEY', '')

ALPHA = 1.0
BETA = 2.0
EVAPORATION_RATE = 0.5
Q = 100

