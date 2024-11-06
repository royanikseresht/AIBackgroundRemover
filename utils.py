import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
import pandas as pd
import numpy as np

def css_local(filepath: str):
    """
    Method to load the desired stylesheet from the given filepath
    """
    with open(filepath) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def lottie_local(filepath: str):
    """
    Method to load the desired Lottie Animation from the given filepath
    """
    with open(filepath, "r") as f:
        return json.load(f)

def lottie_url(url: str):
    """
    Method to load the desired Lottie Animation from a given URL
    """
    try:
        r = requests.get(url)
        r.raise_for_status()  # Will raise an exception for 4xx/5xx HTTP errors
        return r.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching Lottie animation from URL: {e}")
        return None

def display_map(l1: list = [22.572645], l2: list = [88.363892], z: int = 9) -> None:
    """
    Method to display the desired coordinates on a map using OpenStreetMap API
    Parameters
    -----------
    l1 : list
        Desired latitude coordinate(s); default set for Kolkata ([22.572645])
    l2 : list
        Desired longitude coordinate(s); default set for Kolkata ([88.363892])
    z  : int 
        Desired zoom level; default set to metropolitan area level (9)
    Returns
    --------
    None
    
    See Also
    --------
    For plotting multiple cities, simply pass their respective latitude and longitude coordinates in
    the same list.
    """
    # Ensure that latitude and longitude lists are the same length
    if len(l1) != len(l2):
        st.error("Latitude and Longitude lists must have the same length!")
        return
    
    map_data = pd.DataFrame({"latitude": np.array(l1), "longitude": np.array(l2)})
    st.map(map_data, zoom=z)

def hide_footer():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
