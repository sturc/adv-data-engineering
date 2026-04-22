import random
from datetime import datetime, timedelta
import pandas as pd

# Parameter
num_customers = 20
max_orders_per_customer = 20
max_support_per_customer = 4
max_emails_per_customer = 12

customer_ids = list(range(1, num_customers + 1))

orders = []
support = []
emails = []

# Aktuelles Jahr für Daten
current_year = 2025

for cid in customer_ids:
    # Bestellungen
    num_orders = random.randint(1, max_orders_per_customer)
    order_dates = [datetime(current_year, 1, 1) + timedelta(days=random.randint(0, 364)) for _ in range(num_orders)]
    order_values = [round(random.uniform(20, 250), 2) for _ in range(num_orders)]
    order_discount = [random.choice([0, round(random.uniform(5, 50), 2)]) for _ in range(num_orders)]
    
    for dt, val, disc in zip(order_dates, order_values, order_discount):
        orders.append({
            "Customer_ID": cid,
            "Order_Date": dt.strftime("%Y-%m-%d"),
            "Order_Value": val,
            "Discount_Used": disc
        })
    
    # Supportanfragen
    num_support = random.randint(0, max_support_per_customer)
    support_dates = [datetime(current_year, 1, 1) + timedelta(days=random.randint(0, 364)) for _ in range(num_support)]
    support_types = [random.choice(["Frage", "Beschwerde", "Sonstiges"]) for _ in range(num_support)]
    
    for dt, typ in zip(support_dates, support_types):
        support.append({
            "Customer_ID": cid,
            "Support_Date": dt.strftime("%Y-%m-%d"),
            "Support_Type": typ
        })
    
    # E-Mail-Kampagnen
    num_emails = random.randint(1, max_emails_per_customer)
    email_dates = [datetime(current_year, 1, 1) + timedelta(days=random.randint(0, 364)) for _ in range(num_emails)]
    opened = [random.choice([True, False]) for _ in range(num_emails)]
    clicked = [random.choice([True, False]) if o else False for o in opened]
    
    for dt, o, c in zip(email_dates, opened, clicked):
        emails.append({
            "Customer_ID": cid,
            "Email_Date": dt.strftime("%Y-%m-%d"),
            "Opened": o,
            "Clicked": c
        })

# DataFrames
orders_df = pd.DataFrame(orders)
support_df = pd.DataFrame(support)
emails_df = pd.DataFrame(emails)

# Export
orders_path = "data/grunddaten_bestellungen.csv"
support_path = "data/grunddaten_support.csv"
emails_path = "data/grunddaten_emails.csv"

orders_df.to_csv(orders_path, index=False,sep=';')
support_df.to_csv(support_path, index=False,sep=';')
emails_df.to_csv(emails_path, index=False,sep=';')

orders_path, support_path, emails_path