import requests

from args import args
from tledetach import detach

def tlereader(noradid):
    url = args['url_main'] + noradid

    print(f"Get information from: {url}")

    aux_list = []
    tle_list = []

    data = requests.get(url)
    data_lines = data.text.split('\n')

    # Separated each 3 lines, according to TLE
    aux = 0
    for line in data_lines:
        line = line.strip()
        if aux < 3:
            aux_list.append(line)
        else:
            tle_list.append(aux_list)
            aux_list = []
            aux_list.append(line)
            aux = 0
        aux += 1

    # Function to detach TLE lines
    if not tle_list:
        print(f"NoradID: {noradid} does not return any data!")
    else:
        detach(tle_list)