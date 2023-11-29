#1
nimi=input("Teie nimi on? ")
print("Tere,", nimi)

#2
print(int(3+8/(4-2)*4)) #Пример решаеться по верной очерёдности, начиная с внутрених скобок

print(int(3+8/4-2*4)) #Пример решаеться начиная с 

#2.1
import math

radius=float(input("radius kruga: "))

storona_kvadrata= 2*radius #или sqrt() 

ploshad_kvadrata= radius*radius 

perimetr_kvadrata= 4*storona_kvadrata

ploshad_kruga= math.pi * radius**2  #S=pi*R**2

dlina_okruznosti= 2*math.pi*radius

print("storona kvadrata", storona_kvadrata)
print("plashad kvadrata", ploshad_kvadrata)
print("perimetr kvadrata", perimetr_kvadrata)
print("ploshad kruga", ploshad_kruga)
print("dlina_okruznosti", dlina_okruznosti)

#2.2
diametr_moneti= 0.00002575

print("diametr moneti:",diametr_moneti,"km")

radius_zemli= 6378

print("radius_zemli:",radius_zemli,"km")

diametr_zemli= radius_zemli * 2

print("diametr_zemli:",diametr_zemli,"km")

okruznst_zemli= diametr_zemli * 3.141

print("okruznst_zemli:",okruznst_zemli,"km")

skolko_monet= okruznst_zemli / diametr_moneti

print("ctolko monet nado stobi rad oboshol zemlu",int(skolko_monet))


#3

pervoe= "kill-koll"
vtoroe= "killadi-koll"
trete= "killkoll"

print("{0} {0} {1} {0} {0} {1} {0} {0} {2} {0}".format(pervoe,vtoroe,trete))


#4

pervoe= "tsuhh tsuhh tsuhh"

vtoroe= "rat tat taa"

print("Rong see sõitis {0},\npiilupart oli rongijuht.\nRattad tegid {1},\n{1} ja {1}.\nAga seal rongi peal,\nkas sa tead, kes olid seal?".format(pervoe,vtoroe))


#5


shirina= float(input("shirina pramougolnika: "))

dlina= float(input("dlina pramougolnika: "))

ploshad=(shirina+dlina)*2

perimetr=shirina * dlina

print("ploshad: ", ploshad)

print("perimetr: ", perimetr)


#6 

litri=float(input("zapravleno litrov: "))

rastojanie=float(input("proideno rastijanie v km: "))

sredni=float((litri / rastojanie)*100)

print("sredni rashod topliva", sredni)


#7 

skorost=29.9 

M=float(input("vvedite vrjema v minutah: "))

vrjema= M / 60

za_skolko=skorost * vrjema

print("rolikovi konkor projdet {3} killometrov za {1} minut".format(skorost,M,vrjema,za_skolko))


#8

Vremja=int(input("vrejema: "))

v_chas=Vremja//60

v_minuti=Vremja % 60

print("vvod {1}:{2}".format(Vremja,v_chas,v_minuti))