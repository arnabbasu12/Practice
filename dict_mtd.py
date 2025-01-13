info={
    "name":"Arnab",
    "Subjects": { #nested dictionary
        "phy":"98",
        "chem": "99",
        "bio" : "95"
    }
}
print(info.keys()) #return all keys
print(list(info.keys())) # can be type casting
print(info.values()) #return all values
print(info.items()) #all (key:val) pairs as tuples
print(info.get("name"))
info.update({"city" : "Khulna"})
print(info)
#can be also update:
print("alternative method")
new_info={"city" : "Khulna"}
info.update(new_info)
print(info)