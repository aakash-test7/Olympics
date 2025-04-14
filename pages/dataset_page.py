import streamlit as st
from cloud import show_data_main, show_data_result

def dataset_page():
    show_data_main()
    show_data_result()
    return

if __name__=="__main__":
    dataset_page()