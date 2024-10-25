import os
import requests
from dotenv import load_dotenv

class RaindropAPI:
    def __init__(self):
        load_dotenv()
        self.base_url = "https://api.raindrop.io/rest/v1"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('RAINDROP_ACCESS_TOKEN')}",
            "Content-Type": "application/json"
        }

    def get_user(self):
        """Retrieve user information."""
        url = f"{self.base_url}/user"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_collections(self):
        """Retrieve all collections."""
        url = f"{self.base_url}/collections"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_raindrop(self, raindrop_id):
        """Retrieve a single raindrop by ID."""
        url = f"{self.base_url}/raindrop/{raindrop_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def create_raindrop(self, data):
        """Create a new raindrop."""
        url = f"{self.base_url}/raindrop"
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def update_raindrop(self, raindrop_id, data):
        """Update an existing raindrop."""
        url = f"{self.base_url}/raindrop/{raindrop_id}"
        response = requests.put(url, headers=self.headers, json=data)
        return response.json()

    def delete_raindrop(self, raindrop_id):
        """Delete a raindrop by ID."""
        url = f"{self.base_url}/raindrop/{raindrop_id}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code == 204

# Example usage:
# api = RaindropAPI()
# user_info = api.get_user()
# print(user_info)