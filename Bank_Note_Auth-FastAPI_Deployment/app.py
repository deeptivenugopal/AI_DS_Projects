'''
Creating FastAPI application
'''

# 1. Library Imports

import uvicorn 
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

#2. Create the app object

app = FastAPI()
pickle_in = open("rf_model.pkl","rb")
model = pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
# This is 1st API page
@app.get('/')
def index():
    return{'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter with a message
# Located at: http://127.0.0.1:8000/AnyNameHere
# This is 2nd API page

@app.get('/{name}')
def get_name(name: str):
    return {"Welcome to FastAPI: " f'{name}'}

# 4. Expose the prediction functionality and make a prediction from the passed
# JSON data and returned the predicted Bank Note with the confidence

@app.post('/predict')
def predict_banknote(data:BankNote): #calling the class for variables
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    print(model.predict([[variance,skewness,curtosis,entropy]]))

    prediction = model.predict([[variance,skewness,curtosis,entropy]])

    # Checking threshold value
    if prediction[0] > 0.5:
        prediction = "Fake Note"
    else:
        prediction = "Its a Bank Note"

    return{

        'prediction': prediction
        }

# 5. Run the API with uvicorn

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)


#uvicorn app:app --reload  # uvicorn filename:objectname function name
# http://127.0.0.1:8000/docs

















