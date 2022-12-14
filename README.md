# Python Flask REST API
 Python + Flask REST API

 This repository was solely built for learning purposes.
 
 This code has been written with the help of [Tech with Tim](https://www.youtube.com/c/TechWithTim)'s video: [Python REST API Tutorial - Building a Flask REST API](https://www.youtube.com/watch?v=GMppyAPbLYk)


## Dependencies
- aniso8601 (9.0.1)
- click (8.1.3)
- Flask (2.2.2)
- Flask-RESTful (0.3.9)
- Flask-SQLAlchemy (2.5.1)
- itsdangerous (2.1.2)
- Jinja2 (3.1.2)
- MarkupSafe (2.1.1)
- pytz (2022.2.1)
- six (1.16.0)
- SQLAlchemy (1.4.40)
- Werkzeug (2.2.2)

All dependencies are available under the repository in `dependencies-uptodate.txt` and `dependencies-listed.txt`

> You can install the up-to-date versions of them with your desired txt file. "uptodate" will install the most up-to-date versions available, where "listed" version will install them with the versions written in the README.md file.

Install all dependencies (up-to-date):

```
pip install -r dependencies-uptodate.txt
```

Install all dependencies (listed):
```
pip install -r dependencies-listed.txt
```

### Available API requests

- GET
- PUT
- PATCH
- DELETE

### How to send data

Data is sent via JSON to the server.
I am using Postman myself, and here is an example image:

![Postman Request](https://github.com/erentomurcuk/Python-Flask-REST-API/blob/main/imgs/postman_example.jpg)

Make sure that you use

```
'Content-Type': 'application/json'
```

Small note for Windows Users: At first I was trying to send requests with `Python` with the use of `requests` package. When you are sending requests that way, make sure you use double-quotes only and put a `\` before the `"` so that it will work correctly. An image is available for an example below.

![Python Request](https://github.com/erentomurcuk/Python-Flask-REST-API/blob/main/imgs/requests_example.jpg)

# How to run the server

Open a terminal window in the repository folder and run:

Windows:
```
python.exe .\main.py
```

Linux/macOS:
```
python3 main.py
```

## Licence

The MIT Licence - Check LICENCE.md for more information.
