import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import client.member_management as mm
import client.event_management as em
import client.registration_system as rs
import client.report_admin_system as ra

def main():
    while True:
        print("\n=== Event Booking System ===")
        print("1. Member Management")
        print("2. Event Management")
        print("3. Register for Event")
        print("4. Admin Panel")
        print("0. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1': mm.menu()
        elif choice == '2': em.menu()
        elif choice == '3': rs.menu()
        elif choice == '4': ra.menu()
        elif choice == '0': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()