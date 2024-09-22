Welcome to Your JWKS Server Project! 🎉

Hey there! 👋

Thank you for choosing to dive into this JWKS (JSON Web Key Set) server project. Whether you're building this for learning purposes, adding it to your portfolio, or integrating it into a larger application, we're here to make the journey smooth and enjoyable.

What's This All About? 🤔

This project is a simple JWKS server built with Python and Flask. It generates RSA key pairs, serves public keys in JWKS format, and provides an endpoint to issue JWTs (JSON Web Tokens). Here's what you can expect:

Dynamic Key Generation: Creates RSA key pairs with unique Key IDs (kid) and expiration times.
JWKS Endpoint: Serves up-to-date public keys at /jwks.
Auth Endpoint: Issues JWTs signed with active or expired keys at /auth.
Automatic Key Expiry Handling: Moves expired keys to a separate store automatically.
Thread-Safe Operations: Ensures smooth performance even when handling multiple requests.
Before You Start 🛠

Prerequisites
Python 3.7 or higher (Python 3.10 recommended)
pip (Python package manager)
Virtual Environment (Optional but highly recommended)
Let's Get Set Up! 🚀

1. Clone the Repository
First things first, let's get the code on your machine.

bash
Copy code
git clone https://github.com/sritan02/CSCE-3550-PROJECT1.gitq
cd jwks-server
2. Set Up a Virtual Environment (Optional but Recommended)
This keeps your project dependencies isolated.

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install the Required Packages
Let's install everything we need.

bash
Copy code
pip install -r requirements.txt
Project Overview 🗂

Here's a quick rundown of what you'll find in the project:

app.py: The main Flask application.
key_manager.py: Handles key generation and management.
test_client.py: A script to test the server.
test_app.py: Unit tests to ensure everything works as expected.
requirements.txt: A list of all Python packages you'll need.
README.md: That's this file! 😊
How to Use This Project 🎈

Running the Server
Activate the Virtual Environment
bash
Copy code
source venv/bin/activate
Start the Server
bash
Copy code
python app.py
You should see something like:

vbnet
Copy code
 * Serving Flask app 'app'
 * Debug mode: off
 WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
Interacting with the Server
1. Get the JWKS (Public Keys)

Endpoint: /jwks
Method: GET
Try it out:

bash
Copy code
curl http://127.0.0.1:8080/jwks
You should get a JSON response with the public keys.

2. Get a JWT Token

Endpoint: /auth
Method: POST
Get a Valid Token:

bash
Copy code
curl -X POST http://127.0.0.1:8080/auth
Get an Expired Token:

bash
Copy code
curl -X POST "http://127.0.0.1:8080/auth?expired=true"
Testing 🧪

Running Unit Tests
We've included some unit tests to make sure everything is working properly.

Run the Tests:

bash
Copy code
pytest --cov=.
What to Expect:

The tests will check key generation, token issuance, and the endpoints.
You should see a coverage report at the end.
Using the Test Client
We've also provided a test_client.py script to perform blackbox testing.

Run the Test Client:

bash
Copy code
python test_client.py
What It Does:

Requests tokens from the /auth endpoint.
Fetches the JWKS from /jwks.
Verifies the tokens using the public keys.
Keeping Your Code Clean 🧹

Linting and Formatting
It's always a good idea to keep your code neat and tidy!

Install flake8 and black:

bash
Copy code
pip install flake8 black
Run Linting:

bash
Copy code
flake8 .
Auto-Format Your Code:

bash
Copy code
black .
Contributing 🤝

We welcome contributions! If you have ideas to improve this project, feel free to fork the repository and submit a pull request.

Steps to Contribute:

Fork the Repo
Create a Branch
bash
Copy code
git checkout -b feature/awesome-feature
Commit Your Changes
bash
Copy code
git commit -m "Add some awesome feature"
Push to Your Branch
bash
Copy code
git push origin feature/awesome-feature
Open a Pull Request
A Few Final Notes 📝

Security Reminder: This project is for educational purposes. In a production environment, make sure to implement proper authentication and security measures.
Python Version: While it may run on Python 3.12, we recommend using Python 3.10 or 3.11 to avoid any potential compatibility issues.
Having Trouble?: If you run into any issues, feel free to open an issue on GitHub or reach out.
