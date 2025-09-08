# def list_file():
#     # ───── Old Method: Shallow listing using iterdir() ─────
#     index = 1
#     for paths in sorted(path_name.iterdir()):
#         # iterdir() iterates over the directories
#         # new_path = paths.absolute()   # absolute() returns the absolute path of the file
#         new_outer_path = paths.name     # .name gives only the name of the files
#         print(f"{index}: {new_outer_path}")
#         if paths.is_dir():
#             for inner_path in sorted(paths.iterdir()):
#                 new_inner_path = inner_path.name
#                 print(f"\t-- {new_inner_path:}")
#         index += 1
#
#     print()
#
# def read_file(filename):
#     for file in directories:
#         if file.name == filename:
#             absolute_path = file.absolute()
#             if absolute_path.is_dir():
#                 for files in absolute_path.iterdir():
#                     print(f"Please choose a file from the folder you selected")
#                     print(f"{files.name}")
#             else:
#                 with open(absolute_path, encoding='utf-8') as input_file:
#                     for row in input_file:
#                         print(row.strip())
#     else:
#         print(f"{filename} is not a valid file or folder")
#

# def read_file(file):
#     name_path = get_file(file)
#     try:
#         for keys in encrypted_password:
#             if name_path.match(keys):
#                 encryption = protected_file(keys)
#                 if not encryption:
#                     return f"The Password is incorrect"
#         with open(name_path, encoding='utf-8', newline='') as input_file:
#             data = input_file.read()
#             # if name_path.suffix == ".csv":
#             #     new_dialect = csv.Sniffer().sniff(data)
#             #     input_file.seek(0)
#             #     reader = csv.DictReader(input_file, dialect=new_dialect)
#             #     value = []
#             #     for row in reader:
#             #         value.append(row)
#             #     return value
#         return data
#     except OSError:
#         return f"Input `folder/file` else `file`"

# useful things
# stage_1_files = load_files("crime_details.txt", "door_logs.csv", "emails.txt", "timeline.txt")
# stage_2_files = load_files("suspects.json")
# stage_3_files = load_files("entry1.txt", "entry2.txt", "entry3.txt", "eleanor_session3.txt")
# stage_4_files = load_files("clue1_email.txt", "clue2_email.bin", "entry4.txt", "entry5.txt",
#                            "entry6.txt", "entry7.txt", "entry8.txt")
# stage_5_files = load_files("photo.enc", "voice_fragment.raw")
# stage_6_files = load_files("maid2_phone_dump.txt", "testimony.txt")


#
# def overwrite_folder(input_path, destination_path) -> None:
#     temp_path = pathlib.Path("Temp")
#     pathlib.Path.mkdir(temp_path)
#
#     if destination_path.exists():
#         shutil.copytree(destination_path, "Temp", dirs_exist_ok=True)
#         shutil.rmtree(destination_path)
#
#     shutil.copy2(input_path, temp_path)
#     shutil.copytree(temp_path, destination_path)
#     shutil.rmtree("Temp")