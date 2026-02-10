m={} # empty dictionary
marks = {    # Dictionaries are store {keys : values} are mutable(allow change), no duplicate keys , and indexed(already indexed with values)
    "Aryan" : 100 , 
    "Harry" : 99,
    "Rahul" : 93,
    "Mohit" : 23,
     0: "Harry" 
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks ,type(marks) )
# marks.update({"Aryan" : 95 ,"shivika" : 89})
# print(marks)
# print(marks["Aryan"])  # this and below function are work as same but the differnce is it use[] and below function use ()
# print(marks.get("Aryan1"))
# print(marks["Aryan1"])  # it returns error
# print(marks.get("Aryan1"))  # and it returns none
print(marks.pop("Aryan"))
print(marks)

