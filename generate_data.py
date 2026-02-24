import pandas as pd
import numpy as np
import os

np.random.seed(42)
rows = 5000

data = {
    "study_hours": np.random.randint(1,10,rows),
    "sleep_hours": np.random.randint(4,9,rows),
    "attendance": np.random.randint(50,100,rows),
    "previous_score": np.random.randint(40,90,rows),
    "extra_classes": np.random.randint(0,2,rows),
}

df = pd.DataFrame(data)

df["final_score"] = (
    df.study_hours*5 +
    df.sleep_hours*2 +
    df.attendance*0.3 +
    df.previous_score*0.5 +
    df.extra_classes*5 +
    np.random.normal(0,5,rows)
)

os.makedirs("data", exist_ok=True)

df.to_csv("data/students.csv", index=False)

print("✅ Dataset Created")
print("Saved at:", os.path.abspath("data/students.csv"))
print("Rows:", len(df))