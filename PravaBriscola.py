#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from operator import index, indexOf
import spade
from spade.agent import Agent
from spade.behaviour import TimeoutBehaviour, CyclicBehaviour, PeriodicBehaviour
import random
from spade import quit_spade

globalneKarteIgracA=[]
globalneKarteIgracB=[]
globalnaZadnjaKarta=[]


class Karta:
  def __init__(self, brojka, ime, boja, vrijednost):
    self.brojka = brojka
    self.ime = ime
    self.boja= boja
    self.vrijednost = vrijednost
    #self.ispis()
  
  def ispis(self):
    print(self.brojka, self.ime, self.boja, self.vrijednost)

class Karte:
  def __init__(self):
    self.spil=[]
    self.ispis()
  
  def ispis(self):
    for spada in range(1, 8, 1):
      if(spada==1):
        ime="As"
        vrijednostSpadaB=11
      elif(spada==3):
        ime=spada
        vrijednostSpadaB=10
      else:
        ime=spada
        vrijednostSpadaB=0
      self.spil.append(Karta(spada,ime,"spade",vrijednostSpadaB))

    for spada in range(11, 14, 1):
      if(spada==11):
        vrijednostSpada=2
        ime="Fanat"
      if(spada==12):
        vrijednostSpada=3
        ime="Konjanik"
      if(spada==13):
        vrijednostSpada=4
        ime="Kralj"
      self.spil.append(Karta(spada,ime,"spade",vrijednostSpada))

    for kupa in range(1,8,1):
      if(kupa==1):
        ime="As"
        vrijednostKupaB=11
      elif(kupa==3):
        ime=kupa
        vrijednostKupaB=10
      else:
        ime=kupa
        vrijednostKupaB=0
      self.spil.append(Karta(kupa,ime,"kupe",vrijednostKupaB))

    for kupa in range(11, 14, 1):
      if(kupa==11):
        vrijednostKupa=2
        ime="Fanat"
      if(kupa==12):
        vrijednostKupa=3
        ime="Konjanik"
      if(kupa==13):
        vrijednostKupa=4
        ime="Kralj"
      self.spil.append(Karta(kupa,ime,"kupe",vrijednostKupa))

    for bastona in range(1, 8, 1):
      if(bastona==1):
        ime="As"
        vrijednostBastonaB=11
      elif(bastona==3):
        ime=bastona
        vrijednostBastonaB=10
      else:
        ime=bastona
        vrijednostBastonaB=0
      
      self.spil.append(Karta(bastona,ime,"bastone",vrijednostBastonaB))
    
    for bastona in range(11, 14, 1):
      if(bastona==11):
        vrijednostBastona=2
        ime="Fanat"
      if(bastona==12):
        vrijednostBastona=3
        ime="Konjanik"
      if(bastona==13):
        vrijednostBastona=4
        ime="Kralj"
      self.spil.append(Karta(bastona,ime,"bastone",vrijednostBastona))

    for dinara in range(1,8,1):
      if(dinara==1):
        ime="As"
        vrijednostDinaraB=11
      elif(dinara==3):
        ime=dinara
        vrijednostDinaraB=10
      else:
        ime=dinara
        vrijednostDinaraB=0
      self.spil.append(Karta(dinara,ime,"dinare",vrijednostDinaraB))
    
    for dinara in range(11, 14, 1):
      if(dinara==11):
        vrijednostDinara=2
        ime="Fanat"
      if(dinara==12):
        vrijednostDinara=3
        ime="Konjanik"
      if(dinara==13):
        vrijednostDinara=4
        ime="Kralj"
      self.spil.append(Karta(dinara,ime,"dinare",vrijednostDinara))
  
  def ispis2(self):
    for karta in self.spil:
      karta.ispis()
  
  def Promjesaj(self):
    random.shuffle(self.spil)
      
class Okruzje(Agent):
  class PosaljiPoruku(PeriodicBehaviour):
    async def on_start(self):
      self.counter=0
      self.spilKarata = Karte()
      self.igracAKarte=[]
      self.igracBKarte=[]
      self.igracAPoeni=[]
      self.igracBPoeni=[]
      self.prednost=True
      self.baceneKarte=[]
      self.igracAbodovi=0
      self.igracBbodovi=0

      

    async def run(self):
      self.counter += 1
      if self.counter==1:
        print("----------------Napravio sam spil talijanskih karata-------")
        print("------------------------Talijanski spil--------------------")
        self.spilKarata.ispis2()
        print("-----------------------------------------------------------")
        self.spilKarata.Promjesaj()
        print("---------------------Promijesao sam spil-------------------")
        self.spilKarata.ispis2()
        #dodaj prve 3 karte igracu A
        self.igracAKarte.append(self.spilKarata.spil.pop())
        self.igracAKarte.append(self.spilKarata.spil.pop())
        self.igracAKarte.append(self.spilKarata.spil.pop())
        print("Dodavanje globalnoj listi karte igraca A")
        for a in self.igracAKarte:
          globalneKarteIgracA.append(a)
          a.ispis()
        #dodaj prve 3 karte igracu B
        self.igracBKarte.append(self.spilKarata.spil.pop())
        self.igracBKarte.append(self.spilKarata.spil.pop())
        self.igracBKarte.append(self.spilKarata.spil.pop())
        print("Dodavanje globalnoj listi karte igraca B")
        for b in self.igracBKarte:
          globalneKarteIgracB.append(b)
          b.ispis()
        
        print(len(self.spilKarata.spil))
        globalnaZadnjaKarta.append(self.spilKarata.spil[0])
        msg = spade.message.Message(
          to="mvulin1@jabbers.one",
          body="prviPotez")

        await self.send(msg)
        
        msg = spade.message.Message(
          to="mvulin2@jabbers.one",
          body="prviPotez")

        await self.send(msg)

      else:
        msg = await self.receive(timeout=100)      
        if msg:
          #self.sadrzaj.append(msg.body)
          if msg.sender.domain=="mvulin1":
            if msg.metadata:
              print("igrac A je prvi na potezu")
              print(f"Okruzije: IgracA je odlucio baciti")
              if len(self.igracAKarte)!=0:
                self.baceneKarte.append(self.igracAKarte[int(msg.body)])
                self.igracAKarte[int(msg.body)].ispis()
                self.igracAKarte.pop(int(msg.body))
                globalneKarteIgracA.pop(int(msg.body))
                self.prednost=True

            else:
              print("igrac B je prvi na potezu")
              print("Okruzije: IgracA je odlucio baciti")
              if len(self.igracAKarte)!=0:
                self.baceneKarte.append(self.igracAKarte[int(msg.body)])
                self.igracAKarte[int(msg.body)].ispis()
                self.igracAKarte.pop(int(msg.body))
                globalneKarteIgracA.pop(int(msg.body))
                self.prednost=False

          
          if msg.sender.domain=="mvulin2":
            print("Okruzije: IgracB je odlucio baciti:")
            if len(self.igracBKarte)!=0:
              self.baceneKarte.append(self.igracBKarte[int(msg.body)])
              self.igracBKarte[int(msg.body)].ispis()
              self.igracBKarte.pop(int(msg.body))
              globalneKarteIgracB.pop(int(msg.body))
            
          
          if len(self.baceneKarte)==2:
            if self.prednost==True:
              #print("napravi odluku kada igrac A baca prvi")
              if(self.baceneKarte[0].boja == globalnaZadnjaKarta[0].boja):
                if(self.baceneKarte[1].boja != globalnaZadnjaKarta[0].boja):
                  self.igracAPoeni.append(self.baceneKarte.pop())
                  self.igracAPoeni.append(self.baceneKarte.pop())
                  print("Igrac A osvojio poen")
                  if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                    for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                    for bodB in self.igracBPoeni:
                      self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                      bodB.ispis()
                    print("Agent A")
                    print(self.igracAbodovi)
                    print("Agent B")
                    print(self.igracBbodovi)

                  if len(self.spilKarata.spil)!=0:
                    self.igracAKarte.append(self.spilKarata.spil.pop())
                    self.igracBKarte.append(self.spilKarata.spil.pop())
                    globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                    globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                  msg = spade.message.Message(
                  to="mvulin1@jabbers.one",
                  body="imamPrednost")
                  await self.send(msg)
                  
                  msg = spade.message.Message(
                  to="mvulin2@jabbers.one",
                  body="nemamPrednost")
                  await self.send(msg)

                else:#oba igraca su odigrali briskulu odnosno adut
                  if(self.baceneKarte[0].vrijednost>self.baceneKarte[1].vrijednost):
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    print("Igrac A osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                    if len(self.spilKarata.spil)!=0:
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)

                  elif(self.baceneKarte[0].vrijednost==self.baceneKarte[1].vrijednost):
                    if(self.baceneKarte[0].brojka>self.baceneKarte[1].brojka):
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      print("Igrac A osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                          bodA.ispis()
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                          bodB.ispis()
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                      if len(self.spilKarata.spil)!=0:
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)
                    else:
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      print("Igrac B osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                          bodA.ispis()
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                          bodB.ispis()
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                      if len(self.spilKarata.spil)!=0:
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)
                  else:
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    print("Igrac B osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                    if len(self.spilKarata.spil)!=0:
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)
              else:
                if(self.baceneKarte[1].boja == globalnaZadnjaKarta[0].boja):
                  self.igracBPoeni.append(self.baceneKarte.pop())
                  self.igracBPoeni.append(self.baceneKarte.pop())
                  print("Igrac B osvojio poen")
                  if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                  if len(self.spilKarata.spil)!=0:
                    self.igracBKarte.append(self.spilKarata.spil.pop())
                    self.igracAKarte.append(self.spilKarata.spil.pop())
                    globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                    globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                  msg = spade.message.Message(
                  to="mvulin2@jabbers.one",
                  body="imamPrednost")
                  await self.send(msg)
                  
                  msg = spade.message.Message(
                  to="mvulin1@jabbers.one",
                  body="nemamPrednost")
                  await self.send(msg)

                elif(self.baceneKarte[0].boja == self.baceneKarte[1].boja): #boje jednake

                  if(self.baceneKarte[0].vrijednost>self.baceneKarte[1].vrijednost):
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    print("Igrac A osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                    if len(self.spilKarata.spil)!=0:
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)
                  

                  elif(self.baceneKarte[0].vrijednost==self.baceneKarte[1].vrijednost):
                    if(self.baceneKarte[0].brojka>self.baceneKarte[1].brojka):
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      print("Igrac A osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                      if len(self.spilKarata.spil)!=0:
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)

                    else:
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      print("Igrac B osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                      if len(self.spilKarata.spil)!=0:
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)
                  else:
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    print("Igrac B osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                    if len(self.spilKarata.spil)!=0:
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)
                  
                else:#znaci da ni A ni B nisu igrali aduta a B nije postivao boju
                  self.igracAPoeni.append(self.baceneKarte.pop())
                  self.igracAPoeni.append(self.baceneKarte.pop())
                  print("Igrac A osvojio poen")
                  if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                  if len(self.spilKarata.spil)!=0:
                    self.igracAKarte.append(self.spilKarata.spil.pop())
                    self.igracBKarte.append(self.spilKarata.spil.pop())
                    globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                    globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                  msg = spade.message.Message(
                  to="mvulin1@jabbers.one",
                  body="imamPrednost")
                  await self.send(msg)
                  
                  msg = spade.message.Message(
                  to="mvulin2@jabbers.one",
                  body="nemamPrednost")
                  await self.send(msg)

                

            else:
              print("napravi odluku kada igrac B baca prvi")
              #self.baceneKarte.reverse()
              if(self.baceneKarte[0].boja == globalnaZadnjaKarta[0].boja):
                if(self.baceneKarte[1].boja != globalnaZadnjaKarta[0].boja):
                  self.igracBPoeni.append(self.baceneKarte.pop())
                  self.igracBPoeni.append(self.baceneKarte.pop())
                  print("Igrac B osvojio poen")
                  if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                  if len(self.spilKarata.spil)!=0:
                    self.igracBKarte.append(self.spilKarata.spil.pop())
                    self.igracAKarte.append(self.spilKarata.spil.pop())
                    globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                    globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                  msg = spade.message.Message(
                  to="mvulin2@jabbers.one",
                  body="imamPrednost")
                  await self.send(msg)
                  
                  msg = spade.message.Message(
                  to="mvulin1@jabbers.one",
                  body="nemamPrednost")
                  await self.send(msg)

                else:#oba igraca su odigrali briskulu odnosno adut
                  if(self.baceneKarte[0].vrijednost>self.baceneKarte[1].vrijednost):
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    print("Igrac B osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                    if len(self.spilKarata.spil)!=0:
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)

                  elif(self.baceneKarte[0].vrijednost==self.baceneKarte[1].vrijednost):
                    if(self.baceneKarte[0].brojka>self.baceneKarte[1].brojka):
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      print("Igrac B osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                      if len(self.spilKarata.spil)!=0:
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)

                    else:
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      print("Igrac A osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                      if len(self.spilKarata.spil)!=0:
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)

                  else:
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    print("Igrac A osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                    if len(self.spilKarata.spil)!=0:
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)

              else:
                if(self.baceneKarte[1].boja == globalnaZadnjaKarta[0].boja):
                  self.igracAPoeni.append(self.baceneKarte.pop())
                  self.igracAPoeni.append(self.baceneKarte.pop())
                  print("Igrac A osvojio poen")
                  if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                  if len(self.spilKarata.spil)!=0:
                    self.igracAKarte.append(self.spilKarata.spil.pop())
                    self.igracBKarte.append(self.spilKarata.spil.pop())
                    globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                    globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                  msg = spade.message.Message(
                  to="mvulin1@jabbers.one",
                  body="imamPrednost")
                  await self.send(msg)
                  
                  msg = spade.message.Message(
                  to="mvulin2@jabbers.one",
                  body="nemamPrednost")
                  await self.send(msg)

                elif(self.baceneKarte[0].boja == self.baceneKarte[1].boja): #boje jednake

                  if(self.baceneKarte[0].vrijednost>self.baceneKarte[1].vrijednost):
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    self.igracBPoeni.append(self.baceneKarte.pop())
                    print("Igrac B osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                    if len(self.spilKarata.spil)!=0:
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)


                  elif(self.baceneKarte[0].vrijednost==self.baceneKarte[1].vrijednost):
                    if(self.baceneKarte[0].brojka>self.baceneKarte[1].brojka):
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      self.igracBPoeni.append(self.baceneKarte.pop())
                      print("Igrac B osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                      if len(self.spilKarata.spil)!=0:
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)

                    else:
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      self.igracAPoeni.append(self.baceneKarte.pop())
                      print("Igrac A osvojio poen")
                      if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                        for bodA in self.igracAPoeni:
                          self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        for bodB in self.igracBPoeni:
                          self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        print("Agent A")
                        print(self.igracAbodovi)
                        print("Agent B")
                        print(self.igracBbodovi)
                        self.kill(exit_code=10)
                        return
                        
                      if len(self.spilKarata.spil)!=0:
                        self.igracAKarte.append(self.spilKarata.spil.pop())
                        self.igracBKarte.append(self.spilKarata.spil.pop())
                        globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                        globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                      msg = spade.message.Message(
                      to="mvulin1@jabbers.one",
                      body="imamPrednost")
                      await self.send(msg)
                      
                      msg = spade.message.Message(
                      to="mvulin2@jabbers.one",
                      body="nemamPrednost")
                      await self.send(msg)

                  else:
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    self.igracAPoeni.append(self.baceneKarte.pop())
                    print("Igrac A osvojio poen")
                    if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                        bodA.ispis()
                      for bodB in self.igracBPoeni:
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                        bodB.ispis()
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                      
                    if len(self.spilKarata.spil)!=0:
                      self.igracAKarte.append(self.spilKarata.spil.pop())
                      self.igracBKarte.append(self.spilKarata.spil.pop())
                      globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                      globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                    msg = spade.message.Message(
                    to="mvulin1@jabbers.one",
                    body="imamPrednost")
                    await self.send(msg)
                    
                    msg = spade.message.Message(
                    to="mvulin2@jabbers.one",
                    body="nemamPrednost")
                    await self.send(msg)

                  
                else:#znaci da ni A ni B nisu igrali aduta a A nije postivao boju
                  self.igracBPoeni.append(self.baceneKarte.pop())
                  self.igracBPoeni.append(self.baceneKarte.pop())
                  print("Igrac B osvojio poen")
                  if(len(self.igracAPoeni)+len(self.igracBPoeni)==40):
                      for bodA in self.igracAPoeni:
                        bodA.ispis()
                        self.igracAbodovi=self.igracAbodovi+int(bodA.vrijednost)
                      for bodB in self.igracBPoeni:
                        bodB.ispis()
                        self.igracBbodovi=self.igracBbodovi+int(bodB.vrijednost)
                      print("Agent A")
                      print(self.igracAbodovi)
                      print("Agent B")
                      print(self.igracBbodovi)
                      self.kill(exit_code=10)
                      return
                  if len(self.spilKarata.spil)!=0:
                    self.igracBKarte.append(self.spilKarata.spil.pop())
                    self.igracAKarte.append(self.spilKarata.spil.pop())
                    globalneKarteIgracA.append(self.igracAKarte[len(self.igracAKarte)-1])
                    globalneKarteIgracB.append(self.igracBKarte[len(self.igracBKarte)-1])

                  msg = spade.message.Message(
                  to="mvulin2@jabbers.one",
                  body="imamPrednost")
                  await self.send(msg)
                  
                  msg = spade.message.Message(
                  to="mvulin1@jabbers.one",
                  body="nemamPrednost")
                  await self.send(msg)


  async def setup(self):
    print("Okruzije: Pokrećem se!")
    start_at = datetime.datetime.now() + datetime.timedelta(seconds=6)
    ponasanje = self.PosaljiPoruku(period=1, start_at=start_at)
    self.add_behaviour(ponasanje)   

class IgracA(Agent):
  class SvePoruke(CyclicBehaviour):
    async def on_start(self):
      self.sadrzaj = []
      self.brojacA=0
    
    async def run(self):
      msg = await self.receive(timeout=100)

      if msg:
        #print(self.brojacA)
        self.brojacA=self.brojacA+1
        #self.sadrzaj.append(msg.body)
        print(f"AgentA: Dobio sam: {msg.body} \n")
        if msg.body=="prviPotez":
          for a in globalneKarteIgracA:
            self.sadrzaj.append(a)
          print("dodao sam sadrzaj globalnih karata u sadrzaj svojih karata")
          odabranaKarata=0

          msg = spade.message.Message(
          to="mvulin3@jabbers.one",
          body=str(odabranaKarata),
          sender="mvulin1",
          metadata={"bacio": "0 kartu"})
          await self.send(msg)
          #self.sadrzaj.pop(odabranaKarata)

        elif msg.body=="imamPrednost":
          if self.brojacA<17:
            self.sadrzaj.append(globalneKarteIgracA[len(globalneKarteIgracA)-1])
          #print("AgentA:napravi algoritam sa prednošću")
          odabranaKarata=random.randint(0,len(self.sadrzaj)-1)
          msg = spade.message.Message(
          to="mvulin3@jabbers.one",
          body=str(odabranaKarata),
          sender="mvulin1",
          metadata={"bacio": "0 kartu"})
          await self.send(msg)
          #self.sadrzaj.pop(odabranaKarata)

        elif msg.body=="nemamPrednost":
          if self.brojacA<17:
            self.sadrzaj.append(globalneKarteIgracA[len(globalneKarteIgracA)-1])
          #print("AgentA:napravi algoritam kad si 2 na redu")
          minimalnaKarta=10
          indexMinimalneKarte=0
          for a in self.sadrzaj:
            if a.vrijednost<minimalnaKarta:
              minimalnaKarta=a.vrijednost
              indexMinimalneKarte=indexOf(self.sadrzaj,a)

          odabranaKarata=indexMinimalneKarte
          msg = spade.message.Message(
          to="mvulin3@jabbers.one",
          body=str(odabranaKarata),
          sender="mvulin1")
          await self.send(msg)
          #self.sadrzaj.pop(odabranaKarata)
          

       # for k in self.sadrzaj:
       #   k.ispis()
       # print("")
        if self.brojacA<18:
          self.sadrzaj.pop(odabranaKarata)
        
      else:
        print("IgracA: Čekao sam, ali nema poruke.")

              
  async def setup(self):
      print("IgracA: Pokrećem se!")
      ponasanjeSve = self.SvePoruke()
      self.add_behaviour(ponasanjeSve)

class IgracB(Agent):
  class SvePoruke2(CyclicBehaviour):
    async def on_start(self):
      self.sadrzaj = []
      self.brojacB=0
    
    async def run(self):
      msg = await self.receive(timeout=100)
      if msg:
        #print(self.brojacB)
        self.brojacB=1+self.brojacB
        if msg.body=="prviPotez":
          for b in globalneKarteIgracB:
            self.sadrzaj.append(b)
          print("AgentB:Dodao sam sadrzaj globalnih karata u svoj sadrzaj")
          odabranaKartaB=1

          msg = spade.message.Message(
          to="mvulin3@jabbers.one",
          body=str(odabranaKartaB),
          sender="mvulin2",
          metadata={"bacio": "0 kartu"})
          await self.send(msg)
          #self.sadrzaj.pop(odabranaKartaB)
        
        elif msg.body=="imamPrednost":
          if self.brojacB<17:
            self.sadrzaj.append(globalneKarteIgracB[len(globalneKarteIgracB)-1])
          #print("AgentB:napravi algoritam sa prednošću")
          odabranaKartaB=random.randint(0,len(self.sadrzaj)-1)
          msg = spade.message.Message(
          to="mvulin3@jabbers.one",
          body=str(odabranaKartaB),
          sender="mvulin2")
          await self.send(msg)
          #self.sadrzaj.pop(odabranaKartaB)

        elif msg.body=="nemamPrednost":
          if self.brojacB<17:
            self.sadrzaj.append(globalneKarteIgracB[len(globalneKarteIgracB)-1])
          #print("AgentB:napravi algoritam kad si 2 na redu")
          maksimalnaKarta=0
          indexMaksimalneKarte=0
          for a in self.sadrzaj:
            if a.vrijednost>maksimalnaKarta:
              maksimalnaKarta=a.vrijednost
              indexMaksimalneKarte=indexOf(self.sadrzaj,a)

          odabranaKartaB=indexMaksimalneKarte
          #print("max karta")
          #print(odabranaKartaB)
          msg = spade.message.Message(
          to="mvulin3@jabbers.one",
          body=str(odabranaKartaB),
          sender="mvulin2")
          await self.send(msg)
          #self.sadrzaj.pop(odabranaKartaB)

      #  for k in self.sadrzaj:
      #    k.ispis()
      #  print("")
        if self.brojacB<18:
          self.sadrzaj.pop(odabranaKartaB)

      else:
        print("IgracB: Čekao sam, ali nema poruke.")
              
  async def setup(self):
      print("IgracB: Pokrećem se!")
      ponasanjeSve2 = self.SvePoruke2()
      self.add_behaviour(ponasanjeSve2)



if __name__ == '__main__':
    igracA = IgracA("mvulin1@jabbers.one", "tajna")
    igracA.start()

    igracB = IgracB("mvulin2@jabbers.one", "tajna")
    igracB.start()

    okruzije = Okruzje("mvulin3@jabbers.one", "tajna")
    okruzije.start()

    input("Press ENTER to exit.\n")
    igracA.stop()
    igracB.stop()
    okruzije.stop()
    quit_spade()
