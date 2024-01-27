import streamlit as st
def calculate_emi(p,n,r):
	emi = p * (r/100)*(1+r/100)**n / ((1+r/100)**n-1)
	st.write("emi calculated ", emi)
st.title("EMI Calculator")
p = st.slider("value of principle amount", 1000.0, 1000000.0)
r = st.slider("value of rate of interest", 1.0, 15.0)
n = st.slider("value of tenure", 1.0, 30.0)
n = n*12
r = r/12
if st.button("calculate"):
	calculate_emi(p,n,r)
