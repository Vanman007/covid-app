own:
	sudo chmod 777 -R ~/Desktop/covid-app

dropdb:
	docker exec -it covidapp_db_1 bash 
	psql -U postgres
	\dt
	"drop table <tablename>"	

superuser:
	docker-compose run web python manage.py createsuperuser

fake users:
	docker-compose run web python manage.py fake_users 10