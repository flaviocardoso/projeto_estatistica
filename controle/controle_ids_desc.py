#!/usr/bin/env python
#controle de arquivos e dados para ids e descrições
import urllib.request, json, csv

with urllib.request.urlopen("http://api.bbce.com.br/produto/todos") as url:
    data = json.loads(url.read().decode())

c_data = len(data)
output = csv.writer(open("../arquivos/ids_desc.csv", "w"))
#ent_headers = data[0]
#keys = list(ent_headers.keys())
#output.writerow((keys[0], keys[1]))
output.writerow(("id", "descricao"))

i = 0
while c_data > i:
    #cont = list(data[i].values())
    #output.writerow((cont[0], cont[1]))
    output.writerow(data[i]['id'], data[i]['descricao'])
    i = i + 1
