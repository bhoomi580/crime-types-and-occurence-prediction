from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')  # localhost:5000
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])  # localhost:5000/login
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('loginvalidation', username=username, password=password))
    return render_template('login.html')

@app.route('/upload')  # localhost:5000/upload
def upload():
    return render_template('upload.html')  # upload page

@app.route('/preview', methods=['POST'])
def read_data():
    data = request.files['datasetfile']
    if data:
        df = pd.read_csv(data)
        return render_template('preview.html', df_view=df)
    return 'No file uploaded!', 400

@app.route('/register')  # localhost:5000/register
def register():
    return 'register page'

@app.route('/loginvalidation/<username>/<password>') 
# localhost:5000/loginvalidation/admin/admin
def loginvalidation(username, password):
    if username == "admin" and password == "admin":
        return redirect(url_for('upload'))
    elif username == "user" and password == "user":
        return redirect(url_for('upload'))
    else:
        return 'invalid %s' % username

@app.route('/admin')
def adminpage():
    return '<h1>Admin Home Page</h1>'

@app.route('/user')
def userpage():
    return '<h1><center>User Home Page</center></h1>'

@app.route('/printname/<uname>')  # localhost:5000/printname/sandy
def printname(uname):
    return 'Your name: %s' % uname

# @app.route('/predict')
# def predict():
#     try:
#         model = pickle.load(open('model.pkl', 'rb'))
#         inp_values = [2, 2, 200, 1, 2006]
#         arr_values = np.array([inp_values])
#         price = model.predict(arr_values)
#         print(price)
#         return f'Predicted price: {price[0]}'
#     except Exception as e:
#         return str(e), 500

import pickle
model = pickle.load(open('model.pkl','rb'))
    
@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    return render_template('predict.html')

@app.route('/prediction',methods=['POST']) 
def prediction():
    int_feature=[x for x in request.form.values()]
    print(int_feature)
    int_feature=[float(i) for i in int_feature]
    final_feature=[np.array(int_feature)]
    prediction=model.predict(final_feature)

    output=format(prediction[0])
    print(output)
    return render_template('predict.html',prediction_text=output)

@app.route('/chart')
def chart():
    return render_template('chart.html')
           
@app.route('/pref')
def pref():
    return render_template('performance.html')

if __name__ == '__main__':
    app.run(debug=True)
