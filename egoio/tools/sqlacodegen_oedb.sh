#!/bin/bash

db_user=""
db_password=""
db_host=""
db_port=""
db="oedb"
path="../db_tables/"

if [ -d "../db_tables" ]; then
    schemas=("climate" "demand" "economy" "emission" "environment" "grid" "openstreetmap" "boundaries" "reference" "scenario" "society" "supply" "model_draft")
    for schema in ${schemas[*]}
    do 
        {
            echo "Write table schemas for $schema"
            sqlacodegen postgres://$db_user:$db_password@$db_host:$db_port/$db --schema=$schema --outfile=$path$schema.py 
        } || { 
            echo "Error in schema ${schemas[$i]}"
            mv $path$schema.py  {$path$schema}_err.py 
        }
    done
else
    echo "Folder ../db_tables does not exist"
fi

