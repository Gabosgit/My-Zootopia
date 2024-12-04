import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


def load_html_template(file_path):
  """ Loads a html file """
  with open(file_path, "r") as template_html:
      text_data = template_html.read()
      return text_data

template_html = load_html_template('animals_template.html')
#print(template_html)

output = ''  # define an empty string

for animal in animals_data:
    name = animal['name']
    diet = animal['characteristics']['diet']
    location = animal['locations'][0]
    try:
        animal['characteristics']['type']
    except KeyError:
        animal_type = f""
    else:
        animal_type = f'\t\t\t\t\t<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    # append information to each string
    output += '\n'
    output += '\t\t\t<li class="cards__item">\n'
    output += f'\t\t\t\t<div class="card__title">{name}</div>\n'
    output += f'\t\t\t\t<p class="card__text">\n'
    output += f'\t\t\t\t\t<strong>Diet:</strong> {diet}<br/>\n'
    output += f'\t\t\t\t\t<strong>Location:</strong> {location}<br/>\n'
    output += f'{animal_type}'
    output += '\t\t\t\t</p>\n'
    output += '\t\t\t</li>\n'

print(output)

new_html_template = template_html.replace('__REPLACE_ANIMALS_INFO__', output)
#print(new_html_template)

def write_new_html(file_path):
  """ Write a html file """
  with open(file_path, "w") as new_html:
      new_html.write(new_html_template)

write_new_html('animals.html')