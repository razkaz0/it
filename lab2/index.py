h=180 #сантиметры 
w=74
stepCount=10000
time=60 #минуты
steplengt=h/4 +0.37
s=steplengt*stepCount/100 # из сантиметров в метры
v=s/time
energyCount=0.035* w +(v*v/h)*0.029*w
a=s/1000
print("Расстояние в м" , s)
print("Кол-во энергии", energyCount)
print("Дистанция в км" , a)
if a<2:
    print("Нужно ходить больше")
elif a<4:
    print("Ты почти у цели")
else:
    print("Ты супер крут")
