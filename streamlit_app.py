import streamlit as st
import pandas as pd

st.title("Machine learning app")

st.info("This app is built using ML")

with st.expander("Data"):
    st.write("**Raw data**")
    df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
    st.write(df)

    st.write("**X**")
    X = df.drop("species", axis=1)
    st.write(X)

    st.write("**y**")
    y = df.species
    st.write(y)

with st.expander("Data Visualization"):
    st.scatter_chart(data=df, x="bill_length_mm", y='body_mass_g', color="species")

# Sidebar inputs
with st.sidebar:
    st.header("Input Features")
    island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    gender = st.selectbox('Gender', ('male', 'female'))
    bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.0)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 200.0)
    body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4200.0)

# Create DataFrame from inputs
data = {
    'island': island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'body_mass_g': body_mass_g,
    'sex': gender
}
input_df = pd.DataFrame(data, index=[0])

# Combine input with dataset
input_penguins = pd.concat([input_df, X], axis=0)

with st.expander('Input features'):
    st.write("**Input Pengiuns**")
    input.df
    st.write("**Combined data**")
    input_pengiuns
    


