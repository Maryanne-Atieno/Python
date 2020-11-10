#Combined objects
Towns = {
  "Ongata Rongai": "Nkoroi",
  "Nairobi": ["Roysambu", "Westlands", "Muthaiga","Ngara"],
  "Mombasa":["Lamu", "Malindi","Nyali"]
}
print("Combined Objects")
print(Towns["Nairobi"])
print(Towns["Mombasa"][0])
print(Towns["Ongata Rongai"] + "\n\n")

#To print multiple types, you need to use print
print("Object Data Types")
print (type(Towns["Nairobi"]))
print (type(Towns["Mombasa"][2]))
print(type(Towns))
print(Towns.keys(), "\n\n") #show all keys in List

#Using len()
print("Check length")
print("There are ", len(Towns), " items in this dictionary.") #Length of dictionary
print("There are",len(Towns["Nairobi"]), "items in object Nairobi.")#length of object in dictionary
print("An item in object Mombasa is", len(Towns["Mombasa"][1])," characters long.")                        