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


label stage5:
    $ quick_menu = True    
    scene BG_hutan
    Narator "Setelah keberhasilan di wilayah Kedu, Pangeran Diponegoro memusatkan perhatian pada Goa Brubus. Goa ini, yang terletak di daerah perbukitan strategis, digunakan oleh Belanda sebagai pusat logistik dan tempat perlindungan bagi pasukan mereka. Namun, bagi Pangeran Diponegoro, tempat ini lebih dari sekadar wilayah musuh—ia adalah simbol kehormatan, karena goa tersebut sering digunakan oleh rakyat sebagai tempat perlindungan sejak zaman leluhur."
    Narator "Belanda memperkuat Goa Brubus dengan membangun benteng kecil di pintu masuknya, melengkapi pertahanan dengan meriam, dan menempatkan pasukan elit untuk menjaga wilayah itu. Pangeran Diponegoro menyadari bahwa merebut tempat ini bukan hanya soal strategi militer, tetapi juga soal menjaga semangat rakyat di daerah sekitar."
    show Diponegoro:
        xpos -400
    show Kyai_mojo:
        xpos 400
    show Sentot:
        xpos 100
    diponegoro "Kyai Mojo, bagaimana pandanganmu tentang wilayah ini? Goa Brubus adalah tempat suci bagi banyak rakyat kita. Jika kita tidak bertindak, kehormatan mereka akan tercabik-cabik oleh tangan penjajah."
    kyai_mojo "Gusti Pangeran, tempat ini memang istimewa. Namun, merebutnya membutuhkan kehati-hatian. Belanda tahu betapa pentingnya goa ini bagi kita, dan mereka pasti telah menyiapkan jebakan."
    sentot  "Gusti, saya telah memeriksa wilayah ini. Benteng mereka kuat, tetapi mereka bergantung pada satu jalur suplai utama di lereng sebelah utara. Jika kita memutus jalur itu, mereka akan kehilangan akses ke makanan dan amunisi."
    diponegoro "Bagus, Sentot. Kita akan mulai dengan memutus suplai mereka. Sampaikan kepada pasukan untuk bersiap dalam dua hari. Kita akan menyerang dengan kehormatan dan kecerdikan."
    Narator "Dua malam kemudian, pasukan Diponegoro bergerak di bawah naungan kegelapan. Kelompok pertama, yang dipimpin oleh Sentot, bertugas memutus jalur suplai di lereng utara. Kelompok kedua, yang dipimpin langsung oleh Pangeran Diponegoro, mendekati benteng utama di pintu masuk Goa Brubus."
     
    scene BG_TebingSelarong #(ini ntar dulu)

    Narator "Di lereng utara, Sentot dan pasukannya memasang jebakan di sepanjang jalan kecil yang digunakan oleh konvoi suplai Belanda. Saat fajar tiba, sebuah konvoi yang membawa amunisi dan makanan mulai melewati jalan tersebut."
    sentot  "Pasukan, bersiap! Jangan serang sampai mereka benar-benar masuk ke jebakan."
    hide Diponegoro
    hide Sentot
    hide Kyai_mojo
    Narator "Ketika gerobak terakhir dari konvoi memasuki jebakan, Sentot memberi tanda. Seketika, pasukan Diponegoro menyerang dengan hujan anak panah dan tombak. Para prajurit Belanda, yang tidak siap untuk serangan mendadak, segera terpukul mundur."
    Komandan_Konvoi_Belanda "Kita disergap! Kembalikan gerobak dan mundur ke benteng!"
    #Stage 5-2 #(battle)

    #@BATTLE(@3&@8)

    #Stage 5-3 (story)
    #@3
    show Sentot
    sentot "Kirim pesan kepada Gusti Pangeran. Katakan bahwa jalur suplai telah berhasil kita rebut."
    hide Sentot
    scene BG_Goa_Selarong#(ini ntar dulu)
    Narator "Sementara itu, di pintu masuk Goa Brubus, Pangeran Diponegoro memimpin serangan utama. Pasukan Belanda, yang mulai kehabisan suplai, mencoba bertahan dengan meriam mereka. Namun, posisi mereka yang terbatas di pintu masuk goa membuat mereka kesulitan untuk menghadapi taktik gerilya pasukan Jawa."
    Komandan_Belanda "Pertahankan posisi kalian! Jangan biarkan mereka mendekat!"
    Narator "Pasukan Diponegoro membagi diri menjadi beberapa kelompok kecil, menyerang dari berbagai arah untuk mengacaukan formasi Belanda. Saat Belanda fokus menangkis serangan dari satu sisi, kelompok lain menyusup mendekati benteng mereka."
    show Diponegoro:
        xpos -400
    show Sentot:
        xpos 200
    diponegoro "Kita tidak perlu menghancurkan mereka dengan kekuatan, cukup buat mereka menyerah. Sentot, apa laporan dari jalur suplai?"
    sentot"Gusti, jalur suplai telah diputus. Mereka tidak akan bertahan lama tanpa makanan dan amunisi."
    diponegoro "Bagus. Terus tekan mereka, tetapi jangan terburu-buru menyerang langsung. Biarkan kelelahan dan kelaparan menjadi senjata kita."
    Narator "Setelah tiga hari bertahan tanpa suplai, pasukan Belanda di Goa Brubus mulai kehilangan semangat. Para prajuritnya kelelahan, sementara persediaan makanan hampir habis. Dalam situasi ini, Pangeran Diponegoro memberikan perintah akhir untuk menyerang."
    diponegoro "Ini saatnya. Serang dari semua sisi. Biarkan mereka tahu bahwa tanah ini tidak akan pernah jatuh ke tangan penjajah!"
    hide Diponegoro
    hide Sentot
#Stage 5-4 #(battle)
#@BATTLE(@3&@8)        

#Stage 5-5 #(story)

    Komandan_Belanda "Kita tidak punya pilihan lain. Perintahkan mundur! Tinggalkan benteng!"
    Narator "Belanda akhirnya mundur, meninggalkan Goa Brubus di bawah kendali pasukan Diponegoro. Kemenangan ini tidak hanya memperkuat posisi Pangeran Diponegoro, tetapi juga memberikan harapan baru bagi rakyat di wilayah tersebut."
    Penduduk_Desa "Gusti Pangeran, terima kasih telah membebaskan kami dari penjajahan. Kami akan selalu mendukung perjuanganmu!"
    show Diponegoro
    diponegoro "Perjuangan ini adalah milik kita bersama. Terus kuatkan tekad kalian, karena jalan masih panjang."
    hide Diponegoro
    Narator "Setelah kemenangan di Goa Brubus, pasukan Diponegoro melanjutkan perjuangan mereka ke wilayah-wilayah lainnya, memperluas pengaruh dan membangkitkan semangat perlawanan di seluruh Jawa. Namun, Belanda juga mulai mengubah strategi mereka, menggunakan pendekatan yang lebih sistematis untuk menghadapi taktik gerilya Diponegoro. Perang semakin memanas, membawa kedua belah pihak ke pertempuran-pertempuran yang lebih besar dan menentukan."
        
#(Kalo misalnya ada stage yang mau dihapus, misal stage 5 lanjutnya kesini)

    Narator "Setelah bertahun-tahun bertempur, keadaan mulai berubah tidak menguntungkan bagi Pangeran Diponegoro. Pasukan Belanda, yang sebelumnya kewalahan menghadapi taktik gerilya, mulai mengadopsi strategi baru di bawah pimpinan Jenderal De Kock. Mereka menerapkan Benteng Stelsel, sebuah sistem untuk membangun benteng-benteng kecil di daerah strategis guna mempersempit ruang gerak pasukan Diponegoro. Di sela-sela pertempuran, Pangeran Diponegoro mengadakan pertemuan penting dengan para pemimpin pasukannya. Wajahnya yang penuh wibawa masih memancarkan keteguhan meskipun situasi kian sulit."
    scene BG_Desa_Tegalrejo
    show Diponegoro:
        xpos -400
    show Kyai_mojo:
        xpos 400
    show Sentot:
        xpos 100
    diponegoro "Saudara-saudaraku, Belanda telah mengubah cara mereka. Mereka membangun benteng-benteng kecil di sepanjang jalur kita. Ini memperlambat gerak pasukan kita."
    sentot "Gusti, pasukan kita juga mulai kekurangan makanan dan perlengkapan. Banyak rakyat yang ketakutan untuk membantu karena ancaman Belanda."
    kyai_mojo "Kita masih memiliki semangat dan iman. Tapi jika keadaan terus begini, kita harus memikirkan langkah baru."
    diponegoro "Kyai, iman kita tidak akan tergoyahkan. Namun, aku tidak akan membiarkan rakyat kita menderita lebih dari ini. Aku akan mencari jalan untuk melindungi mereka."
    Narator "Waktu pun terus berlalu, belum ada tanda kemenangan dari kedua kubu namun Belanda mulai menggunakan taktik licik. Mereka mengirim mata-mata untuk menyusup ke desa-desa yang mendukung Pangeran Diponegoro. Banyak pemimpin desa yang ditangkap atau dibunuh. Pada suatu malam, seorang utusan Belanda datang ke markas Diponegoro membawa pesan."
    hide Sentot
    hide Kyai_mojo    
    Utusan_Belanda "Pangeran Diponegoro, Jenderal De Kock ingin menawarkan perundingan damai. Kami ingin mengakhiri pertumpahan darah ini."
    diponegoro "Damai? Setelah apa yang kalian lakukan terhadap rakyatku? Ini bukan tawaran damai, ini hanyalah tipu muslihat."
    Utusan_Belanda "Gusti, rakyatmu telah menderita cukup lama. Jika perang ini berlanjut, banyak nyawa akan melayang, termasuk orang-orang tak bersalah."
    diponegoro "Aku tidak akan menyerah pada pengkhianatan. Sampaikan kepada De Kock, jika ia ingin damai, bebaskan rakyatku dan kembalikan tanah leluhur kami."
    Narator "Pada tahun 1830, situasi semakin sulit bagi Pangeran Diponegoro. Pasukannya kian terdesak, sementara sumber daya semakin menipis. Dengan berat hati, ia memutuskan untuk menghadiri perundingan dengan Jenderal De Kock di Magelang. Sebelum berangkat, ia berbicara dengan Sentot dan Kyai Mojo."
        
    scene BG_Desa_Tegalrejo #(Zoom Ke Salah Satu Rumah)
    show Kyai_mojo:
        xpos 400
    show Sentot:
        xpos 100
    sentot "Gusti, apakah ini keputusan yang tepat? Aku tidak percaya pada mereka."
    kyai_mojo "Benar, Gusti. Ini bisa saja jebakan."
    diponegoro "Aku tahu risikonya. Tapi jika ini adalah jalan untuk menyelamatkan rakyatku, aku harus mencobanya. Aku pergi bukan untuk menyerah, tetapi untuk memastikan mereka tidak lagi menderita."
    Narator "Pangeran Diponegoro tiba di Magelang bersama beberapa pengikut setianya. Di sana, ia disambut dengan penuh kehormatan oleh Jenderal De Kock dan para pejabat Belanda."
    hide Sentot
    hide Kyai_mojo
    scene BG_Keraton
    show Dipenogoro:
        xpos -400
    De_Kock "Pangeran Diponegoro, terima kasih telah datang. Kami menghormati keberanian dan tekad Anda. Kami berharap pertemuan ini dapat membawa perdamaian."
    diponegoro "Jika kalian benar-benar menginginkan perdamaian, bebaskan rakyatku dari pajak yang memberatkan. Kembalikan tanah mereka. Hanya itu yang aku minta."
    De_Kock "Itu adalah tuntutan yang sulit, Pangeran. Tapi mari kita bicarakan lebih lanjut."
    Narator "Pertemuan itu berlangsung dengan suasana yang penuh ketegangan. Namun, setelah beberapa saat, pasukan Belanda yang tersembunyi muncul dan mengepung tempat perundingan."
    show Sentot:
        xpos 100
    sentot "Gusti! Ini jebakan!"
    hide Sentot
    diponegoro "Aku sudah menduganya. Tapi mereka tidak akan pernah menang atas kebenaran."
    De_Kock "Pangeran, Anda ditangkap. Perang ini telah berakhir."
    diponegoro "Kalian mungkin menang hari ini, tetapi semangat perjuangan kami tidak akan pernah mati. Rakyat Jawa akan melanjutkan perlawanan."
    Narator "Diponegoro dan pengikutnya dibawa ke Semarang, lalu ke Batavia, sebelum akhirnya diasingkan ke Manado."
    Narator "Pada tahun 1834, Pangeran Diponegoro dipindahkan ke Makassar. Ia hidup dalam pengasingan, tetapi tetap dihormati oleh rakyat yang mengenang keberaniannya. Seorang pengikut setianya, yang berhasil mengunjunginya di Makassar, berbicara dengan sang pangeran."
    Pengikut "Gusti, rakyat masih merindukan Anda. Mereka percaya suatu hari nanti penjajahan akan berakhir."
    diponegoro "Sampaikan kepada mereka untuk terus berjuang. Aku mungkin tidak lagi bersama mereka, tetapi semangat ini tidak akan pernah padam."
    Narator "Pada Akhirnya Pangeran Diponegoro wafat pada 8 Januari 1855 di Benteng Rotterdam, Makassar. Namun, perjuangannya menjadi inspirasi besar bagi rakyat Indonesia untuk terus melawan penjajahan hingga akhirnya meraih kemerdekaan pada tahun 1945."
    hide Diponegoro

        #Setelah Membaca Cerita
        
#Stage 5-6 #(story)
    scene bg_library_path
    show Ali:
        xpos -500
    show Siti:
        xpos -100
    siti "Wow, ceritanya begitu mendalam dan emosional. Aku benar-benar merasakan semangat perjuangan Pangeran Diponegoro di setiap langkahnya. Bagaimana menurutmu, Ali?"
    ali "Aku setuju. Ini bukan sekadar cerita tentang perang fisik melawan penjajah, tapi juga perang moral. Perhatikan bagaimana Pangeran Diponegoro selalu menekankan pentingnya keadilan dan iman. Itu luar biasa."
    siti "Benar. Aku terkesan dengan karakternya yang tegas namun bijaksana. Dia tahu bahwa perjuangan melawan penjajahan bukan hanya tentang balas dendam, tapi tentang membela kehormatan dan tanah leluhur. Dia seorang pemimpin yang punya prinsip."
    ali "Betul. Tapi di sisi lain, aku merasa kasihan padanya. Bayangkan, dia tidak hanya melawan pasukan Belanda yang lebih kuat secara senjata, tetapi juga menghadapi pengkhianatan dari bangsawan keraton. Itu pasti sangat menyakitkan."
    siti "Ya, bagian itu sangat menyayat hati. Namun, aku juga kagum bagaimana dia tetap teguh meskipun menghadapi tantangan dari luar dan dalam. Lihat saja ketika utusan keraton datang dengan tawaran damai palsu. Dia tidak tergoda dan tetap pada pendiriannya."
    ali "Dia benar-benar visioner. Dia tahu apa yang dia perjuangkan bukan hanya untuk dirinya, tapi untuk seluruh rakyat Jawa, bahkan generasi mendatang. Namun, yang membuatku frustrasi adalah taktik licik Belanda. Mereka tahu mereka tidak bisa menang secara langsung, jadi mereka menggunakan Benteng Stelsel dan mata-mata."
    siti "Itu memang kejam. Tapi aku rasa di situlah kekuatan cerita ini—ia menunjukkan betapa kerasnya perjuangan melawan penjajahan. Tidak ada yang mudah. Bahkan dengan semua penderitaan itu, semangat Pangeran Diponegoro tidak pernah padam."
    ali "Dan itu terbukti ketika dia memutuskan untuk menghadiri perundingan dengan De Kock. Dia tahu itu berisiko, tapi dia tetap pergi demi rakyatnya. Aku tidak bisa membayangkan beban mental yang dia tanggung saat membuat keputusan itu."
    siti "Bagian itu benar-benar memilukan. Ketika jebakan itu terungkap, aku merasa marah sekaligus bangga. Marah karena Belanda tidak punya kehormatan, tapi bangga karena Pangeran Diponegoro tidak pernah kehilangan martabatnya. Bahkan saat ditangkap, dia tetap menolak untuk tunduk."
    ali "Itulah yang membuatnya menjadi simbol perlawanan. Meskipun dia diasingkan, perjuangannya menjadi inspirasi. Aku suka bagian di akhir, ketika dia berkata bahwa semangat perjuangan tidak akan pernah padam. Itu memberi harapan."
    siti "Ya, dan aku pikir penting bagi kita untuk mengingat cerita seperti ini. Pangeran Diponegoro tidak hanya berjuang dengan senjata, tetapi juga dengan keyakinan dan cinta untuk tanah air. Dia adalah contoh nyata bagaimana seorang pemimpin harus bertindak."
    ali "Setuju. Dan bukan hanya itu, perjuangannya juga menunjukkan pentingnya persatuan. Bayangkan, para petani, tokoh agama, dan pemuda desa bersatu di bawah kepemimpinannya. Kalau saja kita bisa belajar lebih banyak dari semangat itu hari ini."
    siti "Benar sekali. Cerita ini mengajarkan bahwa meskipun kita menghadapi rintangan besar, kita harus tetap percaya pada tujuan kita. Perjuangan Pangeran Diponegoro mengingatkan kita bahwa kemerdekaan tidak datang dengan mudah."
    ali "Dan aku pikir, selain untuk mengenang, cerita ini juga seharusnya menjadi pengingat bagi kita untuk menghargai kemerdekaan yang telah diperjuangkan dengan darah dan air mata."
    siti "Tepat. Kita hidup di zaman yang berbeda, tapi semangat dan nilai-nilai perjuangan itu tetap relevan. Aku harap cerita seperti ini terus diceritakan, terutama untuk generasi muda, agar mereka tidak melupakan sejarah."
    ali "Ya, dan aku pikir kita beruntung bisa membaca cerita seperti ini. Membuatku merasa lebih menghargai perjuangan mereka."
    siti "Aku juga. Jadi, bagaimana kalau kita coba mencari tahu lebih banyak tentang kisah perjuangan lainnya? Aku penasaran dengan pahlawan-pahlawan lain yang juga menginspirasi."
    ali "Itu ide bagus. Ayo, kita mulai."
    Narator "Ketika mereka ingin mengambil buku cerita pahlawan yang baru, tiba-tiba pak Joko menghampiri mereka."
    show Joko:
        xpos 400
    pak_joko "Ali, Siti, bapak tahu kalian sangat bersemangat mengenai cerita pahlawan, tapi lebih baik kalian pulang dulu hari ini. Waktu sudah terlalu sore dan sebentar lagi perpustakaan juga akan tutup."
    Narator "Ali dan Siti melihat-lihat keluar."
    ali "Oh iya, benar kata Pak Joko ini sudah terlalu sore, lebih baik kita pulang sekarang Ti."
    siti "Iya kita terlalu fokus pada ceritanya sampai hamper lupa waktu. Kalua begitu kita langsung pulang yuk Li."
    ali "Yuk Siti. Oh ya terima kasih telah mengingatkan kami ya Pak Joko, kalua tidak kami akan terbablas tadi."
    pak_joko "Sama-sama, cepatlah kalian pulang sebelum malam hari tiba."
    ali_siti "Baik pak joko. Selamat sore."
    pak_joko "Sore juga."
    hide ali
    hide siti
    hide pak_joko
    jump goa_brubus