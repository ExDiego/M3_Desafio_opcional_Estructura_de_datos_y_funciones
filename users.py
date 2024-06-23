import requests
def get_users():
    response = requests.get('https://reqres.in/api/users')
    users_data = response.json()
    print("información de los usuarios:")
    print(users_data)
    return users_data
def create_user():
    new_user = {
        "name": "Ignacio",
        "job": "Profesor"
    }
    response = requests.post('https://reqres.in/api/users', json=new_user)
    created_user = response.json()
    print("\nUsuario creado:")
    print(created_user)
    return created_user

def update_user():
    updated_info = {
        "name": "Morpheus",
        "residence": "Zion"
    }

    response = requests.put('https://reqres.in/api/users/2', json=updated_info)
    updated_user = response.json()
    print("\nUsuario actualizado:")
    print(updated_user)
    return updated_user

def delete_user():
    response = requests.delete('https://reqres.in/api/users/6')
    print("\nUsuario eliminado:")
    print(response.status_code)
    return response.status_code

# dejar comentadas las funiones que no se utilicen antes de ejecutar el programa

get_users()
#create_user()
#update_user()
#delete_user()


