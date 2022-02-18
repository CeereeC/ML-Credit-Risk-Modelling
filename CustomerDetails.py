from xmlrpc.client import boolean
from numpy import float64
from pydantic import BaseModel


class CustomerDetails(BaseModel):
    gender           :    str
    SeniorCitizen   :    float64
    Partner          :    str
    Dependents       :    str
    tenure           :   float64
    PhoneService      :   str
    MultipleLines     :   str
    InternetService   :   str
    OnlineSecurity    :   str
    OnlineBackup      :   str
    DeviceProtection   :  str
    TechSupport      :    str
    StreamingTV        :  str
    StreamingMovies  :    str
    Contract          :   str
    PaperlessBilling  :   str
    PaymentMethod    :    str
    MonthlyCharges    :  float64
    TotalCharges     :   float64
