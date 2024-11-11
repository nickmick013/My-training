my_dict = {'Viktor': 2010, 'Alex': 2001, 'Ann': 1999}
print('My dict:', my_dict)
print('Existing value:', my_dict['Ann'])
print('Not existing value:', my_dict.get('Serge'))
my_dict.update({'Tom': 2002, 'Sara': 2005})
print('Deleted value:', my_dict.pop('Alex'))
print('Modified dictionary:', my_dict)
my_set = {4,2,8,4,6,2,7,'apple','flower'}
print('My set:', my_set)
my_set.add((5, 'hat', 354.6))
my_set.discard("flower")
print('Modified set:', my_set)