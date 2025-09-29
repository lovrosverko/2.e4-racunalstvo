# Izbornik za kalkulator
print("----------------------")
print("Izbornik za kalkulator")
print("----------------------")
print("1. Izračun napona struje")
print("2. Izračun otpora struje")
print("3. Izračun jakosti struje")
print("----------------------")
opcija = int(input("Izaberite operaciju (1 / 2 / 3):"))
#Struktura grananja
if opcija == 1:     # == != < > <> >= <= - operatori usporedbe
    print("Izračun napona struje")
    jakost = int(input("Upiši jakost struje: "))
    otpor = int(input("Upiši otpor: "))
    napon = jakost*otpor
    print(f"Napon struje je: {napon} V")
elif opcija == 2:
    print("Izračun otpora struje")
    napon = int(input("Upiši napon: "))
    jakost = int(input("Upiši jakost struje: "))
    otpor = napon/jakost
    print(f"Otpor je: {otpor} Ohm")
elif opcija == 3:
    print("Izračun jakosti struje")
    napon = int(input("Upiši napon: "))
    otpor = int(input("Upiši otpor: "))
    jakost = napon/otpor
    print(f"Jakost struje je: {jakost} A")
else:
    print("Pogrešan unos")
    

