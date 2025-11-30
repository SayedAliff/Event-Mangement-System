import requests

URL = "http://127.0.0.1:8000/reg"

def menu():
    while True:
        print("\n--- Registration ---")
        print("1. Add Member for registration")
        print("0. Back")
        
        choice = input("Choice: ")
        if choice == '0': break
        
        if choice == '1':
            data = {
                "member_id": input("Member ID: "),
                "event_id": input("Event ID: ")
            }
            try:
                res = requests.post(URL + "/", json=data)
                if res.status_code == 200:
                    print("Registration Successful!")
                    print(res.json())
                else:
                    print("Failed:", res.text)
            except: print("Connection Error")