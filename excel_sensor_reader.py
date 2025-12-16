import pandas as pd

EXCEL_FILE = "patient_vitals_500_rows.xlsx"  # make sure this filename exists

df = pd.read_excel(EXCEL_FILE)

# ✅ Column names EXACTLY as in your Excel file
REQUIRED_COLUMNS = [
    "Heart_Rate_bpm",
    "Pulse_Rate_bpm",
    "Blood_Pressure_mmHg",
    "Body_Temperature_C"
]

# Validate columns once (fail fast if wrong file)
for col in REQUIRED_COLUMNS:
    if col not in df.columns:
        raise ValueError(f"Missing column in Excel file: {col}")

row_index = 0

def get_next_vitals():
    global row_index

    if row_index >= len(df):
        row_index = 0  # loop again

    row = df.iloc[row_index]
    row_index += 1

    return {
        "heart_rate": int(row["Heart_Rate_bpm"]),
        "pulse_rate": int(row["Pulse_Rate_bpm"]),
        "blood_pressure": row["Blood_Pressure_mmHg"],
        "body_temperature": float(row["Body_Temperature_C"])
    }

