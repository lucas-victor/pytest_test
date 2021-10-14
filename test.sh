#!/bin/bash

FIM="n"
while [[ "$FIM" != "s" ]]; do

  echo "Execucao finalizada? (S/n)";
  read FIM

  if [[ "$FIM" == "s" ]]; then
         sleep 1 
  fi
  sleep 1
done

