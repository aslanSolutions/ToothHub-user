from mongoengine import connect

# Update the connection URL with your actual database details
connection_url = 'mongodb+srv://dbUser:root123@aslan.im1wsjq.mongodb.net/patient'

# Establish the connection
connect(host=connection_url)
