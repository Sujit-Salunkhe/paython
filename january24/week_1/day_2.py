phone_numbers ={
    'sujit':'4548978963',
    'Ganpat':'4548978962',
    'pandu':'4248978963'
}

class HashTable:
    def insert(self,key,value):
        pass
    def find(self,key):
        pass
    def update(self,key,value):
        pass
    def list_all(self):
        pass


MAX_HASH_TABLE_SIZE = 4096
data_list =[None] * 4096
# data_list[4000] ='sujit'
# print(data_list)
for item in data_list:
    assert item == None

print(ord('i'))

def get_index(data_list,a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
    list_index = result % len(data_list)
    return list_index


data_list[get_index(data_list,'sujit')] = ('sujit',4548978963)
