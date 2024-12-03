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
    # append information to each string
    output += '<li class="cards__item">\n'
    name = animal['name']
    output += f"name: {name}<br/>\n"
    diet = animal['characteristics']['diet']
    output += f"diet: {diet}<br/>\n"
    location = animal['locations'][0]
    output += f"location: {location}<br/>\n"
    try:
        animal_type = animal['characteristics']['type']
    except KeyError:
        output += f"<br/>\n"
    else:
        output += f"type: {animal_type}<br/>\n"
    output += '</li>\n'
print(output)

new_html_template = template_html.replace('__REPLACE_ANIMALS_INFO__', output)
#print(new_html_template)

def write_new_html(file_path):
  """ Write a html file """
  with open(file_path, "w") as new_html:
      new_html.write(new_html_template)

write_new_html('animals.html')