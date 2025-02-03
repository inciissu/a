def kdv_hesapla(fiyat):
    return fiyat * 0.18

def toplam_fiyat_hesapla(fiyat):
    return fiyat + kdv_hesapla(fiyat)

fiyat = 100
toplam_fiyat = toplam_fiyat_hesapla(fiyat)
print(toplam_fiyat)