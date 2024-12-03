# Format string
# kata kunci 'if' '()'

#contoh umum
# tipe data
nama = "ishigami senku"
format_str = (f"selamat datang {nama}")
print (format_str)
print (f"selamat datang {nama}")

# tipe data boolean
bool_var = False
format_str = f"boolean: (bool_var)"
print (format_str)
print (type (bool))
print (type (format_str))

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print (format_str)

# bilangan bulat
angka = 10
format_str = f"bilangan bulat: {angka: d}"
print (format_str)

# bilangan dengan ordo ribuan
angka = 2000000 # 2,000,000
format_str = f'jutaan = (angka:,)'
print (format_str)

#bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print (format_str)

# menampilkan tanda atau tanda
angka_minus = -10
angka_plus = +10.54321
format_minus = f" minus: (angka_minus= -10)"
format_plus = f" plus (angka_plus: + .2f)"

print(format_minus)
print(format_plus)

# format persen
persentase = 0.025
format_persen = f"persen = (persentase :.2%)"
print (format_persen)

# melakukan operasi artitmatika
harga = 5000
jumlah = 5

format_string = f"harga total Rp. (harga*jumlah:,)"
print("format_string")