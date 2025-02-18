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


label stage3:
    $ quick_menu = True 
#Stage 3-1 #(story)
    Narator "Setelah kemenangan gemilang di Sungai Progo dan Lembah Selarong, pasukan Pangeran Diponegoro melanjutkan perjuangan mereka ke daerah strategis berikutnya, Bagelen. Terletak di jalur utama menuju Yogyakarta, wilayah ini menjadi target penting baik bagi pasukan Diponegoro maupun kolonial Belanda. Pasukan Belanda, yang mulai menyadari ancaman dari Diponegoro, telah mendirikan benteng pertahanan sementara di dekat desa Karangjati."
    Narator "Pangeran Diponegoro, yang memahami betapa pentingnya posisi Bagelen, mengadakan rapat perang di tengah malam. Suasana tegang, hanya diterangi oleh cahaya obor, ketika para pemimpin dan tokoh agama berkumpul untuk mendiskusikan rencana serangan."

    scene BG_Desa_Tegalrejo
    show Diponegoro:
        xpos -400
    show Kyai_mojo:
        xpos 400
    show Sentot:
        xpos 100
    diponegoro "Saudara-saudaraku, Bagelen adalah kunci menuju kemenangan kita di wilayah selatan Jawa. Jika kita menguasai jalur ini, kita dapat memotong suplai makanan dan senjata Belanda ke Yogyakarta. Kita harus menyerang dengan cepat dan tanpa keraguan."
    sentot "Gusti Pangeran, laporan dari mata-mata kita menunjukkan bahwa benteng Belanda di Karangjati dijaga oleh sekitar 300 prajurit, termasuk pasukan kavaleri. Mereka juga membawa dua meriam besar. Apa strategi kita untuk menghadapi mereka?"
    kyai_mojo "Serangan frontal mungkin akan terlalu berbahaya, Gusti. Kita harus memanfaatkan medan dan kehati-hatian mereka terhadap kita. Jangan lupakan, ini bukan hanya tentang kekuatan, tetapi juga kecerdikan."
    Narator "Dengan pemahaman yang mendalam tentang medan di Bagelen, Pangeran Diponegoro memutuskan untuk memanfaatkan taktik gerilya. Strateginya adalah memancing pasukan Belanda keluar dari benteng mereka dengan serangan kecil, sebelum menyergap mereka di lembah yang sempit."
    scene BG_Desa_Tegalrejo #(Mirror)
    Narator "Ketika malam tiba, pasukan Diponegoro bergerak dengan tenang menuju desa Karangjati. Para prajurit membawa senjata sederhana—tombak, pedang, dan panah—tetapi semangat mereka tidak tertandingi. Di sisi lain, pasukan Belanda bersiap menghadapi kemungkinan serangan, tanpa mengetahui bahwa mereka sedang diintai."
    Mata_mata_Desa "Gusti, kami telah memastikan bahwa pasukan Belanda sedang bersiap untuk patroli malam. Mereka tampaknya tidak menyadari keberadaan kita."
    
    diponegoro "Bagus. Serangan kita akan dimulai ketika mereka bergerak keluar dari benteng. Sentot, pastikan pasukanmu bersiap di sisi selatan lembah. Pasukan panah akan menyerang lebih dulu untuk menciptakan kekacauan."
    sentot "Siap, Gusti. Mereka tidak akan tahu apa yang menghantam mereka."
    Narator "Ketika fajar hampir tiba, suara gong kecil terdengar sebagai tanda dimulainya serangan. Pasukan panah Diponegoro, yang tersembunyi di balik pepohonan, mulai melepaskan hujan panah ke arah patroli Belanda. Dalam kepanikan, pasukan Belanda berusaha mundur ke benteng mereka, tetapi jalan mereka sudah ditutup oleh pasukan infanteri Diponegoro."
    penjaga_belanda "Serangan! Mereka menyerang dari segala arah! Cepat, mundur ke benteng!"
    sentot "Jangan biarkan mereka melarikan diri! Tutup semua jalan keluar!"
    Narator "Pasukan Belanda, yang terbiasa bertempur di medan terbuka dengan formasi yang rapi, terjebak dalam kekacauan. Para prajurit Diponegoro menyerang dengan keberanian luar biasa, memanfaatkan medan lembah untuk menggempur musuh mereka."
        
#Stage 3-2 #(battle)

        #@BATTLE(@3&@6)
        
#Stage 3-3 #(story)
#@3

    scene bg_benteng_belanda
    Komandan_Belanda "Kita tidak bisa bertahan lebih lama lagi! Mundur ke benteng dan siapkan meriam!"
    Narator "Namun, sebelum mereka bisa kembali ke benteng, pasukan Diponegoro telah menduduki pos-pos strategis di sekitar benteng. Dengan panah menyala dan tombak tajam, mereka menghancurkan pertahanan terakhir pasukan Belanda."
    sentot "Kemenangan ada di tangan kita, Gusti! Benteng ini sekarang menjadi milik kita!"
    diponegoro "Kemenangan ini bukan milik kita, tetapi milik rakyat yang kita perjuangkan. Bagelen adalah awal dari sesuatu yang lebih besar. Jangan lengah, karena Belanda pasti akan datang kembali dengan kekuatan lebih besar."
    Narator "Kemenangan di Bagelen membawa semangat baru bagi pasukan Diponegoro dan rakyat setempat. Desa-desa di sekitar wilayah ini mulai bergabung dengan perjuangan, memberikan makanan, senjata, dan dukungan moral. Namun, di sisi lain, Belanda mulai merasakan ancaman yang semakin nyata dari pasukan gerilya Diponegoro."
    hide Diponegoro
    hide Sentot
    hide Kyai_mojo 
    scene BG_Keraton
    Narator "Di Yogyakarta, para pejabat kolonial Belanda mengadakan rapat darurat untuk membahas strategi baru. Mereka tahu bahwa jika Bagelen tidak segera direbut kembali, kontrol mereka atas Jawa akan terancam."
    Pejabat_Belanda "Kita harus memobilisasi lebih banyak pasukan dan senjata ke wilayah Bagelen. Jika kita kehilangan jalur ini, pasukan Diponegoro akan semakin mendekati Yogyakarta. Tidak ada waktu untuk menunggu!"
    Narator "Perang di Bagelen hanya awal dari serangkaian pertempuran panjang yang akan menguji tekad dan keberanian Pangeran Diponegoro serta pengikutnya. Dengan semangat yang tak tergoyahkan, mereka melanjutkan perjuangan mereka, siap menghadapi tantangan  berikutnya."
     
    jump bangelan