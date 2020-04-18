# Step 1 ~ 3 in shell with git
# Step 4
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
# Step 5
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
# Step 6 ~ 7 in shell with git
# Step 8
def get_destination_index(destination):
# Step 9
  destination_index = destinations.index(destination)
# Step 10
  return destination_index
# Step 11, 12
print(get_destination_index("Los Angeles, USA"))
# Step 13, 14
# print(get_destination_index("Hyderabad, India"))
# Step 15
def get_traveler_location(traveler):
# Step 16
  traveler_destination = test_traveler[1]
# Step 17
  traveler_destination_index = get_destination_index(traveler_destination)
# Step 18
  return traveler_destination_index
  
print(get_traveler_location('Erin Wilkes'))