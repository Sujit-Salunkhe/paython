# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x =thisdict["model"]
# print(x)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys() 
# print(x)
# thisdict["color"]= "white"
# print(x)
# y = thisdict.values()
# thisdict["whells"]="alloy"
# print(y)
# z =thisdict.items()
# print(z)
# cars["mirrors"]="bold"
# cars.update({"youtube":"tecno"})
# cars={"name":"mustange","wheels":"alloy","screen":"dark"}
# cars.pop("screen")
# print(cars)
# cars={"name":"mustange","wheels":"alloy","screen":"dark"}
# cars.popitem()
# print(cars)
# cars={"name":"mustange","wheels":"alloy","screen":"dark"}
# del cars["name"]
# # print(cars)
# for x,y in cars.items():
#     print(x,y)
# x = cars.values()
# print(x)
# cars
# cars={"name":"mustange","wheels":"alloy","screen":"dark"}
# cars["reverse"]="camera"
# cars.update({"remote":"tv"})
# print(cars)
# cars={"name":"mustange","wheels":"alloy","screen":"dark"}
# cars2=cars.copy()
# print(cars2)
# my_family={"chiled1":{
#     "name":"sujit",
#     "height":"139"
#     },"chiled2":{
#         "name":"zandu",
#         "height":"567"
#     },"chiled3":{
#         "name":"pagel",
#         "height":"675"
#     }
#     }
# x = my_family.values()
# print(x)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
my_family= {
    "child1":child1,
    "child2":child2,
    "child3":child3

}
x = ('key1', 'key2', 'key3')
y = 0
dictionary=dict.fromkeys(x,y)
print(dictionary)