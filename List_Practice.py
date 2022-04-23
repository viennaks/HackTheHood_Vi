City_Name=["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

Social_Media_Name=["Facebook","Instagram","TikTok","Snapchat","Twitter","Pinterest","LinkedIn","Youtube","Reddit","Whatsapp"]
print(Social_Media_Name)

print(City_Name[0])
print(City_Name[2])
print(City_Name[7])

four_cities = City_Name[0:4]
print(four_cities)

social_media = Social_Media_Name[1:5]
print(social_media)

City_Name[0]= "San Francisco"
City_Name[2]= "Brooklyn"
City_Name[7]= "Hollywood"
City_Name[5]= "Tampa"
print(City_Name)

City_Name.append("Oakland")
City_Name.extend(["New York City", "Los Angeles"])
City_Name.insert(5, "Miami")
print(City_Name)

del City_Name[4]
City_Name.pop(8)
City_Name.remove("New Orleans")
print(City_Name)