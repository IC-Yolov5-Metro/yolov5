import torch

print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.zeros(1).cuda())