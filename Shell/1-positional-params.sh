#!/bin/bash
echo "Nom du script : "$(basename $0)
echo "Premier paramètre : "$1
echo "Deuxième paramètre : "$2
echo "PID du script : "$$
echo "Nombre de paramètres : "$#
echo "Liste des paramètres : "$*
