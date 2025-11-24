from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .storage import read_data, write_data, log_audit

app = FastAPI()

class Event(BaseModel):
    id: str
    name: str
    fee: float
    capacity: int

@app.get("/")
def get_events():
    return read_data("events")

@app.post("/")
def add_event(e: Event):
    events = read_data("events")
    if any(x['id'] == e.id for x in events):
        raise HTTPException(status_code=400, detail="ID exists")
    events.append(e.model_dump())
    write_data("events", events)
    log_audit(f"EVENT ADDED: {e.id}")
    return {"msg": "Event added"}

@app.delete("/{eid}")
def delete_event(eid: str):
    events = read_data("events")
    new_list = [e for e in events if e['id'] != eid]
    write_data("events", new_list)
    log_audit(f"EVENT DELETED: {eid}")
    return {"msg": "Event deleted"}