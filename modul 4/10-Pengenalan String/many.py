# string adalah kumpulan dari karakter

data = "nilai adalah string"
print(data)
print("panjang karakter : ", len (data))
print("tipe data : ", type (data))

# 1. cara membuat string

"""
1. dengan menggunakan single quete '...'
2. dengan menggunakan doubel quote '...'
"""

data = 'menggunakan single quete'
print (data)

data = "menggunakan doubel quote"
print (data)

print("ini adalah hari jum'at")
print("nama saya ma'ruf")

# 2. kekuatan tanda \

# membuat ' menjadi string
print('mari sholat jum\'at')
print('Saya ma\'ruf') 

# doubel backslash
print('C: \\user\\adam')

# tap (\b)
print("MU\t\tJuara")

# backspace (\b)
print("MU\bJuara")

# newline (enter)
print("baris satu.\nabaris dua.") # LF ->line feed # macOS
print ("baris satu. \n\rbaris dua.") # CRLF -> windows

# raw string
print (r"C:\user\adam")