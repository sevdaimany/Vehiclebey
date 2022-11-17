import requests
from config import email_config


API_KEY_EMAIL = email_config['API_KEY']
DOMAIN  = email_config["DOMAIN"]
email = "imanysevda@gmail.com"
def send_message(subject, text):
    	return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", API_KEY_EMAIL),
		data={"from": f"<mailgun@{DOMAIN}>",
			"to": [email],
			"subject": subject,
			"text": text})
     
		
	