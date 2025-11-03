import numpy as np
samplearray=np.random.randint(0,50,size=(5,4))
print("original array",samplearray)
mean_column=samplearray.mean(axis=0)
print("mean of each column is",mean_column)
max_value=samplearray.max(axis=1)
print("maximum value in each row is",max_value)
sum=samplearray.sum()
print("sum of the array is",sum)

#slicing
slice_arr=samplearray[0:2,2:4]
print("slicing an array is",slice_arr)
boo_in=samplearray[samplearray>20]
print("greater than the value",boo_in)



