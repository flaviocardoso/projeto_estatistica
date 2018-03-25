#!/usr/bin/env python3

import json, csv, requests, os, time
from datetime import date
init = time.time()

hj = date.today()
dia = str(hj)

pastas = dia.replace("-", "/")
pasta =  "../arquivos/{0}".format(pastas)
#t = "./teste/2018/03/23"
if not os.path.exists(pasta):
    os.makedirs(pasta)

uri_produtos = "http://api.bbce.com.br/produto/todos"
r_produtos = requests.get(uri_produtos)
json_produtos = r_produtos.json()

c_ids_desc = len(json_produtos)

ids_descs = []
c_i = 0
while c_ids_desc > c_i:
    ids_descs.append((json_produtos[c_i]['id'], json_produtos[c_i]['descricao']))
    c_i = c_i + 1

for id_desc in ids_descs:
    e_id = id_desc[0]
    print(e_id)
    uri_negocios = "http://api.bbce.com.br/produto/{0}/negocios".format(e_id)
    print(uri_negocios)
    r_negocios = requests.get(uri_negocios)
    json_negocios = r_negocios.json()

    c_negocio = len(json_negocios['model'])

    if c_negocio > 0:
        arquivo = id_desc[1].replace("/", " ")
        output = csv.writer(open("{0}/{1}.csv".format(pasta, arquivo), "w"))

        negocio_headers = json_negocios['model'][0]
        keys = negocio_headers.keys()
        output.writerow(keys)

        i = 0
        while c_negocio > i:
            json_negocios['model'][i]['dataHora'] = json_negocios['model'][i]['dataHora'].replace("T", " ")
            output.writerow(json_negocios['model'][i].values())
            i = i + 1

fim = time.time()
print("Tempo de execução em {0:.0f} segundos".format(fim - init))
