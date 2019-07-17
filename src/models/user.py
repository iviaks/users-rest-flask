users = [
    {
        'id': 1,
        'firstName': 'Rosalva',
        'lastName': 'Manwarren',
        'age': 28,
        'likes': 0
    },
    {
        'id': 2,
        'firstName': 'Susanne',
        'lastName': 'Germond',
        'age': 28,
        'likes': 0
    },
    {
        'id': 3,
        'firstName': 'Catina',
        'lastName': 'Lyseski',
        'age': 28,
        'likes': 0
    },
    {
        'id': 4,
        'firstName': 'Herma',
        'lastName': 'Stoffel',
        'age': 28,
        'likes': 0
    },
]


def find():
    return users

def findById(pk: int):
    return next((user for user in users if user['id'] == pk), None)

def create(data: dict = {}):
    user = data.copy()
    user['id'] = users[-1]['id'] + 1 if len(users) else 1
    users.append(user)

    return user

def update(pk: int, data: dict = {}):
    for index in range(len(users)):
        if users[index]['id'] == pk:
            users[index].update(data)
            return users[index]

def delete(pk: int):
    for index in range(len(users)):
        if users[index]['id'] == pk:
            users.pop(index)

            return None, 204

def like(pk: int, value: int):
    for index in range(len(users)):
        if users[index]['id'] == pk:
            users[index]['likes'] += value
            return users[index]
