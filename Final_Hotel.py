
import numpy as np
from flask import Flask,request,jsonify,render_template
import  pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('xb_boost.pkl')
sc = joblib.load('xg_boost_scalar.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_col = ['name', 'Distance to City centre(km)', 'Distance to Airport(km)',
       'Pool', 'Free parking', 'Airport transfer', 'Spa', 'Restaurant', 'Gym',
       'Bar', 'Bathtub', 'Meeting Facilities', 'Connecting rooms available',
       'Pet-friendly', 'Kitchen', 'Internet access', 'Check_in_year',
       'Check_in_month', 'Check_in_day', 'Check_out_year', 'Check_out_month',
       'Check_out_day', 'Banglore', 'Bhopal', 'Chandigarh', 'Chennai', 'Goa',
       'Gurgaon', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata', 'Kullu', 'Leh',
       'Lucknow', 'Mumbai', 'Munnar', 'Nagpur', 'New Delhi', 'Noida', 'Pune',
       'Rishikesh', 'Tirupati, Andhra Pradesh, India', 'Varanasi',
       'Visakhapatnam, Andhra Pradesh, India']
    
    data = np.array([[x for x in request.form.values()]])
    data = sc.transform(data)
    
    prediction = model.predict(data)
    
    print(prediction)
    return render_template('index.html',prediction_text=prediction)

if __name__ == '__main__':
    app.run()
    
    