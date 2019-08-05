import glob2

import re

def get_files():
    content = dict()
    for file in glob2.glob('*.csv'):
        print(file)
        with open(file,'r') as filehandle:
            content[file] = filehandle.readlines()
    return content


def normal_form(name : str):
    """normalizes a string. removes all non-chars and converts to lower."""
    name_lower = name.lower()
    words = re.sub(r'[^A-Za-z0-9]','',name_lower).strip()
    normal = ''.join(sorted(words))
    return normal



if __name__ == "__main__":
    content = get_files()
    ingrds = {v.strip() for _,vs in content.items() for v in vs }
    nmap = {n : normal_form(n) for n in ingrds}


