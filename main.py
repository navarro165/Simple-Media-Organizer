from media_organizer import organize_media
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter


def main():
    completer = PathCompleter()
    src_dir = prompt("Enter the path of the source directory: ", completer=completer)

    # Check if the user is ok with the given path
    while True:
        confirm = input(f"Is {src_dir} the correct path? (y/n)")
        if confirm.lower() == 'y':
            break
        elif confirm.lower() == 'n':
            src_dir = prompt("Enter the path of the source directory: ", completer=completer)
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
    
    organize_media(src_dir)
    print("Media files have been organized successfully.")


if __name__ == '__main__':
    main()
