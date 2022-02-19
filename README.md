# ML-Credit-Risk-Modelling

## About

In this exercise, I deploy an Artificial Neural Network (ANN) on FastAPI. The task is to predict the likelihood of a customer defaulting on telco payments based on their telco data.

The customer dataset I used contains information about a fictional telco company that provides home phone and Internet services to 7048 customers. It indicates which customers have left, stayed, or signed up for their service.



## Tools required

Python >=3.9   
Pip    
Docker (For building of Docker Image from Dockerfile     


## Getting Started

1. Clone the repository 

2. Run the following command in the terminal:

```
pip install -r requirements.txt
```

To run the app locally: 
```
uvicorn main:app --reload
```

To setup Docker Image
```
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage
```
To run jupyter notebook
```
python3 -m jupyter notebook
```
## Interacting with the API

```
POST /predict
```
Post a json object of customer data. Returns the model prediction.

Sample Data:
```
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "Yes",
  "tenure": 58.0,
  "PhoneService": "No",
  "MultipleLines": "No phone service",
  "InternetService": "DSL",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "Yes",
  "TechSupport": "Yes",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Two year",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 55.5,
  "TotalCharges": 1421
}
```
Response:
```
{
  'prediction': False, 
  'value': 0.004211
 } 
```

```
GET /score
```
Returns the accuracy score of the model.   
Response:
```
0.8125232
```






