# Delivery 1 
# Celina Hansen

# Import
import pandas as pd


# Importer frar excel fil, 4 forskellige ark --> openpyxl bruges til at åbne .xlsx fil
df_order = pd.read_excel(r"/Users/celinahansen/Documents/Delivery/delivery-1/my_shop_data.xlsx", engine='openpyxl', sheet_name="order")
df_employee = pd.read_excel(r"/Users/celinahansen/Documents/Delivery/delivery-1/my_shop_data.xlsx", engine='openpyxl', sheet_name="employee")
df_products = pd.read_excel(r"/Users/celinahansen/Documents/Delivery/delivery-1/my_shop_data.xlsx", engine='openpyxl', sheet_name="products")


def get_data():
    # Employee name
    df_employee["emp_name"] = df_employee["firstname"] + " " + df_employee["lastname"]

    # Product name
    df_products["prod_name"] = df_products["productname"]

    # Data for at få total salg
    df_order['total'] = df_order['unitprice'] * df_order['quantity']

    # Data - Relationer
    order = pd.merge(df_order, df_products, on='product_id')
    order = pd.merge(order, df_employee, on='employee_id')

    # Order - Valg af kolonner
    order = order[['order_id', 
                'product_id', 'prod_name', 'type',
                'employee_id', 'emp_name',
                'total']]

    # Retuner til delivery_1_app.py
    return order

