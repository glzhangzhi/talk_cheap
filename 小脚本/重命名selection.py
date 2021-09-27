from pathlib import Path

def update_file_to_new_Mbilly_plate_number(path_to_file):

    file = Path(path_to_file)

    with open(file, 'r') as f1:
        content = f1.read()
        content_new = content.replace("Mbilly3", "AZEMB3")
        split1 = str(file).split('.')
        newname = split1[0] + '_new.txt'
        with open(newname, 'w') as f2:
            f2.write(content_new)