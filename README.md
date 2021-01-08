# Python-data-analysis-Project
## Introduction

Ce projet a pour but d'estimer le temps de transcodage d'une vidéo youtube suivant une vingtaine de critères. Pour cela, nous avons créé un modèle de machine learning qui s'appuie sur le dataset suivant : 
https://archive.ics.uci.edu/ml/datasets/Online+Video+Characteristics+and+Transcoding+Time+Dataset#.
Ce dataset est composé de deux fichiers, le premier, contenant environ 160K lignes et 11 colonnes, permet d'avoir une vue générale des paramètres et le deuxième, qui est plus complet avec 68 lignes et  21 colonnes, nous as permis d'entraîner notre modèle.

## Contenu

Ce projet contient : 
1. Une présentation du projet en version pdf
2. Notre notebook python
3. Les fichiers composant notre API

## Install

Notre notebook nécessite l'installation de plusieurs modules :
1. pandas, pour gérer notre dataset
2. matplotlib, afin de créer des graphes

## API

L'api est directement relié avec notre modèle et vous permet d'envoyer une requête contenant les paramètres d'une vidéo. Elle renvoie ensuite l'estimation du temps de transcodage de cette vidéo.
Voici un exemple de requête : ""

## Conclusion

