# Definisi karakter
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

default stage_completed = {
    "tegalrejo": True,      # Stage pertama terbuka secara default
    "sungai_progo": False,
    "kedu": False,
    "bangelan": False,
    "lembah_selarong": False,
    "goa_brubus": False,
}

# Transform untuk animasi teks berjalan
transform text_scroll_left:
    xpos -1.0 ypos 0.5 # Posisi awal di luar layar (kiri)
    linear 5.0 xpos 0.5  # Bergerak ke tengah layar selama 5 detik

transform text_scroll_up:
    xpos 0.5 ypos 1.2  # Posisi awal di bawah layar
    linear 5.0 ypos 0.5  # Bergerak ke tengah layar selama 5 detik

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 1.0

transform darken:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    linear 0.5 matrixcolor TintMatrix("#4e4e4e") * SaturationMatrix(1.0)

transform lighten:
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)


# Definisikan layar untuk menu utama
# screen main_menu():
#     tag menu
    
#     # Gambar latar belakang menu
#     add "Menu.png"  # Sesuaikan nama file gambar dengan file yang Anda unggah
    
#     # Tombol menu
#     vbox:
#         align (0.9, 0.5)  # Posisi tombol (X, Y)
#         spacing 20

#         # Tombol Mulai Game
#         textbutton "Mulai Game" action Start() style "menu_button"
        
#         # Tombol Load Game
#         textbutton "Lanjutkan" action ShowMenu("load") style "menu_button"
        
#         # Tombol Keluar
#         textbutton "Keluar" action Quit() style "menu_button"

        


# # Gaya tombol menu
# style menu_button:
#     size 30
#     font "DejaVuSans.ttf"  # Ganti font jika perlu
#     background "#8B4513"
#     hover_background "#CD853F"
#     text_align 0.5
#     padding (10, 20)

# screen rollback():
    
#     # Gambar latar belakang menu
#     #image Previous : "gui/Page 3 Visual Novel dll/Visual Novel page/Previous.png"
#     # Tombol menu
#     vbox:
#         align (0.99, 0.65)  # Posisi tombol (X, Y)
#         spacing 20

#         # Tombol Mulai Game
#         textbutton _("Previous") action Rollback() style "rollback"
       



# # Gaya tombol previous
# style rollback:
#     size 30
#     font "DejaVuSans.ttf"  # Ganti font jika perlu
#     background "#FFFFFF"
#     hover_background "Previous.png"
#     text_align 0.5
    
    
# Label untuk cerita visual novel
label start:
    # Tampilkan layar rollback
    # show screen rollback
    # Scene 1: Ali di rumah
    scene bg_room with fade

    # Teks berjalan dari kanan ke tengah
    show text "{color=#FFFFFF}Cerita ini mengambil kisah tentang Pangeran Diponegoro. Beberapa bagian mungkin tidak sesuai dengan cerita aslinya. Tolong jangan terlalu serius." at text_scroll_left
    pause 6  # Durasi lebih panjang agar teks terlihat lebih lama

    # Hilangkan teks pertama
    hide text with fade

    # Teks berjalan dari bawah ke tengah
    show text "{color=#FFFFFF}Di malam yang cerah." at text_scroll_up
    pause 6
    # Tambahkan tombol Previous dengan gambar


    call screen Choosehero with fade


label prolog:
    $ quick_menu = True 

    scene bg_kmmalam
    
    ibu "Ali, cepat tidur. Sudah jam setengah sepuluh sekarang."

    show Ali
    ali "Iya bu, sebentar lagi Ali tidur."
    ali "Sebelum tidur coba baca buku sebentar ah. Mumpung besok pelajaran sejarah, coba baca-baca dikit deh."
    hide Ali
    # Ali membaca buku
    narrator "Ali mengambil buku Sejarah dari dalam tasnya."
    show Ali 
    ali "Ok, sekarang apa yang harus kubaca ya?"
    ali "Coba baca bagian sejarah perjuangan pahlawan deh."
    hide Ali
    narrator "Ali pun membaca buku sampai rasa kantuk mulai menghampirinya."
    show Ali 
    ali "Aduh, mata mulai ngantuk nih. Tapi baru sedikit bacanya. Lanjut lagi deh sedikit lagi."
    hide Ali
    narrator "Ali melanjutkan membaca buku, sampai akhirnya tertidur saat membaca."
    scene bg_room
    hide bg_kmmalam

    # Prolog P-2
    #story and battle

    # Ali bermimpi
    Narator "Setelah tertidur, Ali pun bermimpi tentang apa yang dibacanya tadi."
    # Kembali ke dunia nyata
    scene bg_forest_path
    show Ali
    ali "Hah, dimana ini."
    hide Ali
    show sentot
    sentot"Semua pasukan, siapkan senjata. Jangan serang sampai ada aba-aba."
    prajurit "Siap, Panglima!"
    hide sentot
    Narator "Tiba-tiba, suara gong kecil berbunyi sebagai tanda dimulainya serangan. Pasukan pemanah melepaskan hujan anak panah ke arah pasukan Belanda. Para penjaga berteriak, terkejut oleh serangan mendadak ini. Ali merasa semakin bingung dimana dia berada."

    prajurit_belanda "Serangan! Cepat, bentuk formasi!"

    Narator "Saat Belanda berusaha bertahan, pasukan Diponegoro dari kedua sisi keluar dari persembunyian mereka. Mereka menyerang dengan cepat, memanfaatkan kekacauan di kubu Belanda."

    show sentot 
    sentot "Jangan beri mereka waktu untuk mengatur ulang barisan!"
    hide sentot
    jump first_battle
    #Battle
    #show Bg_hutan
label battle_conclusion:
    stop music fadeout 2.0
    show sentot 
    sentot "Jangan beri mereka waktu untuk mengatur ulang barisan!"
    hide sentot 
    # Kembali ke dunia nyata
    narrator "Ali tiba-tiba terbangun, kaget dengan apa yang baru saja dialaminya."
    show Ali
    ali "Wah, mimpi tadi terasa nyata sekali. Sepertinya aku harus lebih banyak belajar tentang sejarah Pangeran Diponegoro."
    hide Ali
    # Adegan setelah pertempuran
    prajurit_belanda "Mundur! Mundur ke tengah benteng! "
    narrator "Pertempuran berlangsung sengit hingga fajar tiba. Dengan taktik yang cerdik, pasukan Diponegoro berhasil menguasai benteng."
    show Diponegoro 
    diponegoro "Kemenangan ini bukan akhir, tetapi awal dari perlawanan yang lebih besar. Bersiaplah, karena Belanda pasti akan membalas."
    hide Diponegoro 
    # Ali menyadari situasi
    narrator "Ali yang melihat itu kemudian teringat dengan buku yang dia baca."
    show Ali 
    ali "Sepertinya aku mulai ingat. Bukannya itu Pangeran Diponegoro?"
    ali "Iya, itu benar Pangeran Diponegoro. Aku akan coba untuk mendekat."
    hide Ali
    scene bg_room
    hide bg_battlefield
    narrator "Saat Ali mencoba mendekati pasukan Pangeran Diponegoro, tiba-tiba Ali mendengar suara yang tidak asing."
    narrator "*Kringggggg* *Kringggggg*"
    narrator "Ali pun terbangun setelah mendengar suara itu dan mencoba menggapai suara tersebut."
    scene bg_kmsiang
    hide bg_room
    show Ali
    ali "Ternyata cuma alarm HP. Oh ya, sekarang jam berapa?"
    hide Ali
    narrator "Ali pun melihat jam yang ada pada handphonenya dan merasa terkejut."
    show Ali 
    ali "Astaga, udah jam 6 lewat aja. Aku harus buru-buru!"
    hide Ali
    narrator "Ali pun dengan terburu-buru pergi ke sekolah."
    scene bg_classroom
    hide bg_kmsiang
    label class_scene:
    # Adegan kelas sejarah
    show bg_school_afternoon
   
    show bg_room
    Narator "Di siang hari tepatnya pukul 14.00 WIB, Ali dan Siti sedang berada di kelas Sejarah. Di kelas ini mereka belajar tentang para pahlawan masa lalu."
    bu_guru "Baik anak-anak, kali ini kita akan belajar tentang sejarah pahlawan-pahlawan di masa lalu. Siapkan buku kalian ya."
    
    murid "Baik, Bu."
    
    narrator "Selama 2 jam, Ibu memberikan cerita tentang para pahlawan masa lalu. Tak terasa, waktu pelajaran pun sudah berakhir."
    bu_guru "Baik anak-anak, sampai di sini saja pelajaran kita hari ini. Jangan lupa, ambil pesan-pesan penting dari cerita yang Bapak sampaikan tadi. Selamat siang semuanya."
    murid "Baik, Bu. Selamat siang juga, Bu."
    scene bg_library_night
    hide bg_school_afternoon
# Adegan menuju perpustakaan
    scene bg_library_night
    narrator "Matahari mulai condong ke arah barat, meninggalkan warna jingga di langit. Ali dan Siti, dua sahabat yang suka baca buku, melangkah keluar dari gerbang sekolah."
    narrator "Hari ini, mereka sedang ingin belajar lebih dalam soal perjuangan bangsa Indonesia. Mereka pun sepakat untuk mampir ke perpustakaan."
    narrator "Langkah mereka terasa ringan sambil menyusuri jalan setapak di dekat sekolahan. Pohon-pohon besar di sepanjang jalan seolah ikut mendukung semangat mereka."
    narrator "Suasana sore itu membuat hati mereka tenang dan makin siap untuk menjelajahi dunia pengetahuan. Setelah beberapa saat berjalan, tibalah mereka di depan perpustakaan."
    show Ali:
        xpos -200
    show Siti:
        xpos 200
    siti "Akhirnya kita tiba juga, Li, di perpustakaan."
    ali "Iya, aku udah nggak sabar lagi untuk baca cerita mereka berdua."
    siti "Kita masuk yuk."
    ali "Ayuk."
    
    #scene bg_library_inside
    narrator "Mereka pun masuk ke dalam perpustakaan tersebut."
    ali "Wah, besar juga ya perpustakaannya."
    siti "Iya, besar juga. Di perpustakaan sebesar ini, gimana caranya kita menemukan buku yang kita ingin baca ya?"
    ali "Iya, gimana ya?"
    
    # Bertemu Pak Joko
    narrator "Setelah melihat-lihat sekeliling, mereka melihat ada seorang penjaga perpustakaan di bagian pinggir. Mereka berdua pun memutuskan untuk menghampirinya."
    siti "Lihat, di pinggir sana, Li. Ada penjaga perpustakaan di ujung sana."
    ali "Oh iya, kita samperin ke sana yuk."
    siti "Yuk."
    hide Ali 
    hide Siti 
    #show librarian neutral at center
    narrator "Mereka berdua menghampiri penjaga perpustakaan tersebut."
    show Ali:
        xpos -500
    show Siti:
        xpos -200
    show Joko:
        xpos 400
    ali "Selamat sore, Pak. Kami ingin mencari buku cerita tentang Pangeran Diponegoro. Kira-kira ada di rak bagian mana ya, Pak?"
    librarian "Oh, kalian ingin membaca buku tentang sejarah perjuangan para pahlawan ya? Kalian bisa temukan di rak berikutnya setelah rak di depan saya. Untuk cerita Pangeran Diponegoro, ada di bagian atas rak."
    siti "Terima kasih untuk infonya, Pak."
    librarian "Tidak apa-apa, Nak. Oh iya, siapa nama kalian? Bapak ingin membuatkan kartu perpustakaan untuk kalian berdua."
    ali "Nama saya Ali, Pak, dan teman saya ini namanya Siti."
    librarian "Oke, Ali dan Siti, silakan, ini kartunya. Oh iya, kalian bisa panggil saya Pak Joko."
    siti "Terima kasih, Pak Joko. Kami berdua akan ke rak yang Bapak bilang tadi."
    librarian "Oke, kalau perlu bantuan, panggil Pak Joko aja ya."
    ali_siti "Baik, Pak."
    hide Joko
    # Mencari buku
    scene bg_reading_room 
    show Ali:
        xpos -500
    show Siti:
        xpos -200
    narrator "Mereka berdua pun berjalan menuju ke arah yang diberitahukan oleh Pak Joko tadi."
    ali "Wah, banyak juga buku sejarahnya ya, Siti."
    siti "Iya, banyak banget. Oh iya, jangan lupa, Li, kita ke sini untuk baca buku Pangeran Diponegoro."
    ali "Oh iya, kata Pak Joko tadi ada di bagian atas, tapi aku tidak menemukannya. Coba kamu cari di bagian kanan, Ti. Aku cari di bagian kiri."
    siti "Oke, Li."

    narrator "Mereka pun mencari buku itu selama beberapa menit."
    siti "Li, ke sini, Li! Aku nemu bukunya."
    ali "Di mana, Ti, bukunya?"
    siti "Di bagian situ, Li. Kamu sampai nggak buat ambil bukunya?"
    ali "Aku coba dulu deh."

    narrator "Ali berusaha mengambil buku itu sambil jinjit, tetapi tetap tidak sampai untuk mengambil bukunya."
    ali "Ti, kayaknya aku nggak sampai deh. Boleh kamu ke Pak Joko untuk minta tolong ambilkan buku yang kita mau?"
    siti "Oke, Li."

    # Meminta bantuan Pak Joko
    #show librarian neutral at left
    show bg_reading_room
    show Ali:
        xpos -500
    show Siti:
        xpos -200
    narrator "Siti pun pergi menghampiri Pak Joko untuk meminta tolong."
    siti "Oh iya, Pak Joko, aku mau minta tolong. Bukunya terlalu tinggi, jadi kami nggak bisa ambilnya."
    show Joko:
        xpos 400
    librarian "Oh begitu, ayo antar Bapak, nanti Bapak ambilkan."
    siti "Terima kasih, Pak Joko."
    narrator "Siti pun membawa Pak Joko ke tempat Ali."
    ali "Halo lagi, Pak Joko. Maaf mengganggu waktunya."
    librarian "Gak papa, ini bukunya."
    ali "Terima kasih, Pak Joko."
    librarian "Sama-sama, semoga senang membacanya."
    ali_siti "Baik, Pak."


    # Membaca buku
    scene bg_library_path
    show Ali:
        xpos -500
    show Siti:
        xpos -200
    narrator "Ali dan Siti mencari tempat duduk untuk membaca bukunya. Tidak lama berjalan, mereka pun duduk di kursi yang kosong."
    ali "Kita baca aja yuk bukunya."
    siti "Yuk."
    narrator "Mereka pun membaca buku tentang kisah Pangeran Diponegoro."

# Adegan membaca buku
    scene bg_school_afternoon 
    narrator "Ali dan Siti mulai membaca buku tentang Pangeran Diponegoro. Mereka larut dalam kisah perjuangan sang pahlawan."
    
    scene bg_forest_path
    narrator "Pada suatu malam yang tenang di bulan November 1785, Kesultanan Yogyakarta diselimuti kedamaian. Langit malam dipenuhi bintang-bintang, seolah menjadi saksi atas keajaiban yang akan terjadi."
    narrator "Di sebuah rumah sederhana jauh dari hiruk-pikuk istana, Raden Ayu Mangkarawati tengah berbaring, merasakan detik-detik kelahiran putranya."
    narrator "Sementara itu, di luar ruangan, suasana tegang menyelimuti para abdi dalem yang berkumpul. Mereka berbisik-bisik, saling berbagi harapan bahwa bayi yang akan lahir ini akan membawa berkah bagi Kesultanan Yogyakarta."

    midwife "Raden Ayu, tarik napas yang dalam. Sebentar lagi, bayi ini akan lahir."
    show Ibu
    raden_ayu "Semoga ia lahir dengan selamat. Aku merasakan kekuatan yang besar dalam dirinya."
    hide Ibu
    narrator "Tak lama kemudian, tangisan bayi pecah, memenuhi malam yang sunyi. Suara itu menggema, seperti menggetarkan hati setiap orang yang mendengarnya."
    midwife "Selamat, Raden Ayu. Seorang putra telah lahir. Lihatlah, ia kuat dan sehat."
    show Ibu
    raden_ayu "Anakku, kau adalah karunia dari Yang Maha Kuasa. Kelak, kau akan membawa perubahan besar untuk tanah ini."
    hide Ibu
    
    abdi_dalem "Tangisan bayi ini berbeda. Ada sesuatu dalam dirinya, sesuatu yang agung."

    scene bg_forest_path
    narrator "Sejak kecil, Raden Mas Mustahar tumbuh dengan nilai-nilai kerakyatan yang ditanamkan oleh ibunya."
    narrator "Pada suatu sore, ketika Raden Mas Mustahar bermain di pinggir sawah bersama para petani, ia melihat seekor burung bangau bertengger di atas pohon."

    show Young_mustahar :
        xpos -200
    show Ibu :
        xpos 200
    young_mustahar "Ibu, lihatlah burung itu. Ia terlihat begitu tenang meskipun angin berhembus kencang."
    show Ibu
    raden_ayu "Itulah kekuatan yang harus kau miliki, Nak. Seorang pemimpin harus tetap tenang meski badai datang."

    narrator "Seiring waktu, Raden Mas Mustahar tumbuh menjadi anak yang bijaksana. Pada suatu malam, ia duduk di serambi rumah bersama ibunya."
    
    scene bg_forest_path
    young_mustahar "Ibu, aku ingin seperti Gunung Merapi."
    raden_ayu "Mengapa begitu, Nak?"
    young_mustahar "Gunung itu kokoh dan melindungi semua yang ada di bawahnya. Aku ingin menjadi seperti itu, melindungi tanah ini dan rakyatnya."
    raden_ayu "Jika itu yang kau inginkan, kau harus belajar banyak, bukan hanya dari buku, tapi juga dari kehidupan rakyat kecil."
    hide Young_mustahar
    hide Ibu
    # Perjalanan Belajar
    narrator "Perkataan ibunya menjadi pedoman bagi Raden Mas Mustahar. Ia mulai belajar dari para petani, pedagang, dan ulama."
    show Kyai_mojo :
        xpos 200
    show Young_mustahar:
        xpos -200
    kyai_mojo "Mas Mustahar, kau adalah keturunan raja. Namun, ingatlah, darah biru bukanlah alasan untuk merasa lebih tinggi dari orang lain."
    young_mustahar "Aku mengerti, Kyai. Seorang pemimpin harus melayani rakyatnya, bukan sebaliknya."
    hide Kyai_mojo
    hide Young_mustahar
    narrator "Hari-hari berlalu, Raden Mas Mustahar tumbuh menjadi seorang pemuda yang tangguh. Ia dikenal dengan nama Pangeran Diponegoro."
    
    scene bg_forest_path
    narrator "Meskipun berdarah bangsawan, ia memilih untuk tinggal di desa Tegalrejo, jauh dari kehidupan mewah keraton. Ia merasa bahwa istana telah kehilangan semangat perjuangan dan terlalu tunduk kepada pengaruh Belanda."
    show Diponegoro:
        xpos -300
    show Ibu:
        xpos 300
    diponegoro "Di sini, di desa ini, aku bisa merasakan denyut kehidupan rakyat. Istana terlalu sunyi dari suara rakyat kecil."
    raden_ayu "Kau benar, Nak. Kemewahan sering kali membutakan hati. Tetaplah dekat dengan mereka, karena dari merekalah kekuatan sejati seorang pemimpin berasal."
    hide Diponegoro
    hide Ibu
    # Semangat Perjuangan
    narrator "Setiap pagi, Pangeran Diponegoro berjalan mengelilingi desa. Ia berbincang dengan petani, mendengar keluhan mereka tentang pajak yang mencekik dan tanah-tanah mereka yang mulai dirampas oleh pemerintah kolonial."
    
    petani "Gusti Pangeran, tanah kami telah diambil oleh Belanda. Kami tak tahu harus ke mana lagi."
    show Diponegoro
    diponegoro "Aku mendengar kesedihanmu, Pak Wiryo. Ketahuilah, ini bukan hanya tentang tanahmu, tapi tentang kehormatan kita sebagai rakyat Jawa."
    hide Diponegoro
    narrator "Rasa marah dan ketidakadilan mulai membara di dalam dirinya. Ia menyadari bahwa Belanda tidak hanya ingin menguasai tanah Jawa, tetapi juga menghancurkan nilai-nilai luhur yang dipegang oleh rakyatnya."
    narrator "Suatu hari, di ladang yang gersang, ia bertemu dengan seorang pemuda bernama Santri Suro, yang kemudian menjadi salah satu pengikut setianya."
    santri_suro "Gusti Pangeran, aku telah melihat banyak kezaliman. Jika kau memimpin perlawanan, aku akan menjadi prajuritmu."

    narrator "Semangat perjuangan mulai berkobar di hati rakyat Jawa. Perjalanan Pangeran Diponegoro menuju perlawanan besar pun dimulai."

    # Akhiri adegan
    scene bg_library_path 
    narrator "Ali dan Siti menutup buku itu dengan wajah kagum. Kisah perjuangan Pangeran Diponegoro begitu membekas di hati mereka."
    show Ali:
        xpos -200
    show Siti:
        xpos 200
    ali "Ti, aku jadi ingin belajar lebih banyak tentang sejarah kita."
    siti "Aku juga, Li. Pangeran Diponegoro adalah teladan bagi kita semua."
    jump tegalrejo
    

    return
