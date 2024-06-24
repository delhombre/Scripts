#!/bin/bash
<<COMMENT1
Simple case statement
Multiple lines are authorized
but simple line comments are preferred
COMMENT1

action=$1

case $action in
  s|start)
    echo "Démarrage du service ..."
    ;;
  k|stop)
    echo "Arrêt du service ..."
    ;;
  *)
    echo "Usage: s|start or k|stop"
esac
