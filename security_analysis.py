import pandas as pd
from time_series_analysis import TimeSeriesAnalysis as tsa
class SecurityAnalysis:
    def __init__(self,input_data):
        self.input_data=tsa(input_data)
        self.incidents=self.input_data.data_t.load_incidents()
    def analyze_severity(self):
        return self.incidents["severity"].value_counts().to_dict()
    def filter_events(self):
        return self.incidents[self.incidents
        ["severity"].isin(["HIGH","CRITICAL"])].to_dict(orient="records")
    def analyze_login_failed(self,column:str):
        self.incidents[column]=pd.to_datetime(self.incidents[column])
        data=self.incidents.set_index(column).sort_values(by=column,ascending=True)
        filter_data=data[data["event_type"]=="LOGIN_FAILED"]
        return filter_data.resample("1h").size()
    def get_open_high_priority(self):
        return self.incidents[(self.incidents["status"]=="OPEN")&
        (self.incidents["severity"].isin(["HIGH","CRITICAL"]))].to_dict(orient="records")
    def event_login_failed(self):
        return self.incidents[self.incidents["event_type"]=="LOGIN_FAILED"]
    def analyze_ip(self):
        return self.incidents["source_ip"].value_counts().to_dict()


    