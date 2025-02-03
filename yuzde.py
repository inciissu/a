def yuzde_hesapla(fiyat, yuzde):
    return (fiyat * yuzde) / 100

def indirimli_fiyat_hesapla(fiyat, indirim_yuzdesi):
    indirim = yuzde_hesapla(fiyat, indirim_yuzdesi)
    return fiyat - indirim

fiyat = 200
indirim_yuzdesi = 10
indirimli_fiyat = indirimli_fiyat_hesapla(fiyat, indirim_yuzdesi)

print(indirimli_fiyat)