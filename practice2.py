import streamlit as st
from scipy.optimize import minimize

def optimize_function(x):
    return x**2 + 5*x + 6

def optimize():
    st.title("Optimization App")
    x0 = st.number_input("Initial value for x")
    res = minimize(optimize_function, x0)
    st.write("Optimized value for x: ", res.x)
    st.write("Optimized function value: ", res.fun)

if __name__=='__main__':
    optimize()