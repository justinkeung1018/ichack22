import json

with open('sample2.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
    print(data["FaceDetails"][0].get('Pose')) # gets face pose
