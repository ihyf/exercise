# coding:utf-8
import requests
from lxml import html

# 模拟github登录
LOGIN_URL = "https://github.com/login"
SESSION_URL = "https://github.com/session"

s = requests.session()
r = s.get(LOGIN_URL)
tree = html.fromstring(r.text)
el = tree.xpath('//input[@name="authenticity_token"]')[0]
authenticity_token = el.attrib['value']
data = {}
data.setdefault('commit', 'Sign in')
data.setdefault('utf-8', '✓')
data.setdefault('authenticity_token', authenticity_token)
data.setdefault('login', '565267598@qq.com')
data.setdefault('password', 'password')
s.post(SESSION_URL, data=data)
el = tree.xpath('//ul[@id="repo_listing"]')
print el
