riwayat = []
saldo = 0
programJalan = True

def format_angka (angka):
    return f'Rp.{angka:,.2f}'.replace(',', 'X').replace('.',',').replace('X','.')


print ('=== SISTEM PENCATATAN KEUANGAN SEDERHANA ===')

while programJalan:
    print('1, Tambah pemasukan')
    print('2, Tambah pengeluaran')
    print('3, Lihat riwayat transaksi')
    print('4, Lihat saldo ')
    print('5, Keluar')
    print('---------------------------------------------------------------------------')

    pilihan = input('Masukan pilihan dari 1 sampai 5: ')

    print('---------------------------------------------------------------------------')


    if pilihan == '1':
        keterangan = input('Masukan asal pemasukan: ')
        nominal = int(input('Masukan jumlah uang masuk: '))
        if nominal > 0:
            riwayat.append({
                'tipe' : 'masuk',
                'keterangan' : keterangan,
                'nominal' : nominal
            })
            saldo += nominal
            print('data transaksi tersimpan')
            print('---------------------------------------------------------------------------')
        else:
            print('keterangan dan nominal tidak valid')
            print('---------------------------------------------------------------------------')

            

    elif pilihan == '2':
        keterangan = input("Masukan jenis pengeluaran: ")
        nominal = int(input('Masukan jumlah uang keluar: '))
        if nominal > 0:
            riwayat.append({
                'tipe' : 'keluar',
                'keterangan': keterangan,
                'nominal': nominal
            })
            saldo -= nominal
            print('data transaksi tersimpan')
            print('---------------------------------------------------------------------------')
        else:
            print('jenis dan nominal tidak valid')
            print('---------------------------------------------------------------------------')

    
    
    
    elif pilihan == '3':
        print('+++ Riwayat transaksi +++')
        if len(riwayat) == 0:
           print('Belum ada transaksi')
        else:
            print(f'Keterangan {:<20}')
            for item in riwayat:
                hasil = format_angka(item['nominal'])
                if item['tipe'] == 'keluar':
                    hasil = '-' + hasil
                print(f'{item['keterangan']:<20}|{hasil:<22}')
        print('---------------------------------------------------------------------------')
    
   
   
    elif pilihan == '4':
        print(f'Saldo anda ada di angka Rp.{saldo:,.2f}'.replace(',', 'X').replace('.',',').replace('X','.'))
        print('---------------------------------------------------------------------------')

   
   
    elif pilihan == '5':
        print('Terima Kasih sudah menggunakan program ini')
        programJalan = False
        print('---------------------------------------------------------------------------')

    
    else:
        print('Pilihan tidak valid silahkan coba lagi')
        print('---------------------------------------------------------------------------')
