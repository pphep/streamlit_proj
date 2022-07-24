import streamlit as st

st.title('Additon of two numbers')
a = st.number_input('Enter first number')
b = st.number_input('Enter second number')
result = a + b
st.write(a, ' + ', b , '= ', result)
