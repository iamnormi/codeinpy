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
ytembed="https://youtube.com/embed/"
ytl=ytembed+id
print(ytl)
os.system("xdg-open "+ytl)
