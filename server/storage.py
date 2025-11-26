import json
import os
from datetime import datetime
from typing import Dict, Any

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