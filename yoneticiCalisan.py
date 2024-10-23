class Calisan:
    def __init__(self,isim,departman,maas):
        self.isim=isim
        self.departman=departman
        self.maas=maas
    def bilgi(self):
        print(f"İsim:{self.isim}, Departman:{self.departman}, Maaş:{self.maas}")
    def maasHesaplama(self):
        return self.maas

class Yoneticiler(Calisan):
    def __init__(self,isim,departman,maas,bonus):
        super().__init__(isim,departman,maas)
        self.bonus=bonus
    def bilgi(self):
        super().bilgi()
        print(f"bonus:{self.bonus}")
    def maasHesaplama(self):
        return self.maas+self.bonus
calisan1=Calisan("Ece","IT",25000)
calisan2=Calisan("Ali","Finans",20000)
yonetici1=Yoneticiler("Arif","Müdür",30000,2000)
yonetici2=Yoneticiler("Elif","Müdür Yardımcısı",28000,1500)
calisan1.bilgi()
calisan2.bilgi()
yonetici1.bilgi()
yonetici2.bilgi()

print(f"Yönetici Maaşı:{yonetici1.maasHesaplama()}TL")
print(f"Yönetici Maaşı:{yonetici2.maasHesaplama()}TL")
