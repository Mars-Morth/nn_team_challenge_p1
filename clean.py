import pandas as pd
import numpy as np

INPUT_CSV = "nimbus_orders_messy.csv"
OUTPUT_CSV = "nimbus_orders_clean.csv"

def clean_orders(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    print(f"Before dropping junk rows: {len(df)}")
    
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    print(f"After dropping junk rows: {len(df)}")

    df.to_csv(output_csv)

def unique_more_than_one(input_csv):
    df = pd.read_csv(input_csv)


def seattle_revenue(input_csv):
    df = pd.read_csv(input_csv)
    total = df.loc[df["city"] == "Seattle", "total"].sum()
    print(total)

def outdoor_total(input_csv):
    df = pd.read_csv(input_csv)
    total = df.loc[df["category"] == "Outdoor", "quantity"].sum()
    print(total)

clean_orders(INPUT_CSV, OUTPUT_CSV)
seattle_revenue(OUTPUT_CSV)
outdoor_total(OUTPUT_CSV)

