# Raindrop.io Python API Client & Recently Bookmarked Script

This project provides a simple Python wrapper for interacting with the Raindrop.io API. It allows you to manage your bookmarks, collections, and more through a set of convenient methods. Also included is a script that will download the most recent bookmarks and save it as a json file.

## Features

- Retrieve user information
- Manage collections
- Create, update, and delete raindrops
- Fetch recent raindrops with customizable limits

## Getting Started

### Prerequisites

To use this project, you need to have Python installed on your system. Additionally, you'll need to install the following Python packages:

- `json`
- `requests`

You can install these packages using pip:
```python
pip install requests json
or
python3 -m pip install requests json
```
**recommended**or you can use the requirements.txt file to install them:
```python
python3 -m pip install -r requirements.txt
```
It's also recommended to use a virtual environment to run this and any other python project but you already knew that.

### You will need either a raindrop.io access or testing token to use the API.
To get your own access or testing token you need to login to your Raindrop.io account and go to [https://app.raindrop.io/settings/integrations](https://app.raindrop.io/settings/integrations) and create a new application under "For Developers." Fill that all out and make sure to save the client id and client secret. You won't need those for this library UNLESS you plan on integrating this into your own project that would let users access their own data. If you just want to fool around with your own bookmarks and collections then you can use the testing token. The main access token that you get with your client secret/id resets every two weeks requiring you to re-auth whereas the testing token does not.

To get the testing token go back to the integrations page, click on your application then click on "Generate Testing Token" and there you go. 

You can get more instructions on how to integrate the API into your own project on their API page, it also includes information on how to turn your client id/client secret into an access token via OAuth2. Find that here: [https://developer.raindrop.io/](https://developer.raindrop.io/)

### The .env file
Copy the example.env file to .env in your main directory.
```bash
cp example.env .env
```
Then replace the placeholder text with your access token or testing token.
```
ACCESS_TOKEN="PUT YOUR RAINDROP ACCESS TOKEN HERE"
```

## Using RaindropAPI:
Use raindrop_api.py in your own projects by importing RaindropAPI at the top of your python file:
```python
from raindrop_api import RaindropAPI
```

Included is a script that will fetch the most recently added bookmarks and save them as a json file in the current working directory. The default is the last 25 however you can change that by calling it with the -l or --limit flag. Example if you wanted to call 30 of your most recent bookmarks:
```
python3 get_recent_raindrops.py -l 30
```

### Notes and rdl.ink/render images:
The output of the get_recent_raindrops script parses out 90% of the usual data returned from the main API that I didn't need for my project (which was just listing the most recent items I had bookmarked) so I just kept creationdate, cover, title, link, tags and excerpt. You can modify the script to keep more or less information at your discretion. Just an fyi, there are a good number of bookmarks that use Raindrop.io's own web clipper for the image, those all start with the url: https://rdl.ink/render/ 
They're all just a screenshot of the top half of the webpage saved as a 1200 X 800 .webp image. Some of the item fields from the API include additional tags that sometimes included images from the original source but that's not always the case. I have another script that reverts all the images to my own CDN but I didn't include it in this repo because it was out of scope. Once again, you've been warned.


## Contributing

Pull requests are welcome. Heck even just download it as a .zip using a vpn connected to 12 different proxies funneled through tor. Just let me know if you make something useful out of it.

I threw this together pretty quickly so that it'd work with another project I'm working on so this went through one single round of testing. That was a "is it working without warnings/errors" test. Maybe I'll come back to it later and fix it up a bit but until then you're on your own.

## License

[MIT](https://choosealicense.com/licenses/mit/)