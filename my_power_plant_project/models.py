from pydantic import BaseModel
from typing import List, Dict

class Fuel(BaseModel):
    gas: float
    kerosine: float
    co2: float
    wind: float

class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int

class Payload(BaseModel):
    load: int
    fuels: Dict[str, float]
    powerplants: List[PowerPlant]

class ProductionPlan(BaseModel):
    name: str
    p: float
