import sys
import os
import streamlit as st
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='emoCare.log'
)

def main():
    try:
        # Dynamically add project root to Python path
        project_root = os.path.abspath(os.path.dirname(__file__))
        sys.path.insert(0, project_root)

        # Import frontend main function
        from frontend.frontend import main as frontend_main
        
        # Run frontend
        frontend_main()

    except ImportError as e:
        st.error(f"Import Error: {e}")
        st.error("Please check your project structure and Python path")
        logging.error(f"Import error: {e}", exc_info=True)
    
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected error: {e}", exc_info=True)

if __name__ == "__main__":
    main()