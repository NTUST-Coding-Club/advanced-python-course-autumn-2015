import requests
import bs4

ret = requests.get('http://inndy.me:8090').text
document = bs4.BeautifulSoup(ret, 'html5lib')

for post in document.select('div.post'):  # '.post'
    # print(post.text.split(maxsplit=3))
    for field in post.select('span.field'):  # 'span' or '.field'
        field.decompose()
    # print(post.text.split(maxsplit=1))
    p = post.select('p')
    author = p[0].text.strip()
    msg = p[1].text.strip()
    print('author: %s, msg: %s' % (author, msg))
