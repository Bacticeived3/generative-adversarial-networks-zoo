import torch
import torch.nn as nn
class Generator(nn.Module):
    def __init__(self, nz, ngf, nc):
        super(Generator, self).__init__()
        self.main = nn.Sequential(nn.ConvTranspose2d(nz, ngf, 4, 1, 0))