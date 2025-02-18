image Ali:
    "images/Ali 1.png"
    pause 0.5
    "images/Ali 2.png"
    pause 0.5
    repeat
image Siti:
    "images/Siti 1.png"
    pause 0.5
    "images/Siti 2.png"
    pause 0.5
    repeat
image Ibu:
    "images/Ibu 1.png"
    pause 0.5
    "images/Ibu 2.png"
    pause 0.5
    repeat
image Diponegoro:
    "images/Diponegoro 1.png"
    pause 0.5
    "images/Diponegoro 1.1.png"
    pause 0.5
    repeat
image Joko:
    "images/Joko 1.png"
    pause 0.5
    "images/Joko 2.png"
    pause 0.5
    repeat
image Kyai_mojo:
    "images/km 1.png"
    pause 0.5
    "images/km 2.png"
    pause 0.5
    repeat    
image bg_kmmalam = "images/Bg/kamar malam.png"
image bg_kmsiang = "images/Bg/kamar siang.png"
# Definisi gambar latar dan karakter
#image Siti = "images/Siti.png"
#image joko = "images/Joko.png"
image bg_school_afternoon = "images/Taman Sekolah.png"
image bg_library_path = "images/Bg/Perpus 1.png"
image bg_library_bookshelf = "images/Bg/Perpus 2.png"
image bg_reading_room = "images/Bg/Perpus 2 1.png"
image bg_imagination = "images/Bg/Hutan.png"
image bg_battlefield = "images/Bg/Hutan.png"
image BG_hutan = "images/Bg/Hutan.png"
image bg_library_afternoon = "images/Bg/Perpus 2 2.png"
image bg_library_night = "images/Bg/Perpus 2 3.png"
image bg_forest_path = "images/Bg/Hutan.png"
image bg_room = "images/bghitam.jpg"
image bg_benteng_belanda = "images/Bg/benteng  belanda vredeburg.png"
image BG_Desa_Tegalrejo = "images/Bg/Desategalrejo.png"
image BG_Goa_Selarong = "images/Bg/GOA SELARONG.png"
image BG_Keraton = "images/Bg/Keraton.png"
image BG_TebingSelarong = "images/Bg/TebingSelarong.png"
#image diponegoro = "images/Dipenogoro 2 5.png"
image Sentot = "images/sentot.png"
image penjaga_belanda = "images/Dutch Army.png"
image Librarian = "images/Dutch Army.png"
image Young_mustahar ="images/young_mustahar.png"

# Definisi karakter
define ali = Character("Ali", image="Ali", color="#3498db",)
define siti = Character("Siti", image="siti", color="#e74c3c")
define ali_siti = Character("Ali siti", image="ali_siti", color="#3498db")
define pak_joko = Character("Pak Joko", image="joko", color="#2ecc71")
define player = Character("Player", color="#ffffff")
define prajurit_belanda = Character("prajurit_belanda", image="belanda", color="#2ecc71")
define diponegoro = Character("Diponegoro", image="diponegoro", color="#2ecc71")
define sentot = Character("Sentot", image="sentot", color="#2ecc71")
define enemy = "Goblin"
define ibu = "Ibu"
define raden_ayu = "Raden Ayu"
define prajurit = "Prajurit"
define penjaga_belanda = "Penjaga Belanda"
define murid = "Murid-murid"
define bu_guru = "Ibu Guru"
define librarian = Character("Pak Joko", image="joko", color="#2ecc71")
define young_mustahar = Character("Young mustahar", image="Young_mustahar", color="#2ecc71")
define midwife = "Midwife"
define abdi_dalem = "Abdi Dalem"
define kyai_mojo = "Kyai Mojo"
define petani = "Petani"
define santri_suro = "Santri suro"
define Narator = "Narator"
define Mata_mata_Desa = "Mata-Mata Desa"
define Komandan_Belanda = "Komandan Belanda"
define Penduduk_Desa = "Penduduk Desa" 
define Utusan_Keraton = "Utusan Keraton"
define Pemuda_Desa ="Pemuda Desa"
define Komandan_Konvoi_Belanda= "Komandan Konvoi Belanda"
define Pejabat_Belanda = "Pejabat Belanda"
define Pengikut = "Pengikut"
define Utusan_Belanda = "Utusan Belanda"
define De_Kock = "De Kock"


label stage4:
    $ quick_menu = True 
#screen stage4:
#Stage 4-1 #(story)

    scene BG_TebingSelarong
    Narator "Setelah kemenangan di Bagelen, Pangeran Diponegoro memutuskan untuk melanjutkan perjuangannya ke wilayah Kedu, yang merupakan jalur penting di dataran tinggi Jawa. Wilayah ini terkenal dengan lahan pertaniannya yang subur, tetapi saat itu menjadibasis kekuatan Belanda yang kuat karena kedudukannya yang strategis. Pasukan Belanda mendirikan benteng utama di daerah Magelang untuk mengontrol wilayah Kedu, sekaligus memantau pergerakan pasukan Diponegoro."
    Narator "Pangeran Diponegoro memahami bahwa keberhasilan merebut Kedu akan memberikan keuntungan besar bagi perjuangannya. Dengan menguasai wilayah ini, mereka dapat memutus suplai logistik Belanda sekaligus menarik lebih banyak dukungan dari rakyat."
    show Diponegoro:
        xpos -400
    show Kyai_mojo:
        xpos 400
    show Sentot:
        xpos 100
    diponegoro "Saudara-saudaraku, Kedu adalah jantung logistik Belanda. Jika kita berhasil merebut wilayah ini, kita tidak hanya melemahkan mereka, tetapi juga memperkuat posisi kita. Sentot, bagaimana laporan terakhir dari mata-mata kita?"
    sentot "Gusti, pasukan Belanda di Magelang dipimpin oleh seorang komandan berpengalaman, Kolonel Van der Smissen. Mereka memiliki sekitar 400 prajurit, termasuk kavaleri dan senjata berat. Tetapi rakyat di sekitar Kedu mulai bosan dengan penjajahan mereka, dan banyak yang siap membantu perjuangan kita."
    kyai_mojo "Perang ini bukan hanya soal merebut wilayah, Gusti. Kita harus memenangkan hati rakyat, menunjukkan kepada mereka bahwa kita bertarung untuk keadilan, bukan untuk kekuasaan."
    Narator "Rapat malam itu menghasilkan strategi gerilya yang cermat. Pangeran Diponegoro memutuskan untuk menyerang jalur suplai Belanda terlebih dahulu, membuat pasukan mereka di Magelang terisolasi sebelum melakukan serangan besar-besaran."
    hide Diponegoro
    
    hide Kyai_mojo
    scene BG_TebingSelarong
    Narator "Pada malam yang gelap, pasukan Diponegoro yang dipimpin oleh Sentot bergerak diam-diam menuju konvoi suplai Belanda yang melintas di dekat perbatasan Kedu. Di tengah jalan sempit yang diapit oleh tebing curam, mereka menunggu saat yang tepat untuk menyerang."
    sentot "Pemanah, siapkan senjata kalian. Tunggu sampai konvoi memasuki posisi jebakan."
    hide Sentot
    Narator "Saat suara roda gerobak mulai terdengar, Sentot memberi tanda dengan mengangkat tombaknya. Dalam sekejap, hujan panah menghujani konvoi Belanda, membuat para prajurit musuh terjebak dalam kekacauan."
    Komandan_Konvoi_Belanda "Serangan! Cepat, bentuk formasi bertahan!"
    Narator "Namun, pasukan Diponegoro telah memblokir semua jalan keluar. Serangan dari segala arah membuat pasukan Belanda kehilangan kendali, dan suplai penting mereka berhasil direbut oleh para pejuang Jawa."
    Narator "Kemenangan ini memaksa Belanda di Magelang untuk bertahan dengan sumber daya yang terbatas. Sementara itu, Pangeran Diponegoro mempersiapkan pasukannya untuk serangan langsung ke benteng utama."
        
#Stage 4-2 #(story)
    scene BG_Desa_Tegalrejo
    Narator "Dua hari kemudian, pasukan Diponegoro mendekati Magelang. Pangeran memimpin sendiri pasukan utama, didampingi oleh Sentot Alibasya dan Kyai Mojo. Saat mereka beristirahat di sebuah desa dekat benteng, seorang pemuda desa datang membawa pesan."
    Pemuda_Desa "Gusti Pangeran, kami mendengar tentang perjuanganmu. Kami ingin membantu dengan menyediakan makanan dan informasi tentang benteng Belanda."
    show Diponegoro
    diponegoro "Terima kasih, anak muda. Perjuangan ini adalah perjuangan kita bersama. Sampaikan kepada rakyat desa, keberanian mereka akan dikenang selamanya."
        
    scene bg_benteng_belanda
    Narator "Pada malam ketiga, pasukan Diponegoro memulai serangan ke benteng Magelang. Pasukan panah menembakkan serangan pertama untuk mengalihkan perhatian, sementara pasukan infanteri menyusup melalui sisi benteng yang kurang dijaga."
    diponegoro "Jangan menyerang tanpa perhitungan. Fokuskan serangan kita pada titik lemah pertahanan mereka. Sentot, pimpin pasukanmu ke pintu utama."
    hide Dipenogoro
    show Sentot
    sentot "Siap, Gusti. Kita akan membuka jalan untuk kemenangan."
    Narator "Setelah menguasai Kedu, pasukan Diponegoro terus memperluas pengaruh mereka ke wilayah-wilayah sekitarnya. Tetapi kemenangan ini juga membawa perhatian lebih besar dari pihak Belanda, yang mulai mengirim pasukan tambahan untuk memadamkan perlawanan. Perang Jawa, yang awalnya hanya dipandang sebagai pemberontakan kecil, kini berubah menjadi konflik besar yang mengguncang kekuasaan kolonial di Nusantara."

    jump lembah_selarong