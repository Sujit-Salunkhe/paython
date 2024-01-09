list1=[1,2,3,4,5,6]
list2 = [x for x in list1]
# print(list2)
def getIndex(data_list,string):
    result = 0
    for a_character in string:
        a = ord(a_character)
        result += a
    return result % len(data_list) 

MAX_HASH_TABLE_SIZE = 4096
class HashTable:

    def __init__(self,max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self,key,value):
        idx = getIndex(self.data_list,key)
        self.data_list[idx] = (key,value)

    def find(self,key):
        idx = getIndex(self.data_list,key)
        kv = self.data_list(idx)
        if kv is None:
            return None
        else:
            key,value = kv
            return value
        
    def update(self,key,value):
        idx = getIndex(self.data_list,key)
        self.data_list[idx][1] = value

    def list_all(self):
        return [kv for kv in self.data_list if kv is not None]

basic_Table = HashTable(1024)   
basic_Table.insert('sujit','smart')
basic_Table.insert('salunkhe','lion')
basic_Table.insert('kohli','night')
basic_Table.update('sujit','braine')
a=basic_Table.list_all()
print(a) 
# print(len(basic_Table.data_list) == 1024)
# dic = {'sujit':'smart','king':'sujit','lion':'lionking'}
# print(dic['lion'])

# class PobingHashTable:
#     def __init__(self):
#         self.data_list =

#     def
