import numpy as np
import pandas as pd
from flask import Flask, request, render_template
#import pickle
import joblib

app = Flask(__name__)

breast_cancer_detector_model = joblib.load('/Users/user/Dropbox/Data Science/Final Project V2/Model/model.h5')
breast_cancer_detector_scaler = joblib.load('/Users/user/Dropbox/Data Science/Final Project V2/Model/scaler.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST']) 
def predict():
  input_features = [float(x) for x in request.form.values()]
  features_value = [np.array(input_features)]
  
  prediction_feature = ['radius_mean','perimeter_mean','area_mean','symmetry_mean',
  'compactness_mean','concave points_mean']
    
  df = pd.DataFrame(features_value, columns=prediction_feature) 
  output = breast_cancer_detector_model.predict(df)

  #output = breast_cancer_detector_model.predict(scaler.transform([df]))[0]
   
  if output == 1:
    predict = "Breast cancer"
  else:
    
    #res_val = "Breast cancer"
    predict = "No Breast cancer"
    
  return render_template('index.html', predict='Patient has {}'.format(predict))
    
if __name__ == "__main__":
    app.run(debug=True) #, host = "127.0.0.1:5000")
    