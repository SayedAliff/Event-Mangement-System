import requests

URL = "http://127.0.0.1:8000/event"

def menu():
    while True:
        print("\n--- Event Panel ---")
        print("1. List Events")
        print("2. Add Event")
        print("3. Delete Event")
        print("0. Back")
        
        c = input("Choice: ")
        if c == '0': break
        
        if c == '1':
            try:
                res = requests.get(URL + "/")
                for e in res.json():
                    print(f"ID: {e['id']}, Name: {e['name']}, Fee: {e['fee']}")
            except: print("Connection Error")
                
        elif c == '2':
            data = {
                "id": input("Event ID: "),
                "name": input("Name: "),
                "fee": float(input("Fee: ")),
                "capacity": int(input("Capacity: "))
            }
            try:
                res = requests.post(URL + "/", json=data)
                print("Server:", res.json())
            except: print("Connection Error")
            
        elif c == '3':
            eid = input("ID to Delete: ")
            try:
                requests.delete(f"{URL}/{eid}")
                print("Deleted.")
            except: print("Connection Error")