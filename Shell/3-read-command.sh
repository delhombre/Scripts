#!/bin/bash
echo -n "Entrez votre prénom : "
read prenom
read -p "Entrez votre nom : " nom
read -p "Entrez votre code postal et votre commune : " code commune

echo "Bonjour $prenom $nom habitant à $code $commune"
