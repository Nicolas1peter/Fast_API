# Fast_API
Le but de l'expérience sera de créer une api rest avec fast api ainsi que de la dockeriser pour la déployer,
l'avantage de fast api avec les autres serais qu'elle permet directement de faire la programmation asynchrone
Pour commencer, je vais créer un nouvel environnement avec virtual env et l'activer.
Dans ce nouvel environnement, on peut installer fast api pour pouvoir créer notre api rest ainsi qu'uvicorn pour pouvoir la déployer.

Step 1:

Je créer un api basique qui renvoie hello word pour commencer et qui se lancer avec uvicorn dans un script python "api.py"
Je vois que pour faire un patch paramétrer par exemple récupérer l'id d'un component il faut juste faire une requête @app.get("/component/{component_id}")
On peut aussi faire passer plusieurs component à la fois en "posant une question" avec le ? Avec @app.get("/component/")

step 2:

Je vais créer un BaseModel (une class) avec des arguments que je pourrais modifier avec une requête post.
Je créer une requête post avec une modèle de réponse qui ajoute une "priority" dans la class
Je peux tester avec 127.0.0.1:8000/docs pour tester toutes mes requêtes api avec fastapi.
Je peux faire en sorte de cacher des donnée sur le mode de retour comme des mot de passe en utilisant un "reponse model" qui est la class, mais avec uniquement ce qu'on veut afficher pour sécuriser certaines valeurs.

Step 3:

Ajouter des requêtes de login et register pour simuler l'ajoute dans une data base, je vais utiliser sqlalchemy
Je fais les requêtes pour se connect et déconnecter a la db ainsi que la création de compte la suppression et juste afficher en fonction de l'id du compte.
On peut maintenant grâce au requête api créer des data dans la db


Step 4:

Il me reste a dockeriser l'application je fais donc un dockerfile et un docker-compose.yaml

Conclusion

Lors de cette expérience, j'ai appris à utiliser FastApi pour créer une api avec des requêtes basique ainsi que des requêtes lié a une database pour simuler la création de compte, puis dockeriser l'application pour la rendre déployable.








