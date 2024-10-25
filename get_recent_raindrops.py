from raindrop_api import RaindropAPI
import requests
import json
import argparse
# You can change the number of results it will pull with -l or --limit - Default is 25

def get_recent_raindrops(api, limit=25):
    """Fetch the most recent raindrops."""
    url = f"{api.base_url}/raindrops/0?perpage={limit}&sort=-created"
    response = requests.get(url, headers=api.headers)
    return response.json()

def filter_raindrops(raindrops):
    """Filter the raindrops to only include specific fields."""
    filtered = []
    for item in raindrops['items']:
        filtered.append({
            'link': item.get('link'),
            'title': item.get('title'),
            'excerpt': item.get('excerpt'),
            'cover': item.get('cover'),
            'tags': item.get('tags'),
            'created': item.get('created')
        })
    return filtered

def main():
    parser = argparse.ArgumentParser(description='Fetch and filter recent raindrops.')
    parser.add_argument('-l', '--limit', type=int, default=25, help='Number of recent raindrops to fetch')
    args = parser.parse_args()
    
    # Initialize the RaindropAPI
    api = RaindropAPI()
    
    # Get the most recent raindrops
    recent_raindrops = get_recent_raindrops(api, limit=args.limit)
    
    # Filter the raindrops
    filtered_raindrops = filter_raindrops(recent_raindrops)
    
    # Print the filtered raindrops in JSON format
    print(json.dumps(filtered_raindrops, indent=4))
    
    # Save the filtered raindrops to a file in JSON format
    with open('recentraindrops.json', 'w') as file:
        json.dump(filtered_raindrops, file, indent=4)

if __name__ == "__main__":
    main()

