import requests

URL = "http://127.0.0.1:8000/member"

def menu():
    while True:
        print("\n--- Member Panel ---")
        print("1. List Members")
        print("2. Add Member")
        print("3. Update Member")
        print("4. Delete Member")
        print("0. Back")
        
        c = input("Choice: ")
        if c == '0': break
        
        if c == '1':
            try:
                res = requests.get(URL + "/")
                for m in res.json():
                    print(f"ID: {m['id']}, Name: {m['name']}, Level: {m['level']}")
            except: print("Connection Error")
                
        elif c == '2':
            data = {
                "id": input("Member ID: "),
                "name": input("Name: "),
                "level": input("Level (Basic/Gold): ")
            }
            try:
                res = requests.post(URL + "/", json=data)
                print("Server:", res.json())
            except: print("Connection Error")

        elif c == '3':
            mid = input("ID to Update: ")
            print("Enter New Details:")
            data = {
                "id": mid,
                "name": input("New Name: "),
                "level": input("New Level (Basic/Gold): ")
            }
            try:
                res = requests.put(f"{URL}/{mid}", json=data)
                if res.status_code == 200:
                    print("Server:", res.json())
                else:
                    print("Failed:", res.text)
            except: print("Connection Error")
            
        elif c == '4':
            mid = input("ID to Delete: ")
            try:
                requests.delete(f"{URL}/{mid}")
                print("Deleted.")
            except: print("Connection Error")