class tarifApp :
    def tarifAdd(self) :
        tarifAdi = input("Tarıf Adı : ")
        tarif.append(tarifAdi)
        while True :
            tarifAdim = input('Tarif Adımı Ekle(Adımlarınız Sonlandıysa "-1" giriniz.) : ')
            if tarifAdim == "-1" :
                tarifler_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarifAdim)


    def indexle(self) :
        number = len(tarifler_listesi)
        print("Tüm Tarifler")
        for adim in tarif :
                print(adim)




def main_menu() :
    while True :
        print("\nYeni Bir Tarif Ekle : 1\nVar Olan Tarifleri İndexle : 2\nÇıkış Yap : 3 ")
        secim = input("Yapmak İstediğiniz İşlem Rakamını Giriniz : ")
        islem = tarifApp()
        if secim == "1" :
            islem.tarifAdd()
        elif secim == "2" :
            islem.indexle()
        elif secim == "3" :
            exit(0)
        else :
            print("Hatalı Bir Tuşlama Yaptınız. Lütfen Tekrar Gözden Geçiriniz.")



tarifler_listesi = []
tarif = []

main_menu()