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



label stage2:
    $ quick_menu = True 
#Stage 2-1 #(story)
    Narator "Beberapa minggu kemudian, Belanda berusaha menyerang markas utama Diponegoro di Goa Selarong. Namun, sang pangeran telah mempersiapkan jebakan. Pasukannya memanfaatkan jalanan sempit di lembah untuk mengisolasi pasukan musuh."
    scene BG_Goa_Selarong
    show sentot:
        xpos 300
    show Diponegoro:
        xpos -300
    sentot "Mereka datang, Gusti. Pasukan infanteri dan kavaleri."
    diponegoro "Biarkan mereka masuk lebih dalam. Pasukan panah, tunggu aba aba."
    Narator "Ketika pasukan Belanda memasuki lembah, suara tabuhan drum terdengar menggema. Pasukan panah Diponegoro menyerang dari atas tebing, membuat pasukan Belanda kebingungan."
    hide sentot
    hide Diponegoro
    Komandan_Belanda "Percepat maju! Keluar dari lembah ini!"
    Narator "Namun, jalan keluar telah ditutup oleh pasukan infanteri Diponegoro yang dipimpin oleh Santri Suro. Dengan tombak di tangan, mereka menyerang pasukan Belanda yang panik."
    santri_suro "Majulah, saudara-saudaraku! Pertahankan tanah leluhur kita!"
    jump third_battle
    
    #Stage 2-2 #(battle)

    #@BATTLE(@3&@5)

    #tage 2-3 #(story)
#@3
label after_third_battle:
    stop music fadeout 2.0
    Narator "Pertempuran berlangsung hingga siang hari. Pasukan Belanda mengalami kekalahan telak, dengan banyak tentaranya tewas atau ditawan."
    show Diponegoro
    diponegoro "Ini adalah pelajaran bagi mereka. Tanah ini tidak akan mudah mereka taklukkan."
    Narator "Kemenangan di Sungai Progo dan Lembah Selarong memberikan semangat besar bagi rakyat Jawa. Desa-desa yang sebelumnya takut kini mulai bergabung dengan perjuangan. Pangeran Diponegoro menjadi simbol harapan, sementara Belanda mulai merasa tertekan oleh panjangnya perang ini."
    Penduduk_Desa "Gusti Pangeran, kami mendengar tentang kemenanganmu. Kami ingin bergabung dalam perjuangan ini."
    diponegoro "Kuatkan tekad kalian. Bersama-sama, kita akan melawan ketidakadilan."
    Narator "Semua yang dilakukan oleh Pangeran Diponogoro telah mendapatkan hati para rakyat disana. Namun, tidak semua pihak di Jawa mendukung perjuangan Pangeran Diponegoro. Beberapa bangsawan keraton memilih untuk berpihak pada Belanda demi mempertahankan kedudukan mereka. Pada suatu malam, seorang utusan dari keraton datang menemui Pangeran Diponegoro di persembunyiannya."
    Utusan_Keraton "Gusti Pangeran, Sri Sultan memohon agar Anda menghentikan perlawanan ini. Perang ini hanya membawa penderitaan bagi rakyat."
    diponegoro "Penderitaan ini bukan karena perang, tetapi karena penjajahan. Apakah Sultan lupa bahwa tanah ini adalah warisan leluhur kita?"
    Utusan_Keraton "Tetapi Belanda menawarkan perdamaian, Gusti. Mereka bersedia mengembalikan sebagian tanah Anda."
    diponegoro "Perdamaian macam apa itu, jika rakyat tetap menderita? Sampaikan kepada Sultan, aku tidak akan menyerah."
    hide Diponegoro
    jump kedu
