
import torch 
import torch.nn as nn
import torch.optim as optim


class ServerNetwork:
    def __init__(self, config_object):
        self.task: str = config_object.task
        self.server_input_size = config_object.server_input_size
        self.layers = config_object.layers
        self.hidden_units = config_object.hidden_units
        self.random_seed = config_object.random_seed
        
        self.block = nn.Sequential(
            nn.Linear(self.hidden_units, self.hidden_units),
            nn.ReLU()
        )
    
    def create_server_network(self):
        self.server_input_layer = nn.Linear(self.server_input_size, self.hidden_units)
        
        for idx, layer in enumerate(self.layers):
            
            self.block = nn.Sequential(
                        nn.Linear(self.hidden_units, self.hidden_units),
                        nn.ReLU()
                        )

            
