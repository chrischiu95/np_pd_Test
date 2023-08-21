#  streamlit run d:\Users\Iris\First.py [ARGUMENTS

import numpy as np
import pandas as pd
import streamlit as st

st.title("Test numpy/pandas SDK")
a = np.array([1,2,3,4,5])

b = st.number_input("pls input : ",key="num_b")

if st.button("") : 
    a = np.append(a,b)
    st.write(a)
    

