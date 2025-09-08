import csv
import datetime
import json
import pathlib


from decoding_functions import *

date = datetime.date(2009, 8, 13)

decoded_things = {}
commands_used = {}


def get_dict_files(path_name: pathlib.Path = pathlib.Path("Files")) -> dict:
    all_paths = path_name.rglob("**/*")
    directories_dict = {}

    for path in all_paths:
        if path.is_file():
            folder = path.parent.relative_to(path_name)  # check almost like `in`, relative to in sub-paths
            directories_dict.setdefault(str(folder), []).append(path)

    return directories_dict


def list_files(path="files") -> str:
    if path.casefold() == "files":
        dict_items = get_player_files()
    elif path == "interrogates":
        dict_items = get_dict_files(pathlib.Path("Admin_files/speeches"))
    else:
        dict_items = get_dict_files(pathlib.Path(path))

    indexes = 1
    for folder, files in dict_items.items():
        print(f"\n\U0001F4C1 {folder}\\")   #\U0001F4C1 is the Unicode for folder

        for file in sorted(files):
            print(f"{indexes}: {file.name}")
            indexes += 1
    return "\n"


directory = get_dict_files()
admin_files = get_dict_files(pathlib.Path("Admin_files"))


def get_file(file_name, lists=None):
    if lists is None:
        lists = directory
    file_to_read = f"{pathlib.Path(file_name).name} does not exists"
    for folder, files in lists.items():
        for file in files:
            if file_name == folder:
                file_to_read = "Please choose a file not a folder. "
            if pathlib.Path(file).match(file_name.lower()):
                # match function checks for any matches b/w them.
                file_to_read = file
                break
            if file.stem == file_name.lower():
                file_to_read = file
                break

    return file_to_read



def load_game():
    list_load_files = get_dict_files(pathlib.Path("Admin_files/save_data"))

    list_files("Admin_files/save_data")

    print()
    print("Enter the name of the saved data to load: ")
    print("Type 'New' to create a new game")
    file_input = input(">> ").strip().casefold()

    if "new" in file_input:
        load_data = pathlib.Path("Admin_files/main_game_save.json")
    else:
        load_data = get_file(file_input, list_load_files)

    try:
        with open(load_data, 'r', encoding='utf-8') as input_file:
            loaded_data = json.load(input_file)
            current_save_dict = {}
            for words, values in loaded_data.items():
                if isinstance(values, list):
                    values = set(values)
                current_save_dict[words] = values
            print(f"Data is loaded")
            return current_save_dict
    except FileNotFoundError:
        print("The File is not Found")
        return None
    except OSError:
        print("Save data couldn't be loaded")
        return None


save_dict = load_game()
current_stage = save_dict.get("current_stage")

# save_dict = {
#     "files_read": {
#         "Files/crime_details.txt",
#         "Files/door_logs.csv",
#         "Files/timeline.txt",
#         "Files/suspects.json",
#         "diary/entry1.txt",
#         "diary/entry2.txt",
#         "therapist_notes/eleanor_session3.txt",
#         "emails/clue1_email.txt",
#         "emails/clue2_email.bin"
#     },
#     "suspects_asked": {
#         "Eleanor Riggs",
#         "Dr. Marcus Beck",
#         "John Ellory"
#     },
#     "decoded_clues": {
#         "clue1_email.txt": {
#             "type": "language",
#             "original_language": "Japanese",
#             "translation": "The truth hides in plain sight under the floorboard."
#         },
#         "clue2_email.bin": {
#             "type": "binary",
#             "decoded_text": "Check the basement logs."
#         },
#         "door_logs.csv": {
#             "type": "csv_pattern",
#             "suspicious_entry": "03:12 - Unknown ID - Basement Access"
#         }
#     },
#     "current_stage": 1,
#     "timestamp": "2025-06-27T18:45:00"
# }



encrypted_password = {"photo.bmp": "hughjackman", "maid2_phone_dump.txt": "12345678",
                      "Admin_files": "admin_123", "Files": "files_123"}





def get_player_files():
    player_files = get_dict_files(pathlib.Path("Player"))
    return player_files



def interrogate_suspect(name):
    interrogation = read_file(name, admin_files)
    save_dict.get("suspects_asked").add(name)
    return interrogation




def save_game(name_path=None):
    save_data = pathlib.Path("Admin_files/save_data")

    if name_path is None:
        file_save_index = 1
        while True:
            temp_data = save_data.joinpath("Untitled-" + str(file_save_index) + ".json")
            if temp_data.exists():
                file_save_index += 1
            else:
                save_data = temp_data
                break


    else:
        name_path = pathlib.Path(name_path)
        if name_path.suffix:
            save_data.joinpath(name_path)
        else:
            name_path = str(name_path)
            save_data = save_data.joinpath(name_path + ".json")

    try:
        with open(save_data, 'w', encoding='utf-8') as input_file:
            current_save_dict = {}
            for words, values in save_dict.items():
                if isinstance(values, set):
                    values = list(values)
                current_save_dict[words] = values

            json.dump(current_save_dict, input_file, indent=2)

    except OSError:
        print("Save data couldn't be finished")



def accuse(character):
    if character == 'howard':
        print("Congratulations: You have won the game")
        return True
    return False


def load_files(*files):
    errors = []
    list_of_files = []
    for file in files:
        try:
            list_of_files.append(get_file(file))
        except FileNotFoundError:
            errors.append(errors)
    if not errors:
        return list_of_files
    else:
        return errors


def read_file(file, files=None):
    player_files = get_player_files()
    if files is None:
        files = player_files
    name_path = pathlib.Path(get_file(file, files))
    if not name_path.is_file():
        return "File does not exist"

    try:
        name_path = file_type_returner(name_path)
        with open(name_path, encoding='utf-8', newline='') as input_file:
            data = input_file.read()
            if name_path.suffix == ".csv":
                new_value = read_csv(data)
                data = new_value
        save_dict.get("files_read").add(name_path.name)
        return data
    except OSError:
        return f"Input <folder/file> else <file>"



def file_type_returner(name_path):
    if name_path.name in encrypted_password:
        encryption = protected_file(name_path.name)
        if not encryption:
            return f"Retry Later"
        else:
            return name_path
    if name_path.suffix == ".bmp":
        save_dict.get("files_read").add(name_path.name)
        print_image()
        return None
    if name_path.suffix == ".raw":
        new_path = pathlib.Path(r"Admin_files\evidence\voice_fragment\voice_fragment.txt")
        return new_path
        # should not pass a string as a path
    return name_path


def list_commands() -> dict:
    commands_dict = {
        "read": read_file,
        "list": list_files,
        "interrogate": interrogate_suspect,
        "decode": decode_clue,
        "add-suspects": add_suspect,
        "accuse": accuse,
        "history-commands": history_command,
        "save": save_game,
        "help": help_command,
    }

    print("Commands you can use: ")
    for number, (commands, functions) in enumerate(commands_dict.items()):
        print(f"{number + 1}: {commands}")
    return commands_dict
    # Return both dict and printed list only if needed — you might separate UI from logic later.
    # Add descriptions in future (e.g., "read": "Read a file") for help menu.


def read_csv(data):
    new_data = data.strip().split("\n")
    sample_line = new_data[0]
    try:
        new_dialect = csv.Sniffer().sniff(sample_line)
        delimiters = new_dialect.delimiter
    except csv.Error:
        return "Error when sniffing lines"
    finalized_data = ""
    for line in new_data:
        word = line.split(delimiters)
        finalized_data += f" ".join(word) + "\n"
    return finalized_data


def help_command():
    return """
Available commands:
- read <filename>
- list [files/interrogates]
- decode <file> <morse/binary/language/base64/hex> 
- interrogate <suspect_name>
- add-suspects <suspect_name>
- accuse <suspect_name>
- help - Show this message
"""


def protected_file(file):
    times = 3
    print(f"You have {times} tries")
    while True:
        input_password = input("Enter password: ").strip().lower()
        # input_password = getpass.getpass().strip().lower() # may use later
        password = encrypted_password[file]
        if input_password == password:
            return True
        if file == "photo.bmp" and times == 2:
            print("Clue: Your favorite actor")
        else:
            print("The entered password is incorrect")
            print()
        times -= 1
        if times == 0:
            break
        elif times == 1:
            print(f"You still have remaining {times} attempt")
        else:
            print(f"You still have remaining {times} attempts")
    return False


def decode_clue(file, clue_type):
    data = read_file(file)

    decode_dict = {
        "morse": [decode_morse_code, data],
        "language": [decode_language, data, "language"],
        "binary": [decode_binary, data, "decoding technique"],
        "base64": [decode_enc, data],
        "hex": [decode_hex, data],
    }

    param_list = decode_dict.get(clue_type)

    if param_list:
        func_call = param_list[0]
        args = param_list[1:]
        split_clue = args

        if len(args) > 1:
            print(f"Please enter the correct value for below: ")
            split_clue = [data]
            for param_index in range(1, len(args)):
                clue_decode = input(f"{args[param_index].capitalize()}: ")
                split_clue.append(clue_decode)


        clue = func_call(*split_clue)
        return clue
    else:
        return f"Please choose a correct clue"

# for index, value in enumerate(decoded_things):
#     save_dict.get("decoded_clues")[index] = value


def add_suspect(add_name):
    player_files = get_player_files()
    suspects = get_file("suspects.json", player_files)
    suspects_to_add = get_file("suspect_master_list.json", admin_files)
    try:
        with open(suspects_to_add, "r", encoding='utf-8') as data_file:
            data = json.load(data_file)

        with open(suspects, 'r+', encoding='utf-8') as write_file:
            write_data = json.load(write_file)
            write_file.seek(0)
            write_file.truncate()
            suspects_name_list = [inner_data.get("name").lower() for inner_data in write_data]
            for datum in data:
                for name, details in datum.items():
                    if add_name == name and add_name not in suspects_name_list:
                        write_data.append(details)
                        print(f"{name} added as Suspect")
                        break
                    if add_name in suspects_name_list:
                        print(f"{add_name.capitalize()} is already in suspects list")
                        break
                    else:
                        print(f"{add_name.capitalize()} cannot be a suspect in the game...")
                break
            json.dump(write_data, write_file, indent=2)
    except OSError:
        print("Problem with adding suspects right now")

    return "\n"

def history_command() -> dict:
    return commands_used



if __name__ == "__main__":
    # value = read_file("door_logs.csv")
    # save_game()
    list_files("FILES")