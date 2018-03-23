#!/usr/bin/env python
#controle json teste

import json, csv, requests, time
init = time.time()

uri = "http://api.bbce.com.br/produto/todos"

r = requests.get(uri)
json = r.json()
c_data = len(json)
output = csv.writer(open("../arquivos/ids_desc.csv", "w"))
output.writerow(("id", "descricao"))
#print(len(r))
i = 0
while c_data > i:
    #rint(json[i]['id'], json[i]['descricao'])
    output.writerow((json[i]['id'], json[i]['descricao']))
    i = i + 1

fim = time.time()
print("Tempo de execução em {0:.0f} segundos".format(fim - init))
