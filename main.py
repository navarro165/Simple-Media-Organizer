from media_organizer import organize_media
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter


def main():
    completer = PathCompleter()
    src_dir = prompt("Enter the path of the source directory: ", completer=completer)
    organize_media(src_dir)
    print("Media files have been organized successfully.")


if __name__ == '__main__':
    main()
