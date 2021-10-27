def kabisat(tahun):
  habis_dibagi_400 = tahun % 400 == 0
  habis_dibagi_100 = tahun % 100 == 0
  habis_dibagi_4 = tahun % 4 == 0

  return habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100)

tahun_awal = int(input('Masukkan tahun awal: '))
tahun_akhir = int(input('Masukkan tahun akhir: '))
print()

tahun_kabisat = []

for tahun in range(tahun_awal, tahun_akhir + 1):
  if kabisat(tahun):
    tahun_kabisat.append(tahun)

print('Daftar Tahun kabisat:')
print(tahun_kabisat)
