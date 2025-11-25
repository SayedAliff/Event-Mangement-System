import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

DATA_DIR = "data"
FILES = {
    "members": os.path.join(DATA_DIR, "members.jsonl"),
    "events": os.path.join(DATA_DIR, "events.jsonl"),
    "registrations": os.path.join(DATA_DIR, "registrations.jsonl"),
    "audit": os.path.join(DATA_DIR, "audit.log"),
    "admin": os.path.join(DATA_DIR, "admin.json")
}

def setup():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    for key, path in FILES.items():
        if not os.path.exists(path):
            with open(path, 'w') as f:
                if key == "admin":
                    json.dump({"username": "admin", "password": "123"}, f)

def read_data(entity):
    data = []
    path = FILES.get(entity)
    if os.path.exists(path):
        with open(path, 'r') as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
    return data

def write_data(entity, data_list):
    path = FILES.get(entity)
    with open(path, 'w') as f:
        for item in data_list:
            f.write(json.dumps(item) + '\n')

def log_audit(msg):
    path = FILES.get("audit")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, 'a') as f:
        f.write(f"[{time}] {msg}\n")

def get_admin_creds():
    with open(FILES["admin"], 'r') as f:
        return json.load(f)

def update_entity(entity_type: str, entity_id: str, new_data: Dict[str, Any]) -> bool:
    items = read_data(entity_type)
    updated = False
    
    for i, item in enumerate(items):
        if item.get('id') == entity_id:
            # Ensure the ID is not accidentally overwritten
            if 'id' in new_data:
                del new_data['id'] 
            
            items[i].update(new_data)
            updated = True
            break
            
    if updated:
        write_data(entity_type, items)
        log_audit(f"{entity_type.upper()} UPDATED: ID {entity_id}")
        return True
    return False

# --- Helper functions for APIs ---
def get_next_id(filepath: str, prefix: str) -> str:
    records = read_data(filepath)
    if not records:
        return f"{prefix}001"
    
    max_num = 0
    id_key = 'reg_id' if prefix == 'R-' else 'id'
    
    for r in records:
        current_id = r.get(id_key, "")
        if current_id.startswith(prefix) and current_id[len(prefix):].isdigit():
            try:
                max_num = max(max_num, int(current_id[len(prefix):]))
            except ValueError:
                continue
    
    return f"{prefix}{(max_num + 1):03d}"


def register_for_event(member_id: str, event_id: str) -> tuple[bool, str, Optional[str]]:
    members = read_data("members")
    events = read_data("events")
    regs = read_data("registrations")

    if not any(m['id'] == member_id for m in members):
        return False, "Member not found.", None
    
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return False, "Event not found.", None

    current_regs = [r for r in regs if r['event_id'] == event_id]
    if len(current_regs) >= event['capacity']:
        return False, f"Event {event_id} is full.", None

    if any(r['member_id'] == member_id for r in current_regs):
        return False, f"Member {member_id} already registered.", None
        
    reg_id = f"R-{len(regs) + 1:03d}"
    
    new_reg = {
        "reg_id": reg_id,
        "member_id": member_id,
        "event_id": event_id,
        "date_registered": datetime.now().isoformat()
    }
    
    regs.append(new_reg)
    write_data("registrations", regs)
    
    log_audit(f"EVENT REGISTERED - Reg: {reg_id} | Event: {event_id} | Member: {member_id}")
    return True, f"Registration {reg_id} successful.", reg_id

def generate_event_report(event_id: str) -> tuple[bool, str, Dict[str, Any]]:
    events = read_data("events")
    regs = read_data("registrations")
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return False, "Event not found.", {}
        
    event_regs = [r for r in regs if r['event_id'] == event_id]
    reg_count = len(event_regs)
    
    expected_revenue = reg_count * event['fee']
    remaining_capacity = event['capacity'] - reg_count
    
    report_data = {
        "event_name": event['name'],
        "event_fee": event['fee'],
        "max_capacity": event['capacity'],
        "current_registrations": reg_count,
        "remaining_capacity": remaining_capacity,
        "expected_revenue": round(expected_revenue, 2)
    }
    return True, "Report generated.", report_data