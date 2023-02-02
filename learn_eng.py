import json
import os


def read_json(file_name: str="lucas_dictionary.json"):
    
    dictionary_stored_place = "lucas_note/"    # Where dictionary directory
    relative_path = dictionary_stored_place + file_name
    
    assert file_name in os.listdir(dictionary_stored_place)
    with open(relative_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    print(data)


if __name__ == "__main__":
    read_json()

