import pandas as pd
import pyodbc
import pymssql
from faker import Factory, Faker
import random
# Categories dictionary
categories = {
    "Top": 1,
    "Bottom": 2,
    "Socks":3
}

# Collections dictionary
collections = {
    "Sweat Off The Stress": 1,
    "Inhale Peace Exhale Stress": 2,
    "Sun Believable":3,
    "All Day":4
}

# Colors dictionary
colors = {
    "Black": 1,
    "Light Grey Melange": 2,
    "Lapis Blue": 3,
    "Baby Blue": 4,
    "White": 5
}

# Sizes dictionary
sizes = {
    "XS": 1,
    "S": 2,
    "M": 3,
    "L": 4,
    "XL": 5
}

seasons = {
    "S": 1,
    "C": 2
}

types = {
    "TT": 1,
    "TS": 2,
    "CR": 3,
    "BR": 4,
    "LG": 5,
    "SH": 6,
    "PN": 7,
    "YP": 8,
    "JG": 9,
    "SW": 10,
    "BS": 11,
    "DR": 12,
    "SK": 13,
    "RC": 14,
    "WB": 15,
    "SC": 16,
    "AC": 17,
    "JP": 18
}

filepath = r"C:\Users\demir\Desktop\DataBaseSystem/zenatives_product_data.xlsx"

df = pd.read_excel(filepath, sheet_name="zenatives_product_data")[::10]
product_list = list()

for i, row in (df.iterrows()):
    product = {
        "seasons": row[1],
        "fabrictech": row[2],
        "gender": row[3],
        "type": types[row[4]],
        "productsize": row[5],
        "colors": row[6],
        "collection":collections[row[7]],
        "category": categories[row[8]],
        "productname": row[9],
        "skunumber": row[10],
        "barcode": row[11],
        "stock": row[12],
        "price": row[13]

    }
    product_list.append(product)

print(product_list)

print(len(product_list))

#print(df["Color Name"].unique())
#print(df["Product Type Code"].unique())

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'FURKAN'
DATABASE_NAME = 'DataBaseSystems'

connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust_Connection=yes;
"""

conn = pyodbc.connect(connection_string)
cur = conn.cursor()

#print(df[["Product Type Code","Product Type Name"]])


keywords=set()
df2 = df[["Product Type Code","Product Type Name"]]
for i, row in (df2.iterrows()):
    keywords.add((row[0],row[1]))

# for i,t in enumerate(product_list[108:]):
#     print(t)
#     prompt = (f"Insert Into Product values("
#               f"'{t["barcode"]}',"
#               f"'{t["skunumber"]}',"
#               f"'{t["productname"]}',"
#               f"'{t["price"]}',"
#               f"'{t["category"]}',"
#               f"'{t["collection"]}',"
#               f"'{t["colors"]}',"
#               f"'{t["productsize"]}',"
#               f"'{t["seasons"]}',"
#               f"'{t["fabrictech"]}',"
#               f"'{t["type"]}',"
#               f"'{t["gender"]}')")
#     cur.execute(prompt)
#     conn.commit()

fake = Factory.create()
fake2 = Faker()

#customers = [fake2.profile() for _ in range(30)]
#print(customers)
#print(fake2.profile())
#print(fake2.profile())

# for i,cus in enumerate(customers[6:]):
#     babapro = f"Insert Into Customer Values({i+6},'{cus["name"]}', '{cus["address"]}', '{cus["ssn"]}','{fake.country()}','{fake.city()}')"
#     cur.execute(babapro)
#     conn.commit()

xkraltr = "Select ProductId from Product"
ids = cur.execute(xkraltr).fetchall()
for id in ids:
    prompt2 = f"UPDATE Product SET Stock ={random.randint(13,43)} WHERE ProductId ={id[0]}"
    cur.execute(prompt2)
    conn.commit()

