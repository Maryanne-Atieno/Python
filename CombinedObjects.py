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
print(Towns.keys()) #show all keys in List