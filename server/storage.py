import os
from datetime import datetime
from typing import Dict, Any

DATA_DIR = "data"
FILES = {
    "members": os.path.join(DATA_DIR, "members.txt"),
    "events": os.path.join(DATA_DIR, "events.txt"),
    "registrations": os.path.join(DATA_DIR, "registrations.txt"),
    "audit": os.path.join(DATA_DIR, "audit.txt"),
    "admin": os.path.join(DATA_DIR, "admin.txt")
}

DELIMITER = ","

def setup():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    admin_path = FILES["admin"]
    if not os.path.exists(admin_path):
        with open(admin_path, 'w') as f:
            f.write(f"admin{DELIMITER}123\n")

    for key, path in FILES.items():
        if key != "admin" and not os.path.exists(path):
            with open(path, 'w') as f:
                pass 

def read_data(entity):
    data = []
    path = FILES.get(entity)
    
    if os.path.exists(path):
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                
                parts = [p.strip() for p in line.split(DELIMITER)]
                item = {}
                
                try:
                    if entity == "members" and len(parts) >= 3:
                        item = {"id": parts[0], "name": parts[1], "phone": parts[2]}
                    
                    elif entity == "events" and len(parts) >= 4:
                        item = {
                            "id": parts[0], 
                            "name": parts[1], 
                            "fee": float(parts[2]), 
                            "capacity": int(parts[3])
                        }
                    
                    elif entity == "registrations" and len(parts) >= 3:
                        item = {"id": parts[0], "member_id": parts[1], "event_id": parts[2]}
                        
                    elif entity == "admin" and len(parts) >= 2:
                        item = {"username": parts[0], "password": parts[1]}
                        
                    if item:
                        data.append(item)
                except ValueError:
                    continue
                    
    return data

def write_data(entity, data_list):
    path = FILES.get(entity)
    with open(path, 'w') as f:
        for item in data_list:
            line = ""
            if entity == "members":
                line = f"{item['id']}{DELIMITER}{item['name']}{DELIMITER}{item['phone']}"
            
            elif entity == "events":
                line = f"{item['id']}{DELIMITER}{item['name']}{DELIMITER}{item['fee']}{DELIMITER}{item['capacity']}"
            
            elif entity == "registrations":
                line = f"{item['id']}{DELIMITER}{item['member_id']}{DELIMITER}{item['event_id']}"
                
            elif entity == "admin":
                line = f"{item['username']}{DELIMITER}{item['password']}"
            
            f.write(line + '\n')

def log_audit(msg):
    path = FILES.get("audit")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, 'a') as f:
        f.write(f"[{time}] {msg}\n")

def get_admin_creds():
    admins = read_data("admin")
    if admins:
        return admins[0]
    return {"username": "admin", "password": "123"}

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