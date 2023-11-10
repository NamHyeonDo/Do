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
""" import time
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

print("proc-end", end - start) """

# 비동기 처리

""" import asyncio
import random as rd
import time

async def tester (name):
    snum = rd.randint(10, 20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
    print(f"end of {name}")
    
async def main():
    task1 = asyncio.create_task(tester("1test"))
    task2 = asyncio.create_task(tester("2test"))
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time() 
    print("end", end - start)
    
if __name__  == '__main__':
    asyncio.run(main()) """
    
# 랜덤 없이 숫자를 넣어준것도 있다 비도기 방식의 선언 asyncio에서 지정

#스케쥴
""" import time
import sched

start = time.time()

def tester(name):
    print(f"start-time{time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
    print(f"end of {name}")

def run():  
    s = sched.scheduler()
    s.enter(5, 1, tester('1num',))
    s.enter(3, 1, tester('2num',))
    s.enter(7, 1, tester('3num',))
    s.run()
    
if __name__ == "__main__" :
    run()
    #main()
    print("end") """
    
# 문자열 비교
""" import diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d) """

# 테스트용 데이터 생성 
""" from faker import Faker as fk
temp = fk()
print(temp.name())

with open ("fktemp.csv", "w", newline='') as f:
    for i in range(30):
    f.write(temp.name() + "," +
        temp.address() + "," +   
        temp.postcode() + "," +   
        temp.country() + "," +   
        temp.company() + "," +   
        temp.job() + "," +   
        temp.- phone_number() + "," +   
        temp.email() + "," +   
        temp.user_name() + "," +   
        temp.ipv4_private() + "," +   
        temp.catch_phrase() + "," +   
        temp.color_name() + "\n") """
        
# 시스템명령어 사용
""" import subprocess as sp
#res = sp.run(["cmd", "/c", "dir"], capture_output=True)
#res = sp.run(["cmd", "/c", "dir"], capture_output=False)
#res = sp.run(["cmd", "/c", "ipconfig", "all"], capture_output=True)
res = sp.run(["cmd", "/c", "ipconfig", "all"], capture_output=False)
print(res) """

#에러처리
import traceback as tb

def taster():
    #return 1/0
    return 1

def caller():
    taster()
    
def main():
    try:
        caller()
        
    #except ZeroDivisionError:
        #print("zde error")
        
    except ValueError:
        print("ve error")
    except Exception as ex:
        print("ex error")
    else :
        print("ok")
    finally:
        print("end")
        
main()