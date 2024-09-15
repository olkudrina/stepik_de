import pandas as pd


class Reader():

    def __init__(self, file_path):
        self.path = file_path

    def read_csv_file(self):
        df = pd.read_csv(self.path)
        return df

    def read_excel_file(self):
        df = pd.read_excel(self.path)
        return df
