import requests
import pandas as pd
from sqlalchemy import create_engine

# Extract data from API
def extract():
    response = requests.get('https://api.ecommerce.com/orders')
    return response.json()

# Transform data
def transform(data):
    df = pd.DataFrame(data)
    df['order_value'] = df['quantity'] * df['price']
    return df

# Load data into database
def load(df):
    engine = create_engine('postgresql://username:password@localhost:5432/dbname')
    df.to_sql('orders', engine, index=False, if_exists='replace')

if __name__ == "__main__":
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)