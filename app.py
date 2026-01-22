import streamlit as st
name = st.text_input(" Vavedete tekst.")
grade = st.number_input("Vuvedete ocenka.")
st.button(Proverka)
if ( grade > 6):
  st.warning("Ocenkata e po golqma ot 6")
  
