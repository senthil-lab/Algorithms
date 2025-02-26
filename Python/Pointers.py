i = 11
j = i

print("value of i is", i)
print("value of j is", j)

print ("address of i is", id(i))
print ("address of j is", id(j))

j = 22

print("value of i is", i)
print("value of j is", j)

print ("address of j is", id(j))

i = { "data" : 11 }
j = i

print("value of i is", i)
print("value of j is", j)

print ("address of i is", id(i))
print ("address of j is", id(j))

j["data"] = 22

print("value of i is", i)
print("value of j is", j)

print ("address of i is", id(i))
print ("address of j is", id(j))

