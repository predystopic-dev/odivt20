def extract_number(filename):
    return int(filename.split(".")[0])

def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total