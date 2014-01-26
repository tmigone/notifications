import httplib, urllib

def sendNotification(message):
	conn = httplib.HTTPSConnection("api.pushover.net:443")

	conn.request("POST", "/1/messages.json",
             urllib.urlencode({
                              "token": "adn3bgkZG1ywNi8YmWcFREjqPsov9a",
                              "user": "u8q5UGNSFJoKpJaX7XyaNYHzpoAKzG",
                              "message": message,
                              }), { "Content-type": "application/x-www-form-urlencoded" })

	conn.getresponse()