import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
    #print(animal)
    name = animal['name']
    #print(name)
    diet = animal['characteristics']['diet']
    #print(diet)
    location = animal['locations'][0]
    #print(location)
    print(f"name: {name}\n"
          f"diet: {diet}\n"
          f"location: {location}"
          )
    try:
        animal_type = animal['characteristics']['type']
    except KeyError:
        print()
    else:
        print(f"type: {animal_type}\n")