# User REST API (Flask + Flask-RESTplus)

## Abilities

Client is able to:

1. Receive list of users
1. Receive user details by id
1. Create new user
1. Update user by id
1. Delete user by id
1. Like user by id

## Project structure

```
.
├── main.py
├── README.md
└── src
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   └── user.py
    ├── server.py
    └── views
        ├── __init__.py
        └── user.py
```

## How to start?

-   Install libraries via `pip install -r requirements.txt`
-   Start application via:

```bash
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```
