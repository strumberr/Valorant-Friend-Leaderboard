from flask import Flask
from flask import Flask, render_template, request # Import Flask Class
import requests
import json
import time
import multiprocessing
import random
from playerform import send_simple_message

app = Flask('')

region="eu"
api_url = "https://api.henrikdev.xyz/valorant/v1"

@app.route('/leaderboard/', methods=["GET", "POST"])
def leaderboard():

	list1 = []
	list2 = []
	
	with open("usernames.txt") as file_in:
		for line in file_in:
				list2.append(line)

	print(list2)

	leaderboard_list = ["ａｓｈｅ/240hz", "jaredthejelly/69420", "Oskarito/4737", "Linike/EUW", "crmsn/1064", "Emvipi/lmao", "9comme/EUW"]
	
	for el in list2:

		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		headers1 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8.210.83.33 Safari/537.36'}
		headers2 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.48.119.28 Safari/537.36'}
		headers3 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/169.57.1.85 Safari/537.36'}
		headers4 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/216.137.184.253 Safari/537.36'}
		headers5 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/185.187.29.140 Safari/537.36'}
		headers6 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.199.97.42 Safari/537.36'}
		headers7 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/186.67.230.45 Safari/537.36'}
		headers8 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/219.94.129.37 Safari/537.36'}
		headers9 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/190.189.188.174 Safari/537.36'}
		
		rand_header = random.choice([headers, headers1, headers2, headers3, headers4, headers5, headers6, headers7, headers8, headers9])

		#get the player level
		url_level = f"https://api.henrikdev.xyz/valorant/v1/account/{el}"
		account_info_level = requests.get(url_level, headers=rand_header).json()
		
		player_level = account_info_level["data"]["account_level"]
		last_update = account_info_level["data"]["last_update"]
		level = player_level

		url_rank = f"https://api.henrikdev.xyz/valorant/v2/mmr/eu/{el}"
		account_info_rank = requests.get(url_rank, headers=headers).json()
		player_rank = account_info_rank["data"]["current_data"]["currenttierpatched"]
		player_wins_c_season = account_info_rank["data"]["by_season"]["e4a3"]["wins"]
		rank = player_rank

		url_last_played = f"https://api.henrikdev.xyz/valorant/v1/mmr-history/{region}/{el}"
		account_info_last_played = requests.get(url_last_played, headers=headers).json()
		player_last_played = account_info_last_played["data"][0]["date"]
		last_played = SyntaxError(player_last_played)

		el_1 = f"{el}.{level}.{rank}.{last_played} GMT+2. {player_wins_c_season}"
		el_2 = el_1.replace("/", "#")
		el_3 = el_2.replace(".", '&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;')

		list1.sort()
		list1.append(el_3)

	return render_template("index.html", level=level, rank=rank, last_played=last_played, list1=list1)


@app.route('/', methods=["GET", "POST"])
def home():
	return render_template("home.html")

@app.route('/playerform', methods=["GET", "POST"])
def contact_form():
	if request.method == "POST":
		username = request.form.get("username")
		print(username)
		if username == "" or username == None:
			return render_template("playerform.html")

		f = open("usernames.txt", "a")
		usernames2 = str(username)

		tag = request.form.get("tag")

		send_simple_message(usernames2, tag)
		
		return render_template("home.html")

	return render_template("playerform.html")

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5550, debug=True, threaded=True)

#https://api.henrikdev.xyz/valorant/v1/account/jaredthejelly/69420
#https://api.henrikdev.xyz/valorant/v1/account/jaredthejelly/69420
#https://api.henrikdev.xyz/valorant/v2/mmr/eu/jaredthejelly/69420
#https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/jaredthejelly/69420
#Iron.Bronze.Silver.Gold.Platinum.Diamond.Immortal.Radiant