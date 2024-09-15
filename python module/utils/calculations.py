import pandas as pd


class AnalyticsMethods():

    def __init__(
            self,
            df: pd.DataFrame,
            product_column: str,
            date_column: str,
            qt_columns: str,
            price_column: str
        ):
        self.df = df
        self.product = product_column
        self.date = date_column
        self.qt = qt_columns
        self.price = price_column

    def calculate_sales(self):
        self.df['sales'] = self.df[self.qt] * self.df[self.price]
        return self.df

    def total_sales_per_product(self):
        data = self.calculate_sales()[[self.product, 'sales']]
        result = data.groupby(self.product).sum()
        return result
    
    def sales_over_time(self):
        data = self.calculate_sales()[[self.date, 'sales']]
        result = data.groupby(self.date).sum()
        return result
