import streamlit as st
import pandas as pd

st.title("Machine learning app")

st.info("This app is build using ml")

with st.expander("Data"):
  st.write("**Raw data**")
  df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write("**X**")
  X=df.drop("species",axis=1)
  X

  st.write("**y**")
  y=df.species
  y

with st.expander("Data Visualization"):
  st.scatter_chart(data=df,x="bill_length_mm",y='body_mass_g',color="species")


#Data  Preparation

with st.sidebar:
  st.header("Input Features")
  #"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island=st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  island=st.selectbox('Gender',('Gender',('male','female')))
  bill_length_mm=st.slider('Bill length (mm)',32.1,59.6,43.9)
  
                   
