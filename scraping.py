import base64
import hashlib
import os
import requests
from requests_oauthlib import OAuth2Session

def generate_code_verifier():
    return base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8').rstrip('=')

def generate_code_challenge(code_verifier):
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    return base64.urlsafe_b64encode(code_challenge).decode('utf-8').rstrip('=')

def authenticate_myanimelist(client_id, client_secret, redirect_uri):
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)
    
    authorization_base_url = 'https://myanimelist.net/v1/oauth2/authorize'
    token_url = 'https://myanimelist.net/v1/oauth2/token'
    
    myanimelist = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = myanimelist.authorization_url(authorization_base_url, code_challenge=code_challenge, code_challenge_method='S256')
    
    print('Por favor, abre el siguiente URL en tu navegador y autoriza la aplicación:')
    print(authorization_url)
    
    redirect_response = input('Pega aquí la URL completa de redirección: ')
    
    token = myanimelist.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response, code_verifier=code_verifier)
    
    return token

def fetch_anime_data(token, query='naruto', limit=10):
    headers = {
        'Authorization': f'Bearer {token["access_token"]}'
    }
    response = requests.get(f'https://api.myanimelist.net/v2/anime?q={query}&limit={limit}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al acceder a la API: {response.status_code}")
        return None

def main():
    client_id = 'f009bc1ba96fb2f9e9b67f5581a3cab7'
    client_secret = 'e7e3a17e1b8d13bdb3ec7fdb45fc0bc99b2c895d5c17e76ffa67b7018dead0f3'
    redirect_uri = 'http://localhost:8000/callback'
    token = authenticate_myanimelist(client_id, client_secret, redirect_uri)
    anime_data = fetch_anime_data(token, query='naruto', limit=10)
    if anime_data:
        for anime in anime_data['data']:
            title = anime['node']['title']
            score = anime['node'].get('mean', 'No rating')
            print(f"Title: {title}, Score: {score}")

if __name__ == "__main__":
    main()