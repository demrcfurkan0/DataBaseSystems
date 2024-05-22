import tkinter as tk
from tkinter import ttk
import pandas as pd
import pyodbc

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

def fetch_product_data():
    query = "SELECT ProductId, Barcode, SKUNumber, ProductName, Stock, ProductPrice FROM Product"
    df = pd.read_sql(query, conn)
    return df

def fetch_customer_data():
    query = "SELECT CustomerId, CustomerName, Address, Phone, Country, City FROM Customer"
    df = pd.read_sql(query, conn)
    return df

def update_stock():
    product_id = int(product_id_entry.get())
    new_stock = int(stock_entry.get())
    query = f"UPDATE Product SET Stock = ? WHERE ProductId = ?"
    cur.execute(query, (new_stock, product_id))
    conn.commit()
    refresh_data()
    product_id_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)

def refresh_data():
    for row in tree.get_children():
        tree.delete(row)
    if current_page == "products":
        df = fetch_product_data()
    else:
        df = fetch_customer_data()
    for index, row in df.iterrows():
        tree.insert("", "end", values=tuple(row))

def handle_enter(event):
    update_stock()

def switch_page(page):
    global current_page
    current_page = page
    refresh_data()
    if page == "products":
        product_page.lift()
        customer_page.lower()
        product_id_label.grid(row=0, column=0, sticky=tk.E)
        product_id_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
    else:
        customer_page.lift()
        product_page.lower()
        product_id_label.grid_remove()
        product_id_entry.grid_remove()

def add_customer():
    customer_name = customer_name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    country = country_entry.get()
    city = city_entry.get()

    query = "INSERT INTO Customer (CustomerName, Address, Phone, Country, City) VALUES (?, ?, ?, ?, ?)"
    cur.execute(query, (customer_name, address, phone, country, city))
    conn.commit()
    refresh_data()
    customer_name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)

current_page = "products"  # Default page

root = tk.Tk()
root.title("MSSQL Database Monitor")

# Tab control for switching pages
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Products page
product_page = ttk.Frame(notebook)
notebook.add(product_page, text="Products")

# Top grid for product information
top_frame = ttk.Frame(product_page, padding="10")
top_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

columns = ("ProductId", "Barcode", "SKUNumber", "ProductName", "Stock", "ProductPrice")
tree = ttk.Treeview(top_frame, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=0, column=0, columnspan=2)

# Bottom grid for stock update
bottom_frame = ttk.Frame(product_page, padding="10")
bottom_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Product ID label and entry
product_id_label = ttk.Label(bottom_frame, text="Product ID:")
product_id_label.grid(row=0, column=0, sticky=tk.E)

product_id_entry = ttk.Entry(bottom_frame)
product_id_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

# New stock label and entry
new_stock_label = ttk.Label(bottom_frame, text="New Stock:")
new_stock_label.grid(row=1, column=0, sticky=tk.E)

stock_entry = ttk.Entry(bottom_frame)
stock_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

# Update stock button
update_button = ttk.Button(bottom_frame, text="Update Stock", command=update_stock)
update_button.grid(row=2, columnspan=2, pady=5)

# Bind Enter key to update stock function
stock_entry.bind("<Return>", handle_enter)

# Customers page
customer_page = ttk.Frame(notebook)
notebook.add(customer_page, text="Customers")

customer_frame = ttk.Frame(customer_page, padding="10")
customer_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

customer_columns = ("CustomerId", "CustomerName", "Address", "Phone", "Country", "City")
customer_tree = ttk.Treeview(customer_frame, columns=customer_columns, show='headings')
for col in customer_columns:
    customer_tree.heading(col, text=col)
customer_tree.grid(row=0, column=0, columnspan=2)

# Bottom grid for adding a new customer
new_customer_frame = ttk.Frame(customer_page, padding="10")
new_customer_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Customer name label and entry
customer_name_label = ttk.Label(new_customer_frame, text="Customer Name:")
customer_name_label.grid(row=0, column=0, sticky=tk.E)
customer_name_entry = ttk.Entry(new_customer_frame)
customer_name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

# Address label and entry
address_label = ttk.Label(new_customer_frame, text="Address:")
address_label.grid(row=1, column=0, sticky=tk.E)
address_entry = ttk.Entry(new_customer_frame)
address_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

# Phone label and entry
phone_label = ttk.Label(new_customer_frame, text="Phone:")
phone_label.grid(row=2, column=0, sticky=tk.E)
phone_entry = ttk.Entry(new_customer_frame)
phone_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

# Country label and entry
country_label = ttk.Label(new_customer_frame, text="Country:")
country_label.grid(row=3, column=0, sticky=tk.E)
country_entry = ttk.Entry(new_customer_frame)
country_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

# City label and entry
city_label = ttk.Label(new_customer_frame, text="City:")
city_label.grid(row=4, column=0, sticky=tk.E)
city_entry = ttk.Entry(new_customer_frame)
city_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

# Add customer button
add_customer_button = ttk.Button(new_customer_frame, text="Add Customer", command=add_customer)
add_customer_button.grid(row=5, columnspan=2, pady=5)

# Navigation buttons
nav_frame = ttk.Frame(root, padding="10")
nav_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

products_button = ttk.Button(nav_frame, text="Products", command=lambda: switch_page("products"))
products_button.grid(row=0, column=0, padx=5)

customers_button = ttk.Button(nav_frame, text="Customers", command=lambda: switch_page("customers"))
customers_button.grid(row=0, column=1, padx=5)

# Configure grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Initial data load
refresh_data()

# Start the main loop
root.mainloop()
