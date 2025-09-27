import os

filename = "data.txt"
jumlah_baris = 1_000  # ubah sesuai kebutuhan

if not os.path.exists(filename):
    print(f"{filename} belum ada. Membuat {jumlah_baris} baris...")
    with open(filename, "w") as f:
        for i in range(1, jumlah_baris + 1):
            f.write(f"Ini adalah baris ke-{i}\n")
    print(f"File '{filename}' berhasil dibuat.")
else:
    print(f"File '{filename}' sudah ada, langsung dipakai.")