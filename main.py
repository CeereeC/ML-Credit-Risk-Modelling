import uvicorn
from fastapi import FastAPI, HTTPException
from CustomerDetails import CustomerDetails
import joblib
import pandas as pd
from model_builder import generate_train_test_set, fit_pipeline
from sklearn.metrics import accuracy_score

app = FastAPI()
# fit_pipeline()
pipeline = joblib.load("pipeline.joblib")

@app.get('/')
def index():
    return {'message': 'Customer Credit Risk Modelling'}

@app.post('/predict')
def predict(customerData : CustomerDetails):
    try: 
        data = dict(customerData)
        d = pd.DataFrame([data])
        prediction = pipeline.predict(d)
        return {'prediction': prediction.tolist()[0] > 0.5, 'value': prediction.tolist()[0]} 
    except:
        raise HTTPException(status_code=400)

@app.get('/score')
def score():
    X_train, X_test, y_train, y_test = generate_train_test_set()
    preds = pipeline.predict(X_test)
    preds = (preds > 0.5)
    return accuracy_score(y_test, preds)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
# uvicorn main:app --reload
