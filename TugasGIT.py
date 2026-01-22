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