# You need this to use FastAPI, work with statuses and be able to end HTTPExceptions
from fastapi import FastAPI, status, HTTPException
 
# You need this to be able to turn classes into JSONs and return
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# Needed for json.dumps
import json

# Both used for BaseModel
from pydantic import BaseModel

from datetime import datetime
from kafka import KafkaProducer, producer

class BankClient(BaseModel):
    Id: int
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: int
    housing: str
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/post_bank_clients/")
async def post_bank_client(bankclient:BankClient):
    try:
        # Parses the bankclient item to json
        json_of_bankclient = jsonable_encoder(bankclient)

        # Dumps the json as string
        json_as_string = json.dumps(json_of_bankclient)
        print(json_as_string)

        #Sends the json string via the produce_kafka_string function
        #produce_kafka_string(json_as_string)

        #Encodes the bank client into a json and sends a status code of 201 back to the client
        return JSONResponse(content=json_as_string, status_code=201)
    
    except ValueError:
        return JSONResponse(content=jsonable_encoder(bankclient), status_code=401)


def produce_kafka_string(json_as_string):
        # Create producer
        producer = KafkaProducer(bootstrap_servers='kafka:9092',acks=1)
        
        # Writes the string as bytes because Kafka needs it this way
        producer.send('ingestion-topic', bytes(json_as_string, 'utf-8'))
        producer.flush() 