import csv
import os

DATA_FOLDER = "data"
OUTPUT_FILE = "formatted_data.csv"

with open(OUTPUT_FILE, "w", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Sales", "Date", "Region"])  # Header

    for file_name in os.listdir(DATA_FOLDER):
        if file_name.endswith(".csv"):
            file_path = os.path.join(DATA_FOLDER, file_name)

            with open(file_path, "r", newline="") as in_file:
                reader = csv.DictReader(in_file)

                for row in reader:
                    product = row["product"].strip()
                    quantity = int(row["quantity"])
                    # Remove $ sign, then convert to float
                    price = float(row["price"].replace("$", ""))
                    date = row["date"].strip()
                    region = row["region"].strip()

                    if product.lower() == "pink morsel":
                        sales = quantity * price
                        writer.writerow([sales, date, region])

print(f"✅ Finished! Saved cleaned data to '{OUTPUT_FILE}'")
