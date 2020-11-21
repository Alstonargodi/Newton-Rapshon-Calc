#MetodeNewton-Raphson 

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
