
import torch 
import torch.nn as nn

class ServerNN(nn.Module):
    def __init__(self, input_size, 
                 output_size):
        super(ServerNN, self).__init__()
        self.layer1 = nn.Linear(input_size, 160)
        self.layer2 = nn.Linear(160, output_size)
    
    def forward(self, x):
        model = nn.Sequential(
            self.layer1,
            nn.ReLU(),
            self.layer2,
            nn.ReLU()
        )
        return model(x)
        

            
