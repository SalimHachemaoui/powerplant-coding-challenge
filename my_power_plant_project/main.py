from fastapi import FastAPI, HTTPException
from models import Payload, ProductionPlan
from calculator import calculate_production_plan
from typing import List

app = FastAPI()

@app.post("/productionplan", response_model=List[ProductionPlan])
def production_plan(payload: Payload):
    try:
        plan = calculate_production_plan(payload)
        return plan
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
