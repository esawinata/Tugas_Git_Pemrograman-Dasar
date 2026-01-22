# Data panen dari berbagai lokasi
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Desa Makmur',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 750,
            'kedelai': 400
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Desa Sejahtera',
        'hasil_panen': {
            'padi': 1350,
            'jagung': 850,
            'kedelai': 500
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Desa Subur',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 600,
            'kedelai': 450
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Desa Jaya',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 900,
            'kedelai': 550
        }
    }
}


print("1. SELURUH DATA PANEN")
for lokasi, data in data_panen.items():
    print(f"{lokasi}:")
    print(f"  Nama Lokasi: {data['nama_lokasi']}")
    print(f"  Hasil Panen:")
    print(f"    - Padi    : {data['hasil_panen']['padi']} kg")
    print(f"    - Jagung  : {data['hasil_panen']['jagung']} kg")
    print(f"    - Kedelai : {data['hasil_panen']['kedelai']} kg")
print()

print("2. HASIL PANEN JAGUNG LOKASI 2")
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi2: {jagung_lokasi2} kg")
print()

print("3. NAMA LOKASI 3")
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi3: {nama_lokasi3}")
print()

print("4. HASIL PANEN PADI DAN KEDELAI SETIAP LOKASI")
padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
print(f"Lokasi 1 ({data_panen['lokasi1']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi1} kg")
print(f"  Kedelai: {kedelai_lokasi1} kg")

padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
print(f"\nLokasi 2 ({data_panen['lokasi2']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi2} kg")
print(f"  Kedelai: {kedelai_lokasi2} kg")

padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
print(f"\nLokasi 3 ({data_panen['lokasi3']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi3} kg")
print(f"  Kedelai: {kedelai_lokasi3} kg")

padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
print(f"\nLokasi 4 ({data_panen['lokasi4']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi4} kg")
print(f"  Kedelai: {kedelai_lokasi4} kg")
print()

print("5. ANALISIS KONDISI LOKASI (PERCABANGAN)")
print(f"Lokasi 1 ({data_panen['lokasi1']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi1} kg, Jagung: {data_panen['lokasi1']['hasil_panen']['jagung']} kg")
if padi_lokasi1 > 1300 or data_panen['lokasi1']['hasil_panen']['jagung'] > 800:
    print("  Status: PERLU PERHATIAN KHUSUS")
else:
    print("  Status: KONDISI BAIK")
print(f"\nLokasi 2 ({data_panen['lokasi2']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi2} kg, Jagung: {data_panen['lokasi2']['hasil_panen']['jagung']} kg")
if padi_lokasi2 > 1300 or data_panen['lokasi2']['hasil_panen']['jagung'] > 800:
    print("  Status: PERLU PERHATIAN KHUSUS")
else:
    print("  Status: KONDISI BAIK")
print(f"\nLokasi 3 ({data_panen['lokasi3']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi3} kg, Jagung: {data_panen['lokasi3']['hasil_panen']['jagung']} kg")
if padi_lokasi3 > 1300 or data_panen['lokasi3']['hasil_panen']['jagung'] > 800:
    print("  Status: PERLU PERHATIAN KHUSUS")
else:
    print("  Status: KONDISI BAIK")
print(f"\nLokasi 4 ({data_panen['lokasi4']['nama_lokasi']}):")
print(f"  Padi: {padi_lokasi4} kg, Jagung: {data_panen['lokasi4']['hasil_panen']['jagung']} kg")
if padi_lokasi4 > 1300 or data_panen['lokasi4']['hasil_panen']['jagung'] > 800:
    print("  Status: PERLU PERHATIAN KHUSUS")
else:
    print("  Status: KONDISI BAIK")