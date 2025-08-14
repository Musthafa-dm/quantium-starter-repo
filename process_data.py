import pandas as pd
import glob

# 1) Get all CSV files in the "data" folder
csv_files = glob.glob("data/*.csv")

# 2) Read all CSVs and combine into one table
all_data = pd.concat([pd.read_csv(f) for f in csv_files])

# 3) Keep only rows where product is "Pink Morsel"
pink_data = all_data[all_data["product"] == "Pink Morsel"]

# 4) Create a new column "sales" = quantity × price
pink_data["sales"] = pink_data["quantity"] * pink_data["price"]

# 5) Keep only the columns we need
final_data = pink_data[["sales", "date", "region"]]

# 6) Save to a new CSV file
final_data.to_csv("output.csv", index=False)

print("✅ Data processing complete! File saved as output.csv")
