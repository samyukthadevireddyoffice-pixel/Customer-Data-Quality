import pandas as pd

# Read customer data
customers = pd.read_csv("../data/customers.csv")

# Find missing customer IDs
missing_ids = customers[customers["customer_id"].isna()]
print("Customers with missing IDs:")
print(missing_ids)

# Find duplicate customer IDs
duplicates = customers[customers.duplicated("customer_id", keep=False)]
print("\nDuplicate customer IDs:")
print(duplicates)

# Remove records with missing IDs
cleaned_customers = customers.dropna(subset=["customer_id"])

# Remove duplicate customer IDs
cleaned_customers = cleaned_customers.drop_duplicates(
    subset=["customer_id"],
    keep="first"
)

# Save cleaned data
cleaned_customers.to_csv(
    "../output/cleaned_customers.csv",
    index=False
)

print("\nCleaned customer data created successfully.")
print("Total records:", len(customers))
print("Cleaned records:", len(cleaned))
#test