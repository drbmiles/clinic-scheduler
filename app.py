import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
from io import BytesIO
from streamlit_calendar import calendar

st.set_page_config(page_title="Clinic & Inpatient Scheduler", layout="wide")
st.title("📅 Clinic & Inpatient Schedule Generator")

st.header("Step 1: Enter Providers")
providers = st.text_area("Enter provider names (one per line)").split("\n")
providers = [p.strip() for p in providers if p.strip()]

st.header("Step 2: Choose Coverage Days")
clinic_days = st.multiselect(
    "Select Clinic Days", 
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], 
    default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
)
inpatient_days = st.multiselect(
    "Select Inpatient Days", 
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 
    default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

st.header("Step 3: Upload Vacation File (Optional)")
vacation_file = st.file_uploader("Upload a CSV: Provider, Start Date, End Date", type=["csv"])

st.header("Step 4: Upload Admin Days File (Optional)")
admin_file = st.file_uploader
