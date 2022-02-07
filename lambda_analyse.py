import json

def lambda_handler(event, context):
    
    # TODO implement
    # data = event["TableName"]
    facedetails = event["FaceDetails"]
    total = len(facedetails)
    looking = 0
    
    for face in facedetails:
        ryp = face["Pose"]
        roll = ryp["Roll"]
        yaw = ryp["Yaw"]
        pitch = ryp["Pitch"]
        if -20 < yaw < 20 and 5 < pitch < 20:
            looking = looking + 1
    
    fraction = looking / total
    
# Roll doesn't matter
# Yaw makes sure face doesn't tilt too far off to the side
# Pitch has lower limit to make sure person isn't looking at their phones (less likely to look upwards so upper limit is quite high)


    return {
        'statusCode': 200,
        'body': total
    }
