import requests

URL = "http://127.0.0.1:8000/reg"

def menu():
    print("\n--- Registration ---")
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