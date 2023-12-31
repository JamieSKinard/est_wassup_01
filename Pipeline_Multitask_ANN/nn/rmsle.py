import torch
import torch.nn as nn

class RMSLELoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.mse = nn.MSELoss()
        
    def forward(self, pred, actual):
        return (torch.sqrt(self.mse(torch.log(pred[:,0] + 1), torch.log(actual[:,0] + 1)))*10+
                torch.sqrt(self.mse(torch.log(pred[:,1] + 1), torch.log(actual[:,1] + 1)))*5+
                torch.sqrt(self.mse(torch.log(pred[:,2] + 1), torch.log(actual[:,2] + 1)))*3+
                torch.sqrt(self.mse(torch.log(pred[:,3] + 1), torch.log(actual[:,3] + 1))))


class RMSELoss(torch.nn.Module):
    def __init__(self):
        super(RMSELoss,self).__init__()

    def forward(self,x,y):
        criterion = nn.MSELoss()
        #print('1',x[:,0], y)
        loss = (torch.sqrt(criterion(x[:,0], y[:,0]))+
                torch.sqrt(criterion(x[:,1], y[:,1]))+
                torch.sqrt(criterion(x[:,2], y[:,2]))+
                torch.sqrt(criterion(x[:,3], y[:,3])))
        
        return loss