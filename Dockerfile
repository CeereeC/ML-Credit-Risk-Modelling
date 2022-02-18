# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./main.py /code/
COPY ./pipeline.joblib /code/
COPY ./CustomerDetails.py /code/
COPY ./model_builder.py /code/
COPY ./model_builder.py /code/
ADD dataset /code/dataset

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
