import os,sys
ch=int(input("Enter the Choice: \n 1.Default link \n 2.ShareClick Link\n 3.MobileVer link \n"))

alink=sys.argv[1]
if ch==1:
	id = alink[32:]
elif ch==2:
	id = alink[17:]
else :
	id = alink[30:]
print(id)
piped = "https://piped.kavin.rocks/watch?v="
pipede= "https://piped.kavin.rocks/embed/"
ytembed="https://youtube.com/embed/"
li = int(input("Enter Your Choice:\n 1.Piped \n 2.Piped(embed) \n 3.Watch Youtube Live\n"))

match li:
    case 1:
            opd=piped+id
            print(opd)
            os.system("xdg-open "+opd)
    case 2:
	        opde=pipede+id
	        print(opde)
	        os.system("xdg-open "+opde)
    case 3:
	        ytl=ytembed+id
	        print(ytl)
	        os.system("xdg-open "+ytl)
