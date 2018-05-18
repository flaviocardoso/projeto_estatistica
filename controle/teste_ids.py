#!/usr/bin/env python3

import json, csv, requests, os, time

for e_id in range(0, 3000):
    uri_negocios = "http://api.bbce.com.br/produto/{0}/negocios".format(e_id)
    r_negocios = requests.get(uri_negocios)
    json_negocios = r_negocios.json()

    c_negocio = len(json_negocios['model'])

    if c_negocio > 0:
        print(e_id)
