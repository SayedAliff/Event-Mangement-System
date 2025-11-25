# 🎉 Event Management System

A professional and user-friendly **Event Management System** designed to
simplify managing members, events, registrations, and admin-level
reporting through a clean console interface backed by a FastAPI server.\
This system ensures secure data handling, clear modular architecture,
and persistent file-based storage --- designed for academic and
production-style environments....

------------------------------------------------------------------------

## 🚀 Features

-   👤 **Member Management** (Add, List, Delete)
-   🗓️ **Event Creation & Management**
-   📝 **Smart Registration System** (capacity + duplicate protection)
-   🔐 **Admin Panel** with login authentication
-   💰 **Event Revenue Report**
-   📜 **System-wide Audit Log**
-   💾 **Persistent JSONL Storage**
-   ⚙️ **FastAPI Server + Console Client Architecture**

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python 3.12+**
-   **Backend:** FastAPI
-   **Server:** Uvicorn
-   **Client:** Python Requests
-   **Validation:** Pydantic
-   **Storage:** JSONL File Database
-   **Version Control:** Git & GitHub

------------------------------------------------------------------------

# 📘 API Documentation

After running the server, open:

### 📄 Swagger UI

http://127.0.0.1:8000/docs

### 📑 ReDoc

http://127.0.0.1:8000/redoc

APIs include:

-   /member/\* --- Member CRUD\
-   /event/\* --- Event CRUD\
-   /registration/\* --- Booking operations\
-   /admin/\* --- Revenue & audit logs

------------------------------------------------------------------------

# 📂 Project Structure

``` bash
EventManagementSystem/
│
├── main.py                         # 🚀 Server Entry Point
│
├── server/                         # 🧠 Backend Logic + API
│   ├── storage.py                  # File Database Manager
│   ├── app.py                      # API Router Setup
│   ├── api_member_management.py
│   ├── api_event_management.py
│   ├── api_registration_system.py
│   └── api_report_admin_system.py
│
├── client/                         # 💻 Console Client
│   ├── client.py                   # Main Menu
│   ├── member_management.py
│   ├── event_management.py
│   ├── registration_system.py
│   └── report_admin_system.py
│
└── data/                           # 💾 Auto-Generated Data
    ├── members.jsonl
    ├── events.jsonl
    ├── registrations.jsonl
    ├── admin.json.                 
    └── audit.log                   # 📝 Auto add the Data
```

------------------------------------------------------------------------

# ⚙️ Installation Guide

Below are complete installation steps for **Windows**, **macOS**, and
**Linux**.

------------------------------------------------------------------------

# 🪟 Windows Installation

### 1️⃣ Install Git

Download: https://git-scm.com/download/win

### 2️⃣ Clone the Repository

``` bash
git clone https://github.com/SayedAliff/Event-Mangement-System
cd event-management-system
```

### 3️⃣ Install Dependencies

``` bash
pip install fastapi "uvicorn[standard]" requests pydantic
```

------------------------------------------------------------------------

# 🍎 macOS Installation

### 1️⃣ Install Git

``` bash
brew install git
```

### 2️⃣ Clone the Repository

``` bash
git clone https://github.com/SayedAliff/Event-Mangement-System
cd event-management-system
```

### 3️⃣ Install Dependencies

``` bash
pip3 install fastapi "uvicorn[standard]" requests pydantic
```

------------------------------------------------------------------------

# 🐧 Linux Installation

### 1️⃣ Install Git

Ubuntu / Debian:

``` bash
sudo apt update
sudo apt install git -y
```

Fedora:

``` bash
sudo dnf install git -y
```

### 2️⃣ Clone the Repository

``` bash
git clone https://github.com/your-username/event-management-system.git
cd event-management-system
```

### 3️⃣ Install Dependencies

``` bash
pip3 install fastapi "uvicorn[standard]" requests pydantic
```

------------------------------------------------------------------------

# ▶️ Running the System

## 1️⃣ Start the Server

Windows:

``` bash
python main.py
```

macOS / Linux:

``` bash
python3 main.py
```

------------------------------------------------------------------------

## 2️⃣ Start the Console Client

Windows:

``` bash
python client/client.py
```

macOS / Linux:

``` bash
python3 client/client.py
```

------------------------------------------------------------------------

# 🎮 User Guide

### 👤 Member Management

-   Add Member
-   List Members
-   Update Member
-   Delete Members

### 🗓️ Event Management

-   Create Event (fee + capacity)
-   Update Event
-   Prevent duplicate event IDs

### 📝 Registration

-   Register Member
-   Auto-check capacity
-   Prevent duplicate entry

### 🔐 Admin Panel

-   Login: Username: admin | password: 123
-   View Revenue
-   View Audit Log

------------------------------------------------------------------------

# 🤝 Contributing

1.  Fork
2.  Create Branch
3.  Commit
4.  Push
5.  Pull Request
