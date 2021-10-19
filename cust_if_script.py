#!/usr/bin/env python3
""" Test script for if else """
 
seasons= ["summer", "autumn", "winter", "spring"]
cities= ["cayman islands", "london", "switzerland", "germany"]

#def main():
#        print(seasons)
#        print(cities)
#        print("This is a today's season: " + seasons[1] + ", and next will be " + seasons[2])

countme= 0 
while True:
      countme = countme + 1
      print('Let me know which season it is, "Today season is ______"')
      answer= input("Your answer is ")
      if answer == 'autumn':
          print("you are correct")
          print("Best to travel to " + cities[1])
          break
      elif countme==3:
          print("need to choose the given season")
          break
else:
      print("sorry, try again!")

#main()    

