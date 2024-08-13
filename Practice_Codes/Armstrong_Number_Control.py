# 2024_07_06 Yusuf Delikkaya

# Check if the inputted number is an Armstrong number.

while True:
    sayı = input("Bir sayı girin.Çıkmak için ( q ) harfine basın.")

    if sayı == "q":
        print("Çıkış yaptınız.")
        break

    if int(sayı) == sum ( [ int(i) ** len(sayı)  for i in sayı ] ):
        print(f"Girilen sayı: {sayı} armstrong bir sayıdır.")
    
    else:
        print(f"Girilen sayı: {sayı} armstrong bir sayı değildir.")