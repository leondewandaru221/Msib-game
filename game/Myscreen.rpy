label Myscreen:


screen Mapscreen:
    on "show" action SetVariable("quick_menu", False)
    add "images/Stage/background.png" at truecenter

    # Tegalrejo
    if stage_completed["tegalrejo"]:
        imagebutton:
            xpos 180
            ypos 600
            idle "images/Stage/tegalrejo.png"
            hover "images/Stage hover/tegalrejo.png"
            action Jump("prolog")

    # Sungai Progo
    if stage_completed["sungai_progo"]:
        imagebutton:
            xpos 470
            ypos 450
            idle "images/Stage/sungai progo.png"
            hover "images/Stage hover/sungai progo.png"
            action Jump("stage1")

    # Kedu
    if stage_completed["kedu"]:
        imagebutton:
            xpos 780
            ypos 650
            idle "images/Stage/kedu.png"
            hover "images/Stage hover/kedu.png"
            action Jump("stage2")

    # Bangelan
    if stage_completed["bangelan"]:
        imagebutton:
            xpos 960
            ypos 400
            idle "images/Stage/bangelan.png"
            hover "images/Stage hover/bangelan.png"
            action Jump("stage3")

    # Lembah Selarong
    if stage_completed["lembah_selarong"]:
        imagebutton:
            xpos 1260
            ypos 680
            idle "images/Stage/lembah selarong.png"
            hover "images/Stage hover/lembah selarong.png"
            action Jump("stage4")

    # Goa Brubus
    if stage_completed["goa_brubus"]:
        imagebutton:
            xpos 1430
            ypos 440
            idle "images/Stage/goa brubus.png"
            hover "images/Stage hover/goa brubus.png"
            action Jump("stage5")

    # Tombol Pengaturan
    imagebutton:
        xpos 100
        ypos 70
        idle "images/Stage/settings.png"
        hover "images/Stage hover/settings.png"
        action ShowMenu("preferences")

    # Tombol Kembali
    # imagebutton:
    #     xpos 100
    #     ypos 70
    #     idle "images/Stage/return.png"
    #     hover "images/Stage hover/return.png"
    #     action Return()

# Logika untuk menyelesaikan stage
screen Choosehero:
    on "show" action SetVariable("quick_menu", False)
    add "images/hero/background-01.png "   


    imagebutton:
        idle "images/hero/diponegoro select-01.png" 
        hover "images/hero hover/diponegoro select-01_hover.png"
        focus_mask True
        action Jump("Mapscreen_label") 

    imagebutton:
        idle "images/hero/hero select 2-01.png" 
        hover "images/hero hover/hero select 2-01_hover.png"
        focus_mask True
        action NullAction()

    imagebutton:
        idle "images/hero/hero select 3-01.png"
        hover "images/hero hover/hero select 3-01_hover.png"
        focus_mask True
        action NullAction()
    
    imagebutton:
        idle "images/hero/flag earned-01.png" 

    imagebutton:
        idle "images/hero/left button-01.png" 
        hover "images/hero hover/left button-01_hover.png"
        focus_mask True
        action NullAction()
       

    # imagebutton:
    #     idle "images/hero/return button-01.png" 
    #     hover "images/hero hover/return button-01_hover.png"
    #     focus_mask True
    #     action Return()
       

    imagebutton:
        idle "images/hero/right button-01.png" 
        hover "images/hero hover/right button-01_hover.png"
        focus_mask True
        action NullAction()
       

    imagebutton:
        xpos -380
        idle "images/hero/settings button 2-01.png" 
        hover "images/hero hover/settings button 2-01_hover.png"
        focus_mask True
        action ShowMenu("preferences")
        
    
        
label tegalrejo:
    "Kamu telah menyelesaikan stage Sungai Progo!"
    $ stage_completed["sungai_progo"] = True  # Membuka stage berikutnya
    jump Mapscreen_label  # Kembali ke peta

label sungai_progo:
    # Logika dan narasi stage Sungai Progo
    "Kamu telah menyelesaikan stage Sungai Progo!"
    $ stage_completed["kedu"] = True
    jump Mapscreen_label  

label kedu:
    # Logika dan narasi stage Kedu
    "Kamu telah menyelesaikan stage Kedu!"
    $ stage_completed["bangelan"] = True
    jump Mapscreen_label 

label bangelan:
    # Logika dan narasi stage Bangelan
    "Kamu telah menyelesaikan stage Bangelan!"
    $ stage_completed["lembah_selarong"] = True
    jump Mapscreen_label 

label lembah_selarong:
    # Logika dan narasi stage Lembah Selarong
    "Kamu telah menyelesaikan stage Lembah Selarong!"
    $ stage_completed["goa_brubus"] = True
    jump Mapscreen_label 

label goa_brubus:
    # Logika dan narasi stage Goa Brubus
    "Kamu telah menyelesaikan stage Goa Brubus!"
    "Selamat, kamu telah menyelesaikan semua stage!"
    jump Mapscreen_label 





    
   