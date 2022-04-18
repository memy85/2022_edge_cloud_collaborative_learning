
class Aggregator:
    '''
    class that returns aggregated value of weights.
    This clas requires data(weights), and aggregation_method
    data : list of weights from edge devices
    aggregation_method : a string that indicates aggregation method
    '''
    def __init__(self, data:list, aggregation_method):
        self.data = data
        self.aggregation_method = aggregation_method
    
    def aggregate(self, aggregation_method):
        pass
    
    def fedavg(self):
        pass
    
    def loss_basedAvg(self):
        pass
        