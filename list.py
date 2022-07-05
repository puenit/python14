fruits = ["apple","banana","cherry"]
print(fruits[1])

fruits[1] ="blackcurrant"
print(fruits[1])

fruits[1:3]= ["mango","kiwi","pineapple"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.insert(1,"orange")
print(fruits)

tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)

fruits.remove("apple")
fruits.pop(1)
#del fruits

fruits.sort(reverse=True)
print(fruits)

#เจษฎา ทรัพย์วิบูลพงษ์ มใ6/14 เลขที่ 7