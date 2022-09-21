# UG04 - JSON
# Kinanthi (71210745)

import json

data = None
with open('karyawan.json', 'r') as datafile:
    data = json.load(datafile)

d = {
    "Caca": [
        {"Alamat": "Pati"},
        {"Kolega": ["Andy","Banu"]}],
    "Kaka": [
        {"Alamat": "Pati"},
        {"Kolega": ["Andy","Banu"]}]
    }

data.update(d)

with open('karyawan.json','w') as datafile:
    json.dump(data, datafile)
