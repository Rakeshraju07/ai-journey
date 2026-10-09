import numpy as np
marks = [70,80,90]
print([m*2 for m in marks]) #list way need a loop/comprehension

arr = np.array(marks) #numpy way
print(arr*2) #numpy way, no loop needed

arr = np.array([10,20,30,40,50])
print(arr.shape) #shape of the array
print(arr.dtype) #data type of the array    
print(arr[0])
print(arr[-1])
print(arr[1:4])

print(arr>25)
print(arr[arr>25]) #filtering the array
print(arr.mean()) #mean of the array
print(arr.sum()) #sum of the array
print(arr.max()) #max of the array

#2D arrays

m= np.array([[1,2,3],[4,5,6]])
print(m.shape)
print(m[1])
print(m[1,2]) #row 1, column 2

marks = np.array([82, 67, 91, 45, 73])
print(marks[marks>marks.mean()]) #filtering the array based on mean
print(len(marks[marks>marks.mean()])) #count of students above mean

nums = np.arange(1,11) #1 to 10
print(nums%2==0) #boolean array for even numbers
print(nums[nums%2==0]) #filtering even numbers
prices = np.array([100, 250,80,400])
print(prices*0.9) #10% discount
print(prices*0.8) #20% discount