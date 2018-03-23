#!/usr/bin/env python
#entrada de id por negocios

import json, csv, requests, os, time
init = time.time()

cmd = os.getcwd()
files = os.listdir(cmd) # lista arquivos do diretorio
#dirs = os.mkdir(diretorio) #faz diretorio

print("Insira o id")
id = input()
uri = "http://api.bbce.com.br/produto/{0}/negocios".format(id)
r = requests.get(uri)
json = r.json()

c_negocio = len(json['model'])
if c_negocio == 0:
    print("SEM negocios!")
else:
    print("COM negocios!")
    uri_desc = "http://api.bbce.com.br/produto/todos"
    r_desc = requests.get(uri_desc)
    json_desc = r_desc.json()

    j = 0
    f = 0
    desc = ""
    while (len(json_desc) > j and f == 0) :
        print(id == json_desc[j]['id'], id, json_desc[j]['id'])
        if int(id) == json_desc[j]['id']:
            desc = json_desc[j]['descricao']
            f = 1
        j = j + 1
    #print("Nomei o arquivo")
    #arquivo = input()
    arquivo = desc.replace("/", " ")
    output = csv.writer(open("../arquivos/{0}.csv".format(arquivo), "w"))

    negocio_headers = json['model'][0]
    keys = negocio_headers.keys()
    output.writerow(keys)

    i = 0
    while c_negocio > i:
        json['model'][i]['dataHora'] = json['model'][i]['dataHora'].replace("T", " ")
        output.writerow(json['model'][i].values())
        i = i + 1

fim = time.time()
print("Tempo de execução em {0:.0f} segundos".format(fim - init))
