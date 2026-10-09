import os
import sys
import time
from dotenv import load_dotenv
from colorama import Style, Fore, Back
import pyperclip
import random

if getattr(sys, "frozen", False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))
 
env_path = os.path.join(base_dir, ".env")
if not os.path.exists(env_path):
    print(f"Could not find the .env file. Put it in the same folder as this program:\n{base_dir}")
    input("\nPress enter to exit.")
    sys.exit(1)
    
    
load_dotenv()

key=os.getenv("KEY")
salt=os.getenv("SALT")
chars=key+salt

keylist=key.split(",")
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,n1,n2,n3,n4,n5,n6,n7,n8,n9,n0,space=keylist
saltlist=salt.split(",")
charlist=keylist+saltlist

english="abcdefghijklmnopqrstuvwxyz1234567890"



def banner(clear=True, animation=False):
    if clear:
        os.system("cls" if os.name=="nt" else "clear")
    # ASCII ART Picked from internet, and edited through AI.
    text = [
    "⛥ . · •  🕸️ ☠️  . ·  • ⛧  . · • ⚰️   · • .  🪦  · • . 🕷️  • · .  🩸 ⛥",
    " / ╳ \\  / \\ /  / ╳ \\  / \\ /  / ╳ \\  / \\ /  / ╳ \\  / \\ /  / ╳ \\  / \\ / ",
    "_/_/_/_//_/_/_//_/_/_//_/_/_//_/_/_//_/_/_//_/_/_//_/_/_//_/_/_//_/_/_/_",
    " 🜏  .   ·      .     •      .   ☠️    ·      •      .    ☥    .   ·  🜚",
    " ▄████▄   █████▄   ████▄  ███▄  ██  ▄██▀  ████▄  ██▄  ██  ██ ███████ ███████ ██████▄ ",
    "██▀        ██  ██ ██  ██ ██  ██ ██▄██▀   ██  ██ ███▄ ██  ██     ▄█▀  ██      ██  ██ ",
    " ▀████▄    █████▀ ██  ██ ██  ██ ████▄    ██████ ██▀████  ██   ▄█▀    █████   ██████▀ ",
    "      ██   ██     ██  ██ ██  ██ ██ ▀██▄  ██  ██ ██  ▀██  ██ ▄█▀      ██      ██  ▀█▄ ",
    "▀██████▀  ▄██▄    ▀████▀  ▀███▀ ██  ▄██▄  ▄██  ▄██▄ ▄██ ▄██ ▄███████ ███████ ▄██   ▄██▄",
    ""
    "      S      P      O      O      K      A      N      I      Z      E      R",
    " .       ·      .      •     .  💀      ·      •      .   🜲    .   ·  ",
    "________________________________________________________________________",
    "  \\ ╳ /  \\ / \\  \\ ╳ /  \\ / \\  \\ ╳ /  \\ / \\  \\ ╳ /  \\ / \\  \\ ╳ /  \\ / \\ ",
    " ⛧ . · •  🦇  . ·  • ⛥  . · • 🕯️   · • .  👁️  · • . 🔮  • · .  🖤 ☥"
]

    colors=[Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN]
    
    
    for i in text:
        print(f"{random.choice(colors)}{Style.BRIGHT}{i}")
        if animation==True:
            time.sleep(0.05)


def encode(text):
    convertedstring=""
    
    if os.getenv("salting").lower()=="true":
        saltstrength=6-int(os.getenv("saltstrength"))
        saltlength=os.getenv("salt-length")
        rnd1=random.randint(0,saltstrength) #To do salting or not
        if rnd1==0:
            #Yup, we are doing salting for this char
            rnd2=random.randint(1,int(saltlength)) #Number of salt additions to do
            saltchr=random.choices(saltlist,k=int(rnd2))
            for chr in saltchr:
                convertedstring+=chr


    for chr2 in text:
        if chr2.lower()=="a":
            convertedstring+=str(a)
            
        elif chr2.lower()=="b":
            convertedstring+=str(b)

        elif chr2.lower()=="c":
            convertedstring+=str(c)

        elif chr2.lower()=="d":
            convertedstring+=str(d)

        elif chr2.lower()=="e":
            convertedstring+=str(e)

        elif chr2.lower()=="f":
            convertedstring+=str(f)

        elif chr2.lower()=="g":
            convertedstring+=str(g)

        elif chr2.lower()=="h":
            convertedstring+=str(h)

        elif chr2.lower()=="i":
            convertedstring+=str(i)

        elif chr2.lower()=="j":
            convertedstring+=str(j)

        elif chr2.lower()=="k":
            convertedstring+=str(k)

        elif chr2.lower()=="l":
            convertedstring+=str(l)

        elif chr2.lower()=="m":
            convertedstring+=str(m)

        elif chr2.lower()=="n":
            convertedstring+=str(n)

        elif chr2.lower()=="o":
            convertedstring+=str(o)

        elif chr2.lower()=="p":
            convertedstring+=str(p)

        elif chr2.lower()=="q":
            convertedstring+=str(q)

        elif chr2.lower()=="r":
            convertedstring+=str(r)

        elif chr2.lower()=="s":
            convertedstring+=str(s)

        elif chr2.lower()=="t":
            convertedstring+=str(t)

        elif chr2.lower()=="u":
            convertedstring+=str(u)

        elif chr2.lower()=="v":
            convertedstring+=str(v)

        elif chr2.lower()=="w":
            convertedstring+=str(w)

        elif chr2.lower()=="x":
            convertedstring+=str(x)

        elif chr2.lower()=="y":
            convertedstring+=str(y)
            
        elif chr2.lower()=="z":
            convertedstring+=str(z)

        elif chr2.lower()=="1":
            convertedstring+=str(n1)

        elif chr2.lower()=="2":
            convertedstring+=str(n2)

        elif chr2.lower()=="3":
            convertedstring+=str(n3)

        elif chr2.lower()=="4":
            convertedstring+=str(n4)

        elif chr2.lower()=="5":
            convertedstring+=str(n5)

        elif chr2.lower()=="6":
            convertedstring+=str(n6)

        elif chr2.lower()=="7":
            convertedstring+=str(n7)

        elif chr2.lower()=="8":
            convertedstring+=str(n8)

        elif chr2.lower()=="9":
            convertedstring+=str(n9)

        elif chr2.lower()=="0":
            convertedstring+=str(n0)

        elif chr2.lower()==" ":
            convertedstring+=str(space)
        else:
            convertedstring+=chr2
            
            
        if os.getenv("salting").lower()=="true":
            saltstrength=6-int(os.getenv("saltstrength"))
            saltlength=os.getenv("salt-length")
            rnd1=random.randint(0,saltstrength) #Probability to salt
            if rnd1==0:
                #Yup, we are doing salting for this char
                rnd2=random.randint(1,int(saltlength)) #Number of salt additions to do
                saltchr=random.choices(saltlist,k=int(rnd2))
                for chr in saltchr:
                    convertedstring+=chr
                    
    return convertedstring
            
        

def decode(text):
    decodedlist=""
    unsalted_list=[]
    for i1 in text:
        if i1 not in saltlist:
            unsalted_list.append(i1)
    
    for chr1 in unsalted_list:
        
        if chr1 == a:
            decodedlist+="a"
        elif chr1 == b:
            decodedlist+="b"
        elif chr1 == c:
            decodedlist+="c"
        elif chr1 == d:
            decodedlist+="d"
        elif chr1 == e:
            decodedlist+="e"
        elif chr1 == f:
            decodedlist+="f"
        elif chr1 == g:
            decodedlist+="g"
        elif chr1 == h:
            decodedlist+="h"
        elif chr1 == i:
            decodedlist+="i"
        elif chr1 == j:
            decodedlist+="j"
        elif chr1 == k:
            decodedlist+="k"
        elif chr1 == l:
            decodedlist+="l"
        elif chr1 == m:
            decodedlist+="m"
        elif chr1 == n:
            decodedlist+="n"
        elif chr1 == o:
            decodedlist+="o"
        elif chr1 == p:
            decodedlist+="p"
        elif chr1 == q:
            decodedlist+="q"
        elif chr1 == r:
            decodedlist+="r"
        elif chr1 == s:
            decodedlist+="s"
        elif chr1 == t:
            decodedlist+="t"
        elif chr1 == u:
            decodedlist+="u"
        elif chr1 == v:
            decodedlist+="v"
        elif chr1 == w:
            decodedlist+="w"
        elif chr1 == x:
            decodedlist+="x"
        elif chr1 == y:
            decodedlist+="y"
        elif chr1 == z:
            decodedlist+="z"
        elif chr1 == n1:
            decodedlist+="1"
        elif chr1 == n2:
            decodedlist+="2"
        elif chr1 == n3:
            decodedlist+="3"
        elif chr1 == n4:
            decodedlist+="4"
        elif chr1 == n5:
            decodedlist+="5"
        elif chr1 == n6:
            decodedlist+="6"
        elif chr1 == n7:
            decodedlist+="7"
        elif chr1 == n8:
            decodedlist+="8"
        elif chr1 == n9:
            decodedlist+="9"
        elif chr1 == n0:
            decodedlist+="0"
        elif chr1 == space:
            decodedlist+=" "
    return decodedlist


def home():
    front=""
    back=""
    welcomechar=random.sample(charlist,12)
    for chr in welcomechar[0:6]:
        front+=chr+" "
    for chr in welcomechar[6:12]:
        back+=" "+chr
    banner(clear=True, animation=True)
    print(f"\n\n{Style.RESET_ALL}"+front+ f"{Fore.BLACK}{Style.BRIGHT}{Back.LIGHTCYAN_EX}  Welcome to Spookanizer! I convert your language to spooktext and back!  {Style.RESET_ALL}"+back)


    inp=input(f"\n{Style.BRIGHT}--::>")
    iseng=True

    for i in inp:
        if i not in english and i in charlist:
            iseng=False
            break

    if iseng:
        banner()
        print(f"\n\n{Fore.BLUE}{Style.BRIGHT}--::> {inp}\n")
        print(f"{Fore.GREEN}{Style.BRIGHT}Detected Language {Style.RESET_ALL}: {Fore.YELLOW}{Style.BRIGHT}HumanText\n{Style.RESET_ALL}{Style.DIM}Converting to Spooktext...{Style.RESET_ALL}")
        time.sleep(0.2)
        output=encode(inp)
        if len(output)>64:
            ans=output[:64]
        else:
            ans=output
        nc=0
        while nc<=5:
            rn= random.sample(charlist,nc)
            prnt=""
            for ltr in rn:
                prnt+=ltr
            print(f"\r{Fore.CYAN}{Style.BRIGHT}{Back.RED}{prnt}{Style.RESET_ALL}",end="")
            nc+=1
            time.sleep(0.1)
        done=""
        for chr in ans:
            done+=chr
            rn= random.sample(charlist,nc)
            prnt=""
            for ltr in rn:
                prnt+=ltr
            print(f"\r{Fore.GREEN}{Style.BRIGHT}{done}{Fore.CYAN}{Style.BRIGHT}{Back.RED}{prnt}{Style.RESET_ALL}",end="")
            
            time.sleep(0.1)
        
        nc=5
        while nc>=0:
            rn= random.sample(charlist,nc)
            prnt=""
            for ltr in rn:
                prnt+=ltr
            print(f"\r{Fore.GREEN}{Style.BRIGHT}{done}{Fore.CYAN}{Style.BRIGHT}{prnt}{Style.RESET_ALL}     ",end="")
            nc-=1
            time.sleep(0.1)
        banner(animation=False)
        pyperclip.copy(output)
        print(f"\n\n\r{Fore.GREEN}{Style.BRIGHT}{output}",end="")
        input("\n\nPress enter to return to homepage. Text has been copied to clipboard.")
        return
    else:
        banner()
        print(f"\n\n{Fore.BLUE}{Style.BRIGHT}--::> {inp}\n")
        print(f"{Fore.GREEN}{Style.BRIGHT}Detected Language {Style.RESET_ALL}: {Fore.RED}{Style.BRIGHT}Spooktext\n{Style.RESET_ALL}{Style.DIM}Converting to HumanText...{Style.RESET_ALL}")
        time.sleep(0.2)
        output=decode(inp)
        if len(output)>64:
            ans=output[:64]
        else:
            ans=output
        letterlist=[]
        for ltr in english:
            letterlist.append(ltr)
        nc=0
        while nc<=5:
            rn= random.sample(letterlist,nc)
            prnt=""
            for ltr in rn:
                prnt+=ltr
            print(f"\r{Fore.CYAN}{Style.BRIGHT}{Back.RED}{prnt}{Style.RESET_ALL}",end="")
            nc+=1
            time.sleep(0.1)
        done=""
        for chr in ans:
            done+=chr
            rn= random.sample(letterlist,nc)
            prnt=""
            for ltr in rn:
                prnt+=ltr
            print(f"\r{Fore.GREEN}{Style.BRIGHT}{done}{Fore.CYAN}{Style.BRIGHT}{Back.RED}{prnt}{Style.RESET_ALL}",end="")
            
            time.sleep(0.1)
        
        nc=5
        while nc>=0:
            rn= random.sample(letterlist,nc)
            prnt=""
            for ltr in rn:
                prnt+=ltr
            print(f"\r{Fore.GREEN}{Style.BRIGHT}{done}{Fore.CYAN}{Style.BRIGHT}{prnt}{Style.RESET_ALL}     ",end="")
            nc-=1
            time.sleep(0.1)
        banner(animation=False)
        pyperclip.copy(output)
        print(f"\n\n\r{Fore.GREEN}{Style.BRIGHT}{output}",end="")
        input("\n\nPress enter to return to homepage. Text has been copied to clipboard.")
        return

        
if __name__=="__main__":
    while True:

        home()