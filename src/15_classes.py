# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        print("Parent Class has received coordinates")
    def __str__(self):
        rep = "Latlon object"
        rep += "Name: " + self.name
        return rep
    def talk(self):
        print("Hi, here's my name: ", self.name)

# YOUR CODE HERE
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
    super().__init__(lat, lon)
    print("Waypoint child class has received coordinates", name, " at ", "lat", lat, ", and lon ", lon)
    

# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(LatLon):
    def __init__(self, name, difficulty, size, lat, lon):
        self.name = name
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon
        super().__init__(lat, lon)
        print("Geocache child class has received coordinates", name, " at ", "lat", lat, ", and lon ", lon, " difficulty is rank ", difficulty, " and size is ", size)
    def talk(self):
        print("Geocache has ", self.name, "as the cache")
        

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

#waypoint = ("Catacombs", 41.70505, -121.51521)
Waypoint("Catacombs", 41.70505, -121.51521)

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# YOUR CODE HERE

# Print it--also make this print more nicely

print(Geocache.talk())
speak = Waypoint("Cata", 41.70505, -121.51521)
speak.talk()
