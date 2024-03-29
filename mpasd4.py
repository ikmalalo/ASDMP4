from prettytable import PrettyTable

class CircularNode:
    def __init__(self, robux):
        self.robux = robux
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambahcircularlinkedlist(self, robux):
        new_node = CircularNode(robux)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("Circular Linked Listnya kosong")
        else:
            temp = self.head
            while True:
                print(f"Kode Robux: {temp.robux.kode}, Paket Robux: {temp.robux.paket_robux}, "
                    f"Paket Subscription: {temp.robux.paket_subscription}, Harga: {temp.robux.harga}, "
                    f"Diskon: {temp.robux.diskon}%")
                temp = temp.next
                if temp == self.head:
                    break
class akun:
    def __init__(self, nama, emoney):
        self.nama = nama
        self.emoney = emoney

class Robux:
    def __init__(self, kode, paket_robux, paket_subscription, harga, diskon):
        self.kode = kode
        self.paket_robux = paket_robux
        self.paket_subscription = paket_subscription
        self.harga = harga
        self.diskon = diskon

class CRUD:
    def __init__(self):
        self.daftar_robux = {
            "KOP13": Robux("KOP13", 600, 400, 70000, 12),
            "HGH67": Robux("HGH67", 400, 200, 50000, 12),
            "KAS12": Robux("KAS12", 700, 500, 80000, 12),
            "HO9SA": Robux("HO9SA", 500, 300, 60000, 12),
            "SO125": Robux("SO125", 800, 600, 90000, 12)
        }
        self.circular_linked_list = CircularLinkedList()
        self.table = PrettyTable()


    def lihat_robux(self):
        if not self.daftar_robux:
            print("Data Robux tidak ada")
        else:
            table = PrettyTable()
            table.field_names = ["No", "Kode Robux", "Paket Robux", "Paket Subscription", "Harga", "Diskon"]

            for idx, (kode_robux, robux) in enumerate(self.daftar_robux.items(), start=1):
                rupiah = f"Rp.{robux.harga}"
                persen = f"{robux.diskon}%"
                table.add_row([idx, kode_robux, robux.paket_robux, robux.paket_subscription, rupiah, persen])
            print(table)

    def quicksort(self, arr, reverse=False):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0].harga
            kecil = [robux for robux in arr[1:] if robux.harga < pivot]
            besar = [robux for robux in arr[1:] if robux.harga >= pivot]

            if reverse:
                return self.quicksort(besar, reverse=True) + [arr[0]] + self.quicksort(kecil, reverse=True)
            else:
                return self.quicksort(kecil) + [arr[0]] + self.quicksort(besar)

    def robuxkodejumpsearch(self, hurufawal):
        if not self.daftar_robux:
            print("Data Robux tidak ada di tabel")
        else:
            kodefilter = [robux for robux in self.daftar_robux.values() if robux.kode.startswith(hurufawal.upper())]

            if not kodefilter:
                print(f"Kode huruf awal yang Anda masukkan tidak ada '{hurufawal}'")
                return

            urutrobux = sorted(kodefilter, key=lambda robux: robux.kode)

            table = PrettyTable()
            table.field_names = ["No", "Kode Robux", "Paket Robux", "Paket Subscription", "Harga", "Diskon"]

            for idx, robux in enumerate(urutrobux, start=1):
                rupiah = f"Rp.{robux.harga}"
                persen = f"{robux.diskon}%"
                table.add_row([idx, robux.kode, robux.paket_robux, robux.paket_subscription, rupiah, persen])
            print(table)

            hurufawal = hurufawal.upper()
            panjang_data_robux = len(urutrobux)
            jumpsearch = int(panjang_data_robux ** 0.5)
            cekindex = 0
            while urutrobux[min(jumpsearch, panjang_data_robux) - 1].kode < hurufawal:
                cekindex = jumpsearch
                jumpsearch += int(panjang_data_robux ** 0.5)
                if cekindex >= panjang_data_robux:
                    print(f"Kode '{hurufawal}'yang di masukkan tidak ada")
                    return
            while urutrobux[cekindex].kode < hurufawal:
                cekindex += 1
                if cekindex == min(jumpsearch, panjang_data_robux):
                    break
        
    def tambahcircularlinkedlist(self, kode_robux):
        robux = self.daftar_robux.get(kode_robux)
        if robux:
            self.circular_linked_list.tambahcircularlinkedlist(robux)
            print(f"Kode Robux {kode_robux} dari table sudah ditambahkan ke Circular Linked List")
        else:
            print(f"Kode {kode_robux} Robux Yang Anda Masukkan Tidak Ada")
    
    def lihatcircularlinkedlist(self):
        self.circular_linked_list.display()
    
    def tambah_robux(self):
        kode_robux = input("Masukkan Kode robux: ")
        paket_robux = input("Masukkan Paket robux: ")
        paket_subscription = input("Masukkan Paket Subscription Robux: ")
        harga = input("Masukkan Harga Robux: ")
        diskon = input("Apakah anda ingin menambahkan diskon? (y/n): ")

        if diskon == "y":
            tambah_diskon = int(input("Masukin Diskon untuk paket ini: "))
        else:
            tambah_diskon = 0

        self.daftar_robux[kode_robux] = Robux(kode_robux, paket_robux, paket_subscription, harga, tambah_diskon)
        print("Data Robux Sudah ditambahkan di table")

    def edit_robux(self):
        kode_robux = input("Masukkan Kode Robux yang mau di edit: ")

        while kode_robux in self.daftar_robux:
            robux = self.daftar_robux[kode_robux]
            print(f"Data Robux untuk Kode {kode_robux}:")
            print(f"1. Paket Robux: {robux.paket_robux}")
            print(f"2. Paket Subscription: {robux.paket_subscription}")
            print(f"3. Harga Robux: {robux.harga}")
            print(f"4. Diskon: {robux.diskon}%")

            pilih = input("Pilih data yang ingin diubah 1-4, atau 0 untuk keluar: ")

            if pilih == "0":
                break

            if pilih in ["1", "2", "3", "4"]:
                if pilih == "1":
                    robux.paket_robux = input("Masukkan Paket Robux baru: ")
                elif pilih == "2":
                    robux.paket_subscription = input("Masukkan Paket Subscription baru: ")
                elif pilih == "3":
                    robux.harga = input("Masukkan Harga Robux baru: ")
                elif pilih == "4":
                    robux.diskon = input("Masukkan Diskon baru: ")
                else:
                    print("Pilihan tidak ada")
            else:
                print("Pilihan tidak ada. coba masukkin angka 1-4 atau 0 untuk kembali.")
        else:
            print(f"Kode {kode_robux} Robux Yang Anda Masukkan Salah!")

    def hapus_robux(self):
        kode_robux = input("Masukkan Kode Robux yang mau di hapus dari tabel: ")

        if kode_robux in self.daftar_robux:
            del self.daftar_robux[kode_robux]
            print("Sudah terhapus")
        else:
            print(f"Kode {kode_robux} Robux Yang Anda Masukkan Tidak Ada")

    def menu_admin(self):
        while True:
            print("\n==== Selamat Datang Admin ====")
            print("1. Lihat Robux di tabel")
            print("2. Tambah Data Robux")
            print("3. Ubah Data Robux")
            print("4. Hapus Data Robux")
            print("5. Lihat Hagra Robux di tabel (Terkecil)")
            print("6. Lihat Harga Robux di tabel (Terbesar)")
            print("7. Cari Robux menggunakan jumpsearc dengan kode awal")
            print("8. Tambah Data robux tabel ke Circular Linked List")
            print("9. Lihat Circular Linked List")
            print("10. Keluar")

            pilih = input("Pilih menu (1-10): ")

            if pilih == "1":
                self.lihat_robux()
            elif pilih == "2":
                self.tambah_robux()
            elif pilih == "3":
                self.edit_robux()
            elif pilih == "4":
                self.hapus_robux()
            elif pilih == "5":
                self.urutan_robux()
            elif pilih == "6":
                self.urutan_robux(reverse=True)
            elif pilih == "7":
                hurufawal = input("Masukkan huruf kode yang anda mau: ")
                self.robuxkodejumpsearch(hurufawal)
            elif pilih == "8":
                kode_robux = input("Masukkan Kode Robux dari tabel yang ingin ditambahkan ke Circular Linked List: ")
                self.tambahcircularlinkedlist(kode_robux)
            elif pilih == "9":
                self.lihatcircularlinkedlist()
            elif pilih == "10":
                break

class TopUp:
    def __init__(self, daftar_robux):
        self.daftar_robux = daftar_robux

    def lihat_robux(self):
        if not self.daftar_robux:
            print("Daftar Robux tidak ada")
        else:
            table = PrettyTable()
            table.field_names = ["No", "Kode Robux", "Paket Robux", "Paket Subscription", "Harga", "Diskon"]

            for idx, (kode_robux, robux) in enumerate(self.daftar_robux.items(), start=1):
                rupiah = f"Rp.{robux.harga}"
                persen = f"{robux.diskon}%"
                table.add_row([idx, kode_robux, robux.paket_robux, robux.paket_subscription, rupiah, persen])
            print(table)

    def beli_robux(self, player, kode_robux, jumlah_robux):
        if kode_robux in self.daftar_robux:
            robux = self.daftar_robux[kode_robux]
            harga_per_robux = float(robux.harga)
            total_harga = harga_per_robux * jumlah_robux

            if robux.diskon > 0:
                diskon_amount = (robux.diskon / 100) * total_harga
                total_harga -= diskon_amount

            print(f"\n===== Struk Pembelian Atas Nama {player.nama} =====")
            print(f"Robux yang anda beli: {jumlah_robux} Robux")
            print(f"Paket Robux Yang Anda Beli Ada Diskon {robux.diskon}%")
            print(f"Jadi Total Harga Anda Menjadi: Rp.{int(total_harga)} dari Rp.{int(robux.harga)} menjadi Rp.{int((robux.diskon / 100) * harga_per_robux * jumlah_robux)}")

            if total_harga <= player.emoney:
                player.emoney -= total_harga
                print(f"Berhasil Dibeli Sekarang Sisa E-Money Anda: Rp.{int(player.emoney)}")
            else:
                print("Maaf E-Money Anda tidak Cukup")
        else:
            print(f"Kode {kode_robux} Robux Yang Anda Masukkan Salah!")

    def menu_player(self, player):
        while True:
            print(f"\n==== Selamat Datang {player.nama} ====")
            print("1. Lihat List harga paketan robux")
            print("2. Beli Robux")
            print("3. Lihat Harga Robux Terkecil")
            print("4. Lihat Harga Robux Terbesar")
            print("5. Keluar")

            pilih = input("Pilih menu(1-3): ")

            if pilih == "1":
                self.lihat_robux()
            elif pilih == "2":
                kode_robux = input("Masukkan kode Robux yang ingin dibeli: ")
                jumlah_robux = int(input("Masukkan Jumlah Paket Robux yang ingin dibeli: "))
                self.beli_robux(player, kode_robux, jumlah_robux)
            elif pilih == "3":
                self.urutuan_robux()
            elif pilih == "4":
                self.urutuan_robux(reverse=True)
            elif pilih == "5":
                break

def menu_login():
    admin_crud = CRUD()
    while True:
        print("\n==== Selamat Datang di Toko Robux Kami ====")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Player")
        print("3. Keluar")

        pilih = input("Pilih menu (1-3): ")

        if pilih == "1":
            admin_crud.menu_admin()
        elif pilih == "2":
            xakun = akun("ikmalgans", 1000000) 
            player_topup = TopUp(admin_crud.daftar_robux)
            player_topup.menu_player(xakun)
        elif pilih == "3":
            print("Terima kasih. Sudah Mampir Di Toko Kami!")
            break 
        else:
            print("Pilihan Gak Ada Coba masukkan angka 1-3.")
            break 
        
if __name__ == "__main__":
    menu_login()
        
crud = CRUD()
crud.menu_admin()
topup = TopUp(crud.daftar_robux)
topup.menu_player(akun) 
