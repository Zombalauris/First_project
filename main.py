nivele_brad=int(input("Cate nivele sa aibe bradul? "))
interval=range(2,20)
if nivele_brad in interval:
     print ("OK, bradul este realizabil")
     print ("Asa arata bradul:")
else:
     print("Bradul nu este realizabil")

x= "*"
# pentru_trunchi=interval[len(interval)-2:][0]
  # nivel_de_brad=nivele_brad(map(double(fiecare_nivel)))
  #   range[1]==x

for fiecare_nivel in range(0,nivele_brad):
    stelute_pe_rand="*"* fiecare_nivel + "*"
    spatii= " ><"*5
    print(spatii+ stelute_pe_rand)
