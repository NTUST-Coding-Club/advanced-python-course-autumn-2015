import requests


post_data = {
    'author': "Inndy's Bot",
    'message': 'This is a bot post.' * 2
}

ret = requests.post('http://inndy.me:8090/post', data=post_data)
print('This is a' in ret.text)
