import sys
import os
import logging

def print_python_path():
    print("Python Path:")
    for path in sys.path:
        print(path)

def check_module_imports():
    print("\nChecking Module Imports:")
    try:
        import streamlit as st
        print("Streamlit imported successfully")
    except Exception as e:
        print(f"Streamlit import error: {e}")

    try:
        from backend.chatbot import EmoCareAssistant
        print("EmoCareAssistant imported successfully")
    except Exception as e:
        print(f"EmoCareAssistant import error: {e}")

def main():
    logging.basicConfig(level=logging.INFO)
    
    print("Current Working Directory:", os.getcwd())
    print_python_path()
    check_module_imports()

if __name__ == "__main__":
    main()