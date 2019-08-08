# what-the-fat-server
a very simple flask server that we used for what-the-fat 

## development setup

In order to run the backend, you'll need access to a shell and Python 3 installed on your system.

```sh
$ git clone https://github.com/malsf21/what-the-fat-server.git
$ cd what-the-fat-server
$ pip3 install -r requirements.txt
$ python3 server.py
* Serving Flask app "server" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## production server

I've configured this repo to deploy as a Heroku app, using `gunicorn`. You can test if the server works locally with:

```sh
$ gunicorn -w 4 server:app
```

This is a better webserver than Flask's development server. Then, it's up to you on how you want to use the production server - if you're not using something like Heroku, I'd probably recommend using nginx and uwsgi, as [this blog post explains](http://markjberger.com/flask-with-virtualenv-uwsgi-nginx/).

If you do want to use Heroku and deploy your instance of the app, it's pretty simple. Create a Heroku account, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), and the log in. Then, you just need to run:

```sh
heroku create what-the-fat-server # or whatever name you want
git push heroku master
```
