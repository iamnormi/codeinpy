import os,sys
ch=int(input("Enter the Choice: \n 1.Default link \n 2.ShareClick Link\n  "))
alink=sys.argv[1]
if ch==1:
	id = alink[32:]
else:
	id = alink[17:]

link = "https://www.youtube-nocookie.com/embed/"
embedlink = link+id
piped = "https://piped.kavin.rocks/watch?v="
pipedlink = piped+id
print(embedlink)
ch=int(input("Enter Your Choice Of Client: \n 1.Brave Browser \n 2.freetube\n 3.piped\n 4.motionbox  "))
if ch == 1:
	os.system("brave-browser "+embedlink)
elif ch == 2:
	os.system("freetube "+embedlink)
elif ch == 3:
	os.system("brave-browser "+pipedlinnk)
else:
	os.system("motionbox "+embedlink)
