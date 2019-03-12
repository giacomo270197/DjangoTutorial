**If you want to use the code I provided**, you can just pull the repository and bring the Docker container up.
In order to do so you must have docker and docker-compose installed, check:
	
https://docs.docker.com/install/   ->  Docker installation (pick your system from the menu).
https://docs.docker.com/compose/install/ -> Docker Compose installation.
	
In order to bring the container up, run the `docker-compose up --build` command. This will start your container AND your Django server.

As discussed in the tutorial, there will be a app you can work on, called `emptyapp`. If you want to delete the app used in the tutorial (`gitapp`), just delete the folder and the entry in `settings.py/INSTALLED_APPS`. 

Now you are ready to build your app. First off you'll need to build some models for your database. If the info given in the tutorial weren't enough (probably so), please visit the Django page:

https://docs.djangoproject.com/en/2.1/ref/models/fields/ 

Alternatively, you can shoot me an email at g.casoni@student.rug.nl (but please first try the docs and/or StackOverflow). 

Once you models are ready, you can build your actual database. This is made slightly trickier by the fact that you are running on Docker, but following these steps should do the trick:
	
- Make sure you docker container is running, if not, start it up (`docker-compose up --build`).
- On a different shell, run the command `docker exec -it tutorialapp_web_1 bash`.
- Make sure you're in the `code` folder.
- Run `./manage.py makemigrations emptyapp` (if you kept the name amptyapp, change it otherwise).
- You should see a list and a lot of OK's...and no errors!
- Run `./manage.py migrate`.

At this point your database will be set up. If you wanna double check use your favorite SQLite explorer to check your tables have indeed been created. 

Your endpoints are going to be reachable at `localhost:8000/` + whatever endpoint you are going to define.

NOTES:
	
	- The combination `makemigrations` and `migrate` applies the changes you made to the models to your DB, therefore you'll need to run it everytime you change your models.
	- Docker sets all the files it creates as owned by 'root'. This could cause permissions problems. Just run problematic commands with `sudo` or set youself as a owner (`chown`)
