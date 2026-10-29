nilai = []

with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if baris == "":
            continue

        nim, teks_nilai = baris.split(",")
        angka = float(teks_nilai)

        print(f"NIM: {nim}, Nilai: {angka}")
        nilai.append(angka)

if nilai:
    rata_rata = sum(nilai) / len(nilai)
    print(f"Rata-rata = {rata_rata:.2f}")