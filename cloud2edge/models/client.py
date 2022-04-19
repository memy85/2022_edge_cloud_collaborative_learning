# client model

import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torch.nn.functional as F

class ClientNN(nn.Module):
    
    def __init__(self):
        super(ClientNN, self).__init__()
        self.vgg11 = torch.hub.load('pytorch/vision:v0.10.0', 'vgg11', pretrained =True)
        self.fc1 = nn.Linear(1000,200)
        self.fc2 = nn.Linear(200,10)
        # self.fc3 = nn.Linear(10,1)
        
        self.cfc1 = nn.Linear(80, 10)
        self.output = nn.Linear(20, 1)
        
        
        self.server2hidden = nn.Sequential(
            self.vgg11,
            nn.ReLU(),
            self.fc1,
            nn.ReLU(),
            self.fc2,
            nn.ReLU())
        
        self.client2hidden = nn.Sequential(
            self.cfc1,
            nn.ReLU()
        )
        
    
    def forward(self, x_server, x_client):
        
        network1_output = self.server2hidden(x_server)
        network2_output = self.client2hidden(x_client)
        
        x_cat = torch.cat([network1_output, network2_output.unsqueeze(0)], 1)
        x = self.output(x_cat)
        return x
    
