import numpy as np
data=np.random.randint(0,50,size=(5,4))
print("original array",data)
subrtact_mean=data.mean(axis=0)
print()
print("mean of subtraction is",subrtact_mean)
print()
std_dev=(data-subrtact_mean)/data.std(axis=0)
print("standared deviation of datab is",std_dev)

      

