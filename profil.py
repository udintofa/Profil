import streamlit as st
import numpy as np
import pandas as pd

tab1, tab2, tab3 = st.tabs(["Profil", "Pengalaman", "Pasangan"])

with tab1:
    st.header("Profil dari Udin")
    data = [["Nama","Muchammad Udin Mustofa"], ['Panggilan',"Udin"],["Tempat Lahir","Magelang"],["Tanggal Lahir",pd.to_datetime("2003-07-20")],["Alamat","Magelang"]]
    dd = pd.DataFrame(data)
    st.write(dd)
with tab2:
    st.header("Pengalaman Udin")
    st.write("""Udin tidak memiliki pengalaman""")

with tab3:
    st.header("Pasangannya Udin")
    st.write("Zahra si Tukang rewel")