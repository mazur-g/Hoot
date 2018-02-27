# HOOT


<img src="https://github.com/pawel-ta/Django/blob/master/hello/static/img/hoot-logo.png"><br><br>

Hosted on Heroku servers [here](http://hoot-hoot.herokuapp.com/ "Hoot-Hoot")

# Introduction
**Hoot** is a Django web application. The aim of this project is to offer a fast way to broadcast messages, by displaying them on a map in specific location. The service is currently only a foundation for further development

# Installation
Like in every Django project, just start a barebones Django server and put the files in it.

# Usage
Everything is WYSiWYG<br>
Simply register a new account or sign in using an existing user account to explore the map and share your thoughts.
You can look for an user by clicking on search button, and you can change your account information (email and picture)
by going to 'profile' tab and clicking 'Make changes' button.

# Detailed
The whole documentation regarding the app production process is available in documentation.pdf file.

It uses **Django** as backend, **MaxMind** GeoIP datasets for IP-based geolocation, **OpenLayers API** for map handling and Twitter's **Bootstrap** as css and js frontend helper.

The app currently offers user registration, profile browsing and changing personal data, user search, posting 'hoots' on map and viewing posts of others on the map. It uses KML data format for holding post information to be displayed on the map. For browsers that provide geolocation information via javascript geolocation module (based on browser and user permission, more accurate), the location of post is set based on that. If such information isn't present, location is guessed based on IP adress (less accurate).

# Known bugs and errors
Due to Heroku servers filesystem's very nature, posts and images uploaded during app's on-time disappear after the app has gone off (when no users connect to Heroku servers during specific amount of time, the dynos switch off and all static files added during on-time disappear). [https://kb.heroku.com/why-are-my-file-uploads-missing-deleted]
This could be fixed in the future by using Amazon's S3 (for example)

*The logo just looks awful*

Of course static files won't be served by Django automatically if the debug mode was off, we will then move app to a regular unix server where we could serve them with ease directly from there.