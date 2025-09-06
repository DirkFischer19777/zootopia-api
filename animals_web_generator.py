

import data_fetcher





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

def user_input():
    """Asks the user to input animal to request"""
    animal_request = input("please enter animal you like to get information from: ")
    return animal_request


def main():
    # Ask User for animal
    animal_name = user_input()

    # Request API Data
    animals = data_fetcher.fetch_data(animal_name)

    # HTML-Template einlesen
    html_input = read_html()

    # check if animal does exist
    if not animals:
        # if animal does not exist
        html_output = html_input.replace(
            "__REPLACE_ANIMALS_INFO__",
            f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
        )
        print(f"The animal {animal_name} doesn´t exist")
    else:
        # if animal does exist
        output_string = print_animals(animals)
        html_output = replace_placeholder(output_string, html_input)

    # Store HTML
    save_data(html_output)

    # Message to user
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
