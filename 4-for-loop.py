#!/usr/bin/python3

import subprocess

for ch in "banana":
    print(ch)


paths_list = ["/etc", "/var/log", "/srv"]
print()
for path in paths_list:
    subprocess.run(["ls", "-ld", path])


print()
for machine in range(101, 104, 1):
    ip_address = "192.168.122." + str(machine)
    print(ip_address)


veggies_list = ["potato", "carrot", "radish"]
print()
for veggy in veggies_list:
    if veggy == "radish":
        break
    print(veggy)
