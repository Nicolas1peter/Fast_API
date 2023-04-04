# Fast_API
Le but de l'experience sera de créer une api rest avec fast api ainsi que de la dockeriser pour la deployer, 
l'avantage de fast api avec les autres serais qu'elle permet directement de faire la programation asynchrone lorsque on créer l'api
pour commencer je vais crer un nouveau environnement avec virtual env et l'activer.
dans se nouvel environnement on peux installer fast api pour pouvoir créer notre api rest ainsi que uvicorn pour pouvoir la deployer

Step 1:

je créer une api basique qui renvoie hello word pour commencer et qui se lancer avec uvicorn dans un scrip python "api.py"
je vois que pour faire un patch parameter par exemple recuperer l'id d'un component il faut juste faire une requete @app.get("/component/{component_id}")
on peux aussi faire passer plusieur component a la fois en "posant une question" avec le ? avec @app.get("/component/")

step 2:

je vais créer un BaseModel(une class) avec des argument que je pourrais modifier avec une requete post,
je créer une requete post avec une modele de reponse qui ajoute une "priority" dans le cas ici dans le BaseModel
je peux tester avec 127.0.0.1:8000/docs pour tester toutes mes requetes api avec fastapi.
je peux faire en sorte de cacher des donnée sur le model de retour comme des mot de passe en utilisant un "reponse model" qui est la class mais avec uniquement se qu'on veux afficher pour securiser certaines valeur.

Step 3:

ajouter des requetes de login et register pour simuler l'ajoute dans une data base je vais utiliser sqlalchemy
je fais les requetes pour se connect et deconnecter a la db ainsi que la création de compte la suppression et juste afficher en fonction de l'id du compte.
on peux maintenant grace au requete api créer des data dans la db


Step 4:

il me reste a dockeriser l'application je fais donc un dockerfile et un docker-compose.yaml

Conclusion

Lors de cet experience j'ai appris a utiliser FastApi pour créer une api avec des requetes basique ainsi que des requetes lié a une database pour simuler la création de compte, puis dockeriser l'application pour la rendre deployable.
