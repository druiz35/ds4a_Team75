#!/bin/sh
gsed -i 's/bogota_d.c./bogota/g' ../data/mdm_clean.csv
gsed -i 's/tolima_/tolima/g' ../data/mdm_clean.csv
gsed -i 's/bogota_d.c./bogota/g' ../data/comp_dim_clean.csv
gsed -i 's/tolima_/tolima/g' ../data/comp_dim_clean.csv
gsed -i 's/san_andres_y_providencia/san_andres/g' ../data/mintic_investments_clean.csv
gsed -i 's/peðol/peniol/g' ../data/mintic_investments_clean.csv
gsed -i 's/bogota,_d.c./bogota_d.c./g' ../data/mdm_clean.csv
gsed -i 's/bogota,_d.c./bogota_d.c./g' ../data/comp_dim_clean.csv
gsed -i 's/gsican/guican/g' ../data/mintic_investments_clean.csv
gsed -i 's/togsi/togui/g' ../data/mintic_investments_clean.csv
gsed -i 's/chibolo/chivolo/g' ../data/mintic_investments_clean.csv
gsed -i 's/chachagsi/chachagui/g' ../data/mintic_investments_clean.csv
gsed -i 's/magsi/magui/g' ../data/mintic_investments_clean.csv
gsed -i 's/gsepsa/guepsa/g' ../data/mintic_investments_clean.csv
gsed -i 's/guachene_/guachene/g' ../data/mdm_clean.csv
gsed -i 's/guachene_/guachene/g' ../data/comp_dim_clean.csv
