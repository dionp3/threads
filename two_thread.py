import threading
import time

filename = "data.txt"

# Thread 1: Membaca file
def read_file(data_container):
    with open(filename, "r") as f:
        data_container.append(f.read())

# Thread 2: Menampilkan data
def display_data(data_container):
    while not data_container:  # tunggu data terbaca
        pass
    print("Isi file:")
    print(data_container[0])  # tampilkan semua isi file

if __name__ == "__main__":
    start_time = time.time()  # waktu mulai

    data_container = []  # tempat penyimpanan sementara

    t1 = threading.Thread(target=read_file, args=(data_container,))
    t2 = threading.Thread(target=display_data, args=(data_container,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()
    print(f"\nWaktu eksekusi (2 thread): {end_time - start_time:.5f} detik")
