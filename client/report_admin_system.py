import requests
import getpass

URL = "http://127.0.0.1:8000/admin"

def menu():
    
    print("\n--- Admin Login ---")
    u = input("User: ")
    p = getpass.getpass("Password: ")
    
    try:
        res = requests.post(URL + "/login", json={"username": u, "password": p})
        if res.status_code != 200:
            print("Login Failed!")
            return
    except:
        print("Server not running.")
        return

    print("Login Successful!")
    while True:
        print("\n1. View Audit Log")
        print("2. View Revenue Report")
        print("0. Logout")
        
        c = input("Choice: ")
        if c == '0': break
        
        if c == '1':
            try:
                res = requests.get(URL + "/audit")
                for line in res.json()['logs']:
                    print(line.strip())
            except: print("Error")
        
        elif c == '2':
            eid = input("Event ID for Revenue: ")
            try:
                res = requests.post(f"{URL}/report", json={"event_id": eid})
                print(res.json())
            except: print("Error")