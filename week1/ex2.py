'''def danhsach(name,*number,**info):
 	print(f'name:{name}')
 	for x, y in enumerate(number):
 		print(f'phone{x}:{y}') 

 	for key,value in info.items():
 		print(f'{key}:{value}')


danhsach('nguyen huu toi','0372024749','0902751738',address='xuan thoi dong, hoc mon, tp ho chi minh')



'''
'''
 xuất danh sách  đếm số lần xuất hiện trong mảng 
'''
'''
import collections

c= collections.Counter([1,2,3,1,3,4,1,4,4,4])# fuction tính toán và sắp xếp lại số lần 
print(c)
# so lần  xuat hien
print(f'4  lặp lại {c[4]} lần')

#print(f'Most common element is {c.most_common(1)[0][0]} repeated {c.most_common(1)[0][1]} times')
print(f'con so lặp lại nhiều nhất là {c.most_common(1)[0][0]}  lặp lại {c.most_common(1)[0][1]} lần')
'''

###
#
#
#
#
'''
from collections import defaultdict
address= defaultdict(lambda:" error")
address['jack']={'jack':'jacknguyen', 'age': 22}


print(address['jack'])
print(address['top'])
'''
##\
from collections import defaultdict
diachi= defaultdict(lambda:" error")
diachi['jack']={'jack':'jacknguyen', 'age': 22}


print(diachi['jack'])
print(diachi['top'])
