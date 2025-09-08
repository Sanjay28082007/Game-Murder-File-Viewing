from stage_manager import *
import difflib
print()
commands = list_commands()


if player_stage <= 1:
    copy_files()


def main():
    while True:
        user_input = input(">> ").strip().casefold()
        values = user_input.split()
        command = values[0]
        args = values[1:]
        if command == "exit":
            break
        if command in commands:
            valid_command = commands[command]
            if args:
                try:
                    temp = valid_command(*args)
                except TypeError:
                    print("Please enter valid arguments.")
                    continue
                except AttributeError:
                    print("Please enter valid names of the arguments.")
                    continue
            else:
                temp = valid_command()

            print(temp)
            commands_used[command] = set(args)
            update_stage()
        elif command not in commands:
            suggestion = difflib.get_close_matches(command, commands)
            if suggestion:
                print(f"{command} is not a valid command. Did you mean {suggestion[0]}?")
            else:
                print(f"{command} is not a valid command.")


if __name__ == "__main__":
    main()
    print(save_dict)