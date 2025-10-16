import json

print("Les 7 - Collections en JSON")

# Database en album-collectie

albums = {
    "MarvinGaye1971": {"artist": "Marvin Gaye", "album": "What’s Going On", "year": 1971},
    "BeachBoys1966": {"artist": "The Beach Boys", "album": "Pet Sounds", "year": 1966},
    "JoniMitchell1971": {"artist": "Joni Mitchell", "album": "Blue", "year": 1971},
    "StevieWonder1976": {"artist": "Stevie Wonder", "album": "Songs in the Key of Life", "year": 1976},
    "Beatles1969": {"artist": "The Beatles", "album": "Abbey Road", "year": 1969},
    "Nirvana1991": {"artist": "Nirvana", "album": "Nevermind", "year": 1991},
    "FleetwoodMac1977": {"artist": "Fleetwood Mac", "album": "Rumours", "year": 1977},
    "Prince1984": {"artist": "Prince and the Revolution", "album": "Purple Rain", "year": 1984},
    "BobDylan1975": {"artist": "Bob Dylan", "album": "Blood on the Tracks", "year": 1975},
    "LaurynHill1998": {"artist": "Lauryn Hill", "album": "The Miseducation of Lauryn Hill", "year": 1998},
    "Beatles1966": {"artist": "The Beatles", "album": "Revolver", "year": 1966}
    }

my_collection = { "MarvinGaye1971", "LaurynHill1998", "Beatles1966", "Beatles1969" }

# Oefeningen

# Hoe kan ik nu het beste een album uit de database aan mijn collectie toevoegen?
    # Schrijf een functie die een album toevoegt

def add_album(tag):
    my_collection.add(tag)

add_album("BobDylan1975")
add_album("Nirvana1991")
print(my_collection)

# Wat is het verschil tussen myBands1 en myBands2? Welke is in dit geval 'beter'?

def my_bands1():
    return [ albums[tag]["artist"] for tag in my_collection ]

def my_bands2():
    return { albums[tag]["artist"] for tag in my_collection }

my_bands = my_bands2 # Zoveel beter OMG!

# Lijst comprehensies

# lijst = []
# for x in a:
#     lijst.append(float(x))
#
# lijst = [float(x) for x in a]


# Maak een functie die true geeft als ik een album uit een gegeven jaar bezit

def bezit_album_jaar(jaar):
    for tag in my_collection:
        if jaar == albums[tag]["year"]:
            return True
    return False

print(bezit_album_jaar(1991)) # True
print(bezit_album_jaar(2032)) # False

# Print de namen van mijn albums, gesorteerd op jaar

def mijn_albums():
    albs = []
    for tag in my_collection:
        albs.append( (albums[tag]["year"], albums[tag]["album"]) )
    for album in sorted(albs):
        print(album[1])

mijn_albums()

# Exporeer een CSV met de gegevens van alle albums in mijn collectie

def export_collection_csv():
    with open("export.csv", "w", newline='') as csvfile:
        for tag in my_collection:
            album = albums[tag]
            row = f"{album["album"]},{album["artist"]},{album["year"]}\n"
            csvfile.write(row)

export_collection_csv()
    
# Exporeer een JSON file met de gegevens van alle albums in mijn collectie
def dump_json():
    with open('albums.json', 'w') as json_file:
        json.dump(albums, json_file)

dump_json()

# Importeer een JSON file om de albumlijst uit te breiden

def load_json(filename):
    pass
