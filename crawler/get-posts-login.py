import requests
import bs4

# reqeusts.Session() 會建立一個能夠保存 cookie 的 requests 物件
keey_my_cookie = requests.Session()

post_data = {
    'account': 'admin',
    'password': '12345'
}
keey_my_cookie.post('http://inndy.me/gb/', data=post_data)
ret = keey_my_cookie.get('http://inndy.me/gb/').text
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
