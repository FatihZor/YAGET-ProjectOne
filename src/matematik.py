from src.hatalar import hata_yazdir

def toplama(a: int or float, b: int or float) -> int or float:
    try:
        sonuc = a + b
    except Exception as e:
        hata_yazdir(e)
        sonuc = 0
        
    return sonuc


def cikarma(a: int or float, b: int or float) -> int or float:
    try:
        sonuc = a - b
    except Exception as e:
        hata_yazdir(e)
        sonuc = 0
    
    return sonuc
