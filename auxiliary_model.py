import pandas as pd
import numpy as np
__all__ = ['demand_model','pipeline_model']

class demand_model:
    def __init__(self,demand_type = None,distribution = None,file = None,period = 0): 
        self.period = period
        if demand_type == "random":
            self.demand_amount = distribution
        elif demand_type == "input":
            try: 
                demand = pd.read_csv(file,header = None,names = ['v'])
                self.demand_amount = demand.v.tolist()
                if len(self.demand_amount) < period:
                    raise Exception("Demand data is less than period ")
            except:
                raise Exception("Check your input file name")
        else:
            raise Exception("Check your demand_type name")

    def get_demand(self,period):
        return self.demand_amount[period-1]

class pipeline_model:
    def __init__(self,pipeline_type = None,distribution = None,file = None,period = 0):
        """
        args:
            self.pipeline_at:
                list, pipeline arrival time  
        """
        if pipeline_type == "random":
            self.pipeline_at =  distribution
        elif pipeline_type == "input":
            try: 
                pipeline = pd.read_csv(file,header = None,names = ['v'])
                self.pipeline_at = pipeline.v.tolist()
                if len(self.pipeline_at) < period:
                    raise Exception("Pipeline data is less than period ")
            except:
                raise Exception("Check your input file name")
        else:
            raise Exception("Check your pipeline_type name")
    def get_plat(self,period):
        """
        get time period pipeline arrival time (leadtime)
        args:
            period:
                int, period
        returns:
            period pipeline arrival time
        """
        return self.pipeline_at[period - 1]

if __name__ == "__main__":
    # n_period = 10
    # s = np.random.normal(10,1,n_period)
    # s = pd.read_csv("demand/test.csv",header=None,names =['v'])
    # s = s['v'].tolist()
    # s[0]
    # args= {'1':2,'3':2}
    # a = str(1)
    # print(args[a])
    n_period = 10
    s = np.random.normal(10,1,n_period)
    p = pipeline_model(pipeline_type ="input",file = "pipeline_arrival/test.csv",period =n_period)
    p.get_plat(2)


