import pandas as pd
from datetime import datetime
import streamlit as st 
import pytz

def imsakiye(sehir,ilce):
  ramazan = pd.read_html(f'https://www.haberturk.com/ramazan/imsakiye/{sehir}/{ilce}',flavor = 'bs4')[0]
  ramazan['Tarih'] = pd.to_datetime(ramazan['Tarih'])
  return ramazan

def gunGetir(sehir, ilce): 
  df = imsakiye(sehir,ilce)
  hedef_saat_dilimi = pytz.timezone('Europe/Istanbul')
  simdi = datetime.now(hedef_saat_dilimi).strftime('%H:%M')
  sehiriftar = df[df['Tarih'] == '2024-03-12']['AKŞAM'].values[0]
  kalan = pd.Timedelta(pd.to_datetime(sehiriftar)-pd.to_datetime(simdi))
  return kalan

def Bugun(sehir, ilce): 
  df = imsakiye(sehir, ilce)
  bugun = datetime.today().date().strftime('%Y:%m:%d')
  sehiriftar = df[df['Tarih'] == '2024-03-12']
  return sehiriftar
  

st.header('Hoşgeldin Ramazan')

sehirler = {
    "Adana": ["Aladağ", "Ceyhan", "Çukurova", "Feke", "İmamoğlu", "Karaisalı", "Karataş", "Kozan", "Pozantı",
              "Saimbeyli", "Sarıçam", "Seyhan", "Tufanbeyli", "Yumurtalık", "Yüreğir"],

    "Adıyaman": ["Adıyaman", "Besni", "Çelikhan", "Gerger", "Gölbaşı", "Kâhta", "Samsat", "Sincik", "Tut"],

    "Afyonkarahisar": ["Afyonkarahisar", "Başmakçı", "Bayat", "Bolvadin", "Çay", "Çobanlar", "Dazkırı", "Dinar",
                       "Emirdağ", "Evciler", "Hocalar", "İhsaniye", "İscehisar", "Kızılören", "Sandıklı", "Sinanpaşa",
                       "Sultandağı", "Şuhut"],

    "Ağrı": ["Ağrı", "Diyadin", "Doğubayazıt", "Eleşkirt", "Hamur", "Patnos", "Taşlıçay", "Tutak"],

    "Aksaray": ["Ağaçören", "Aksaray", "Eskil", "Gülağaç", "Güzelyurt", "Ortaköy", "Sarıyahşi"],

    "Amasya": ["Amasya", "Göynücek", "Gümüşhacıköy", "Hamamözü", "Merzifon", "Suluova", "Taşova"],

    "Ankara": ["Akyurt", "Altındağ", "Ayaş", "Balâ", "Beypazarı", "Çamlıdere", "Çankaya", "Çubuk", "Elmadağ",
               "Etimesgut", "Evren", "Gölbaşı", "Güdül", "Haymana", "Kalecik", "Kahramankazan", "Keçiören",
               "Kızılcahamam", "Mamak", "Nallıhan", "Polatlı", "Pursaklar", "Sincan", "Şereflikoçhisar", "Yenimahalle"],

    "Antalya": ["Akseki", "Aksu", "Alanya", "Döşemealtı", "Elmalı", "Finike", "Gazipaşa", "Gündoğmuş", "İbradı",
                "Demre", "Kaş", "Kemer", "Kepez", "Konyaaltı", "Korkuteli", "Kumluca", "Manavgat", "Muratpaşa",
                "Serik"],

    "Ardahan": ["Ardahan", "Çıldır", "Damal", "Göle", "Hanak", "Posof"],

    "Artvin": ["Ardanuç", "Arhavi", "Artvin", "Borçka", "Hopa", "Murgul", "Şavşat", "Yusufeli"],

    "Aydın": ["Bozdoğan", "Buharkent", "Çine", "Didim", "Efeler", "Germencik", "İncirliova", "Karacasu", "Karpuzlu",
              "Koçarlı", "Köşk", "Kuşadası", "Kuyucak", "Nazilli", "Söke", "Sultanhisar", "Yenipazar"],

    "Balıkesir": ["Altıeylül", "Ayvalık", "Balya", "Bandırma", "Bigadiç", "Burhaniye", "Dursunbey", "Edremit", "Erdek",
                  "Gömeç", "Gönen", "Havran", "İvrindi", "Karesi", "Kepsut", "Manyas", "Marmara", "Savaştepe",
                  "Sındırgı", "Susurluk"],

    "Bartın": ["Amasra", "Bartın", "Kurucaşile", "Ulus"],

    "Batman": ["Batman", "Beşiri", "Gercüş", "Hasankeyf", "Kozluk", "Sason"],

    "Bayburt": ["Aydıntepe", "Bayburt (İl merkezi", "Demirözü"],

    "Bilecik": ["Bilecik", "Bozüyük", "Gölpazarı", "İnhisar", "Osmaneli", "Pazaryeri", "Söğüt", "Yenipazar"],

    "Bingöl": ["Adaklı", "Bingöl", "Genç", "Karlıova", "Kiğı", "Solhan", "Yayladere", "Yedisu"],

    "Bitlis": ["Adilcevaz", "Ahlat", "Bitlis", "Güroymak", "Hizan", "Mutki", "Tatvan"],

    "Bolu": ["Bolu", "Dörtdivan", "Gerede", "Göynük", "Kıbrıscık", "Mengen", "Mudurnu", "Seben", "Yeniçağa"],

    "Burdur": ["Ağlasun", "Altınyayla", "Bucak", "Burdur", "Çavdır", "Çeltikçi", "Gölhisar", "Karamanlı", "Kemer",
               "Tefenni", "Yeşilova"],

    "Bursa": ["Büyükorhan", "Gemlik", "Gürsu", "Harmancık", "İnegöl", "İznik", "Karacabey", "Keles", "Kestel",
              "Mudanya", "Mustafakemalpaşa", "Nilüfer", "Orhaneli", "Orhangazi", "Osmangazi", "Yenişehir", "Yıldırım"],

    "Çanakkale": ["Ayvacık", "Bayramiç", "Biga", "Bozcaada", "Çan", "Çanakkale", "Eceabat", "Ezine", "Gelibolu",
                  "Gökçeada", "Lapseki", "Yenice"],

    "Çankırı": ["Atkaracalar", "Bayramören", "Çankırı", "Çerkeş", "Eldivan", "Ilgaz", "Kızılırmak", "Korgun",
                "Kurşunlu", "Orta", "Şabanözü", "Yapraklı"],

    "Çorum": ["Alaca", "Bayat", "Boğazkale", "Çorum", "Dodurga", "İskilip", "Kargı", "Laçin", "Mecitözü", "Oğuzlar",
              "Ortaköy", "Osmancık", "Sungurlu", "Uğurludağ"],

    "Denizli": ["Acıpayam", "Babadağ", "Baklan", "Bekilli", "Beyağaç", "Bozkurt", "Buldan", "Çal", "Çameli", "Çardak",
                "Çivril", "Güney", "Honaz", "Kale", "Merkezefendi", "Pamukkale", "Sarayköy", "Serinhisar", "Tavas"],

    "Diyarbakır": ["Bağlar", "Bismil", "Çermik", "Çınar", "Çüngüş", "Dicle", "Eğil", "Ergani", "Hani", "Hazro",
                   "Kayapınar", "Kocaköy", "Kulp", "Lice", "Silvan", "Sur", "Yenişehir"],

    "Düzce": ["Akçakoca", "Cumayeri", "Çilimli", "Düzce", "Gölyaka", "Gümüşova", "Kaynaşlı", "Yığılca"],

    "Edirne": ["Enez", "Havsa", "İpsala", "Keşan", "Lalapaşa", "Meriç", "Merkez", "Süloğlu", "Uzunköprü"],

    "Elâzığ": ["Ağın", "Alacakaya", "Arıcak", "Baskil", "Elâzığ", "Karakoçan", "Keban", "Kovancılar", "Maden", "Palu",
               "Sivrice"],

    "Erzincan": ["Çayırlı", "Erzincan", "İliç", "Kemah", "Kemaliye", "Otlukbeli", "Refahiye", "Tercan", "Üzümlü"],

    "Erzurum": ["Aşkale", "Aziziye", "Çat", "Hınıs", "Horasan", "İspir", "Karaçoban", "Karayazı", "Köprüköy", "Narman",
                "Oltu", "Olur", "Palandöken", "Pasinler", "Pazaryolu", "Şenkaya", "Tekman", "Tortum", "Uzundere",
                "Yakutiye"],

    "Eskişehir": ["Alpu", "Beylikova", "Çifteler", "Günyüzü", "Han", "İnönü", "Mahmudiye", "Mihalgazi", "Mihalıççık",
                  "Odunpazarı", "Sarıcakaya", "Seyitgazi", "Sivrihisar", "Tepebaşı"],

    "Gaziantep": ["Araban", "İslahiye", "Karkamış", "Nizip", "Nurdağı", "Oğuzeli", "Şahinbey", "Şehitkâmil",
                  "Yavuzeli"],

    "Giresun": ["Alucra", "Bulancak", "Çamoluk", "Çanakçı", "Dereli", "Doğankent", "Espiye", "Eynesil", "Giresun",
                "Görele", "Güce", "Keşap", "Piraziz", "Şebinkarahisar", "Tirebolu", "Yağlıdere"],

    "Gümüşhane": ["Gümüşhane", "Kelkit", "Köse", "Kürtün", "Şiran", "Torul"],

    "Hakkâri": ["Çukurca", "Hakkâri", "Şemdinli", "Yüksekova"],

    "Hatay": ["Altınözü", "Antakya", "Arsuz", "Belen", "Defne", "Dörtyol", "Erzin", "Hassa", "İskenderun", "Kırıkhan",
              "Kumlu", "Payas", "Reyhanlı", "Samandağ", "Yayladağı"],

    "Iğdır": ["Aralık", "Iğdır", "Karakoyunlu", "Tuzluca"],

    "Isparta": ["Aksu", "Atabey", "Eğirdir", "Gelendost", "Gönen", "Isparta", "Keçiborlu", "Senirkent", "Sütçüler",
                "Şarkikaraağaç", "Uluborlu", "Yalvaç", "Yenişarbademli"],

    "İstanbul": ["Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler", "Bakırköy", "Başakşehir",
                 "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü", "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy",
                 "Esenler", "Esenyurt", "Eyüp", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane", "Kartal",
                 "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer", "Silivri", "Sultanbeyli", "Sultangazi",
                 "Şile", "Şişli", "Tuzla", "Ümraniye", "Üsküdar", "Zeytinburnu"],

    "İzmir": ["Aliağa", "Balçova", "Bayındır", "Bayraklı", "Bergama", "Beydağ", "Bornova", "Buca", "Çeşme", "Çiğli",
              "Dikili", "Foça", "Gaziemir", "Güzelbahçe", "Karabağlar", "Karaburun", "Karşıyaka", "Kemalpaşa", "Kınık",
              "Kiraz", "Konak", "Menderes", "Menemen", "Narlıdere", "Ödemiş", "Seferihisar", "Selçuk", "Tire",
              "Torbalı", "Urla"],

    "Kahramanmaraş": ["Afşin", "Andırın", "Çağlayancerit", "Dulkadiroğlu", "Ekinözü", "Elbistan", "Göksun", "Nurhak",
                      "Onikişubat", "Pazarcık", "Türkoğlu"],

    "Karabük": ["Eflani", "Eskipazar", "Karabük", "Ovacık", "Safranbolu", "Yenice"],

    "Karaman": ["Ayrancı", "Başyayla", "Ermenek", "Karaman", "Kazımkarabekir", "Sarıveliler"],

    "Kars": ["Akyaka", "Arpaçay", "Digor", "Kağızman", "Kars", "Sarıkamış", "Selim", "Susuz"],

    "Kastamonu": ["Abana", "Ağlı", "Araç", "Azdavay", "Bozkurt", "Cide", "Çatalzeytin", "Daday", "Devrekani",
                  "Doğanyurt", "Hanönü", "İhsangazi", "İnebolu", "Kastamonu", "Küre", "Pınarbaşı", "Seydiler",
                  "Şenpazar", "Taşköprü", "Tosya"],

    "Kayseri": ["Akkışla", "Bünyan", "Develi", "Felahiye", "Hacılar", "İncesu", "Kocasinan", "Melikgazi", "Özvatan",
                "Pınarbaşı", "Sarıoğlan", "Sarız", "Talas", "Tomarza", "Yahyalı", "Yeşilhisar"],

    "Kırıkkale": ["Bahşılı", "Balışeyh", "Çelebi", "Delice", "Karakeçili", "Keskin", "Kırıkkale", "Sulakyurt",
                  "Yahşihan"],

    "Kırklareli": ["Babaeski", "Demirköy", "Kırklareli", "Kofçaz", "Lüleburgaz", "Pehlivanköy", "Pınarhisar", "Vize"],

    "Kırşehir": ["Akçakent", "Akpınar", "Boztepe", "Çiçekdağı", "Kaman", "Kırşehir", "Mucur"],

    "Kilis": ["Elbeyli", "Kilis", "Musabeyli", "Polateli"],

    "Kocaeli": ["Başiskele", "Çayırova", "Darıca", "Derince", "Dilovası", "Gebze", "Gölcük", "İzmit", "Kandıra",
                "Karamürsel", "Kartepe", "Körfez"],

    "Konya": ["Ahırlı", "Akören", "Akşehir", "Altınekin", "Beyşehir", "Bozkır", "Cihanbeyli", "Çeltik", "Çumra",
              "Derbent", "Derebucak", "Doğanhisar", "Emirgazi", "Ereğli", "Güneysınır", "Hadım", "Halkapınar", "Hüyük",
              "Ilgın", "Kadınhanı", "Karapınar", "Karatay", "Kulu", "Meram", "Sarayönü", "Selçuklu", "Seydişehir",
              "Taşkent", "Tuzlukçu", "Yalıhüyük", "Yunak"],

    "Kütahya": ["Altıntaş", "Aslanapa", "Çavdarhisar", "Domaniç", "Dumlupınar", "Emet", "Gediz", "Hisarcık", "Kütahya",
                "Pazarlar", "Şaphane", "Simav", "Tavşanlı"],

    "Malatya": ["Akçadağ", "Arapgir", "Arguvan", "Battalgazi", "Darende", "Doğanşehir", "Doğanyol", "Hekimhan", "Kale",
                "Kuluncak", "Pütürge", "Yazıhan", "Yeşilyurt"],

    "Manisa": ["Ahmetli", "Akhisar", "Alaşehir", "Demirci", "Gölmarmara", "Gördes", "Kırkağaç", "Köprübaşı", "Kula",
               "Salihli", "Sarıgöl", "Saruhanlı", "Selendi", "Soma", "Şehzadeler", "Turgutlu", "Yunusemre"],

    "Mardin": ["Artuklu", "Dargeçit", "Derik", "Kızıltepe", "Mazıdağı", "Midyat", "Nusaybin", "Ömerli", "Savur",
               "Yeşilli"],

    "Mersin": ["Akdeniz", "Anamur", "Aydıncık", "Bozyazı", "Çamlıyayla", "Erdemli", "Gülnar", "Mezitli", "Mut",
               "Silifke", "Tarsus", "Toroslar", "Yenişehir"],

    "Muğla": ["Bodrum", "Dalaman", "Datça", "Fethiye", "Kavaklıdere", "Köyceğiz", "Marmaris", "Menteşe", "Milas",
              "Ortaca", "Seydikemer", "Ula", "Yatağan"],

    "Muş": ["Bulanık", "Hasköy", "Korkut", "Malazgirt", "Muş", "Varto"],

    "Nevşehir": ["Acıgöl", "Avanos", "Derinkuyu", "Gülşehir", "Hacıbektaş", "Kozaklı", "Nevşehir", "Ürgüp"],

    "Niğde": ["Altunhisar", "Bor", "Çamardı", "Çiftlik", "Niğde", "Ulukışla"],

    "Ordu": ["Akkuş", "Altınordu", "Aybastı", "Çamaş", "Çatalpınar", "Çaybaşı", "Fatsa", "Gölköy", "Gülyalı",
             "Gürgentepe", "İkizce", "Kabadüz", "Kabataş", "Korgan", "Kumru", "Mesudiye", "Perşembe", "Ulubey", "Ünye"],

    "Osmaniye": ["Bahçe", "Düziçi", "Hasanbeyli", "Kadirli", "Osmaniye", "Sumbas", "Toprakkale"],

    "Rize": ["Ardeşen", "Çamlıhemşin", "Çayeli", "Derepazarı", "Fındıklı", "Güneysu", "Hemşin", "İkizdere", "İyidere",
             "Kalkandere", "Pazar", "Rize"],

    "Sakarya": ["Adapazarı", "Akyazı", "Arifiye", "Erenler", "Ferizli", "Geyve", "Hendek", "Karapürçek", "Karasu",
                "Kaynarca", "Kocaali", "Pamukova", "Sapanca", "Serdivan", "Söğütlü", "Taraklı"],

    "Samsun": ["Alaçam", "Asarcık", "Atakum", "Ayvacık", "Bafra", "Canik", "Çarşamba", "Havza", "İlkadım", "Kavak",
               "Ladik", "Ondokuzmayıs", "Salıpazarı", "Tekkeköy", "Terme", "Vezirköprü", "Yakakent"],

    "Siirt": ["Siirt", "Tillo", "Baykan", "Eruh", "Kurtalan", "Pervari", "Şirvan"],

    "Sinop": ["Ayancık", "Boyabat", "Dikmen", "Durağan", "Erfelek", "Gerze", "Saraydüzü", "Sinop", "Türkeli"],

    "Sivas": ["Akıncılar", "Altınyayla", "Divriği", "Doğanşar", "Gemerek", "Gölova", "Hafik", "İmranlı", "Kangal",
              "Koyulhisar", "Sivas", "Suşehri", "Şarkışla", "Ulaş", "Yıldızeli", "Zara", "Gürün"],

    "Şanlıurfa": ["Akçakale", "Birecik", "Bozova", "Ceylanpınar", "Eyyübiye", "Halfeti", "Haliliye", "Harran", "Hilvan",
                  "Karaköprü", "Siverek", "Suruç", "Viranşehir"],

    "Şırnak": ["Beytüşşebap", "Cizre", "Güçlükonak", "İdil", "Silopi", "Şırnak", "Uludere"],

    "Tekirdağ": ["Çerkezköy", "Çorlu", "Ergene", "Hayrabolu", "Kapaklı", "Malkara", "Marmara Ereğlisi", "Muratlı",
                 "Saray", "Süleymanpaşa", "Şarköy"],

    "Tokat": ["Almus", "Artova", "Başçiftlik", "Erbaa", "Niksar", "Pazar", "Reşadiye", "Sulusaray", "Tokat", "Turhal",
              "Yeşilyurt", "Zile"],

    "Trabzon": ["Akçaabat", "Araklı", "Arsin", "Beşikdüzü", "Çarşıbaşı", "Çaykara", "Dernekpazarı", "Düzköy", "Hayrat",
                "Köprübaşı", "Maçka", "Of", "Ortahisar", "Sürmene", "Şalpazarı", "Tonya", "Vakfıkebir", "Yomra"],

    "Tunceli": ["Çemişgezek", "Hozat", "Mazgirt", "Nazımiye", "Ovacık", "Pertek", "Pülümür", "Tunceli"],

    "Uşak": ["Banaz", "Eşme", "Karahallı", "Sivaslı", "Ulubey", "Uşak"],

    "Van": ["Bahçesaray", "Başkale", "Çaldıran", "Çatak", "Edremit", "Erciş", "Gevaş", "Gürpınar", "İpekyolu",
            "Muradiye", "Özalp", "Saray", "Tuşba"],

    "Yalova": ["Altınova", "Armutlu", "Çınarcık", "Çiftlikköy", "Termal", "Yalova"],

    "Yozgat": ["Akdağmadeni", "Aydıncık", "Boğazlıyan", "Çandır", "Çayıralan", "Çekerek", "Kadışehri", "Saraykent",
               "Sarıkaya", "Sorgun", "Şefaatli", "Yenifakılı", "Yerköy", "Yozgat"],

    "Zonguldak": ["Alaplı", "Çaycuma", "Devrek", "Gökçebey", "Kilimli", "Kozlu", "Karadeniz Ereğli", "Zonguldak"]
}



# Türkçe karakterleri İngilizce karakterlere dönüştürmek için bir çeviri tablosu oluşturun
turkce_ingilizce_ceviri = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")

# Yeni bir sözlük oluşturun ve her bir şehir adını İngilizce karakterlere dönüştürün
ingilizce_sehirler = {}
for il, ilceler in sehirler.items():
    ingilizce_sehirler[il.translate(turkce_ingilizce_ceviri)] = [ilce.translate(turkce_ingilizce_ceviri) for ilce in ilceler]



# ilceleri kucuk harflere donusturduk
for i in ingilizce_sehirler:
  for a in range(len(ingilizce_sehirler[i])):
    ingilizce_sehirler[i][a] = ingilizce_sehirler[i][a].lower()
    



sehirsec = st.sidebar.selectbox('Sehir Sec', ingilizce_sehirler.keys())
ilcesec = st.sidebar.selectbox('Ilce Sec',ingilizce_sehirler[sehirsec])

st.subheader('Bugun')
st.table(Bugun(sehirsec,ilcesec))


st.subheader('Imsakiye')
st.table(imsakiye(sehirsec,ilcesec))
































