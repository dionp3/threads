import threading
import time

filename = "data.txt"
lock = threading.Lock()
results = {}

# Fungsi untuk membaca sebagian baris
def read_part(lines, thread_id):
    partial_data = "".join(lines)
    with lock:
        results[thread_id] = partial_data

def display_results(num_threads):
    while len(results) < num_threads:
        pass  # tunggu semua thread pembaca selesai
    print("\n=== Gabungan hasil pembacaan file ===")
    # Gabungkan data sesuai urutan thread
    combined_data = ""
    for i in range(num_threads):
        combined_data += results[i]
    print(combined_data)  # tampilkan semua isi file

if __name__ == "__main__":
    start_time = time.time()

    with open(filename, "r") as f:
        lines = f.readlines()

    num_threads = 3  # jumlah thread pembaca
    chunk_size = len(lines) // num_threads + 1

    threads = []
    for i in range(num_threads):
        part = lines[i*chunk_size:(i+1)*chunk_size]
        t = threading.Thread(target=read_part, args=(part, i))
        threads.append(t)
        t.start()

    # Thread untuk menampilkan hasil
    t_display = threading.Thread(target=display_results, args=(num_threads,))
    t_display.start()

    for t in threads:
        t.join()
    t_display.join()

    end_time = time.time()
    print(f"\nWaktu eksekusi (multi-thread): {end_time - start_time:.5f} detik")
