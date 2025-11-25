from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .storage import read_data, write_data, log_audit

app = FastAPI()

class Member(BaseModel):
    id: str
    name: str
    level: str

@app.get("/")
def get_members():
    return read_data("members")

@app.post("/")
def add_member(m: Member):
    members = read_data("members")
    if any(x['id'] == m.id for x in members):
        raise HTTPException(status_code=400, detail="ID already exists")
    members.append(m.model_dump())
    write_data("members", members)
    log_audit(f"MEMBER ADDED: {m.id}")
    return {"msg": "Member added"}

@app.put("/{mid}")
def update_member(mid: str, m: Member):
    members = read_data("members")
    found = False
    for i, member in enumerate(members):
        if member['id'] == mid:
            # Update while keeping the ID same (or allow update if payload has same ID)
            if m.id != mid:
                 raise HTTPException(status_code=400, detail="ID mismatch in body and URL")
            members[i] = m.model_dump()
            found = True
            break
    
    if not found:
        raise HTTPException(status_code=404, detail="Member not found")
        
    write_data("members", members)
    log_audit(f"MEMBER UPDATED: {mid}")
    return {"msg": "Member updated"}

@app.delete("/{mid}")
def delete_member(mid: str):
    members = read_data("members")
    new_list = [m for m in members if m['id'] != mid]
    if len(members) == len(new_list):
        raise HTTPException(status_code=404, detail="Not found")
    write_data("members", new_list)
    log_audit(f"MEMBER DELETED: {mid}")
    return {"msg": "Member deleted"}