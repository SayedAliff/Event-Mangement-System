from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .storage import read_data, write_data, log_audit, update_entity

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

@app.put("/{eid}")
def update_event(eid: str, e: Event):
    if e.id != eid:
        raise HTTPException(status_code=400, detail="ID mismatch in body and URL")
        
    if update_entity("events", eid, e.model_dump()):
        return {"msg": f"Event {eid} updated successfully."}
    raise HTTPException(status_code=404, detail="Event not found.")

@app.delete("/{eid}")
def delete_event(eid: str):
    events = read_data("events")
    new_list = [e for e in events if e['id'] != eid]
    if len(events) == len(new_list):
        raise HTTPException(status_code=404, detail="Not found")
    write_data("events", new_list)
    log_audit(f"EVENT DELETED: {eid}")
    return {"msg": "Event deleted"}