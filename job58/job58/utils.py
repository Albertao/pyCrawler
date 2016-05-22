def format(str):
    str = str.encode("utf8").replace(" ", "").replace("\r", "").replace("\n", "")
    return str