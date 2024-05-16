from fastapi import FastAPI, HTTPException, Body, Form, Depends, status,File, UploadFile,Response,Query
from typing import Dict
import uuid, logging

app = FastAPI()
logging.basicConfig(
    format="[%(asctime)s] :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s",
    level=logging.DEBUG,
    filename="API_log.log",
    filemode="a",
)

@app.post("/input")
def input(input_data: str):
    logging.warning(f"input feild was :{input_data}")
    return input_data
    
    

    