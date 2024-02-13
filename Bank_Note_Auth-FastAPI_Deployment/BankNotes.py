'''
Created a Bank Note base model
Pydantic library uses Bank Note base model for data validation
(data type hints and errors)
'''

from pydantic import BaseModel

#Class decribing Bank Note features and data type

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
