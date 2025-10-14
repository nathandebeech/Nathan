# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

for dictionary in targets:
    print(dictionary)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.

for dictionary in targets:
    print(targets[dictionary]["Spectral Type"])

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

for dictionary in targets:
    if targets[dictionary]["Magnitude"] > 0.1:
        print(dictionary)

# 4) Look up another target, add all the necessary information to the targets list. 

Arcturus = {
    "RA": "14h 15m 40s",
    "Dec": "+19° 10′ 57",
    "Magnitude": -0.04,
    "Spectral Type": "K1.5IIIFe-0.5"
}
targets["Arcturus"] = Arcturus
print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# create arbitrary range and maybe play around with changing the range
# We can say 10 degrees to 30 degrees, and then change that to 15 to 25 etc.
# Super vague question and I was told that any interpretation of the problem is fine.
declinations = []
for star in targets:
    declinations.append(targets[star]["Dec"][0:4])

declinations_degree_value = []
for declination in declinations:
    if declination[0] == "+":
        declinations_degree_value.append(declination[1:3])


dec_between_fifteen_twentyfive = []
for i in range(len(declinations_degree_value)):
    declinations_degree_value[i] = int(declinations_degree_value[i])
    if declinations_degree_value[i] >= 15 and declinations_degree_value[i] <= 25:
        dec_between_fifteen_twentyfive.append(declinations_degree_value[i])

for dec in dec_between_fifteen_twentyfive:
    if dec == 19:
        print("Arcturus")
    elif dec == 89:
        print("Polaris")
    elif dec == 7:
        print("Betelgeuse")
    elif dec == 38:
        print("Vega")


# 6) What is your favorite constellation?
print("Cassiopeia!")