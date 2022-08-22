import torch
print(torch.__version__)
print(torch.cuda.is_available())
a = torch.tensor(1)
a = a.to('cuda')
print(a.is_cuda)
