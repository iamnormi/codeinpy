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

li = int(input("Enter Your Choice:\n 1.Piped \n 2.Piped(embed) \n"))
if li==1:
	opd=piped+id
	print(opd)
	os.system("xdg-open "+opd)
else:
	opde=pipede+id
	print(opde)
	os.system("xdg-open "+opde)
