import requests
import sys

URL = "http://127.0.0.1:8000/event"

def get_input(prompt: str, type_func=str, required: bool = True):
    while True:
        try:
            value = input(prompt).strip()
            if required and not value:
                print("Input is required. Please try again.")
                continue
            if not value and not required:
                return None
            return type_func(value)
        except ValueError:
            print(f"Invalid format. Expected a valid number. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def menu():
    while True:
        print("\n--- Event Panel ---")
        print("1. List Events")
        print("2. Add Event")
        print("3. Update Event")
        print("4. Delete Event")
        print("0. Back")
        
        choice = input("Choice: ").strip()
        if choice == '0': break
        
        if choice == '1':
            try:
                res = requests.get(URL + "/")
                events = res.json()
                if not events:
                    print("No events found.")
                for e in events:
                    print(f"ID: {e['id']}, Name: {e['name']}, Fee: {e['fee']}, Capacity: {e['capacity']}")
            except Exception as e: print(f"Connection Error: {e}")
                
        elif choice == '2':
            print("Enter New Event Details:")
            event_id = get_input("Event ID: ")
            if not event_id: continue
            
            name = get_input("Name: ")
            fee = get_input("Fee: ", float)
            capacity = get_input("Capacity: ", int)

            data = {
                "id": event_id,
                "name": name,
                "fee": fee,
                "capacity": capacity
            }
            try:
                res = requests.post(URL + "/", json=data)
                if res.status_code in [200, 201]:
                    print("Server:", res.json())
                else:
                    print("Error:", res.json().get('detail', 'Unknown error'))
            except Exception as e: print(f"Connection Error: {e}")
            
        elif choice == '3':
            eid = get_input("ID to Update: ")
            if not eid: continue
            
            print(f"Updating Event {eid}. Enter New Details:")
            
            new_name = get_input("New Name: ")
            new_fee = get_input("New Fee: ", float)
            new_capacity = get_input("New Capacity: ", int)

            if not new_name or new_fee is None or new_capacity is None:
                print("Update cancelled due to invalid input.")
                continue

            data = {
                "id": eid,
                "name": new_name,
                "fee": new_fee,
                "capacity": new_capacity
            }
            try:
                res = requests.put(f"{URL}/{eid}", json=data)
                if res.status_code == 200:
                    print("Server:", res.json())
                elif res.status_code == 404:
                    print(f"Error: Event ID '{eid}' not found on server.")
                else:
                    print("Failed:", res.text)
            except Exception as e: print(f"Connection Error: {e}")

        elif choice == '4':
            eid = get_input("ID to Delete: ")
            if not eid: continue
            try:
                requests.delete(f"{URL}/{eid}")
                print("Deleted.")
            except Exception as e: print(f"Connection Error: {e}")