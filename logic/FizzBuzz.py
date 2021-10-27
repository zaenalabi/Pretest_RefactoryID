print ("menampilkan kata fizz buzz ")
print ()

n = int(input("masukkan jumlah range : "))

for fizzbuzz in range(n):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
     
    print(fizzbuzz)
    

