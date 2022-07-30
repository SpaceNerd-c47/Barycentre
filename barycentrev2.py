# Programe for determining the Barycentre for chosen planet and Sun by planet name 
# get name of planet
a_input=input("name of planet: ")
# find values of "a" and "m2" for searched planet
planet_finder = {
    "Mercury":{"a":71.409*(10**6),"m2":0.3301*(10**24)},
    "Venus":{"a":108.2105*(10**6),"m2":4.8673*(10**24)},
    "Earth":{"a":149.5975*(10**6),"m2":5.9722*(10**24)},
    "Mars":{"a":227.9555*(10**6),"m2":0.64169*(10**24)},
    "Jupiter":{"a":778.479*(10**6),"m2":1898.13*(10**24)},
    "Saturn":{"a":1432.0405*(10**6),"m2":568.32*(10**24)},
    "Uranus":{"a":2867.043*(10**6),"m2":86.811*(10**24)},
    "Neptune":{"a":4514.9535*(10**6),"m2":102.409*(10**24)}
    }
# isolate "a" and "m2" values for selected planet
x = planet_finder[a_input]["a"]
y = planet_finder[a_input]["m2"]
# "m1" is a known value
z = 1988500*(10**24)
# use values of searched planet for calculation
# run calculation for r1
r1 = x/(1+(z/y))
# print value of r1
print(f"distance from the center of the Sun to barycentre between the Sun and {a_input}: {r1} km")