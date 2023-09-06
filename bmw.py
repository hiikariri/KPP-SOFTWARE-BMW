import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header('KPP BMW SOFTWARE')
st.subheader('Nama : Nehemy Davis Suryanto')

ecg_1 = np.loadtxt('DATA ECG.txt', dtype='float')
n_data = len(ecg_1)
ecg_arr = np.arange(n_data)
st.line_chart(ecg_1)
plt.figure(figsize=(20, 8))
plt.plot(ecg_arr, ecg_1)
st.pyplot(plt)
