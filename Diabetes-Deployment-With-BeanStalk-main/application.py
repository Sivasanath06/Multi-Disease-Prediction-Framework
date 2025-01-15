from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

model1 = pickle.load(open("Model/diabetes.pkl", "rb"))
model2 = pickle.load(open("Model/heart_disease.pkl", "rb"))
model3 = pickle.load(open("Model/kidney.pkl", "rb"))
model4 = pickle.load(open("Model/lung.pkl", "rb"))
encoder = pickle.load(open("Model/lung1.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')
# Route for Single data point prediction
@app.route('/diabetes',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        Pregnancies=int(request.form.get('Pregnancies'))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        predict=model1.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
       
        if predict[0] ==1 :
            result = 'Non-Diabetic'
        else:
            result ='Diabetic'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('diabetes.html')



## Route for homepage



@app.route('/heart',methods=['GET','POST'])
def predict_datapoint1():
    result=""

    if request.method=='POST':

        age=int(request.form.get("age"))
        sex = int(request.form.get('sex'))
        cp = int(request.form.get('cp'))
        trestbps = int(request.form.get('trestbps'))
        chol = int(request.form.get('chol'))
        fbs = int(request.form.get('fbs'))
        restecg = int(request.form.get('restecg'))
        thalach = int(request.form.get('thalach'))
        exang = int(request.form.get('exang'))
        oldpeak = float(request.form.get('exang'))
        slope = int(request.form.get('exang'))
        ca = int(request.form.get('ca'))
        thal = int(request.form.get('thal'))
        


        


        predict=model2.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope,ca,thal]])
       
        if predict[0] ==1:
            result = 'Heart_Disease_Detected'
        if predict[0] ==0:
            result ='Heart_Disease_Not_Detected'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('heart_disease.html')


@app.route('/lung',methods=['GET','POST'])
def predict_datapoint2():
    result = ""

    if request.method == 'POST':
        gender = request.form.get('Gender')
        # Convert sex to 1 for 'M' and 0 for 'F'
        sex = 1 if gender == 'M' else 0

        age = float(request.form.get('Age'))
        smoking = float(request.form.get('Smoking'))
        yellow_fingers = float(request.form.get('Yellow fingers'))
        anxiety = float(request.form.get('Anxiety'))
        peer_pressure = float(request.form.get('Peer_pressure'))
        chronic_disease = float(request.form.get('Chronic Disease'))
        fatigue = float(request.form.get('Fatigue'))
        allergy = float(request.form.get('Allergy'))
        wheezing = float(request.form.get('Wheezing'))
        alcohol = float(request.form.get('Alcohol'))
        coughing = float(request.form.get('Coughing'))
        shortness_of_breath = float(request.form.get('Shortness of Breath'))
        swallowing_difficulty = float(request.form.get('Swallowing Difficulty'))
        chest_pain = float(request.form.get('Chest pain'))
        
        predict=model4.predict([[sex, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]])
        # Assuming predict is the result of the ML prediction
        if predict[0] == 'yes':
            # Convert output to 1 for 'yes' and 0 for 'no'
            result = "lung disease detected"
        else:
            result = 0
        
        return render_template('single_prediction.html', result=result)

    else:
        return render_template('lung_cancer.html')

@app.route('/kidney',methods=['GET','POST'])
def predict_datapoint3():
    result = ""

    if request.method == 'POST':
        
        age = float(request.form.get('Age'))
        bp = float(request.form.get('Blood Pressure'))
        sg = float(request.form.get('Specific Gravity'))
        al = float(request.form.get('Albumin'))
        su = float(request.form.get('Sugar'))
        rbc = 1 if request.form.get('Red Blood Cells') == 'normal' else 0
        pc = 1 if request.form.get('Pus Cells') == 'normal' else 0
        pcc = 1 if request.form.get('Pus Cell Clumps') == 'present' else 0
        ba = 1 if request.form.get('Bacteria') == 'present' else 0
        bgr = float(request.form.get('Blood Glucose Random'))
        bu = float(request.form.get('Blood Urea'))
        sc = float(request.form.get('Serum Creatinine'))
        sod = float(request.form.get('Sodium'))
        pot = float(request.form.get('Potassium'))
        hemo = float(request.form.get('Hemoglobin'))
        pcv = float(request.form.get('Packed Cell Volume'))
        wc = float(request.form.get('White Blood Cell Count'))
        rc = float(request.form.get('Red Blood Cell Count'))
        htn = 1 if request.form.get('Hypertension') == 'yes' else 0
        dm = 1 if request.form.get('Diabetes Mellitus') == 'yes' else 0
        cad = 1 if request.form.get('Coronary Artery Disease') == 'yes' else 0
        appet = 1 if request.form.get('Appetite') == 'good' else 0
        pe = 1 if request.form.get('Pedal Edema') == 'yes' else 0
        ane = 1 if request.form.get('Anemia') == 'yes' else 0
        
        predict=model3.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet,pe,ane]])
        
        if predict[0] == 'ckd':
            result = 1
        else:
            result = 0
        
        return render_template('single_prediction.html', result=result)

    else:
        return render_template('kidney_disease.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")