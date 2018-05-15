import demand_model,pipeline_model from auxiliary_model

class Environment:
    """
    attrs:
        pipeline:
            dict, means order hasn't arrived
        inventory:
            float, means real inventory_level in warehouse
    """
    def __init__(self,agent = None,pipeline = None,inventory = 0,demand_model = None,arrival_model = None):
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
        self.period = 0  
        self.pipeline = pipeline
        self.inventory =  inventory
        self.demand_model = demand_model
        self.arrive_model = arrive_model
    def next(self,period):
        """
        args:
            order：
                float,push new order
            period:
                str,real period
        """
        neworder = self.agent.order()
        self.pipeline.update({period,order}) 

        #demand_consume
        self.demand = demand_mode
        #order arrival


    def demand_consume(self,order,period)
        self.pipeline
    def order_arrival(self,)   

#class Random

if __name__ =="__main__":
    sim_e = Environment(basestock)