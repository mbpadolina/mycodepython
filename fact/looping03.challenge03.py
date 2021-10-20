#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#for zonep in farms:
#    print(zonep)
#    print(farms, end="")
print ( farms.keys() )
print ( farms.values() )
if farms == "NE Farm":
    print (farms.get["name"])
    print (farms.get["agriculture"])
