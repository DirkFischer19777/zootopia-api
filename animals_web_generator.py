import json


def load_data():
    """ Loads a JSON file """
    with open("animals_data.json", "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">'
    # Name
    if "name" in animal_obj:
        output += f"<div class='card__title'> Name: {animal_obj['name']}</div><br/>\n"

    # Diet
    diet = animal_obj.get("characteristics", {}).get("diet")
    if diet:
        output += f"<p class='card__text'> <strong> Diet: </strong> {diet}<br/>\n"

    # Location (first in list)
    locations = animal_obj.get("locations")
    if locations and len(locations) > 0:
        output += f"<strong> Location:</strong> {locations[0]}<br/>\n"

    # Type
    type_ = animal_obj.get("characteristics", {}).get("type")
    if type_:
        output += f"<strong> Type: </strong> {type_}<br/>\n"

    output += '</p> </li>\n'
    return output


def print_animals(data):
    """Iterates through animals and prints selected info"""
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output


def read_html():
    # HTML-Datei einlesen
    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content


def replace_placeholder(data, html_input):
    # replace placeholder with animal info
    return html_input.replace("__REPLACE_ANIMALS_INFO__", data)


def save_data(data):
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(data)


def main():
    animals = load_data()
    output_string = print_animals(animals)
    html_input = read_html()
    html_output = replace_placeholder(output_string, html_input)
    save_data(html_output)


if __name__ == "__main__":
    main()
