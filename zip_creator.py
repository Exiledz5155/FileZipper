import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    # write a zipfile in the destination passed
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            # Override the original file path to a smart path
            filepath = pathlib.Path(filepath)
            # arcname extracts only the name of the file not the full path
            archive.write(filepath, arcname=filepath.name)


#if __name__ == "__main__":
    #make_archive(filepaths=[])