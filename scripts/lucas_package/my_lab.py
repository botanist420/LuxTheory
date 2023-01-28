import json



# example dictionary
lucas_dict = {
    "english words": ["compose", "Lucas"],
    "command lines": ["head", "less", "ifconfig"]    
}

def write_json(dict_obj, file_name):
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(dict_obj, file, indent=4)
    


def read_json(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    
    print(data)


if __name__ == "__main__":
    write_json(lucas_dict, "lucas_dict.json")
    