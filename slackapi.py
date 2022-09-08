import requests

url = "https://hooks.slack.com/services/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"

payload = '''{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Farmhouse Thai Cuisine*\n:star::star::star::star: 1528 reviews\n They do have some vegan options, like the roti and curry, plus they have a ton of salad stuff and noodles can be ordered without meat!! They have something for everyone here"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/c7ed05m9lC2EmA3Aruue7A/o.jpg",
				"alt_text": "alt text for image"
			}
		}
	]
}'''
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
