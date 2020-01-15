# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)  # inherit from LatLon
        self.name = name            # add to this class
    def __str__(self):
        return self.name + self.lat + self.lon

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, lat, lon, difficulty, size):
        super().__init__(lat, lon, name) # inherit from waypoint
        self.difficulty = difficulty # add to this class
        self.size = size             # add to this class
    def __str__(self):
        return (f'Name: {self.name} | Lat: {self.lat} | Lon: {self.lon} | ' +
                f'Size: {self.size} | Difficulty: {self.difficulty} ') 
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint_1 = Waypoint('Catacombs', 41.70505, -121.51521)
print('waypoint_1 = ', waypoint_1.name, waypoint_1.lat, waypoint_1.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache_1 = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print('geocache_1 = ', geocache_1.name, geocache_1.difficulty, geocache_1.size, geocache_1.lat, geocache_1.lon)

# Print it--also make this print more nicely
# print(geocache)
