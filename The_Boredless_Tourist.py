# git init  # Step 1
# git add script.py  # Step 2
# git commit -m "initial commit"  # Step 3

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]  # Step 4
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]  # Step 5

# git add script.py  # Step 6
# git commit -m "Added test objects"  # Step 7

def get_destination_index(destination):  # Step 8
  destination_index = destinations.index(destination)  # Step 9                      
  return destination_index  # Step 10
# print(get_destination_index("Los Angeles, USA"))  # Step 11, 12
# print(get_destination_index("Hyderabad, India"))  # Step 13, 14

def get_traveler_location(traveler):  # Step 15
  traveler_destination = test_traveler[1]  # Step 16
  traveler_destination_index = get_destination_index(traveler_destination)  # Step 17
  return traveler_destination_index  # Step 18

# test_destination_index = get_traveler_location(test_traveler)  # Step 19
# print(test_destination_index)  # Step 20 ~ 21

# git add script.py  # Step 22
# git commit -m "Added logic to find traveler destinations and convert to internal data"  # Step 23

attractions = [[] for destination in destinations]  # Step 24 ~ 25
# print(attractions)  # Step 26

def add_attraction(destination, attraction):  # Step 27
  try:  # Step 29
    destination_index = get_destination_index(destination)  # Step 28
    attractions_for_destination = attractions[destination_index].append(attraction)  # Step 31
  except SyntaxError:
    return  # Step 30
  
add_attraction('Los Angeles, USA', ['Venice Beach',['beach']])  # Step 33
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])  # Step 35
print(attractions)  # Step 34

# git add script.py  # Step 36
# git commit -m "Created attractions and functionality for adding new attractions"  # Step 37

def find_attractions(destination, interests):  # Step 38
  destination_index = get_destination_index(destination)  # Step 39
  attractions_in_city = attractions[destination_index]  # Step 40
  attractions_with_interest = []  # Step 41
  for attraction in attractions_in_city:  # Step 42
    possible_attraction = attraction  
    attraction_tags = attraction[1]  # Step 43
    for interest in interests:  # Step 44
      if interest in attraction_tags: # Step 45
        attractions_with_interest.append(possible_attraction[0]) # Step 49
  return attractions_with_interest  # Step 46
  
la_art = find_attractions("Los Angeles, USA", ['art']) # Step 47
print(la_art) # Step 48, Step 50

# git add script.py  # Step 51
# git commit -m "Added interest finder logic"  # Step 52

def get_attractions_for_traveler(traveler):  # Step 53
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]  # Step 54
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)  # Step 55
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination  # Step 56, Step 57, Step 58
  for i in range(len(traveler_attractions)):  # Step 59
    if traveler_attractions[-1] == traveler_attractions[i]: 
      interests_string += "the " + traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string  # Step 60

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])  # Step 61
print(smills_france)  # Step 62
# git add script.py  # Step 63
# git commit -m "Added function to generate message for traveler and present attractions they might be interested in."  # Step 64