from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Dict, List
import math
import json

app = FastAPI()

class Island(BaseModel):
    name: str
    latitude: float
    longitude: float

class DistanceCalculation(BaseModel):
    island_name: str
    distance: float

# Load data from JSON file
def load_islands_from_json(file_path: str) -> Dict[str, Island]:
    with open(file_path, 'r') as file:
        islands_data = json.load(file)
    islands = {}
    for island_data in islands_data:
        island = Island(**island_data)
        islands[island.name] = island
    return islands

islands_db: Dict[str, Island] = load_islands_from_json('islands.json')

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371  
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def get_sorted_islands(latitude: float, longitude: float) -> List[DistanceCalculation]:
    distances = []
    for island_name, island in islands_db.items():
        distance = calculate_distance(latitude, longitude, island.latitude, island.longitude)
        distances.append(DistanceCalculation(island_name=island_name, distance=distance))
    sorted_distances = sorted(distances, key=lambda x: x.distance)
    return sorted_distances

@app.get("/islands/", response_model=List[DistanceCalculation])
def get_islands_sorted_by_distance(latitude: float = Query(..., description="Vĩ độ"), longitude: float = Query(..., description="Kinh độ")):
    return get_sorted_islands(latitude, longitude)
