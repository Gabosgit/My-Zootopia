""" Generate an html file handling data from a json file """
import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
animals_data = load_data('animals_data.json')


def load_html_template(file_path):
  """ Loads the html template file """
  with open(file_path, "r") as html_file:
      text_data = html_file.read()
      return text_data
template_html = load_html_template('animals_template.html')


def get_list_animal_skin_type():
    """ Puts unique skin types in a set """
    set_skin_types = set()
    for animal in animals_data:
        skin_type = animal['characteristics']['skin_type']
        set_skin_types.add(skin_type)
    return set_skin_types


def print_skin_type_list(skin_types):
    """ Prints the list of unique skin types """
    print("LIST OF ANIMAL SKIN TYPES")
    for skin_type in skin_types:
        print(f" - {skin_type}")


def serialize_animal(animal):
    """handle a single animal serialization"""
    name = animal['name']
    skin_type = animal['characteristics']['skin_type']
    diet = animal['characteristics']['diet']
    location = animal['locations'][0]
    try: # Excepts if the animal type doesn't exist
        animal['characteristics']['type']
    except KeyError:
        animal_type = f""
    else:
        animal_type = f'\t\t\t\t\t\t<li class="info_line"><strong>Type:</strong> {animal["characteristics"]["type"]}</li>\n'
    output_line = ''  # define an empty string
    # append information to each string
    output_line += '\n'
    output_line += '\t\t\t<li class="cards__item">\n'
    output_line += f'\t\t\t\t<div class="card__title">{name}</div>\n'
    output_line += f'\t\t\t\t<p class="card__text">\n'
    output_line += f'\t\t\t\t\t<ul class="info_list">\n'
    output_line += f'\t\t\t\t\t\t<li class="info_line"><strong>Skin Type:</strong> {skin_type}</li>\n'
    output_line += f'\t\t\t\t\t\t<li class="info_line"><strong>Diet:</strong> {diet}</li>\n'
    output_line += f'\t\t\t\t\t\t<li class="info_line"><strong>Location:</strong> {location}</li>\n'
    output_line += f'{animal_type}'
    output_line += f'\t\t\t\t\t</ul>\n'
    output_line += '\t\t\t\t</p>\n'
    output_line += '\t\t\t</li>\n'
    return output_line


def get_selected_animals_by_skin(skin_type):
    """ Returns only the data of the selected animal by skin as html """
    output = ''
    for animal in animals_data:
        if skin_type.title() in animal['characteristics']['skin_type']:
            output += serialize_animal(animal)
    return output


def write_new_html(file_path, html_data):
    """ Write a html file replacing a html string with html serialized data """
    new_html_template = template_html.replace('__REPLACE_ANIMALS_INFO__', html_data)
    with open(file_path, "w") as new_html:
        new_html.write(new_html_template)


def valid_input_user(skin_types):
    """ Ensures that the input is only one type of skin in a given list """
    while True:
        user_input = input("\nPlease enter a skin type from the list: ")
        try:
            if user_input.title() not in skin_types:
                raise Exception(f"'{user_input}', is not in the list")
        except Exception as error:
            print(error)
        else:
            return user_input


def main():
    """ Some functions get the return of another function as an argument """
    skin_type_set = get_list_animal_skin_type()
    print_skin_type_list(skin_type_set)
    user_choice = valid_input_user(skin_type_set)
    output = get_selected_animals_by_skin(user_choice)
    write_new_html('animals.html', output)


if __name__ == '__main__':
    main()