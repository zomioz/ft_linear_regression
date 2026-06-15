def get_value(path: str) -> tuple[float, float]:

    try:
        open(path)
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return 0, 0
    
    with open(path) as f:
        tmp = f.read()
        splt = tmp.split('\n')
        T0 = float(splt[0])
        T1 = float(splt[1])

    return T0, T1