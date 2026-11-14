import pandas as pd
from data_preparation import DataPreparation as dp
class TimeSeriesAnalysis:
    def __init__(self,data_t):
        self.data_t=dp(data_t)
    def analyze_event_in_hour(self,column:str,Freq:str):
        data=self.data_t.load_incidents()
        data[column]=pd.to_datetime(data[column])
        to_index=data.set_index(column)
        try:
            content=to_index.resample(Freq).size()
        except ValueError:
            print(f"Frequency must be a for example hour,day,week,month,or year:{Freq}")
            return Freq
        return content  
    def rolling(self,column:str,Frequency:str):
        df=self.analyze_event_in_hour(column,Frequency)
        try:
            rol=df.rolling(window=3).mean()
        except ValueError:
            print(f"Frequency must be a for example hour,day,week,month,or year:{Frequency}")
            return Frequency
        return rol
    def diff(self,column:str,freq:str):
        df=self.analyze_event_in_hour(column,freq)
        try:
            dfi=df.diff()
        except ValueError:
            print(f"Frequency must be a for example hour,day,week,month,or year:{freq}")
            return freq
        return dfi
t1=TimeSeriesAnalysis("incidents-3.csv")
print(t1.diff("timestamp","1h"))