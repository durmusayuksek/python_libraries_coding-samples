from sklearn.preprocessing import OrdinalEncoder
from xgboost import XGBRegressor
from IPython.display import HTML
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.error(
    """
## Car Price Prediction App

##### The magic of predicting the car prices according to the 6 features of a car.
##### Come and try :cyclone:
"""
)

def user_input_features():
    make_model = st.sidebar.selectbox('Make-Model',
        ("Audi A3",
        "Audi A1",
        "Opel Astra",
        "Opel Insignia",
        "Opel Corsa",
        "Renault Clio",
        "Renault Espace",
        "Renault Duster"),
    )
    horsepower = st.sidebar.slider("Horsepower (kw)", 40, 239, 50)
    km = st.sidebar.number_input("Kilometers", value=1000, step=1)
    age = st.sidebar.radio('Age of the Car', [0, 1, 2, 3])
    gear_type = st.sidebar.selectbox('Select a Gear Type', ['Automatic', 'Manual', 'Semi-automatic'])
    gears = st.sidebar.radio('Number of Gears', [5, 6, 7, 8])
    new_df = {'make_model':make_model,
              'hp_kW':horsepower,
              'km':km,
              'age':age,
              'Gearing_Type':gear_type,
              'Gears':gears}
    features = pd.DataFrame(new_df, index=[0])
    return features
input_df = user_input_features()

data = pd.read_csv("feature_selected_df.csv")
data2 = data.drop(columns='price')
use_df = pd.concat([input_df, data2], axis=0)

cat = data2.select_dtypes('object').columns
enc = OrdinalEncoder()
use_df[cat] = enc.fit_transform(use_df[cat])
real_df = use_df[:1]
st.subheader('User Input Features')
resa = real_df.astype('int')
resa = resa.rename(columns={'make_model':'Make & Model',
                      'hp_kW':'Hp',
                      'km':'Km',
                      'age':'Age',
                      'Gearing_Type':'Gearing Type',
                      'Gears': 'Number of Gears'})
st.write(HTML(resa.to_html(index=False)))

load_pickle_rf = pickle.load(open('streamlit_final_rf', 'rb'))
load_pickle_xgb = pickle.load(open('streamlit_final_xgb', 'rb'))

prediction_rf = load_pickle_rf.predict(real_df)
prediction_rf = pd.DataFrame(prediction_rf, columns=['Random Forest'])
prediction_xgb = load_pickle_xgb.predict(real_df)
prediction_xgb = pd.DataFrame(prediction_xgb, columns=['XGBoost'])
st.subheader('Prediction')
st.write('Click predict to see the prediction')
if st.button("Predict"):
    res = pd.concat([prediction_rf, prediction_xgb], axis=1)
    res = res.apply(lambda x: int(x))
    res = pd.DataFrame(res, columns=['Price'])
    st.write(res)
    st.write('Predictions in US Dollars')

    a = input_df['make_model']

    if a[0] == 'Audi A3':
        img = Image.open('audi a3.webp')
    elif a[0] == 'Audi A1':
        img = Image.open('audi a1.jpeg')
    elif a[0] == 'Opel Astra':
        img = Image.open('astra.jpeg')
    elif a[0] == 'Opel Insignia':
        img = Image.open('insignia.jpeg')
    elif a[0] == 'Opel Corsa':
        img = Image.open('corsa.jpeg')
    elif a[0] == 'Renault Clio':
        img = Image.open('clio.jpeg')
    elif a[0] == 'Renault Espace':
        img = Image.open('espace.jpeg')
    elif a[0] == 'Renault Duster':
        img = Image.open('duster.webp')
    st.error(f'**{a[0]}**')
    st.image(img, use_column_width=True)