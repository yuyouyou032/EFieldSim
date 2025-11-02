from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from optics_model.model import compute_geometry

app = FastAPI()

# allow frontend dev server to call us:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # dev: wide open
    allow_methods=["*"],
    allow_headers=["*"],
)

class Params(BaseModel):
    amplitude_x: float | None = None
    amplitude_y: float | None = None
    frequency: float | None = None
    phase_diff: float | None = None


@app.post("/api/update")
def update_scene(params: Params):
    # convert Params to dict
    result = compute_geometry(params.dict(exclude_none=True))
    return result