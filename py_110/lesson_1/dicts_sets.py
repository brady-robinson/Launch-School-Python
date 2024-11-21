# data = {'name': 'Srdjan', 'age': 38, 'city': 'Belgrade'}
# # data['state']
# # print(data)
# # print('name' in data)
# # del data['name']
# # print(data)
# # print('name' in data)
# # data_copy = data.copy()
# # print(data == data_copy)
# # print(data is data_copy)
# data.setdefault('country', 'Serbia')
# # data.setdefault('name', 'John')
# # # city = data.pop('job', 'unknown')
# # country = data.popitem()
# # print(data)
# # print(country)
# # data.update({'country': 'England', 'job':'SWE'})
# # data = data | {'country': 'England', 'job':'SWE'}
# data |= {'country': 'England', 'job':'SWE'}
# print(data)

# lst = [['name', 'brady']]
# tuple_data = (('name', 'Srdjan'), ('city', 'Belgrade'))
# dict_lst = dict(tuple_data)
# print(dict_lst)

set1 = {'apple'}
set2 = {'apple', 'pear'}
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set2.isdisjoint(set1))
# set2.remove('carrot')
set2.discard('carrot')
set2.discard('pear')
print(set2)