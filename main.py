# -*- coding: utf8 -*-
#
# (c) 2015 microelly2 MIT
#

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



from kivy.support import *
install_android()


from kivy.config import Config
#Config.set('graphics', 'width', '600')
#Config.set('graphics', 'height', '800')

Config.set('graphics', 'width', '100')
Config.set('graphics', 'height', '420')

superbl=None

import datetime,re,os,random
import httplib
import socket


class KButton(Button):
	key=Property('')

class addon(FloatLayout):
	pass


# die graphische oberflaeche
class kite(FloatLayout):
	pass

# die anwendung ...
class kiteApp(App):

	tag=Property('')
	stunde=Property('')
	klasse=Property('')
	name=Property('Schlaumeier-Neugscheid')
	geraet=Property(None)
	but=Property(None)
	ao=Property(None)
	bl=Property(None)
	ip=Property('192.168.178.26')
	ip=Property('freecadbuch.de')
	
	def build(self):
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
		sendstring= "/appdat_server/appstore.php?m="+ mess+"&u=user&h=1234&k=9876"
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
		c.request("GET", "/appdat_server/appconfig.php?c="+ dateiname +".txt")
		response = c.getresponse()
		print "rsponce:",response.status, response.reason
		
		if response.status == 200:
			print "ok"
		else:
			print "problem : the query returned %s because %s" % (response.status, response.reason)  
		
		data = response.read()
		vals=data.split('\n')
		vals.pop(-1)
		print vals
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
		for t in sorted(buli):
#			print "##",t
			for s in sorted(buli[t]):
#				print "--",s
				for g in sorted(buli[t][s]):
					print [t,s,g,buli[t][s][g]]
					pass
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
				week   = [ 
				  'Mo', 
				  'Di', 
				  'Mi', 
				  'Do',  
				  'Fr', 
				  'Sa','So']
				gs=week[wd] + ss 
				w=KButton(text=gs, on_release = self.setzeTag,key=g)
				print w.key
				self.root.tage.add_widget(w)

	def aktualisiereGeraete(self,but):
		print "aktualisiere GERAAATER"
		lg=self.lesedatei('geraete')
		self.root.geraete.clear_widgets()
		print "aktualisiere geraet"
		for  g in lg:
			print g
			gt=datetime.datetime.now().strftime("%H:%M:%S\n") + g
			gt=g
			w=Button(text=gt,on_release = self.setzeGeraet)
			print w
			print w.on_release
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
						print "skip nich ",nick
						continue

					tt=self.doyString2(t)
					ytext= "  ".join([tt,s,g,buli[t][s][g][0][0:2]]) 
					btn = Button(text=ytext, 
						# size=(280, 40),
						# size_hint=(None, None)
						
					)
					from functools import partial
					s3= t+':'+s+';'+g+':frei'
					print s3
					def myprint(s,btn):
						print s
						btn.parent.remove_widget(btn)
						print "cleared"
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
					pass




	def langeListe(self):
		layout = GridLayout(cols=1, padding=10, spacing=10,
				size_hint=(None, None), width=180)
		layout.bind(minimum_height=layout.setter('height'))
#		ao=Builder.load_file('/home/thomas/Dokumente/kivy_buch/k03_simple/simple.kv')
#		cc=[]
#		for c in ao.children:
#			cc.append(c)
#		for c in cc:
#			ao.remove_widget(c)
#			c.size=(200,40)
#			c.size_hint=(None,None)
#


		buli=self.holeBuchungen()
		for t in sorted(buli):
			print "##",t
			
			if int(t) <self.heute:
				continue
			 
			for s in sorted(buli[t]):
				print "--",s
				for g in sorted(buli[t][s]):
					print [t,s,g,buli[t][s][g]]
					nick=buli[t][s][g][0][0:2]
					
					#if nick <> self.user:
					#	print "skip nich ",nick
					#	continue
					
					tt=self.doyString2(t)
					ytext= "  ".join([tt,s,g,buli[t][s][g][0][0:2]])
					btn = Button(text=ytext, size=(280, 40),
						size_hint=(None, None))
					layout.add_widget(btn)
					pass
	
		
#		for i in range(130):
#			btn = Button(text="Buchung "+str(i), size=(280, 40),
#				 size_hint=(None, None))
#			layout.add_widget(btn)
		# create a scroll view, with a size < size of the grid
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

	def readconfig(self,but):
		l2='xy:9876:Ix Ypslein'
		try:
			f = open("myfile")
			lines = f.readlines()
			for l in lines:
				l2=l.strip()
				print "!"+l2+"!"
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
		# self.meineBuchungen()
		

if __name__ == '__main__' and True:
	sap=kiteApp()
	sap.run()
