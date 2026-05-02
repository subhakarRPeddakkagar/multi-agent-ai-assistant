import os
import streamlit as st

def get_secret(key: str):
    # ✅ FIX: safely check streamlit secrets
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass  # ignore if secrets not available

    # ✅ fallback to .env / local env
    return os.getenv(key)