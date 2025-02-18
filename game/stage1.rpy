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


label stage1:
    $ quick_menu = True 
    #Stage 1-1 #(Story)

    scene BG_Desa_Tegalrejo #(Zoom Ke Salah Satu Rumah)
    Narator "Perang Jawa dimulai pada tahun 1825, dipicu oleh tindakan pemerintah kolonial Belanda yang memasang patok-patok di tanah leluhur Pangeran Diponegoro di Tegalrejo. Bagi sang pangeran, ini adalah penghinaan yang tidak dapat diterima."
    Narator "Di malam hari, di bawah sinar rembulan, Pangeran Diponegoro mengumpulkan pengikut setianya di sebuah pendopo sederhana. Para tokoh agama, petani, dan pemuda desa duduk melingkar, menunggu pidato dari pemimpin mereka."
    show Diponegoro
    diponegoro "Saudara-saudaraku, malam ini kita berkumpul bukan untuk meratapi nasib, tetapi untuk merencanakan langkah kita. Belanda telah melampaui batas. Tanah leluhur kita mereka rampas, kehormatan kita mereka injak. Apakah kita akan diam saja?"
    hide Diponegoro
    santri_suro "Tidak, Gusti Pangeran! Kami siap berjuang di bawah panji-panji Anda."
    show Diponegoro:
        xpos -400
    show Kyai_mojo:
        xpos 400
    show Sentot:
        xpos 100
    kyai_mojo "Benar, Gusti. Tapi, perjuangan ini harus didasari oleh keimanan. Perang ini bukan sekadar melawan penjajah, tetapi juga mempertahankan martabat Islam dan adat kita."
    diponegoro "Kyai Mojo benar. Kita akan berperang bukan karena kebencian, tetapi demi keadilan. Bersiaplah, karena kita akan menggetarkan tanah Jawa."
    
    
    Narator "Perang dimulai dengan serangan mendadak dari pasukan Pangeran Diponegoro ke pos-pos Belanda di sekitar Yogyakarta. Para petani yang sebelumnya hanya memegang cangkul kini mengangkat senjata, meskipun seadanya. Pada suatu pagi, di tengah persiapan pertempuran, Pangeran Diponegoro berbicara dengan seorang panglima kepercayaannya, Sentot Alibasya."
    
    diponegoro "Sentot, kau adalah salah satu panglimaku yang paling aku percayai. Bagaimana persiapan pasukan kita?"
    sentot "Gusti, pasukan kita sudah siap. Mereka mungkin tidak memiliki banyak senjata, tetapi semangat mereka tidak akan terkalahkan."
    diponegoro "Bagus. Ingatlah, kita bertempur bukan untuk balas dendam, tetapi untuk membela tanah kita. Pimpin pasukanmu dengan bijak."
    Narator "Sentot mengangguk dan segera memimpin pasukannya ke garis depan. Sementara itu, Pangeran Diponegoro mengumpulkan para tokoh agama untuk berdoa."
    kyai_mojo "Ya Allah, berikanlah kekuatan kepada hamba-Mu ini untuk melawan kezaliman. Jika ini adalah jalan yang Kau takdirkan, maka kuatkanlah hati kami."
    hide Kyai_mojo
    diponegoro "Aamiin. Dengan nama Allah, kita mulai perjuangan ini."
    Narator "Pasukan Pangeran Diponegoro terus melancarkan perlawanan dengan taktik gerilya. Mereka memanfaatkan medan pegunungan, hutan, dan lembah untuk menyerang pasukan Belanda yang memiliki senjata dan pasukan lebih besar. Suatu pagi, seorang mata mata desa kembali ke markas dengan membawa laporan penting."
        
    scene bg_imagination
    Mata_mata_Desa "Gusti, pasukan Belanda telah mendirikan benteng kecil di dekat Sungai Progo. Mereka tampaknya berencana menguasai jalur air."
    show Diponegoro:
        xpos -400
    show sentot:
        xpos 300
    diponegoro "Ini adalah kesempatan kita. Jika mereka menguasai sungai, pergerakan kita akan terhambat. Sentot, siapkan pasukan."
    sentot "Baik, Gusti. Tapi kita membutuhkan strategi khusus, karena mereka memiliki meriam."
    diponegoro "Kita akan menyerang di malam hari, saat mereka lengah. Siapkan pasukan panah dan penyergap di kedua sisi sungai."
    Narator "Di malam hari, pasukan Diponegoro bergerak diam-diam di sepanjang sungai. Mereka membagi diri menjadi tiga kelompok: satu kelompok bertugas memancing perhatian, sementara dua kelompok lainnya bersiap untuk mengepung dari sisi hutan."
    sentot "Semua pasukan, siapkan senjata. Jangan serang sampai ada aba-aba."
    prajurit "Siap, Panglima!"
    Narator "Tiba-tiba, suara gong kecil berbunyi sebagai tanda dimulainya serangan. Pasukan pemanah melepaskan hujan anak panah ke arah benteng Belanda. Para penjaga berteriak, terkejut oleh serangan mendadak ini."
    hide Dipenogoro
    hide sentot
    #Stage 1-2 #(battle)

        #@BATTLE(@3&@4)
        
    #Stage 1-3 #(Story & Battle)
#@3      
    scene bg_benteng_belanda
    penjaga_belanda  "Serangan! Cepat, lindungi benteng!"
    Narator "Saat Belanda berusaha bertahan, pasukan Diponegoro dari kedua sisi keluar dari persembunyian mereka. Mereka menyerang dengan cepat, memanfaatkan kekacauan di kubu Belanda."
    show sentot
    sentot "Jangan beri mereka waktu untuk mengatur ulang barisan!"
    hide sentot
    jump second_battle
        #@BATTLE(@3&@4)
    #Stage 1-4 #(Story)
#@3

label after_second_battle:
    stop music fadeout 2.0
    scene bg_benteng_belanda
    prajurit "Mundur! Mundur ke tengah benteng!"
    Narator "Pertempuran berlangsung sengit hingga fajar tiba. Dengan taktik yang cerdik, pasukan Diponegoro berhasil menguasai benteng."
    show Diponegoro
    diponegoro "Kemenangan ini bukan akhir, tetapi awal dari perlawanan yang lebih besar. Bersiaplah, karena Belanda pasti akan membalas."
    hide Diponegoro

    jump sungai_progo
