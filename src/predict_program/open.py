def open_file(path: str) -> tuple[float, float]:

    try:
        fd = open(str)
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        print("Error: unable to load image")
        return None
    
    with open("output.txt") as f:
        tmp = f.read()
        splt = tmp.split('\n')
        print(float(splt[1]))