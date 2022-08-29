"""
https://qiita.com/mathlive/items/2a512831878b8018db02#5-dataset%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%E3%81%A8dataset%E3%81%AE%E8%87%AA%E4%BD%9C

"""
import torch
import torchvision
import numpy as np

# Tensor変換；PIL image or ndarray data(H,W,C) -> Tensor data(C,H,W)
# Tensor data = trans(PIL or ndarray) のために利用
trans = torchvision.transforms.ToTensor()

"""
### Tensor変換 + 正規化
###   torchvision.transforms.Compose :
###       引数で渡されたlist型の[~~,~~,...]というのを先頭から順に実行
###       そのためlist内の前処理の順番には十分注意
"""
trans = torchvision.transforms.Compose(
    [
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(mean=(0.5,), std=(0.5,)),
    ]
)

# 自作 transforms
class Plus2(object):
    def __init__(self):
        pass

    """
    # The __call__ method enables Python programmers
    # to write classes where the instances behave like functions and
    # can be called like a function.
    # For Example :
    #   p = Plus2()
    #   print(p(98)) -> 100
    """

    def __call__(self, x):
        data = x + 2
        return data


trans = Plus2()
x = 3
data = trans(x)
print(data)

# 自作のdataset
class Mydatasets(torch.utils.data.Dataset):
    def __init__(self, transform=None):
        self.transform = transform

        self.data = [1, 2, 3, 4, 5, 6]
        self.label = [0, 1, 0, 1, 0, 1]

        self.datanum = len(self.data)

    def __len__(self):
        return self.datanum

    def __getitem__(self, idx):
        out_data = self.data[idx]
        out_label = self.label[idx]

        if self.transform:
            out_data = self.transform(out_data)

        return out_data, out_label


mydataset = Mydatasets(trans)
print('mydataset: ', mydataset)
print('len(mydataset): ', len(mydataset))
print('mydataset[1]: ', mydataset[2])
