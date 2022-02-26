from unittest import result
from flask import Flask, request, render_template
import joblib
import pandas as pd
from sympy import re
import xgboost

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # year = request.form.get('Year')
        # price = request.form.get('Present_Price')
        # kms = request.form.get('Kms_Driven')
        # fuel = request.form.get('Fuel_Type')
        # seller = request.form.get('Seller_Type')
        # trans = request.form.get('Transmission')
        # own = request.form.get('Owner')
        # data = {
        #     'Year':int(year),
        #     'Present_Price':float(price),
        #     'Kms_Drivem':int(kms),
        #     'Fuel_Type':fuel,
        #     'Seller_Type':seller,
        #     'Transmission':trans,
        #     'Owner':own
        # }

        data = {}
        data["Year"]=int(request.form["Year"])
        data["Present_Price"]=float(request.form["Present_Price"])
        data["Kms_Driven"]=int(request.form["Kms_Driven"])
        data["Fuel_Type"]=request.form["Fuel_Type"]
        data["Seller_Type"]=request.form["Seller_Type"]
        data["Transmission"]=request.form["Transmission"]
        data["Owner"]=int(request.form["Owner"])

        df = pd.DataFrame([data])
        df["Year"] = 2018 - df["Year"]
        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
        df = scaler.transform(df)
        result = model.predict(df)
        return render_template('result.html', result= f'$ {result[0]:.4f}')

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return 'My API server is running.'
    if request.method == 'POST':
        data = {}
        data["Year"]=int(request.json['Year'])
        data["Present_Price"]=float(request.json['Present_Price'])
        data["Kms_Driven"]=int(request.json['Kms_Driven'])
        data["Fuel_Type"]=request.json['Fuel_Type']
        data["Seller_Type"]=request.json['Seller_Type']
        data["Transmission"]=request.json['Transmission']
        data["Owner"]=int(request.json['Owner'])
        df = pd.DataFrame([data])
        df['Year'] = 2018 - df['Year']
        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
        df = scaler.transform(df)
        result = model.predict(df)
        return {'Predicted price': f'$ {result[0]:.4f}'}

if __name__ == '__main__':
    scaler = joblib.load(open("scaler.joblib","rb"))
    model = joblib.load(open("xgb_model.joblib","rb"))
    columns = joblib.load("columns.joblib") 
    app.run(debug=True)