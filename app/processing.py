import pandas as pd


def process_csv(file):

    df = pd.read_csv(file)

    required_columns = ["name", "salary"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"{column} column missing")

    result = {
        "total_employees": len(df),
        "average_salary": float(df["salary"].mean()),
        "total_salary": float(df["salary"].sum())
    }

    return result