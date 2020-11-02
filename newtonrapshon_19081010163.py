# -*- coding: utf-8 -*-
"""NewtonRapshon_19081010163

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N7YhhyGtT3124XBxcwJdOtH2GlwPJxXI

#Metode Newton-Raphson 
adalah metode pencarian akar suatu fungsi f(x) dengan pendekatan satu titik, dimana fungsi f(x) mempunyai turunan. Metode ini menggunakan pendekatan satu titik sebagai titik awal. Semakin dekat titik awal yang kita pilih dengan akar sebenarnya, maka semakin cepat konvergen ke akarnya.

# algortima
1. Mulai

2. Definisikan fungsi sebagai f (x)

3. Definisikan turunan pertama dari f (x) g (x) g (x) i (x)

4. Masukkan bilangan pertama,koefisiensi x,konstantan,perkiraan awal (atas), kesalahan yang dapat ditoleransi (error) 
   dan iterasi maksimum (bawah)

5. Inisialisasi pencacah iterasi i = 1

6. Jika g (atas) = 0 maka cetak "Error" 
   dan pergi (12) jika tidak pergi (7) 

7. Calcualte x1 = atas - f (atas) / tambah (atas) untuk penjumlahan dan calcualte x1= atas - f(atas)/kurang(atas) untuk pengurangan

8. Penghitung iterasi kenaikan i = i + 1

9. Jika i> = N maka cetak "tidak konvergen" 
   dan pergi (12) jika tidak pergi (10) 

10. Jika | f (x1) | > e kemudian atur atas = x1
    dan pergi (6) jika tidak pergi (11)

11. Cetak hasil sebagai x1

12. Berhenti

# pseudocode
1. Mulai

2. Definisikan fungsi sebagai f (x)

3. Definisikan turunan dari fungsi sebagai g (x)

4. Masukan:
	Sebuah. Tebakan awal atas
	b. Kesalahan yang Dapat Ditoleransi error
	c. Iterasi Maksimum bawah

5. Inisialisasi langkah penghitung iterasi = 1

6. Lakukan 
	Jika  bawah(atas) = 0
		Cetak "error"
		Berhenti
	Berakhir jika

	jika oprerator +
	x1 = atas - f (atas)/tambah(atas)
  atas = x1

	jika operator -
	x1 = atas - h(atas)/kurang(atas)
	
	langkah = langkah + 1
	
	Jika langkah> bawah
		Cetak "Tidak Konvergen"
		Berhenti
	Berakhir jika

   Sedangkan abs f (x1)> e 

7. Cetak root sebagai x1

8. Berhenti
"""

#ka =kofiensi pertama
#a  =bilangan pertama
#ap =operator pertama
#kb =koefisien kedua
#b  =bilangan kedua
#bp =operator kedua
#k  =kosntanta

print('======================== metode newton raphson ========================')
#mendefinisikan fungsi persamaan
def f(x):
    return ka**x**a + kb*x+k

def tambah(x):                            #jika user memasukan + sebagai perhitungan maka fungsi ini terpanggil
    return ka*a*x*(a-1) + kb*b*(b-1)

def g(x):
    return ka*x**a + kb*x-k

def h(x):
    return ka*x**a - kb*x+k

def kurang(x):                          #jika user memasukan - sebagai perhitungan maka fungsi ini terpanggil
    return ka*a*x**(a-1) - kb*b**(b-1)

def i(X):
    return ka*x**a - kb*x-k

#masukan persamaan yang akan digunakan
a   =float(input("bilangan pertama A: "))       #masukan untuk bilangan pertama yang akan dipangkatkan
ka  =float(input("koefisien pertama A: "))      #masukan untuk koefiesiensi pertama dari persamaan yang akan dimasukan
ap  =input("+:")
if(ap=='+'):
  b  = float(input("bilangan kedua B : "))      #masukan untuk bilangan kedua yang akan dipangkatkan
  kb = float(input("koefiesien kedua B :"))     #masukan untuk koefiesiensi kedua
  bp = input("+:")
  if(bp=='+'):
      k       = float(input("kosntanta:"))         #masukan untuk konstanta persamaan
      atas    = float(input('batas atas :'))       #masukan untuk batas atas/titikawal
      error   = float(input('error :'))            #masukan untuk toleransi error
      bawah   = int(input('batas bawah :'))        #masukan untuk batas bawah
      awal = 1
      flag = 1
      condition = True
      while condition:
          if tambah(atas) == 0.0:                                                
              print('dibagi dengan 0')
              break 

          x1 = atas - f(atas)/tambah(atas)
          print('Iterasi| %d|    x1 = %0.6f dan f(x1) = %0.6f' % (awal, x1,f(x1)))
          atas = x1
          awal = awal + 1
          condition = abs(f(x1)) > error

      if flag==1:
          print('\nHasil iterasi: %0.8f' % x1)
      else:
          print('tidak konvergen')      
  else:
      k       = float(input("kosntanta:"))          
      atas    = float(input('batas atas :') )            
      error   = float(input('error :')  )              
      bawah   = int(input('batas bawah :'))
      awal = 1
      flag = 1
      condition = True
      while condition:
          if tambah(atas) == 0.0:
              print('dibagi dengan 0')
              break   

          x1 = atas - g(atas)/tambah(atas)
          print('Iterasi| %d| x1 = %0.6f dan f(x1) = %0.6f' % (awal, x1,g(x1)))
          atas = x1
          awal = awal + 1
          
          if awal > bawah:
              flag = 0
              break

          condition = abs(g(x1)) > error  
          if flag==1:
              print('\nHasil iterasi: %0.8f' % x1)
          else:
              print('tidak konvergen')
else:
    b  = float(input("bilangan kedua B : "))      #masukan untuk bilangan kedua yang akan dipangkatkan
    kb = float(input("koefiesien kedua B :"))     #masukan untuk koefiesiensi kedua
    bp = input("+:")
    if(bp=='+'):
      k       = float(input("kosntanta:"))          
      atas    = float(input('batas atas :'))             
      error   = float(input('error :'))                
      bawah   = int(input('batas bawah :'))
      awal = 1
      flag = 1
      condition = True
      while condition:
          if kurang(atas) == 0.0:
              print('dibagi dengan 0')
              break   
          x1 = atas - h(atas)/kurang(atas)
          print('Iterasi| %d|    x1 = %0.6f dan f(x1) = %0.6f' % (awal, x1,h(x1)))
          atas = x1
          awal = awal + 1

          if awal > bawah:
            flag=0
            break


          condition = abs(h(x1)) > error  
          if flag==1:
              print('\nHasil iterasi: %0.8f' % x1)
          else:
              print('tidak konvergen')
    else:
      k       = float(input("kosntanta:"))          
      atas    = floatt(input('batas atas :'))             
      error   = float(input('error :'))                
      bawah   = int(input('batas bawah :'))
      awal = 1
      flag = 1
      condition = True
      while condition:
          if kurang(atas) == 0.0:
              print('dibagi dengan 0')
              break   
          x1 = atas - i(atas)/kurang(atas)
          print('Iterasi| %d|    x1 = %0.6f dan f(x1) = %0.6f' % (awal, x1,i(x1)))
          atas = x1
          awal = awal + 1
          condition = abs(i(x1)) > error

          if flag==1:
              print('\nHasil iterasi: %0.8f' % x1)
          else:
              print('tidak konvergen')

#masukan argumen fungsi diatas
atas = float(atas)
error = float(error)
bawah = int(bawah)

#mengambil fungsi dan mecetak fungsi tersebut
print("Hasil dari perhitungan tersebut:")

#@alston with colaborator