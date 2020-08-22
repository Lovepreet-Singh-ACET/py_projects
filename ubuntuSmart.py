import os
import pyttsx3
print("_____________________________________________________________________________________________________________________________________")
print("__________________________________________________________ Smart UBUNTU Assistent ___________________________________________________")
print("Welcome Sir")
print("-----------")
pyttsx3.speak("Welcome Sir")
pyttsx3.speak("What do you want me to do Sir")
print()
while True:
	print("What do you want me to do Sir : "  , end='')
	p = input()
	p = p.lower()

	if (("run" in p) or ("execute" in p ) or ("launch") or ("open" in p)) and ("firefox" in p) or ("browser" in p):
	  os.system("firefox")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and  ("gedit" in p) or ("editor" in p):
	  os.system("gedit")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("liberoffice" in p) and ("writer" in p):
	  os.system("libreoffice --writer")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("liberoffice" in p) and ("calc" in p):
	  os.system("libreoffice --calc")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("liberoffice" in p) and ("draw" in p) or ("paint" in p):
	  os.system("libreoffice --draw")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("liberoffice" in p) and ("impress" in p):
	  os.system("libreoffice --impress")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("thunderbird" in p):
	  os.system("thunderbird")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("file" in p) and ("manager" in p) or ("explorer" in p):
	  os.system("nautilus")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("vlc" in p) or ("media player" in p):
	  os.system("vlc")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("vs code" in p) or ("visual studio code" in p):
	  os.system("code")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("calculator" in p) or ("calc" in p):
	  os.system("gnome-calculator")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("discord" in p):
	  os.system("discord")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("camara" in p):
	  os.system("cheese")

	elif (("run" in p) or  ("execute" in p ) or ("launch" in p) or ("open" in p)) and ("spotify" in p) or ("music" in p):
	  os.system("spotify")

	elif  ("exit" in p)  or ("quit" in p):
	  pyttsx3.speak("Wish to see you soon sir")
	  print("Wish to see you soon sir")
	  break

	else:
	  print("application not supported")
	  pyttsx3.speak("application not supported")


