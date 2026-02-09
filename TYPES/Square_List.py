data=[1,2,2,3,4,4,5,6,7,7]
set_sq={x*x for x in data if x%2!=0 and x*x>10}
print(set_sq)