import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
from torch.autograd import Variable
from torchvision.models import resnet18
import sys
sys.path.append("pytorch-image-models")
import timm
##############################
#         Encoder
##############################


class Encoder(nn.Module):
    def __init__(self, latent_dim):
        super(Encoder, self).__init__()
        # resnet = resnet18(pretrained=True)
        # resnet = timm.create_model('resnet50', pretrained=True)
        # model = timm.create_model('efficientnet_b3a', pretrained=True)

        self.feature_extractor = timm.create_model('efficientnet_b3a', pretrained=True,num_classes=0)
        self.final = nn.Sequential(
            nn.Linear(self.feature_extractor.num_features, latent_dim), nn.BatchNorm1d(latent_dim, momentum=0.01)
        )

    def forward(self, x):
        with torch.no_grad():
            x = self.feature_extractor(x)
        x = x.view(x.size(0), -1)
        return self.final(x)

if __name__ == "__main__":
    jim_input = torch.randn((2,3,320,320))

    model = Encoder(latent_dim=512)

    x = model(jim_input)
    print(x.shape)

