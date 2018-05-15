class BaseStock:
    def __init__(self,basestock = 0):
        """
            params:
                basestock: float,basestock
        """
        self.basestock = basestock
    def push_order(self,inventory = 0,pipeline = 0):
        """
            params:
                inventory: float,inventory_level
                pipeline；float,sum of pipeline stock
            returns：
                order_nums:float,this period should push orders nums
        """
        order_nums = self.basestock - pipeline - inventory
        return order_nums 

    def reset_basestock(self,newbasestock = 0):
        self.basestock = newbasestock
        

def get_nemo(a,b):
    return a+b

def get_tiki(a,b):
    return a-b