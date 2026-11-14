import pandas as pd
class DataPreparation:
    def __init__(self,data_f):
        self.data_f=data_f
        if not isinstance(self.data_f,str):
            raise TypeError("file path must be a str")
    def __repr__(self):
        return f"DataPreparation with data_f:{self.data_f}"
    def load_incidents(self):
        try:
            data=pd.read_csv(self.data_f,usecols=["timestamp","event_type", "severity",
                            "source_ip", "username", "status"])
        except FileNotFoundError:
            print(f"file not found in This location:{self.data_f}")
            return pd.DataFrame()
        except PermissionError:
            print(f"file is open please close the app")
            return pd.DataFrame()
        return data.loc[:,~data.columns.str.contains("^Unnamed")]
    def to_datatime(self,column:str):
        df=self.load_incidents()
        try:
            df[column]=pd.to_datetime(df[column])
        except KeyError:
            print(f"{column} not found in dataframe")
            return column
        return df[column]
    def sort_values(self,column:str):
        data=self.load_incidents().sort_values(by=column,ascending=True)
        return data
    def analyze_missing_valuse(self):
        return self.load_incidents().isnull()
    def count_missing_values(self):
        return self.analyze_missing_valuse().sum()
d1=DataPreparation("incidents-3.csv")
print(d1.analyze_missing_valuse())