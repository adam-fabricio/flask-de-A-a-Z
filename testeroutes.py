import requests

# URL base do servidor Flask
BASE_URL = 'http://127.0.0.1:8000'

def test_get_profile(id, action):
    """Testa a rota GET /profile/<int:id>/action/<action>/"""
    url = f'{BASE_URL}/profile/{id}/action/{action}/'
    response = requests.get(url)
    print(f'GET {url}')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}\n')

def test_create_profile(username, password):
    """Testa a rota POST /profile"""
    url = f'{BASE_URL}/profile'
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    print(f'POST {url}')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}\n')

def test_edit_profile(id, username, password):
    """Testa a rota PUT /profile/<int:id>"""
    url = f'{BASE_URL}/profile/{id}'
    data = {
        'username': username,
        'password': password
    }
    response = requests.put(url, data=data)
    print(f'PUT {url}')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}\n')

if __name__ == '__main__':
    # Testando as rotas
    print('=== Testando rotas ===\n')

    # Teste da rota GET /profile/<int:id>/action/<action>/
    test_get_profile(id=123, action='update')

    # Teste da rota POST /profile
    test_create_profile(username='joao', password='senha123')

    # Teste da rota PUT /profile/<int:id>
    test_edit_profile(id=123, username='maria', password='nova_senha')
