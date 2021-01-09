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

## Install et utilisation du modèle

Notre notebook nécessite l'installation de plusieurs modules :
1. pandas, pour gérer notre dataset
2. matplotlib, afin de créer des graphes

ATTENTION : le modèle final choisi est trop lourd pour être placé dans le github (même en le zipant), je vous invite à relancer tout le notebook afin d'en télécharger le modèle au format pickle.

## API

L'api est directement relié avec notre modèle et vous permet d'envoyer une requête contenant les paramètres d'une vidéo. Elle renvoie ensuite l'estimation du temps de transcodage de cette vidéo.
Le format d'une requête envoyée à l'api est la suivante :
"duration","codec","width","height","bitrate","framerate","i","p","b","frames","i_size","p_size","b_size","size","o_codec","o_bitrate","o_framerate","o_width","o_height","umem"

Pour le test d'une requête, on va tester pour une vidéo de 2 minutes en 720p du format flv au format mpeg4 en 4k avec une allocation mémoire de 60MB. Afin de tester cette requête, il faut lancer le fichier app.py avec python pour que le serveur se lance. Puis, on exécute le fichier "request.py" afin d'en récupérer le résultat de cette requête.

## Conclusion

