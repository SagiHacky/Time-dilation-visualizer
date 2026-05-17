import math
import matplotlib.pyplot as plt
import os
import random

plt.style.use("seaborn-v0_8-whitegrid")

c = int(299792458)
speeds = []
times = []
distances = []
moments = []

časJedna = int(input("Časový interval v letech: ")) * 31536000
rychlostUživatele = int(input("Rychlost v metrech za sekundu: "))
časJednaVLetech = časJedna / 31536000
vzdálenostJedna = int(input("Vzdálenost potřebná pro uletení v světelných letech: "))
hmotnostVKg = int(input("Hmotnost tělesa v kilogramech: "))

if rychlostUživatele > c:
    print("Chyba, rychlost je větší než rychlost světla!")
    exit()

elif rychlostUživatele < 0:
    print("Chyba, rychlost je menší než 0!")
    exit()

for rychlost in range(0,c,100000):
    rychlostNaDruhou = math.pow(rychlost, 2)
    rychlostCNaDruhou = math.pow(c, 2)
    podOdmocninou = 1 - (rychlostNaDruhou / rychlostCNaDruhou)
    časFinální = (časJedna / math.sqrt(podOdmocninou))
    speeds.append(rychlost)
    times.append(časFinální / 31536000)
    distances.append(vzdálenostJedna * math.sqrt(podOdmocninou))
    moments.append(hmotnostVKg * rychlost / math.sqrt(podOdmocninou))

rychlostNaDruhou = math.pow(rychlostUživatele, 2)
rychlostCNaDruhou = math.pow(c, 2)
podOdmocninou = 1 - (rychlostNaDruhou / rychlostCNaDruhou)
časFinální = (časJedna / math.sqrt(podOdmocninou)) / 31536000
kontrakovanáVzdálenost = vzdálenostJedna * math.sqrt(podOdmocninou)
momentumUživatele = hmotnostVKg * rychlostUživatele / math.sqrt(podOdmocninou)

plt.figure(figsize=(18, 6))
plt.subplot(1, 4, 1)
plt.scatter(speeds, times, label="Časová dilatace", color="steelblue")
plt.scatter(rychlostUživatele, časFinální, color="crimson", zorder=5, label="Tvoje rychlost")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Rychlost")
plt.ylabel("Čas")
plt.title("Časová dilatace")
plt.grid(color="gray", alpha=0.3)
plt.annotate("Změna času je " + str(round(časFinální - časJednaVLetech, 2)) + " let", xy=(rychlostUživatele, časFinální), xytext=(20000000, max(times) * 0.9))
plt.axvline(x=c, color="yellow", linestyle="--", label="Rychlost světla")
plt.legend()

plt.subplot(1, 4, 2)
plt.plot([0, časJednaVLetech], [0, časJednaVLetech], label="Kosmický dvojče", color="blue")
plt.plot([0, časJednaVLetech], [0, časFinální], label="Dvojče na Zemi", color="green")
plt.xlabel("Čas lodi")
plt.ylabel("Věk")
plt.title("Paradox dvojčat")
plt.annotate("Kosmický dvojče je o " + str(round(časFinální - časJednaVLetech, 2)) + " let mladší!", xy=(časJednaVLetech, časFinální), xytext=(časJednaVLetech * 0.1, časFinální * 0.8))
plt.grid(color="gray", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.margins(0)
plt.scatter(časJednaVLetech, časJednaVLetech, color="blue", zorder=5, s=100)
plt.scatter(časJednaVLetech, časFinální, color="green", zorder=5, s=100)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.subplot(1, 4, 3)
plt.scatter(speeds, distances, label="Délková kontrakce", color="mediumpurple")
plt.scatter(rychlostUživatele, kontrakovanáVzdálenost, color="crimson", zorder=5, label="Tvoje rychlost")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Rychlost")
plt.ylabel("Vzdálenost (světelné roky)")
plt.title("Délková kontrakce")
plt.grid(color="gray", alpha=0.3)
plt.axvline(x=c, color="yellow", linestyle="--", label="Rychlost světla")
plt.legend()

plt.subplot(1,4,4)
plt.scatter(speeds, moments, label="Relativní momentum", color="teal")
plt.scatter(rychlostUživatele, momentumUživatele, color="crimson", zorder=5, label="Tvoje rychlost")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Rychlost")
plt.ylabel("Hmotnos (Kg)")
plt.title("Relativní momentum")
plt.grid(color="gray", alpha=0.3)
plt.axvline(x=c, color="yellow", linestyle="--", label="Rychlost světla")
plt.legend()

filename = "Celé.png"
counter = 1
while os.path.exists(filename):
    filename = "Celé" + str(counter) + ".png"
    counter += 1
plt.savefig(filename)

plt.show()