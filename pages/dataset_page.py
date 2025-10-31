import streamlit as st
from cloud import show_data_main, show_data_result,plots_data

def dataset_page():
    plots_data()
    show_data_main()
    show_data_result()
    return

if __name__=="__main__":
    dataset_page()
