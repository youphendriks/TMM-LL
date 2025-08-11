import streamlit as st
from functions.get_layout import navigation

def main():
    navigation()

if __name__ == "__main__":
    st.set_page_config(page_title="TMM Legacy League")
    main()
