class Oquvchi:
    def __init__(self, ismi, yosh):
        self.ismi = ismi
        self.yosh = yosh

    def oqish(self):
        return f"{self.ismi} o'qishni boshladi."

    def yozish(self, matn):
        return f"{self.ismi} quyidagi matnni yozdi: {matn}"


class Oqituvchi:
    def __init__(self, ismi, fani):
        self.ismi = ismi
        self.fani = fani

    def ustoz(self):
        return f"{self.ismi} {self.fani} fanini o'qitadi."

    def fani(self):
        return f"{self.fani} Matematika"


class Fan:
    def __init__(self, nomi, ustoz):
        self.nomi = nomi
        self.ustoz = ustoz

    def uqitish(self):
        return f"{self.ustoz.ismi} {self.nomi} fanini o'qitadi."


class Sinf:
    def __init__(self, nomi, fan):
        self.nomi = nomi
        self.fan = fan
        self.oquvchilar = []

    def oquvchi_qoshish(self, oquvchi):
        self.oquvchilar.append(oquvchi)

    def boshlash(self):
        uqitish = self.fan.uqitish()
        oquvchilar = [oquvchi.oqish() for oquvchi in self.oquvchilar]
        return f"{uqitish}\n" + "\n".join(oquvchilar)


class Universitet:
    def __init__(self, nomi):
        self.nomi = nomi
        self.sinf = []

    def sinf_qoshish(self, sinf):
        self.sinf.append(sinf)

    def boshlash(self):
        return f"{self.nomi} universiteti o'qish boshladi!"


class Kutubxona:
    def __init__(self, nomi):
        self.nomi = nomi
        self.kitablar = []

    def kitob_qoshish(self, kitob):
        self.kitablar.append(kitob)

    def kitoblar_royxati(self):
        return f"{self.nomi} kutubxonasidagi kitoblar: " + ", ".join(self.kitablar)


oqituvchi1 = Oqituvchi("Ali", "Matematika")
fan1 = Fan("Matematika", oqituvchi1)

oqituvchi2 = Oqituvchi("Inna", "Fizika")
fan2 = Fan("Fizika", oqituvchi2)

oquvchi1 = Oquvchi("John", 17)
oquvchi2 = Oquvchi("Masha", 16)

sinf1 = Sinf("1-A", fan1)
sinf1.oquvchi_qoshish(oquvchi1)
sinf1.oquvchi_qoshish(oquvchi2)

universitet = Universitet("Toshkent Davlat Universiteti")
universitet.sinf_qoshish(sinf1)

kutubxona = Kutubxona("Toshkent Kutubxonasi")
kutubxona.kitob_qoshish("Python Dasturlash")
kutubxona.kitob_qoshish("Algebra")

print(universitet.boshlash())
print(sinf1.boshlash())
print(kutubxona.kitoblar_royxati())
