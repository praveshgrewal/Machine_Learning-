import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df,iris.target_names

df,target_names = load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])
#give title to sliderbar

# st.slider("Parameters")
sepal_length= st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width= st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length= st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width= st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

features = [[sepal_length,sepal_width,petal_length,petal_width]]

# st.write("The features are ", features)

#prediction

prediction = model.predict(features)

st.title("The prediction  species is ", target_names[prediction[0]])
