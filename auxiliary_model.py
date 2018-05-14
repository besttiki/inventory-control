import pandas as pd
import numpy as np
__all__ = ['demand_model','arrive_model']

class demand_model:
    def __init__(self,demand_type = None,distribution = None,input_file = None,period = 0): 
        self.period = period
        try:
            if demand_type == "fix":
                self.demand = 
                self.
            elif demand_type == "random":

            elif demand_type == "input":
                try: 
                    demand = pd.read_csv(input_file)
                except:
                    raise Exception("Check your input file name")
            else:
                raise Exception("Check your demand_type name")
    def get_demand(self,period):
        return self.demand_amount[period]
if __name__ == "__main__":
    n_period = 10
    s = np.random.normal(10,1,n_period)
    s = pd.read_csv("test.csv")
    s[0]
    args= {'1':2,'3':2}
    a = str(1)
    print(args[a])
    if 2=1