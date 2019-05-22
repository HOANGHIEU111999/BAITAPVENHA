class HCN:
    def __init__(self,rong,dai):
        self .rong =rong
        self.dai = dai
    def dientich (self):
        return self.dai*self.rong
a=HCN(4,6)
b=HCN(2,40)
print(a.dientich())
print(b.dientich())

