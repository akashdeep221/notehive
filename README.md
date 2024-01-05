
# Notehive

Backend of a Note management application where users can create, read, update, and delete notes. The application also allows users to search for notes based on keywords.


## API Reference

#### Get all notes

```http
  GET /api/notes/
```
Gets all notes for the authenticated user.

#### Get note by id

```http
  GET /api/notes/<int:pk>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `bigint` | **Required**. Id of note to fetch |

Gets note using id for the authenticated user.

#### Sign Up User

```http
  POST /api/auth/signup/
```
| Body elements | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. username of user |
| `password`| `string` | **Required**. password of user |


Signs up the user using username and password passed in body(json).


#### Login User

```http
  GET /api/auth/login/
```

| Body elements | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. username of user |
| `password`| `string` | **Required**. password of user |

Logs in the user using username and password passed in body(json). and gets a token as response.

#### Search notes by keywords

```http
  GET /api/search/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `q`      | `string` | **Required**. keyword(s) to search in notes |

Retrieves notes which has the keyword(s) in title or content







## Choice of framework/db

Framework - Django  
Database - PostgreSQL  
  
Django is used as the development framework because it is easy to start, and it takes very less time to build an application.  
  
PostgreSQL is used as the database because it is fast, scalable and offers advanced security features.

## Installation Pre-requisites

python3, pip


## Run Locally (Windows OS)

Clone the project

```bash
  git clone https://github.com/akashdeep221/notehive
```

Go to the project directory

```bash
  cd notehive
```

Setup Virtual Environment

```bash
  python -m venv env
```

Install dependencies

```bash
  pip install -r requirements. txt
```

Go to the project directory

```bash
  cd notehive
```

Start the server

```bash
  python manage.py runserver
```

**The above commands are for Windows OS. For Mac/Linux, please refer to the respective commands for doing the same tasks above.
## Running Tests

To run tests, run the following command in the terminal for the same directory as for running the application

```bash
  python manage.py test notevault
```


## Appendix

Authentication and authorization mechanism used - JWT Token  
Rate limiting and rate throttling - 50/min for anonymous users and 100/min for authenticated users (can be changed).  
## 🚀 About Me
I'm a backend developer currently pursuing MS in Computer Science from Woolf Higher Education Institution.  
My LinkedIn profile - https://www.linkedin.com/in/akashdeep-vasistha-56999a127/  
My email - akashdeep2357asgardia@gmail.com  
Let's connect!
