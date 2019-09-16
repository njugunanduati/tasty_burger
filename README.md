##Tasty Burger
##########################

Tasty burger is an online web portal to allow users to register and oreder for a burger from 
tasty burger.

# Getting Started

1). Clone the application from the repo
	git clone https://github.com/njugunanduati/tasty_burger.git

2). Change the durectoy
	cd tasty_burger

3). Create a virtual enviroment
	python3.6 -m venv venv

4). Install the dependencies

	pip install -r requirements.txt

5). Make the migrations
	python manage.py makemigrations

	python manage.py migrate

6).Add the following to your enviroment 
	export SECRET_KEY='your_secret_key'

	export EMAIL_USERNAME='your_gmail_username'

	export EMAIL_PASSWORD='your_password' 
7). Create a superuser
		python manage.py createsuperuser 

9). Run the application

	python manage.py runserver


##For the heroku hosted one

https://tasty-burger-kenya.herokuapp.com/