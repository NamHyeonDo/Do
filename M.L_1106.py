# 암호처리 입력 암호화
""" import getpass

pw = getpass.getpass ("Pass : ")
# pw = input("Pass :")
print(pw) """

# 해시알고리즘
""" import hashlib

hl = hashlib.sha256()
target = "hello"
#target = "hi"
#target = "Kan ye"
#target = "Post Malone"


hl.update(target.encode("utf-8"))
print(hl.hexdigest())

import Crypto.Hash.keccak as kek
# 모드다운 필요
target = "hello"
#target = "hi"
#target = "Kan ye"
#target = "Post Malone"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest()) """

# 입력키 변환
""" import getpass
import hashlib

pw = getpass.getpass("Pass: ")
print(pw)

h1 = hashlib.sha256()

h1.update(pw.encode("utf-8"))
print(h1.digest())
print(h1.hexdigest()) """

""" import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass : ')
        hs = hashlib.sha256()
        hs.update(pw.encode("utp-8"))
        with open ('pw.txt', 'r') as fp:
            return hs.hexdigest()==fp.read()
    else:
        return True

if pwInsert():
    pw = input('new pass : ')
    with open ('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utp-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password") """


# 시스템 정보 확인
""" import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps) """

# 웹페이지 읽기
""" import urllib.request as ur

# url = 'https://www.google.com'
# url = 'https://daum.net'
url = 'https://xkcd.com/'

res = ur.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
print(web) """

""" import http.client as hc

url = 'https://www.google.com'
# url = 'https://daum.net'
# url = 'https://xkcd.com/'

conn = hc.HTTPSConnection(url)
conn.request("GET", "/") # 서브 url 넣어 가져올 수 있다

r = conn.getresponse()

with open("ulcl.html", "wb") as fp:
    fp.write(r.read())
    
conn.close()

print(r) """

""" import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)

print(web) """

# 싱글스레드
""" import time
def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
start = time.time()
for i in range(3) :
    counter(f"num{i}")
end = time.time()

print("single end", end - start) """

# 멀티스레드
""" import time
import threading as td

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

        
thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

start = time.time() 
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print("multi end", end - start) """

# 병렬처리
import time
import multiprocessing as mp

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
process1 = mp.Process(target=counter, args=("1num",))
process2 = mp.Process(target=counter, args=("2num",))
process3 = mp.Process(target=counter, args=("3num",))

start = time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time()

print("proc-end", end - start)