# -*- coding: utf8 -*-
#
# (c) 2015 microelly2 MIT
#

vers="V123"
 
import kivy
kivy.require('1.0.9')
from kivy.app import App
from kivy.properties import *
from kivy.base import EventLoop

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

#from kivy.lang import Builder

from kivy.clock import Clock
from kivy.properties import BooleanProperty
from kivy.utils import platform

from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from kivy.clock import Clock

from kivy.support import *
install_android()

import datetime,re,os,random, time, threading
import httplib, socket, urllib2, zipfile


from kivy.support import *
install_android()


#from kivy.config import Config
#Config.set('graphics', 'width', '600')
#Config.set('graphics', 'height', '800')

# Config.set('graphics', 'width', '160')
# Config.set('graphics', 'height', '620')

superbl=None

import datetime,re,os,random
import httplib
import socket

def update(btn):
		print "update software .... not implemented"


class KButton(Button):
	key=Property('')

class addon(FloatLayout):
	pass


# die graphische oberflaeche
class kite(FloatLayout):
	pass


if platform == "android":
	import android
	from jnius import autoclass, cast
	from android.runnable import run_on_ui_thread
#	Toast = autoclass("android.widget.Toast")

class PopupBox(Popup):
	pop_up_text = ObjectProperty()
	def update_pop_up_text(self, p_message):
		self.pop_up_text.text = p_message

def unzip(zipFilePath, destDir):
	zfile = zipfile.ZipFile(zipFilePath)
	if not os.path.exists(destDir):
			os.mkdir(destDir)
	for name in zfile.namelist():
		print name
		(dirName, fileName) = os.path.split(name)
		newDir = destDir + '/' + dirName
		if not os.path.exists(newDir):
			os.mkdir(newDir)
		if not fileName == '':
			fd = open(destDir + '/' + name, 'wb')
			fd.write(zfile.read(name))
			fd.close()

def wotagstring(wotagint):
	week   = [ 'Mo', 'Di', 'Mi',  'Do',   'Fr', 'Sa','So']
	return week[wotagint]


# die anwendung ...
class kiteApp(App):
	global update

	exitnext = BooleanProperty(False)
	tag=Property('')
	stunde=Property('')
	klasse=Property('')
	name=Property('Schlaumeier-Neugscheid')
	geraet=Property(None)
	but=Property(None)
	ao=Property(None)
	bl=Property(None)
	ip=Property('192.168.178.22')
	ip=Property('freecadbuch.de')
	
	
	def build(self):
 		self.bind(on_start=self.post_build_init)
		c= kite(title='Hello world')
		
		return c

#	def sayhello(self,button,name):
#		print "Hello " +  name + ", this is the simple App!"
#		button.text = "[size=100][b]Super " + name +  "[/b]\nSay hello [color=#ff0000]again![/size][/color]"

	def setzeFarbe(self,but):
		for b in but.parent.children:
			b.background_color=(1,0,1,1)
		but.background_color=(1,1,0,1)
		
	def setzeTag(self,but):
		print "setze Tage"
		print but.text
		self.tag=but.key
		self.setzeFarbe(but)
		#print self.root.buchen
		print but.parent
		print but.parent.parent
		print but.parent.parent.parent
		print but.parent.parent.parent.parent
		print but.parent.parent.parent.parent.parent
		but.parent.parent.parent.parent.parent.title=but.text
		but.parent.parent.parent.parent.parent.collapse=True
		self.upd()
		self.aktualisiereGeraete(None)
		self.root.tag.collapse=True
		self.root.stunde.collapse=False


	def setzeStunde(self,but):
		print but.text
		self.stunde=but.text
		self.setzeFarbe(but)
		but.parent.parent.parent.parent.parent.title=but.text
		but.parent.parent.parent.parent.parent.collapse=True
		self.upd()
		self.aktualisiereGeraete(None)
		self.root.stunde.collapse=True
		self.root.geraet.collapse=False


	def setzeGeraet(self,but):
		print "SETZT GERAET"
		print but.text
		self.geraet=but.text
		self.geraet=but.key
#		self.setzeFarbe(but)
#		but.parent.parent.parent.parent.parent.title=but.text
		but.parent.parent.parent.parent.parent.collapse=True
		self.upd()
		self.buchen()
#		self.clear()

	def setzeKlasse(self,but):
		print but.text
		self.klasse=but.text
		self.setzeFarbe(but)
		but.parent.parent.parent.parent.parent.title=but.text
		but.parent.parent.parent.parent.parent.collapse=True
		self.upd()


	def upd(self):
		pass

	def buchen(self):
		if self.tag=='':
			print "kein Tag"
			self.root.tag.collapse=False
			self.root.geraet.collapse=True
		elif self.stunde=='':
			print "keine Stunde"
			self.root.tag.collapse=True
			self.root.stunde.collapse=False
			self.root.geraet.collapse=True
		else:
			print "Tag ist da"
			print self.tag
			mess=str(self.tag+self.heute) + ":"+  str(self.stunde) + ";"+ str(self.geraet)+':'+self.name
			print mess
			rc=self.sendeBuchung(mess)
			print rc
			#Buchung anzeigen
			self.meineBuchungen()
			#but=Button()
			#but.text=self.doyString(self.tag) + " -"+  str(self.stunde) + "- "+ str(self.geraet)
			#self.but=but
			#but.on_release=self.loesche
			#self.root.liste.add_widget(but)
			
			self.root.buchen.collapse=True
			self.root.liste.collapse=False
			print self.root.liste.collapse
	#		self.tag=''
			t=int(self.tag)
			s=int(self.stunde)
			if s>=9:
				s=0
				t +=1 
				self.tag=int(t) 
			self.stunde=str(s+1)
			self.geraet=''
			self.klasse=''
			self.upd()
			self.clear()
	
	def clear(self):
		
#		self.root.geraet.title="Geraet ??"
#		self.root.tag.title="Tag"
		self.root.tag.title=self.doyString(self.tag)
		self.root.stunde.title=str(self.stunde)
#		self.root.buchen.title="Clear" 
		return
		if not self.ao:
			self.ao=addon()
			self.bl=self.root.kite
			self.root.remove_widget(self.root.kite)
			self.root.add_widget(self.ao)
		else:
			self.root.remove_widget(self.ao)
			self.root.add_widget(self.bl)
			self.ao=False
	
	
	
	def loesche(self):
		but=self.but
		print "loesche", but
		print but.parent
		but.parent.remove_widget(but)

	def wechseln(self):
		layout = GridLayout(cols=2)
		for i in range(21):
			layout.add_widget(Button(text='Hello 1'))
		# layout.add_widget(Button(text='World 1'))
		button = Button(text='zurick!', font_size=14)
		button.bind(on_release=self.goback)
		layout.add_widget(button)
		self.rest=self.root.children[0]
		self.root.remove_widget(self.rest)
		self.root.add_widget(layout)
		print self.root.children

	def wechseln2(self):
		layout = GridLayout(cols=7)
		
		for stunde in range(9):
			for geraet in range(7):
				b=Button(text=str(geraet+1)+'\n'+str(stunde+1))
				r=random.random()
				if r < 0.6:
					b.background_color=(1,0,1,1)
				else:
					b.background_color=(0,1,1,1)
				layout.add_widget(b)
			# layout.add_widget(Button(text='World 1'))
		for g in ['z','u','r','i','c','k','!']:
			button = Button(text=g)
			
			button.bind(on_release=self.goback)
			layout.add_widget(button)
		self.rest=self.root.children[0]
		self.root.remove_widget(self.rest)
		self.root.add_widget(layout)
		print self.root.children



	def  goback(self,but):
		print self.root.children
		self.root.remove_widget(self.root.children[0])
		self.root.add_widget(self.rest)
		print "giback"

	def on_pause(self):
	# Here you can save data if needed
		return True

	def on_resume(self):
	# Here you can check if any data needs replacing (usually nothing)
		pass

	def on_stop(self):
		print "on_stop"
		#self.schreibeTagDatei()

	def sayhello(self,button,name=None):
		print "Hello " +  str(name) + ", this is the simple App!"
#		button.text = "[size=100][b]Super " + name +  "[/b]\nSay hello [color=#ff0000]again![/size][/color]"
#		button.text='Buchen'
		if name: 
			self.name=name
		
		print self.ao
		global superbl
		print superbl
		self.root.clear_widgets()
		
		if not self.ao:
			self.ao=addon()
			self.bl=self.root.bl
		#	self.root.remove_widget(self.root.bl)
			self.root.add_widget(self.ao)
		else:
		#	self.root.remove_widget(self.ao)
			self.root.add_widget(self.bl)

			self.root.buchen.collapse=True
			self.root.liste.collapse=False
			self.root.tag.collapse=True
			self.root.stunde.collapse=True
			self.root.geraet.collapse=True
			self.meineBuchungen()

			# self.ao=False
			# self.liste fuellen
			

	def sayhello2(self,a):
		self.sayhello(self,a)
		




	def sendeBuchung(self,mess):
		c = httplib.HTTPConnection(self.ip)
		authstring="&u="+self.user+"&n="+self.name+"&p="+self.passw
		sendstring= "/appdat_server/appstore.php?m="+ mess+"&u=user&h=1234&k=9876"+authstring 
		print "Sendstrung"
		print sendstring
		c.request("GET", sendstring)
		response = c.getresponse()
		print "rsponce:",response.status, response.reason
		if response.status == 200:
			data = response.read()
			print data
			vals=data.split('\n')
			vals.pop(-1)
			print vals
			return vals
		else:
			print "Fehler Datensendung" 



	def lesedatei(self,dateiname):
		print "Lese Daten aus dem Netz ..."
		try:
			c = httplib.HTTPSConnection(self.ip)
			c.connect()
		except :
			print "Error HTTPS"
			try:
				c = httplib.HTTPConnection(self.ip)
				c.connect()
			except :
				print "Error HTTP"
				return []
		authstring="&u="+self.user+"&n="+self.name+"&p="+self.passw
		req="/appdat_server/appconfig.php?c="+ dateiname +".txt" + "&u=user&h=1234&k=9876"+authstring
		print  req
		c.request("GET", req)
		response = c.getresponse()
		print "rsponce:",response.status, response.reason
		
		if response.status == 200:
			print "ok"
		else:
			print "problem : the query returned %s because %s" % (response.status, response.reason)  
		
#		print("-----##-")
		data = response.read()
#		print data
#		print("-----++-")
		vals=data.split('\n')
		print "auth string .."
		print vals[0]
		vals.pop(-1)
		vals.pop(0)
#		for v in vals:
#			print "!"+v+"!"

		return vals


	def holeBuchungen(self):
		day_of_year = datetime.datetime.now().timetuple().tm_yday
		self.heute=day_of_year
		day='274'
		ss=(datetime.datetime.now() + datetime.timedelta(days=int(day)-day_of_year)).strftime(", %d.%m")
		print ss
		
		buchs=self.lesedatei("buchungen")
		# print buchs
		buli={}
		for b in buchs:
			try:
				[k,d]=b.split(';')
				[t,s]=k.split(':')
				[g,u]=d.split(':')
				day=t
				ss=(datetime.datetime.now() + datetime.timedelta(days=int(day)-day_of_year)).strftime(", %d.%m")
				print [t,ss,s,g,u]
				try: 
					buli[t]
				except:
					buli[t]={}
				try:
					buli[t][s]
				except:
					buli[t][s]={}
				try:
					buli[t][s][g]
				except:
					buli[t][s][g]=[]
				if u=='frei':
					del(buli[t][s][g])
				else:
					buli[t][s][g].append(u)
			except:
				print "fehler bei verarbeiten von " + b + "!"
		for t in sorted(buli):
#			print "##",t
			for s in sorted(buli[t]):
#				print "--",s
				for g in sorted(buli[t][s]):
					print [t,s,g,buli[t][s][g]]
					pass
		self.buli=buli
		return buli

	def holePersonen(self):
		return self.lesedatei('personen')

	def holeGeraete(self):
		print "hole geraete"
		lg=self.lesedatei('geraete')
		self.root.geraete.clear_widgets()
		for  g in lg:
			#gt=datetime.datetime.now().strftime("%H:%M:%S\n") + g
			gt=g
			w=Button(text=gt,on_release = self.setzeGeraet)
			print w.on_release
			
			self.root.geraete.add_widget(w)

	def holeStunden(self):
		self.root.stunden.clear_widgets()
		for g in range(9):
				w=KButton(text=str(g+1), on_release = self.setzeStunde,key=g)
				print w.key
				self.root.stunden.add_widget(w)


	def holeTage(self):
		self.root.tage.clear_widgets()
		for g in range(14):
			gs="tag " +str(g)
			wd=(datetime.datetime.now() + datetime.timedelta(hours=24*g)).weekday()
			if wd<>5 and wd<>6:
				ss= (datetime.datetime.now() + datetime.timedelta(hours=24*g)).strftime(", %d.%m")
				week   = [ 'Mo', 'Di', 'Mi',  'Do',   'Fr', 'Sa','So']
				gs=week[wd] + ss 
				w=KButton(text=gs, on_release = self.setzeTag,key=g)
				self.root.tage.add_widget(w)

	def aktualisiereGeraete(self,but):
		print "aktualisiere GERAAATER"
		lg=self.lesedatei('geraete')
		self.root.geraete.clear_widgets()
		print "aktualisiere geraet"
		print self.buli
		print "--------------------------------------"
		print self.tag
		print self.heute
		print self.stunde
		print "------------------------------"
		try:
			print self.buli[str(self.heute+self.tag)][str(self.stunde)]
			zz=self.buli[str(self.heute+self.tag)][str(self.stunde)]
		except:
			zz={}
			print "tag/stunde frei"
		print "-------------"
		for  sg in lg:
			print sg
			sgl= sg.split(';')
			g=sgl[0]
			if len(sgl)>1:
				try:
					wotag=self.tag
					if wotag>7: wotag -= 7
					gaddl=sgl[wotag].split(':')
					print (gaddl)
					print self.stunde
					print self.heute
					gadd=  " (" + gaddl[int(self.stunde)] + ")"
				except:
					gadd=""
			else:
				gadd=""
			gt= g +  gadd 
			if zz.has_key(g):
				w=Button(text=gt + "\n"+str(zz[g]))
				w.background_color=(1,0,0,1)
			else:
				w=KButton(text=gt,on_release = self.setzeGeraet)
				w.key=g
				w.background_color=(0,1,0,1)
			#print w
			#print w.on_release
			# w=Button(text=gt+"TT",on_enter = self.setzeTag)
			
			self.root.geraete.add_widget(w)

	def meineBuchungen(self):
		buli=self.holeBuchungen()
		self.root.liste.clear_widgets()
		farbe=True
		for t in sorted(buli):
			print "##",t
			
			if int(t) <self.heute:
				continue
			 
			for s in sorted(buli[t]):
				print "--",s
				for g in sorted(buli[t][s]):
					print [t,s,g,buli[t][s][g]] 
					nick=buli[t][s][g][0][0:2]
					if nick <> self.user:
						continue
					tt=self.doyString2(t)
					ytext= "  ".join([tt,s,g,buli[t][s][g][0][0:2]]) 
					btn = Button(text=ytext)
					from functools import partial
					s3= t+':'+s+';'+g+':frei'
					print s3
					def myprint(s,btn):
						print s
						btn.parent.remove_widget(btn)
						rc=self.sendeBuchung(s)
						print rc
						print "Auswertung ---------------------------------------"
						self.meineBuchungen()
						print "aktualisiert ---------------------------------------------"
					
					btn.on_release =  partial(myprint,s3,btn)
					
					if farbe:
						btn.background_color=(1,0,1,1)
					else:
						btn.background_color=(0,1,1,1)
					farbe = not farbe
					self.root.liste.add_widget(btn)

	def langeListe(self):
		layout = GridLayout(cols=1, padding=10, spacing=10,
				size_hint=(None, None), width=180)
		layout.bind(minimum_height=layout.setter('height'))

		buli=self.holeBuchungen()
		for t in sorted(buli):
			print "##",t
			neuerTag=True
			if int(t) <self.heute:
				continue
			neueStunde=True 
			for s in sorted(buli[t]):
				print "--",s
				if len(buli[t][s]):
					neueStunde= not neueStunde
				print neueStunde
				for g in sorted(buli[t][s]):
					print [t,s,g,buli[t][s][g]]
					nick=buli[t][s][g][0][0:2]
					tt=self.doyString2(t)
					ytext= "  ".join([s,g,buli[t][s][g][0][0:2]])
					btn = Button(text=ytext, size=(280, 40),
						size_hint=(None, None))
					if neueStunde:
						btn.background_color=(1,0,1,1)
					else:
						btn.background_color=(0,1,1,1)
					if neuerTag:
						wotagint=1
						wotagint=self.doy2dow(t)

						ytext2=wotagstring(wotagint) + ", " + tt #  "  ".join([tt,s,g,buli[t][s][g][0][0:2]])
						btn2 = Button(text=ytext2, size=(280, 40),
						size_hint=(None, None))
						btn2.background_color=(0,0,1,1)
						layout.add_widget(btn2)
						neuerTag=False
					layout.add_widget(btn)
					pass
		root2 = ScrollView(size_hint=(None, None), size=(300, 590),
				pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
		root2.add_widget(layout)
		root3=BoxLayout(orientation='vertical')
		b=Button(text="f1 (nofunc)")
		root3.add_widget(b)
		b=Button(text="Buchen",on_release=self.sayhello)
		root3.add_widget(b)
		b=Button(text="Start", on_release=self.gomain)
		root3.add_widget(b)
		root=BoxLayout(	orientation='horizontal')
		root.add_widget(root3)
		root.add_widget(root2)
		self.root.remove_widget(self.ao)
		try:
			self.root.remove_widget(self.bl)
		except:
			pass
		self.root.add_widget(root)

	def gomain(self,a):
		self.root.remove_widget(self.root.children[0])
		try:
			self.root.remove_widget(self.bl)
		except:
			pass
		self.root.add_widget(self.ao)

	def gobl(self,a):
		self.root.remove_widget(self.root.children[0])
		self.root.add_widget(self.bl)


	def doyString(self,doy):
		ss=(datetime.datetime.now() + datetime.timedelta(days=int(doy))).strftime("%d.%m.")
		return ss

	def doyString2(self,doy):
		day_of_year = datetime.datetime.now().timetuple().tm_yday
		ss=(datetime.datetime.now() + datetime.timedelta(days=int(doy)-day_of_year)).strftime("%d.%m.")
		return ss

	def doy2dow(self,doy):
		day_of_year = datetime.datetime.now().timetuple().tm_yday
		ss=(datetime.datetime.now() + datetime.timedelta(days=int(doy)-day_of_year)).weekday()
		return ss

	def configure(self,but):
		print "configure writer file ..."
		f = open('myfile','w')
		
		#print but.parent.children[1]
		#print but.parent.children[1].children
		l=len(but.parent.children) -4
		for i in but.parent.children:
			print i
		print "huhu"  
		print l
		self.passw=but.parent.children[l].children[0].text
		self.user=but.parent.children[l].children[1].text
		self.name=but.parent.children[l].children[2].text
		f.write(self.user + ':1234:'+ self.name+'\n') # python will convert \n to os.linesep
		f.close() # you can omit in most cases as the destructor will call it
		try:
			self.addon.add_widget(self.bucher)
		except:
			pass
		
		self.readconfig(but)

	def readversion(self):
		l2='title=xy:9876:Ix Ypslein'
		try:
			f = open("android.txt")
			lines = f.readlines()
			for l in lines:
				l2=l.split('=')
				print l2
				if l2[0]=='title': 
					f.close()
					return l2[1].strip()
		except:
			return "??"


	def readconfig(self,but):
		l2='xy:9876:Ix Ypslein'
		try:
			f = open("myfile")
			lines = f.readlines()
			for l in lines:
				l2=l.strip()
			f.close()
		except:
			l2='xy:9876:Ix Ypslein' 
		[self.user,self.passw,self.name]=l2.split(':')
		import hashlib
		self.md5=hashlib.md5(self.passw).hexdigest()
		import random
		self.hash=random.randint(1000,9999)
		self.md5hash=hashlib.md5(str(self.hash)).hexdigest()
		print (self.user, self.passw,self.md5,self.hash,self.md5hash)
		try:
			print but
			but.text='angemeldet als ' + '-'.join([self.user, self.passw,self.md5,str(self.hash),self.md5hash])
		except: 
			pass
		print "done"
		return [self.user, self.name, self.passw,self.md5,str(self.hash),self.md5hash]

	def on_start(self):
		global superbl
		global vers
		if not self.ao:
			self.ao=addon()
			self.bl=self.root.kite
			superbl=self.root.kite
			self.root.remove_widget(self.root.kite)
			self.root.add_widget(self.ao)
			ll=self.readconfig(None)
			self.ao.name.text=ll[0]
			self.ao.namelong.text=ll[1]
			self.bucher=self.ao.bucher
			self.addon=self.ao.addon
			self.addon.remove_widget(self.bucher)
			print superbl
		else:
			self.root.remove_widget(self.ao)
			self.root.add_widget(self.bl)
			self.ao=False
		#self.personen=self.holePersonen()
		self.geraete=self.holeStunden()
		self.geraete=self.holeGeraete()
		self.holeTage()
		
		self.root.liste.clear_widgets()
		# testuser
		self.user=self.ao.name.text
		day_of_year = datetime.datetime.now().timetuple().tm_yday
		self.heute=day_of_year
		if sap.updater():
			global update
			print "update yes/no ..."
			btn = Button(
				text='Update Software required', font_size=14,
				on_release = self.process_button_click
			)
			self.addon.add_widget(btn)
		print self.addon.children[0]
		# Titel setzen
		
		self.addon.children[5].text='[color=#ffff00][size=50][b]Snow Kite School V '+vers +'[/b][/size][/color]'
		print "----------------"
		title=self.readversion()
		print "title:"+title
		self.addon.children[5].text='[color=#ffff00][size=50][b]' + title + '[/b][/size][/color]'



	def post_build_init(self, *args):
		# Map Android keys
		if platform == 'android':
			android.map_key(android.KEYCODE_BACK, 1000)
			android.map_key(android.KEYCODE_MENU, 1001)
		win = self._app_window
		win.bind(on_keyboard=self._key_handler)
 
	def _key_handler(self, *args):
		key = args[1]
		print "key handler"
		print key
		try:
			# Escape or Android's back key
			#self.root.lab.text="EXIT key=" + str(key)
			if key in (1000, 27):
				self.hide_kbd_or_exit()
				return True
		except:
			return False

	def reset_exitnext(self,t):
		
		self.exitnext=False

	def hide_kbd_or_exit(self, *args):
		if not self.exitnext:
			self.exitnext = True
			#kurz  warten auf double exit
			Clock.schedule_once(self.reset_exitnext,0.5)
			self.gomain(None)
		else:
			self.stop()

	def updater(self):
			return True
			# hack 
			import re
			source="https://github.com/microelly2/kivy-ressourcen/archive/master.zip"
			print(source)
			plugin="microelly2/kivy-ressourcen"
			fn='https://api.github.com/repos/microelly2/kivy-ressourcen/commits'
			gitdate='no date from git'
			try: 
				fn='https://api.github.com/repos/' + plugin + '/commits'
				import urllib,json
				data=urllib.urlopen(fn).read()
				print data
				d = json.loads(data)
				dit=d[0]
				gitdate=dit['commit']['committer']['date']
				print (gitdate)
				installdate="2015-10-21T15:02:35Z"
				print (installdate)
			except:
				return True
			upd=False
			if installdate >gitdate:
				mess="--- package " + plugin + " is up to date ---"
			else:
				mess="!!! update for " + plugin + " recommented !!!"
				upd=True
			print mess
			return upd

####################
	def show_popup(self):
		#self.pop_up = Factory.PopupBox()
		self.pop_up = PopupBox()
		self.pop_up.update_pop_up_text('Running some task...')
		self.pop_up.open()

	def process_button_click(self,dummy):
		self.show_popup()
		#		self.source=source
		mythread1 = threading.Thread(target=self.something_that_takes_5_seconds_to_run)
		mythread = threading.Thread(target=self.readZip)
		mythread1.start()
		mythread.start()

	def something_that_takes_5_seconds_to_run(self):
		thistime = time.time() 
		while thistime + 5 > time.time(): # 5 seconds
			self.pop_up.update_pop_up_text('running ' + '*' * int(time.time()-thistime))
			time.sleep(1)

	def readZip(self,but=None):
		source='https://github.com/microelly2/kivy-ressourcen/archive/master.zip'
		self.pop_up.update_pop_up_text('get git ' + source + ' ...')
		try:
			
			response = urllib2.urlopen(source)
			zipcontent= response.read()
			with open("my.zip", 'w') as f:
				f.write(zipcontent)
			f.close()
		except:
			self.pop_up.update_pop_up_text('error getting the git')
			return
		self.pop_up.update_pop_up_text('unzip  ...')
		print "download"
		try:
			unzip("my.zip","..")
		except:
			self.pop_up.update_pop_up_text('error unzip')
			return
		self.pop_up.dismiss()




####################


if __name__ == '__main__' and True:
	sap=kiteApp()
	sap.updater()
	sap.run()
