# hiddenimports=['tkinter', 'json', 'uuid', 'subprocess', 'threading','time']

from tkinter import *
from tkinter import filedialog

import json
import uuid
import subprocess as sp

from threading import Thread
import time

uid = ''
def save(uname='noname', cpath='', jpath='', maxmb=1600):
	global lst
	global uid
	if uid == '': uid = str(uuid.uuid1()).replace('-','')

	lst = {
		"username" :    uname,
		"clentpath" :   cpath,
		"javapath" :    jpath,
		"maxmb" :       maxmb,
		"uuid" :        uid,
		"accessToken" : uid,
		"scobe" :       r'{}'
	}

	try:
		file = open(config, 'w')
		file.write(json.dumps(lst))
	except Exception as e:
		print('error of dumps')
	finally:
		file.close()

# открыть джисон файл
lst = {}
config = "PyConfig.json"
try:
	file = open(config, 'r')
	lst = json.loads(''.join([line for line in file])) # взять как славарь
	file.close()
except Exception as e:
	save()
	

# начать рисовать на окно
root = Tk()

width  = 590 # размер окна
height = 280

x = int(root.winfo_screenwidth()//2  - width/2) # середина экрана
y = int(root.winfo_screenheight()//2 - height/2)

root.title("PyLauncher") 
root.resizable(False, False) # размер не изменяемый 
root.geometry(f"{width}x{height}+{x}+{y}") # размер экрана

Label(text="ForgeOptiFine 1.7.10",     font="Arial 12", fg="red").grid(row=0, column=0, pady=10, padx=10)
Label(text="PyLauncher by Adxamjon97", font="Arial 15"          ).grid(row=0, column=1, pady=10, padx=10)

def path(string, string2, row):
	Label(text=string2, font="Arial 12").grid(row=row, column=0, pady=10, padx=10)

	var = StringVar()
	if lst == {} or lst[string] == '': var.set(str(sp.check_output("cd", shell=True))[2:-5].replace(r'\\','\\'))
	else: var.set(lst[string])

	def func():
		dirname = filedialog.askdirectory(initialdir=var.get())
		if dirname != '':
			var.set(dirname.replace('/', '\\'))

	Entry(width=55, textvariable=var).grid(row=row, column=1, pady=10, padx=10)
	Button(text="...", width=3, height=1, command=func).grid(row=row, column=3, pady=10, padx=10)
	return var

clentpath = path('clentpath', "Путь на папку клента: ", 1) # 2-ой строка
javapath  = path('javapath',  "Путь на папку джава: ",  2)  # 3-ый строка

def mbandname(string, string2, default, row):
		var = StringVar()

		if lst == {} or lst[string] == '': var.set(default)
		else: var.set(lst[string])

		Label(text=string2, font="Arial 12").grid(row=row, column=0, pady=10, padx=10)
		Entry(width=25, textvariable=var).grid(row=row, column=1, pady=10, padx=10)
		return var
		
maxmb    = mbandname('maxmb',    "Память: ",     '1600',   3) # 3-ый строка
username = mbandname('username', "Имя игрока: ", 'noname', 4) # 4-ый строка

# 6-ой строка
Button(text="Сохранения",  width=12, height=1, command=lambda:save()).grid(row=5, column=0, pady=10, padx=10)

def start(obj):
	save(username.get(), clentpath.get(), javapath.get(), maxmb.get(), uid)
	text = f"""{lst['javapath']}\\bin\\javaw.exe 
-XX:+UseConcMarkSweepGC 
-XX:-UseAdaptiveSizePolicy 
-XX:+CMSParallelRemarkEnabled 
-XX:+ParallelRefProcEnabled 
-XX:+CMSClassUnloadingEnabled 
-XX:+UseCMSInitiatingOccupancyOnly 
-Xmx{lst['maxmb']}M -Dfile.encoding=UTF-8 
-Dfml.ignoreInvalidMinecraftCertificates=true 
-Dfml.ignorePatchDiscrepancies=true 
-Djava.net.useSystemProxies=true 
-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump 
-Djava.library.path="{lst['clentpath']}\\versions\\ForgeOptiFine 1.7.10\\natives" 
-Dminecraft.launcher.brand=java-minecraft-launcher 
-Dminecraft.launcher.version=1.6.84-j 
-Dminecraft.client.jar="{lst['clentpath']}\\versions\\ForgeOptiFine 1.7.10\\ForgeOptiFine 1.7.10.jar" 
-cp {lst['clentpath']}\\libraries\\optifine\\OptiFine\\1.7.10_HD_U_E7\\OptiFine-1.7.10_HD_U_E7.jar;
{lst['clentpath']}\\libraries\\net\\minecraftforge\\forge\\1.7.10-10.13.4.1614-1.7.10\\forge-1.7.10-10.13.4.1614-1.7.10.jar;
{lst['clentpath']}\\libraries\\net\\minecraft\\launchwrapper\\1.12\\launchwrapper-1.12.jar;
{lst['clentpath']}\\libraries\\org\\ow2\\asm\\asm-all\\5.0.3\\asm-all-5.0.3.jar;
{lst['clentpath']}\\libraries\\com\\typesafe\\akka\\akka-actor_2.11\\2.3.3\\akka-actor_2.11-2.3.3.jar;
{lst['clentpath']}\\libraries\\com\\typesafe\\config\\1.2.1\\config-1.2.1.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\scala-actors-migration_2.11\\1.1.0\\scala-actors-migration_2.11-1.1.0.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\scala-compiler\\2.11.1\\scala-compiler-2.11.1.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\plugins\\scala-continuations-library_2.11\\1.0.2\\scala-continuations-library_2.11-1.0.2.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\plugins\\scala-continuations-plugin_2.11.1\\1.0.2\\scala-continuations-plugin_2.11.1-1.0.2.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\scala-library\\2.11.1\\scala-library-2.11.1.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\scala-parser-combinators_2.11\\1.0.1\\scala-parser-combinators_2.11-1.0.1.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\scala-reflect\\2.11.1\\scala-reflect-2.11.1.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\scala-swing_2.11\\1.0.1\\scala-swing_2.11-1.0.1.jar;
{lst['clentpath']}\\libraries\\org\\scala-lang\\scala-xml_2.11\\1.0.2\\scala-xml_2.11-1.0.2.jar;
{lst['clentpath']}\\libraries\\lzma\\lzma\\0.0.1\\lzma-0.0.1.jar;
{lst['clentpath']}\\libraries\\net\\sf\\jopt-simple\\jopt-simple\\4.5\\jopt-simple-4.5.jar;
{lst['clentpath']}\\libraries\\com\\google\\guava\\guava\\17.0\\guava-17.0.jar;
{lst['clentpath']}\\libraries\\org\\apache\\commons\\commons-lang3\\3.3.2\\commons-lang3-3.3.2.jar;
{lst['clentpath']}\\libraries\\com\\mojang\\netty\\1.6\\netty-1.6.jar;
{lst['clentpath']}\\libraries\\com\\mojang\\realms\\1.3.5\\realms-1.3.5.jar;
{lst['clentpath']}\\libraries\\org\\apache\\commons\\commons-compress\\1.8.1\\commons-compress-1.8.1.jar;
{lst['clentpath']}\\libraries\\org\\apache\\httpcomponents\\httpclient\\4.3.3\\httpclient-4.3.3.jar;
{lst['clentpath']}\\libraries\\commons-logging\\commons-logging\\1.1.3\\commons-logging-1.1.3.jar;
{lst['clentpath']}\\libraries\\org\\apache\\httpcomponents\\httpcore\\4.3.2\\httpcore-4.3.2.jar;
{lst['clentpath']}\\libraries\\java3d\\vecmath\\1.3.1\\vecmath-1.3.1.jar;
{lst['clentpath']}\\libraries\\net\\sf\\trove4j\\trove4j\\3.0.3\\trove4j-3.0.3.jar;
{lst['clentpath']}\\libraries\\com\\ibm\\icu\\icu4j-core-mojang\\51.2\\icu4j-core-mojang-51.2.jar;
{lst['clentpath']}\\libraries\\com\\paulscode\\codecjorbis\\20101023\\codecjorbis-20101023.jar;
{lst['clentpath']}\\libraries\\com\\paulscode\\codecwav\\20101023\\codecwav-20101023.jar;
{lst['clentpath']}\\libraries\\com\\paulscode\\libraryjavasound\\20101123\\libraryjavasound-20101123.jar;
{lst['clentpath']}\\libraries\\com\\paulscode\\librarylwjglopenal\\20100824\\librarylwjglopenal-20100824.jar;
{lst['clentpath']}\\libraries\\com\\paulscode\\soundsystem\\20120107\\soundsystem-20120107.jar;
{lst['clentpath']}\\libraries\\io\\netty\\netty-all\\4.0.10.Final\\netty-all-4.0.10.Final.jar;
{lst['clentpath']}\\libraries\\com\\google\\guava\\guava\\15.0\\guava-15.0.jar;
{lst['clentpath']}\\libraries\\org\\apache\\commons\\commons-lang3\\3.1\\commons-lang3-3.1.jar;
{lst['clentpath']}\\libraries\\commons-io\\commons-io\\2.4\\commons-io-2.4.jar;
{lst['clentpath']}\\libraries\\commons-codec\\commons-codec\\1.9\\commons-codec-1.9.jar;
{lst['clentpath']}\\libraries\\net\\java\\jinput\\jinput\\2.0.5\\jinput-2.0.5.jar;
{lst['clentpath']}\\libraries\\net\\java\\jutils\\jutils\\1.0.0\\jutils-1.0.0.jar;
{lst['clentpath']}\\libraries\\com\\google\\code\\gson\\gson\\2.2.4\\gson-2.2.4.jar;
{lst['clentpath']}\\libraries\\com\\mojang\\authlib\\1.5.21\\authlib-1.5.21.jar;
{lst['clentpath']}\\libraries\\org\\apache\\logging\\log4j\\log4j-api\\2.0-beta9\\log4j-api-2.0-beta9.jar;
{lst['clentpath']}\\libraries\\org\\apache\\logging\\log4j\\log4j-core\\2.0-beta9\\log4j-core-2.0-beta9.jar;
{lst['clentpath']}\\libraries\\org\\lwjgl\\lwjgl\\lwjgl\\2.9.1\\lwjgl-2.9.1.jar;
{lst['clentpath']}\\libraries\\org\\lwjgl\\lwjgl\\lwjgl_util\\2.9.1\\lwjgl_util-2.9.1.jar;
{lst['clentpath']}\\libraries\\tv\\twitch\\twitch\\5.16\\twitch-5.16.jar;"
{lst['clentpath']}\\versions\\ForgeOptiFine 1.7.10\\ForgeOptiFine 1.7.10.jar" net.minecraft.launchwrapper.Launch 
--username {lst['username']} 
--version ForgeOptiFine 1.7.10 
--gameDir "{lst['clentpath']}" 
--assetsDir "{lst['clentpath']}\\assets" 
--assetIndex 1.7.10 
--uuid {lst['uuid']} 
--accessToken {lst['accessToken']} 
--userProperties {lst['scobe']} 
--userType legacy 
--tweakClass cpw.mods.fml.common.launcher.FMLTweaker 
--tweakClass optifine.OptiFineForgeTweaker 
--width 925 
--height 530"""
	command = ''.join(text.split('\n')) # убрать новый строкы
		
	obj['state'] = 'disabled'
	obj['text']  = 'запускается'

	def fun():
		time.sleep(3)
		root.destroy() # закрыть лаунчера
	Thread(target=fun).start()

	def fun2():
		sp.call(command) # запуск команду
	Thread(target=fun2).start()

btn2 = Button(text="Запускать", width=20, height=1, command=lambda: start(btn2))
btn2.grid(row=5, column=1, pady=10, padx=10)

root.mainloop()

