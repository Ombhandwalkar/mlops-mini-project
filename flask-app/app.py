from flask import Flask,render_template,request
import mlflow
import dagshub
import pickle
from preprocessing_utility import normalize_text


import dagshub
mlflow.set_tracking_uri('https://dagshub.com/Ombhandwalkar/mlops-mini-project.mlflow')
dagshub.init(repo_owner='Ombhandwalkar', repo_name='mlops-mini-project', mlflow=True)

vectorizer=pickle.load(open('models/vectorizer.pkl','rb'))

# Load model from model Registry
model_name='my_model'
model_version=2


model_uri=f"models:/{model_name}/{model_version}"
model=mlflow.pyfunc.load_model(model_uri)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',result=None)

@app.route('/predict' ,methods=['POST'])
def predicct():
    text=request.form['text']

    # Clean 
    text=normalize_text(text)

    # BOW
    features=vectorizer.transform([text])

    # Prediction
    result=model.predict(features)




    return render_template('index.html',result=result[0])


app.run(debug=True)