def get_value(path: str) -> tuple[float, float]:

    try:
        open(path)
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        print("Error: unable to load the variable file. Default θ0 & θ1 are set to 0")
        return 0, 0
    
    with open(path) as f:
        tmp = f.read()
        splt = tmp.split('\n')
        T0 = float(splt[0])
        T1 = float(splt[1])

    return T0, T1