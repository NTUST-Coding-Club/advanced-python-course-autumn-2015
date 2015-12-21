import requests

ret = requests.get('http://inndy.me:8090').text
for i in ret.split('<div class="post">')[1:]:
    i = i.split('<span class="field">作者</span>')[1]
    i = i.split('</p>')
    author = i[0].strip()
    msg = i[1].split('<span class="field">訊息</span>')[1].strip()
    print('author: %s, msg: %s' % (author, msg))
