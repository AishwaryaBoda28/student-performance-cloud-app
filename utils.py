import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_input(values):
    try:
        vals = [float(v) for v in values]
        if any(v < 0 for v in vals):
            return None
        return vals
    except:
        return None