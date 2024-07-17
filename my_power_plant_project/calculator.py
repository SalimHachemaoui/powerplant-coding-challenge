from typing import List, Dict
from models import Payload

def calculate_production_plan(payload: Payload):
    load = payload.load
    fuels = payload.fuels
    powerplants = payload.powerplants

    # Créer un dictionnaire pour stocker les coûts des centrales électriques
    plant_costs = {}

    for plant in powerplants:
        if plant.type == "gasfired":
            cost = fuels['gas(euro/MWh)'] / plant.efficiency + 0.3 * fuels['co2(euro/ton)']
        elif plant.type == "turbojet":
            cost = fuels['kerosine(euro/MWh)'] / plant.efficiency + 0.3 * fuels['co2(euro/ton)']
        elif plant.type == "windturbine":
            cost = 0
        plant_costs[plant.name] = cost

    # Trier les centrales par coût
    sorted_plants = sorted(powerplants, key=lambda x: plant_costs[x.name])

    production_plan = []
    remaining_load = load

    for plant in sorted_plants:
        if remaining_load <= 0:
            break
        if plant.type == "windturbine":
            production = plant.pmax * (fuels['wind(%)'] / 100)
        else:
            production = min(plant.pmax, remaining_load)
            if production < plant.pmin:
                production = plant.pmin
        remaining_load -= production
        production_plan.append({"name": plant.name, "p": round(production, 1)})

    return production_plan
