
import time
url_list = {"login": "www.xxx.com/login/rand_{:13.0f}".format(time.time() * 1000),
            "visit":"www.xxx.com/visit/rand_{:13.0f}".format(time.time() * 1000)}

print(url_list)

print(time.time())
print(url_list['login'].split('_'))


h = 'hello girl!'
print(h.title())
print(h.swapcase())

