import pathlib
import shutil

def main():
    print("This is a WIP Quick and Dirty File Sorter (QADFS)")
    print("")
    while True:
        folder_path = input("Please paste in the absolute path (from root down) to the folder to be sorted or leave blank for the current working directory: ")
        if not folder_path:
            folder_path = pathlib.Path.cwd()
        elif not pathlib.Path(folder_path).exists() or not pathlib.Path(folder_path).is_dir():
            print("The provided path does not exist or is not a directory. Please check the path and try again.")
            folder_path = input("Please paste in the absolute path (from root down) to the folder to be sorted or leave blank for the current working directory: ")
        else:
            break
    else:
        folder_path = pathlib.Path(folder_path)
    print(f"Sorting folder: {folder_path}")
    input("Press enter to continue...")

    for item in folder_path.iterdir():
        if item.is_file():
            ext = "".join(item.suffixes[-2:])[1:]

            if not ext:
                ext = "no_extension"
            destination_folder = folder_path / ext
            destination_folder.mkdir(parents=True, exist_ok=True)
            destination_file = destination_folder / item.name

            if destination_file.exists():
                destination_file = destination_folder / f"{item.stem}_copy{item.suffix}"

            shutil.move(str(item), str(destination_file))
            print(f"Moved {item.name} to {destination_file}")
main()