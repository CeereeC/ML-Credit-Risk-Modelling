import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense

from scikeras.wrappers import KerasRegressor

class ModelBuilder:
    pass

def data_cleaning():
    df = pd.read_csv("./dataset/finantier_data_technical_test_dataset.csv", skip_blank_lines=True)
    df.dropna(how="all", inplace=True)
    
    df = df[df['Error'].isnull()]   # Remove rows with errors
    
    df = df.iloc[:, 1:-1]           # Remove customerID and Error Columns

    df = df.replace(' ', 0.0)       # Handle missing values for TotalCharges

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])  # Convert TotalCharges to float 

    X = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]

    le = LabelEncoder()
    y = le.fit_transform(y)

    return X, y

def make_transformer():
    ordinal_columns = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    hot_columns = ['PaymentMethod','MultipleLines', 'InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract']
    numerical_columns = ['tenure','MonthlyCharges','TotalCharges']

    column_trans = make_column_transformer(
        (OneHotEncoder(), hot_columns),
        (OrdinalEncoder(), ordinal_columns),
        (StandardScaler(), numerical_columns),
        remainder='passthrough')
    
    return column_trans

def make_model():
    model = Sequential()
    model.add(Dense(16, input_shape=(40,),activation="relu"))
    model.add(Dense(8, activation="relu"))
    model.add(Dense(1, activation='sigmoid')) 
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return model

def generate_train_test_set():
    X, y = data_cleaning()
    return train_test_split(X, y, test_size=0.3)

def fit_pipeline():
    estimator = KerasRegressor(build_fn=make_model, epochs=50, batch_size=100, loss="binary_crossentropy")
    pipeline = make_pipeline(make_transformer(), estimator)

    X_train, X_test, y_train, y_test = generate_train_test_set()

    pipeline.fit(X_train, y_train)
    
    joblib.dump(pipeline, "pipeline.joblib")

if __name__ == "__main__":
    ModelBuilder.__module__ = "module_builder"
    fit_pipeline()