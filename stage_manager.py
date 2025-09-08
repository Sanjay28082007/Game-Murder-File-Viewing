import shutil
from functions import *

stage_names = [
    "case_intro",  # 🕵️ Stage 1: Crime scene overview
    "suspects_loaded",  # 🧠 Stage 2: Suspects introduced
    "diary_revealed",  # 📓 Stage 3: Found first diary entries
    "clues_decoding",  # 🔎 Stage 4: Decoding binary, Morse, etc.
    "admin_access_unlocked",  # 🔐 Stage 5: Admin files accessed
    "cross_reference",  # 🧬 Stage 6: Cross-checking evidence
    "safe_unlocked",  # 🔓 Stage 7: Solving safe puzzle
    "accusation_made",  # ⚖️ Stage 8: Final accusation
    "epilogue_complete"  # 📖 Stage 9: Endgame and reflection
]

stages_dict = {index + 1: contents for index, contents in enumerate(stage_names)}

with open("Admin_files/stages.json", 'r', encoding='utf-8') as f:
    new_data = json.load(f)
    stage_file = []
    for file_per_stage in new_data:
        temp_new_list = []
        for files_path in file_per_stage:
            temp_new_list.append(pathlib.Path(files_path))
        stage_file.append(temp_new_list)

player_stage = int(current_stage)


def file_conditions():
    pass


def get_stage_file_map():
    get_dict = {}
    for index, files in stages_dict.items():
        stages_files_str = stage_file[index - 1]
        set_stage = set()
        for new_stage in stages_files_str:
            stage_str = new_stage.name
            set_stage.add(stage_str)
        get_dict[index] = set_stage

    return get_dict


def get_unlocked_files():
    """Returns the set of files unlocked in current stage but not yet read."""
    stage_set = get_stage_file_map()
    set_stage = stage_set[player_stage]
    if player_stage != 1:
        set_stage = stage_set[player_stage] - stage_set[player_stage - 1]
        # by this we can get the difference between the previous stage and current stage
        return set_stage.difference(save_dict.get("files_read"))
    values = set_stage.difference(set(save_dict.get("files_read")))
    return values


def update_stage():
    global player_stage

    unread_files_remaining = get_unlocked_files()
    conditions = other_conditions()
    if not unread_files_remaining and conditions:
        player_stage += 1
        copy_files()
        print(f"STAGE: {player_stage} \t{stages_dict.get(player_stage).upper()}")
        print(f"New Files Unlocked!")
    # Ensure print(...) won’t break if player_stage exceeds len(stages_dict).


def other_conditions():
    if len(set(save_dict.get("suspects_asked"))) >= 2:
        return True
    elif player_stage == 3:
        files = ["entry1.txt", "entry2.txt", "entry3.txt"]
        temp_value = [file in save_dict.get("files_read") for file in files]
        if any(temp_value):
            return True
    elif player_stage == 4:
        files = ["clue1_email.txt", "clue2_email.bin", "photo.enc"]
        temp_value = [file in decoded_things for file in files]
        if any(temp_value):
            return True
    elif player_stage ==  5:
        files = ["clue1_email.txt", "clue2_email.txt", "clue3_email.txt", "entry4.txt", "entry5.txt", "entry6.txt", "entry7.txt", "entry8.txt"]
        temp_value = [file in decoded_things for file in files]
        if any(temp_value):
            return True
    elif player_stage == 6:
        files = ["photo.enc", "voice_fragment.raw"]
        temp_value = [file in save_dict.get("files_read") for file in files]
        if any(temp_value):
            return True
    elif player_stage == 7:
        files = ["maid2_phone_dump.txt", "testimony.txt"]
        temp_value = [file in save_dict.get("files_read") for file in files]
        if any(temp_value):
            return True
    elif player_stage == 8:
        pass


    return None


def get_stage_files():
    files_per_stage = []
    for index in range(0, player_stage):
        get_stage_file = stage_file[index]
        files_per_stage.extend(get_stage_file)
    return files_per_stage


def copy_files():
    files_per_stage = get_stage_files()
    for win_files in files_per_stage:
        path_split = list(win_files.parts)

        path_split.pop(-1)  # Removing the index of the file name
        path_split.pop(0)  # Removing the index of the name of the path that file is copied from

        name_change = "/".join(path_split)
        overwrite_folder(win_files, f"Player/{name_change}")


def overwrite_folder(input_path, destination_path) -> None:
    destination_path = pathlib.Path(destination_path)

    if not destination_path.exists():
        pathlib.Path.mkdir(destination_path, parents=True)

    shutil.copy2(input_path, destination_path)


if __name__ == "__main__":
    pass
