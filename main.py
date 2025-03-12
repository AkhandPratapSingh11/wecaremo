import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

import streamlit as st

def main():
    try:
        from frontend.frontend import main as frontend_main
        frontend_main()
    except ImportError as e:
        st.error(f"Import Error: {e}")
        st.error("Please check your project structure and Python path")
        st.error(f"Python Path: {sys.path}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        st.error(f"Traceback: {sys.exc_info()}")

if __name__ == "__main__":
    main()