import pandas as pd
import numpy as np

INPUT_CSV = "nimbus_orders_messy.csv"
OUTPUT_CSV = "nimbus_orders_clean.csv"


def clean_orders(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    df["order_date"] = pd.to_datetime(df["order_date"], format="mixed")

    print(f"Before dropping junk rows: {len(df)}")

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True, how="all")
    df = df[df["order_id"] < 2000]
    df = df[df["customer_name"].notna()]
    df["customer_name"] = df["customer_name"].str.strip()
    df["customer_name"] = df["customer_name"].str.lower()
    df["order_date"] = pd.to_datetime(df["order_date"], format="mixed")
    df["category"] = df["category"].str.lower()
    df["city"] = df["city"].str.lower()

    print(f"After dropping junk rows: {len(df)}")

    df.to_csv(output_csv)


def total_revenue(input_csv):
    df = pd.read_csv(input_csv)
    total = df["total"].sum()
    print(total)

def most_cat_revenue(input_csv):
    df = pd.read_csv(input_csv)
    categories = (df["category"].str.lower()).unique()
    max_ = float("-inf")
    cat_ = ""
    for cat in categories:
        total = df.loc[df["category"].str.lower() == cat, "total"].sum()
        if total > max_:
            max_ = total
            cat_ = cat
    print(f"{cat_} : {max_}")

def average_order_electronics(input_csv):
    df = pd.read_csv(input_csv)
    df = df[df["category"].str.lower() == "electronics"]
    average = df["total"].sum() / len(df)
    print(f"Average order of electronics: {average}")


def average_order_electronics(input_csv):
    df = pd.read_csv(input_csv)
    df = df[df["category"].str.lower() == "electronics"]
    average = df["total"].sum() / len(df)
    print(f"Average order of electronics: {average}")


def seattle_revenue(input_csv):
    df = pd.read_csv(input_csv)
    total = df.loc[df["city"] == "seattle", "total"].sum()
    print(total)


def outdoor_total(input_csv):
    df = pd.read_csv(input_csv)
    total = df.loc[df["category"] == "outdoor", "quantity"].sum()
    print(total)


clean_orders(INPUT_CSV, OUTPUT_CSV)
total_revenue(OUTPUT_CSV)
most_cat_revenue(OUTPUT_CSV)
seattle_revenue(OUTPUT_CSV)
outdoor_total(OUTPUT_CSV)
average_order_electronics(OUTPUT_CSV)
