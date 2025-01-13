info={
    "name":"Arnab",
    "Subjects": { #nested dictionary
        "phy":"98",
        "chem": "99",
        "bio" : "95"
    },
    "topic":{
        "c":"1st",
        "c++": "2nd",
        "java": "3rd"
    }
}
print(info)
print(info["Subjects"])
print(info["Subjects"]["chem"])
print(info["topic"])
print(info["topic"]["java"])