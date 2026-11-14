import pandas as pd
import json
from security_analysis import SecurityAnalysis as sa
class ReportGenerate:
    def __init__(self,input_file,output_file):
        self.input_file=sa(input_file)
        self.output_file=output_file
    def generate_sumary(self):
        return {
            "total_events":int(self.input_file.incidents.shape[0]),
            "severity_summary":len(self.input_file.analyze_severity()),
            "failed_login":len(self.input_file.event_login_failed()),
            "open_high_priority":len(self.input_file.get_open_high_priority()),
            "filter_events":len(self.input_file.filter_events()),
            "analyze_ip":len(self.input_file.analyze_ip())
        }
    def export_json(self):
        data_report=self.generate_sumary()
        if not self.output_file.endswith("json"): 
            raise FileExistsError(f"output_file should be a json file not:{self.output_file}")
        try:
            with open(self.output_file,"w") as f:
                data=json.dump(data_report,f,indent=4)   
        except FileNotFoundError:
            print(f"file not found in This location:{self.output_file}")
            return self.output_file
        return " data Successfully save in json_file"
    def export_csv(self):
        report={}
        for k,v in self.generate_sumary().items():
            report.setdefault(k,[v])
        
        if not self.output_file.endswith("csv"):
            raise FileExistsError(f"output_file should be a csv file not:{self.output_file}")    
        try:
            result=pd.DataFrame(report) 
            result.to_csv(self.output_file,index=False)   
        except FileNotFoundError:
            print(f"file not found in This location")
            return self.output_file
        return f"data successfully save in csv file:{self.output_file}"
       
d1=ReportGenerate("incidents-3.csv","security_report.json")
print(d1.export_json())

    
    