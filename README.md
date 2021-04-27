# Tweeterdemo
I have created a simple Twitter clone where users can post tweets and see other post in our app. It is a simple project , so I did not include a sign up/login in functionality. I have used this project to learn CRUD(Create/Read/Update/Delete) functionality.

### [LIVE DEMO](https://dashboard.heroku.com/apps/tweetclone1)


### Technologies Used

* HTML , CSS and BOOTSTRAP
* JAVASCRIPT 
* DJANGO

### Functionality that had been created are:
1. Users can post tweets
2. Users can comment on tweets
3. Users can delete tweets
4. Users can send a like to a tweet and see like counts

### Requirements

Atfirst install python package. You can download python from https://www.python.org/downloads/
.Then clone this github and save in your device.
```sh
git clone https://github.com/yogendra/tweeterdemo/
cd tweeterdemo
```
It is important to download the requirements to run this app in your localhost , hence to download all the requirements packages used during building phases.
Use this command in local command prompt.

```sh
pip install -r requirements.txt
```
#### Before deployment , migrate all the changes and makemigrations using following shell command prompt:
```sh
python manage.py makemigrations

python manage.py migrate
python manage.py runserver
```

### Deployment
- Application will be serving on http://localhost:8000

