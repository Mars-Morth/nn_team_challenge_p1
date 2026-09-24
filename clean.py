import pandas as pd
import numpy as np

INPUT_CSV = "nimbus_orders_messy.csv"
OUTPUT_CSV = "nimbus_orders_clean.csv"

def clean_orders(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    print(f"Before dropping junk rows: {len(df)}")
    
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True, how="all")

    print(f"After dropping junk rows: {len(df)}")

    df.to_csv(output_csv)

clean_orders(INPUT_CSV, OUTPUT_CSV)