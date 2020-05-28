def kargs(**kwargs):
        return sorted(kwargs, key = kwargs.get)           
print(kargs(f=4.1,b=2,c=3,d=4,e=4.2))