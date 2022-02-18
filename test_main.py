from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Customer Credit Risk Modelling'}

def test_get_score():
    response = client.get("/score")
    assert response.status_code == 200

def test_post_prediction():
    data = {
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

    response = client.post(
        "/predict",
        json = data
    )
    assert response.status_code == 200

def test_basemodel_validation():
    data = {
                "gender": "Female",
                "SeniorCitizen": "Yes",
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
                "Contract": 2,
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 55.5,
                "TotalCharges": 1421
    }

    response = client.post(
        "/predict",
        json = data
    )
    assert response.status_code == 422

def test_pipeline_data_checking():
    data = {
                "gender": "Yes",
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
                "PaymentMethod": "Yes",
                "MonthlyCharges": 55.5,
                "TotalCharges": 1421
    }

    response = client.post(
        "/predict",
        json = data
    )
    assert response.status_code == 400

def test_score():
    response = client.get(
        "/score"
    )
    assert response.status_code == 200