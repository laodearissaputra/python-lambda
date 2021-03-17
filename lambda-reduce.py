from functools import reduce

lis = [ 1 , 3, 5, 6, 2, ]  

print ("1. The maximum element of the list is : ",end="")  
print (reduce(lambda a,b : a if a > b else b,lis)) 

li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print ("\n2. result use sum in reduce : ", sum) 