import json

with open('sample2.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
    #print(data["Labels"]) # gets face pose
    print(data["Persons"][0]) # gets face pose
    #print(data["Labels"]) # gets face pose

