from fastapi import FastAPI
from .api_member_management import app as member_app
from .api_event_management import app as event_app
from .api_registration_system import app as reg_app
from .api_report_admin_system import app as admin_app
from .storage import setup

setup()

app = FastAPI()
app.mount("/member", member_app)
app.mount("/event", event_app)
app.mount("/reg", reg_app)
app.mount("/admin", admin_app)