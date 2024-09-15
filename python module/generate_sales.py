import pandas as pd
import numpy as np
from datetime import datetime
import random


# constants
ALL_PRODUCTS = {
    'apple': 10.5, 'cherry': 25.6,
    'pear': 15.7, 'cigarettes': 123.,
    'mango': 250.99, 'bread': 15.4
}
df = pd.DataFrame(columns=['product_name', 'quantity', 'price', 'date'])


def generate_date(y, m, d):
    try:
        dt = datetime(y, m ,d)
    except ValueError:
        dt = None
    return dt

if __name__ == "__main__":
    for i in range(100000):
        dt_ = None
        d = np.random.randint(1, 31)
        m = np.random.randint(1, 12)
        y = np.random.randint(2021, 2024)

        dt_ = generate_date(y, m, d)
        
        if dt_:
            product = random.choice(list(ALL_PRODUCTS.keys()))
            resulting_list = [
                product,
                np.random.randint(1, 100),
                ALL_PRODUCTS[product],
                dt_
            ]
            df.loc[df.shape[0]] = resulting_list
    

    df.to_csv('sales_data.csv', index=False)
