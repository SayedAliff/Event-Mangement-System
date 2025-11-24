from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .storage import read_data, get_admin_creds
import os

app = FastAPI()

class Login(BaseModel):
    username: str
    password: str

class ReportRequest(BaseModel):
    event_id: str

class AuditFilter(BaseModel):
    filter_type: str
    value: str = None

@app.post("/login")
def login(creds: Login):
    admin = get_admin_creds()
    if creds.username == admin['username'] and creds.password == admin['password']:
        return {"msg": "Login OK"}
    raise HTTPException(status_code=401, detail="Wrong password")

@app.post("/report")
def get_report(req: ReportRequest):
    events = read_data("events")
    event = next((e for e in events if e['id'] == req.event_id), None)
    if not event: raise HTTPException(status_code=404, detail="Event not found")
    
    regs = read_data("registrations")
    count = sum(1 for r in regs if r['event_id'] == req.event_id)
    
    return {
        "event": event['name'],
        "registrations": count,
        "revenue": count * event['fee'],
        "capacity": event['max_capacity']
    }

@app.post("/audit")
def view_audit(filter_data: AuditFilter):
    if not os.path.exists("data/audit.log"): return {"logs": []}
    
    with open("data/audit.log", 'r') as f:
        lines = f.readlines()
        
    if filter_data.filter_type == "all":
        return {"logs": lines}
        
    filtered = [line for line in lines if filter_data.value.lower() in line.lower()]
    return {"logs": filtered}