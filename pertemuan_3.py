# Data Indexing List
x = ['Katib Pasha', 20, 'Desktop Programming', 3.99, True]
x.append("AMCC") #untuk menambah data dalam list
x.remove(20) # untuk menghapus data dalam list
# print(x)

angka = [1,2,3,4,5]
angka.reverse()
angka.sort()
# print(angka)


# Data Indexing Tuple
x = ('Desktop Programming',20,'Katib Pasha',3.99,"AMCC")
# print(len(x[0]))

y = (1,4,5,2,9,10)
# print(max(y))
# print(min(y))


# Data Indexing Set
z = {2,9,1,4,5,3,5}
# print(type(z))
# z.discard(3)
# z.remove(2)
# z.add(10)
z.update('AMCC')
# print(z)

# Data Indexing Dictionary
a = {'name':'Katib Pasha','division':'Desktop Programming','age': 20,'IP':3.99}
a.pop("IP")
a.pop("age")
a.clear()
# print(a)

# Input & Output
# panjang = input('Masukkan nilai panjang: ')
# lebar = input('Masukkan nilai lebar: ')

# luas = int(panjang) * int(lebar)
# print("Luas = ",luas)


# function
def halo_dunia():
    print('Halo Python! Halo Dunia!')

# halo_dunia()

def perkenalan(nama, asal):
    print("Perknelakan saya",nama,"dari", asal)

perkenalan("dandi","surabaya")
perkenalan("dodi","Kebumen")
perkenalan("Faisal","Bogor")