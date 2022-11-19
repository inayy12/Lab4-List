print('#Akses List')
r = [8,6,4,9,2]
print(r)
print('- Elemen ke-3 : ', r[3])
print('-Nilai Elemen ke-2 Sampai Elemen ke-4 : ',r[2:5])
print('-Elemen Terakhir : ', r[-1])

print('# Mengubah Elemen List')
a = ['Asahi', 'Yhosi', 6,18,21]
print(a)
a[1]='Haruto'
print('- mengubah data kedua : ', a)
a[4:5]=12,16
print('- Mengubah data ke-4 sampaidata Terakhir: ', a)
print(a)

print('# Menambahkan Elemen List')
n = ['Landak', 'Singa', 'Serigala', 'kupu-kupu', 'koala']
print(n)
A = n[0:2]
B = n[2:]
print(A)
print(B)
B.append('Harimau')
print('- Menambahkan list B Dengan Nlai String : ', B)
B.extend([3, 6, 8])
print('- Menambahkan List B Dengan 3 Nilai : ',B)
B.extend(A)
print('-Menggabungkan List B Dengan List A : ', B)



