import streamlit as st
import seaborn as sns
import pandas as pd

df = pd.read_csv("diamonds.csv")

st.set_page_config(page_title="Dataset",layout="wide")
st.header("Diamond Dataset Preview")

dt= st.radio('Show in dataset (Head/Tail)',('Head','Tail'))
if dt=='Head':
    st.dataframe(df.head(10))
else:
    st.dataframe(df.tail(10))

ds= st.checkbox('Show the whole dataset')
if ds:
    st.dataframe(df)

dssh= st.selectbox('Check',('Select','Shape','Columns','Statistical Description'))
if dssh=='Shape':
    st.write(df.shape)
elif dssh=='Columns':
    st.write(df.columns)
elif dssh=='Select':
    " "
elif dssh=='Statistical Description':
    st.write(df.describe())

st.header('Data Visualisation')
viz= st.radio('Feature Analysis',('Cut','Color','Clarity','Carat'))
if viz=='Cut':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.countplot(data=df, x='cut')
    st.pyplot()
elif viz=='Color':
    sns.countplot(data=df, x='color')
    st.pyplot()
elif viz=='Clarity':
    sns.countplot(data=df, x='clarity')
    st.pyplot()
elif viz=='Carat':
    st.bar_chart(data=df, x='carat', y='price')
