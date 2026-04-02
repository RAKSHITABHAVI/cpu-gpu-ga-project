import streamlit as st

st.title(" CPU vs GPU Flight Scheduling (GA)")

n = st.slider("Number of Flights", 10, 200, 50)

def cpu_ga(n):
    return n * n * 0.4   # replace with your real logic

def gpu_ga(n):
    return n * n * 0.01  # replace with your real logic

if st.button("Run Comparison"):
    cpu_time = cpu_ga(n)
    gpu_time = gpu_ga(n)

    st.write("### Results")
    st.write("CPU Time:", cpu_time)
    st.write("GPU Time:", gpu_time)

    st.bar_chart({"CPU": cpu_time, "GPU": gpu_time})

    st.success("GPU is faster ")
