from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/get_feature_names')
def get_feature_names():
    response = {'Columns' : util.show_feature_names()}
    return response

@app.route('/predict_rain_tdy_tmrw',methods=['POST'])
def predict_rain_tdy_tmrw():

    MinimumTemp = float(request.form['i_MinTemp'])
    MaximumTemp = float(request.form['i_MaxTemp'])
    Rainfall = float(request.form['i_Rainfall'])
    Evaporation = float(request.form['i_Evaporation'])
    Sunshine = float(request.form['i_Sunshine'])
    WindGustSpeed = float(request.form['i_WindGustSpeed'])
    WindSpeed9am = float(request.form['i_WindSpeed9am'])
    WindSpeed3pm = float(request.form['i_WindSpeed3pm'])
    Humidity9am = float(request.form['i_Humidity9am'])
    Humidity3pm = float(request.form['i_Humidity3pm'])
    Pressure9am = float(request.form['i_Pressure9am'])
    Pressure3pm = float(request.form['i_Pressure3pm'])
    Cloud9am = float(request.form['i_Cloud9am'])
    Cloud3pm = float(request.form['i_Cloud3pm'])
    Temp9am = float(request.form['i_Temp9am'])
    Temp3pm = float(request.form['i_Temp3pm'])
    Month = float(request.form['i_Month'])
    Day = float(request.form['i_Day'])

    Location = request.form['i_Location']
    WindGustDir = request.form['i_WindGustDir']
    WindDir9am = request.form['i_WindDir9am']
    WindDir3pm = request.form['i_WindDir3pm']
    

    Weather_pred = util.predict_RainTodayTomarrow(MinimumTemp,MaximumTemp,Rainfall,Evaporation,Sunshine,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,Month,Day,Location,WindGustDir,WindDir9am,WindDir3pm) 

    response = jsonify({'Weather_Report' : Weather_pred })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response    

app.run()
