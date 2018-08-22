'''
Created on 2018年4月23日

@author: xielin
'''
#3、my @people = qw/Fred barney Fred wila dino barney Fred pebbles/;对这个数组进行排序
arr = ('Fred','barney','Fred', 'wila', 'dino', 'barney', 'Fred', 'pebbles')
print("排序后的arr：",sorted(arr))
list1 = list(arr)
#print(list1)
print("排序后的list1:",sorted(list1))
list2 = [12,16,7,9,9,10]
list2.sort()
print("排序后的list2:",list2)
