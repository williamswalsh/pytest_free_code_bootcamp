import requests

url = "https://jsonplaceholder.typicode.com/users"

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
