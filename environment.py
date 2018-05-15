from auxiliary_model import demand_model,pipeline_model 
from agent import BaseStock
import numpy as np
class Environment:
    """
    attrs:
        pipeline:
            dict, means order hasn't arrived
        inventory:
            float, means real inventory_level in warehouse
    """
    def __init__(self,agent = None,pipeline = None,inventory = 0,demand_model = None,arrive_model = None):
        """
        args:
            agent :
                class, replenishment algorithm
            pipeline :
                dic,
            inventory:
                float,initial_inventory_level
            demand_model:
                list,every_period_demand
            arrive_model:
                list,every_period_pipeline

        """
        self.agent = agent
        self.period = 1 
        if pipeline == None:
             self.pipeline = {}
        else:
            self.pipeline = pipeline
        self.inventory =  inventory
        self.demand_model = demand_model
        self.arrive_model = arrive_model
    def next(self):#,period):
        """
        args:
            order：
                float,push new order
            period:
                str,real period
        """
        pipeline_sum = 0
        for k,v in self.pipeline.items():
            pipeline_sum +=  self.pipeline[k]
        neworder = self.agent.push_order(inventory = self.inventory,pipeline = pipeline_sum)
        print("{} period  order {} inventory{}".format(self.period,neworder,self.inventory))
        period = self.period 
        self.pipeline.update({period:neworder}) 

        #demand_consume
        self.demand_consume(period)
        #order arrival
        self.order_arrival(period)
        #
        self.period += 1


    def demand_consume(self,period):
        self.inventory -= self.demand_model.get_demand(period)
        if self.inventory < 0:
            self.inventory = 0 
    def order_arrival(self,period):
        remove_list = []
        for k,v in self.pipeline.items():
            if k + self.arrive_model.get_plat(k) == period + 1:   
                remove_list.append(k)
        for i in range(len(remove_list)):
            self.inventory += self.pipeline[remove_list[i]]
        for i in range(len(remove_list)):
            del self.pipeline[remove_list[i]]
#class Random

if __name__ =="__main__":

    n_period = 10
    demand_data = [3 for i in range(15)]
    demand_data[1]
    #np.random.normal(5,1,n_period)
    demand = demand_model(demand_type = "random",distribution = demand_data)
    
    pipe_arrival = pipeline_model(pipeline_type = "input",file ="pipeline_arrival/test.csv",period = n_period)
    
    bs = BaseStock(basestock = 10)
    sim_e = Environment(agent = bs,demand_model = demand,arrive_model = pipe_arrival)
    for i in range(n_period+1):
        sim_e.next()
    # s = {1:1,2:3,3:3,4:5}
    # i = 4 
    # remove_list = []
    # for k,v in s.items():
    #     if i + v == 5:
    #         print(k)
    #         remove_list.append(k)
    #         print(len(s))
    #     i -= 1
    # for i in range(len(remove_list)):
    #     del s[remove_list[i]]
    # print(s[2])
    # s = None
    # s.append(1)