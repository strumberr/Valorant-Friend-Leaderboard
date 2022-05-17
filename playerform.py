import requests

def send_simple_message(username, tag):
	return requests.post(
		API,
		auth=("api", API),
		data={"from": "Valorant Leaderboard EMAIL",
			"to": "storm b EMAIL",
			"subject": username + " wants to be put on the valorant leaderboard",
			"text": f"Username and tag: {username}/{tag}"})
