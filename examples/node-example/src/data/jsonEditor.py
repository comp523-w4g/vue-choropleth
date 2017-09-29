import json

with open("ncgeo.json", "r") as jsonFile:
	    data = json.load(jsonFile)

	    for index, county in enumerate(data["features"]):
		    county["properties"]["county_id"] = index
		    print county["properties"]
	    with open("ncgeo.json", "w") as jsonFile:
		        json.dump(data, jsonFile)
