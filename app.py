# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:54:04 2020

@author: Pratik
"""


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

with open('HDClassifierRF.pkl','rb')as pickle_file:
    model=pickle.load(pickle_file)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    
    
    
    if request.method == 'POST':
        
        Age = int(request.form['age'])
       
        
        diabetes = request.form['diabetes']
        if(diabetes=='Yes'):
            diabetes=1
        else:
            diabetes=0
            
        smoking = request.form['smoking']
        if(smoking=='Yes'):
            smoking=1
        else:
            smoking=0
        
        Gender = request.form['sex']
        if(Gender=='Male'):
            Gender_Male=1
        else:
            Gender_Male=0
            
        high_blood_pressure = request.form['high_blood_pressure']
        if(high_blood_pressure=='yes'):
            high_blood_pressure=1
        else:
            high_blood_pressure=0
            
        anaemia = request.form['anaemia']
        if(anaemia=='yes'):
            anaemia=1
        else:
            anaemia=0
            
            
        creatinine_phosphokinase = int(request.form['creatinine_phosphokinase'])
        ejection_fraction = int(request.form['ejection_fraction'])
        platelets = float(request.form['platelets'])
        serum_creatinine= float(request.form['serum_creatinine'])
        serum_sodium= int(request.form['serum_sodium'])
        
        time= int(request.form['time'])
        
        
        prediction=model.predict([[Age, anaemia, creatinine_phosphokinase, diabetes,
       ejection_fraction, high_blood_pressure, platelets,
       serum_creatinine, serum_sodium, Gender_Male, smoking, time]])
        output=prediction[0]
        if output ==0:
           return render_template('index.html',prediction_text = "Will Survive")
        else:
           return render_template('index.html',prediction_text = "High Risk of Death ")
    #else:
      # return render_template('index.html')

if __name__=="__main__":
    app.run()