import pandas as pd
import os

# ===============================
# CONFIG
# ===============================
EXCEL_FILE = "patient_vitals.xlsx"
# If you want the bigger file, change to:
# EXCEL_FILE = "patient_vitals_500_rows.xlsx"

# ===============================
# LOAD EXCEL SAFELY
# ===============================
if not os.path.exists(EXCEL_FILE):
    raise FileNotFoundError(f"Excel file not found: {EXCEL_FILE}")

df = pd.read_excel(EXCEL_FILE)

# Normalize column names (safety)
df.columns = [c.strip().lower() for c in df.columns]

required_columns = [
    "heart_rate",
    "pulse_rate",
    "blood_pressure",
    "body_temperature"
]

for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing column in Excel file: {col}")

# ===============================
# ROW POINTER (LOOP FOREVER)
# ===============================
row_index = 0

def get_next_vitals():
    """
    Returns next row of vitals as dict.
    Automatically loops back to first row after last row.
    """
    global row_index

    if row_index >= len(df):
        row_index = 0  # loop again from start

    row = df.iloc[row_index]
    row_index += 1

    return {
        "heart_rate": int(row["heart_rate"]),
        "pulse_rate": int(row["pulse_rate"]),
        "blood_pressure": str(row["blood_pressure"]),
        "body_temperature": float(row["body_temperature"])
    }


# ===============================
# TEST MODE (OPTIONAL)
# ===============================
if __name__ == "__main__":
    for _ in range(10):
        print(get_next_vitals())

