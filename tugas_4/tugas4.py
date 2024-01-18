# file I/O ada dua mode
# mode pertama -> baca (READ) r
# mode kedua -> tulis (WHITE) w

if __name__ == "__main__":
    nama_file = "contoh.txt"
    text = "hai manusia"

    # contoh write
    with open(nama_file, "w") as f:
        f.write(text)

    # contoh read
    with open(nama_file, "r") as f:
        print(f.read())