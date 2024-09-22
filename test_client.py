import requests
import jwt
import time
import sys

# URLs
AUTH_URL = 'http://127.0.0.1:8080/auth'
JWKS_URL = 'http://127.0.0.1:8080/jwks'

def get_token(expired=False):
    params = {}
    if expired:
        params['expired'] = 'true'
    response = requests.post(AUTH_URL, params=params)
    if response.status_code != 200:
        print(f"Failed to get token: {response.status_code}")
        print(response.text)
        sys.exit(1)
    return response.json()['token']

def get_jwks():
    response = requests.get(JWKS_URL)
    if response.status_code != 200:
        print(f"Failed to get JWKS: {response.status_code}")
        print(response.text)
        sys.exit(1)
    return response.json()

def decode_token(token, jwks):
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get('kid')
    public_key = None

    for key in jwks['keys']:
        if key['kid'] == kid:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
            break

    if not public_key:
        print("Public key not found for kid:", kid)
        sys.exit(1)

    try:
        decoded = jwt.decode(token, public_key, algorithms=['RS256'])
        print("Token is valid. Decoded payload:")
        print(decoded)
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError as e:
        print("Invalid token:", e)

def main():
    print("Testing /auth endpoint...")
    token = get_token()
    print("Received token:")
    print(token)

    print("\nFetching JWKS...")
    jwks = get_jwks()

    print("\nDecoding and verifying token...")
    decode_token(token, jwks)

    print("\nTesting /auth endpoint with expired=true...")
    expired_token = get_token(expired=True)
    print("Received expired token:")
    print(expired_token)

    print("\nDecoding and verifying expired token...")
    decode_token(expired_token, jwks)

if __name__ == '__main__':
    main()

