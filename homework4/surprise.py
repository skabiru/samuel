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
def print_stars(targets):
    for i in targets:
        print(i)
print(print_stars(targets))
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def star_and_spectral(targets):
    for i in targets:
        spectral = targets[i]["Spectral Type"]
        print(i, "-", spectral)
print(star_and_spectral(targets))
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_mag(targets):
    for i in targets:
        mag = targets[i]["Magnitude"]
        if mag > 0.1:
            print(i, "-", mag)
print(stars_mag(targets))
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Acrux"] = {"RA": "12h 26m 35.9s","Dec": "−63° 05′ 56″","Magnitude": 0.77,"Spectral Type": "B0.5IV"}
print(targets)
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def closest_star(targets):
    closest = None
    smallest = 1000
    for i in targets:
        dec = targets[i]["Dec"]
        dec = dec.replace("−","-")   # fix the minus sign
        dec_value = float(dec[:3])
        difference = abs(dec_value - 20)
        if difference < smallest:
            smallest = difference
            closest = i
    print("Closest star:", closest)
print(closest_star(targets))
# 6) What is your favorite constellation?
print("Ursa Major")