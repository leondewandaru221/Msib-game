init python:

    def stage3_reset_battle_variables():
        global stage3_player_health, stage3_player_stamina, stage3_cooldown_turns, stage3_cooldown_turns_health
        global stage3_enemy_health, stage3_turn, stage3_turn_count

        # Reset player stats
        stage3_player_health = stage3_player_max_health
        stage3_player_stamina = stage3_player_max_stamina
        stage3_cooldown_turns = 0
        stage3_cooldown_turns_health = 0

        # Reset enemy stats
        stage3_enemy_health = stage3_enemy_max_health

        # Reset turn indicator
        stage3_turn = "stage3_player"
        stage3_turn_count = 1

    def stage3_enemy3_attack_player():
        global stage3_enemy_damage, stage3_player_defense_up, stage3_player_defense, stage3_player_health
        damage = stage3_enemy_damage
        if stage3_player_defense_up:
            damage = max(0, stage3_enemy_damage - stage3_player_defense)
            stage3_player_defense_up = False
        
        stage3_player_health = max(0, stage3_player_health - damage)
        renpy.play("images/rpg/sound/gun/gun.mp3")
        renpy.show_screen("stage3_fire_animation")
        renpy.show_screen("stage3_delay_screen_enemy", 0.3, Function(stage3_turn_of, "stage3_player"))
        # stage3_turn_of("stage3_player")  # Kembali ke giliran player

    stage3_target_enemy = None  # Target awal belum ditentukan

# Function Action Select Musuh
    def stage3_select_enemy(target):
        global stage3_target_enemy
        stage3_target_enemy = target  # Simpan target yang dipilih
### Function Action Select Musuh


# Function Action Basic Serangan Pangeran
    def stage3_attack_selected_enemy():
        global stage3_target_enemy, stage3_player_damage, stage3_enemy_health, stage3_player_stamina, stage3_player_max_stamina
        if stage3_target_enemy == "enemy3":
            renpy.play("images/rpg/sound/slash/basic_attack.mp3")
            renpy.show_screen("stage3_attack_animation")
            damage = stage3_player_damage
            stage3_enemy_health = max(0, stage3_enemy_health - damage)
            stage3_player_stamina = min(stage3_player_stamina + 7, stage3_player_max_stamina)  # Menambahkan stamina tanpa melebihi batas maksimal
            if stage3_enemy_health <= 0:
                renpy.hide_screen("stage3_attack_animation")
            if stage3_enemy_health > 0 and stage3_player_health > 0:
                renpy.show_screen("stage3_delay_screen", 0.3, Function(stage3_enemy3_attack_player))
        
        # Setelah menyerang, reset target dan hilangkan indikator
        stage3_target_enemy = None
### Function Action Basic Serangan Pangeran


# Function Action Kemampuan Pangeran
    def stage3_kemampuan_selected_enemy():
        global stage3_target_enemy, stage3_player_kemampuan, stage3_enemy_health, stage3_player_stamina, stage3_cooldown_turns

        # Cek apakah ada cooldown
        if stage3_cooldown_turns > 0:
            return  # Tidak lakukan apa-apa jika cooldown belum selesai
        
        if stage3_target_enemy == "enemy3":
            renpy.play("images/rpg/sound/slash/skill_attack.mp3")
            renpy.show_screen("stage3_slash_animation")
            damage = stage3_player_kemampuan
            stage3_player_stamina = max(0, stage3_player_stamina - 35)
            stage3_enemy_health = max(0, stage3_enemy_health - damage)
            stage3_cooldown_turns = 3
            if stage3_enemy_health <= 0:
                renpy.hide_screen("stage3_slash_animation")
            if stage3_enemy_health > 0 and stage3_player_health > 0:
                renpy.show_screen("stage3_delay_screen", 0.5, Function(stage3_enemy3_attack_player))
    
        # Setelah menyerang, reset target dan hilangkan indikator
        stage3_target_enemy = None
### Function Action Kemampuan Pangeran


# Function Image Kemampuan Pangeran
    def stage3_get_skill_image():
        if stage3_player_stamina >= 35 and stage3_cooldown_turns == 0:
            return "images/rpg/ui/icon/skill_slash.png"
        else:
            return "images/rpg/ui/icon/skill_slash_disable.png"

    def stage3_get_skill_hover():
        if stage3_player_stamina >= 35 and stage3_cooldown_turns == 0:
            return "images/rpg/ui/icon/skill_slash_hover.png"
        else:
            return None  # Tidak ada efek hover jika kemampuan sedang cooldown

    def stage3_get_skill_action():
        if stage3_player_stamina >= 35 and stage3_cooldown_turns == 0:
            return Function(stage3_kemampuan_selected_enemy)
        else:
            return NullAction()  # Tidak melakukan apa-apa jika cooldown belum selesai
### Function Image Kemampuan Pangeran


# Function Action Kemampuan Health
    def stage3_kemampuan_health():
        global stage3_target_enemy, stage3_player_kemampuan, stage3_player_health, stage3_player_max_health, stage3_player_stamina, stage3_cooldown_turns_health

        # Cek apakah ada cooldown
        if stage3_cooldown_turns_health > 0:
            return  # Tidak lakukan apa-apa jika cooldown belum selesai
        
        if stage3_player_stamina >= 40:
            renpy.play("images/rpg/sound/health/health.mp3")
            renpy.show_screen("stage3_health_animation")
            stage3_player_stamina = max(0, stage3_player_stamina - 40)
            stage3_player_health = min(stage3_player_health + 40, stage3_player_max_health)
            stage3_cooldown_turns_health = 5
            
            if stage3_enemy_health > 0 and stage3_player_health > 0:
                renpy.show_screen("stage3_delay_screen", 2.8, Function(stage3_enemy3_attack_player))
    
    # Setelah Health, reset indikator
        stage3_target_enemy = None
### Function Action Kemampuan Health


# Function Image Kemampuan Pangeran
    def stage3_get_health_image():
        if stage3_player_stamina >= 40 and stage3_cooldown_turns_health == 0:
            return "images/rpg/ui/icon/skill_health.png"
        else:
            return "images/rpg/ui/icon/skill_health_disable.png"

    def stage3_get_health_hover():
        if stage3_player_stamina >= 40 and stage3_cooldown_turns_health == 0:
            return "images/rpg/ui/icon/skill_health_hover.png"
        else:
            return None  # Tidak ada efek hover jika kemampuan sedang cooldown

    def stage3_get_health_action():
        if stage3_player_stamina >= 40 and stage3_cooldown_turns_health == 0:
            return Function(stage3_kemampuan_health)
        else:
            return NullAction()  # Tidak melakukan apa-apa jika cooldown belum selesai
### Function Image Kemampuan Pangeran


# Function Turn Count
    def stage3_turn_of(stage3_entity):
        global stage3_turn, stage3_turn_count, stage3_cooldown_turns, stage3_cooldown_turns_health

        # Kurangi cooldown setiap turn
        if stage3_cooldown_turns > 0:
            stage3_cooldown_turns -= 1

        if stage3_cooldown_turns_health > 0:
            stage3_cooldown_turns_health -= 1

        # Update turn dan stage3_turn_count
        stage3_turn = stage3_entity
        stage3_turn_count += 1

        renpy.show_screen("stage3_delay_count", 0.3, NullAction())  # Contoh, tergantung giliran yang diinginkan
### Function Turn Count


# Player Stats
define stage3_player_max_health = 100
define stage3_player_health = 100
define stage3_player_max_stamina = 100
define stage3_player_stamina = 100
define stage3_cooldown_turns = 0
define stage3_cooldown_turns_health = 0
define stage3_player_damage = 13
define stage3_player_kemampuan = 30
define stage3_player_defense = 8
define stage3_player_defense_up = False
### Player Stats

# Enemy Stats
define stage3_enemy_max_health = 200
define stage3_enemy_health = 200
define stage3_enemy_damage = 12
define stage3_enemy_defense = 5
define stage3_enemy_defense_up = False
### Enemy Stats


# Turn Turn Count Indicator
define stage3_turn = "stage3_player"
define stage3_turn_count = 1
### Turn Count Indicator

# player Animation
define stage3_pangeran_animation = Animation(
    "images/rpg/character/pangeran/animation/pangeran_animation_100.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_101.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_102.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_103.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_104.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_105.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_106.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_107.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_108.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_109.png", 0.1,
    "images/rpg/character/pangeran/animation/pangeran_animation_110.png", 0.1,
    repeat=True
)

# Enemy Animation
define enemy3_animation = Animation(
    "images/rpg/character/enemy3/animation/enemy3_animation_00.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_01.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_02.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_03.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_04.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_05.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_06.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_07.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_08.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_09.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_10.png", 0.1,
    repeat=True
)

define enemy3_animation_hover = Animation(
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_00.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_01.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_02.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_03.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_04.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_05.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_06.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_07.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_08.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_09.png", 0.1,
    "images/rpg/character/enemy3/animation/enemy3_animation_hover_10.png", 0.1,
    repeat=True
)

define stage3_fire_animation = Animation(
    "images/rpg/effect/fire_animation/enemy3_fire_animation.png", 0.1
)

define stage3_player_attack_animation = Animation(
    "images/rpg/character/enemy3/stage3_attack_animation/stage3_attack_animation_enemy3_1.png", 0.1,
    "images/rpg/character/enemy3/stage3_attack_animation/stage3_attack_animation_enemy3_2.png", 0.1,
    "images/rpg/character/enemy3/stage3_attack_animation/stage3_attack_animation_enemy3_3.png", 0.1
)

define stage3_player_slash_animation = Animation(
    "images/rpg/character/enemy3/stage3_slash_animation/stage3_slash_animation_enemy3_1.png", 0.1,
    "images/rpg/character/enemy3/stage3_slash_animation/stage3_slash_animation_enemy3_2.png", 0.1,
    "images/rpg/character/enemy3/stage3_slash_animation/stage3_slash_animation_enemy3_3.png", 0.1,
    "images/rpg/character/enemy3/stage3_slash_animation/stage3_slash_animation_enemy3_4.png", 0.1,
    "images/rpg/character/enemy3/stage3_slash_animation/stage3_slash_animation_enemy3_5.png", 0.1
)

define stage3_player_health_animation = Animation(
    "images/rpg/effect/health_animation/health_animation_01.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_02.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_03.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_04.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_05.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_06.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_07.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_08.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_09.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_10.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_11.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_12.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_13.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_14.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_15.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_16.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_17.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_18.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_19.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_20.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_21.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_22.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_23.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_24.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_25.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_26.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_27.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_28.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_29.png", 0.1,
    "images/rpg/effect/health_animation/health_animation_30.png", 0.1
)

screen stage3_delay_screen(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("stage3_delay_screen"):
        $ renpy.hide_screen("stage3_delay_screen")
    if renpy.get_screen("stage3_delay_screen_enemy"):
        $ renpy.hide_screen("stage3_delay_screen_enemy")
    if renpy.get_screen("stage3_fire_animation"):
        $ renpy.hide_screen("stage3_fire_animation")

screen stage3_delay_screen_enemy(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("stage3_attack_animation"):
        $ renpy.hide_screen("stage3_attack_animation")
    if renpy.get_screen("stage3_slash_animation"):
        $ renpy.hide_screen("stage3_slash_animation")
    if renpy.get_screen("stage3_delay_screen"):
        $ renpy.hide_screen("stage3_delay_screen")
    if renpy.get_screen("stage3_health_animation"):
        $ renpy.hide_screen("stage3_health_animation")
    if renpy.get_screen("stage3_fire_animation"):
        $ renpy.hide_screen("stage3_fire_animation")

screen stage3_delay_count(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("stage3_attack_animation"):
        $ renpy.hide_screen("stage3_attack_animation")
    if renpy.get_screen("stage3_slash_animation"):
        $ renpy.hide_screen("stage3_slash_animation")
    if renpy.get_screen("stage3_delay_screen"):
        $ renpy.hide_screen("stage3_delay_screen")
    if renpy.get_screen("stage3_delay_screen_enemy"):
        $ renpy.hide_screen("stage3_delay_screen_enemy")
    if renpy.get_screen("stage3_health_animation"):
        $ renpy.hide_screen("stage3_health_animation")
    if renpy.get_screen("stage3_fire_animation"):
        $ renpy.hide_screen("stage3_fire_animation")


# Image Background
image battle_background = "images/rpg/background/battle_forest_background.png"


label third_battle:
    $ quick_menu = False 
    scene battle_background
    hide bg_school_afternoon
    python:
        stage3_reset_battle_variables()

    play music "images/rpg/sound/historical_environment/battle_music.mp3" loop
    
    call screen combat_stage3

screen stage3_attack_animation():
    add stage3_player_attack_animation align (0.5, 0.5)

screen stage3_slash_animation():
    add stage3_player_slash_animation align (0.5, 0.5)

screen stage3_health_animation():
    add stage3_player_health_animation align (0.5, 0.5)

screen stage3_fire_animation():
    add stage3_fire_animation align (0.5, 0.5)
    

# Screen Stage 3
screen combat_stage3:

    # Battle Status
    image "images/rpg/ui/battle_status.png"
    

    imagebutton:
        idle stage3_pangeran_animation


    # Image Musuh
    if stage3_enemy_health > 0:
        imagebutton:
            idle enemy3_animation
            hover enemy3_animation_hover
            focus_mask True
            action Function(stage3_select_enemy, "enemy3")

    # Button Health
    imagebutton:
        idle stage3_get_health_image()
        hover stage3_get_health_hover()
        focus_mask True
        action stage3_get_health_action()
    
    # Button Attack (Hanya berfungsi jika target dipilih)
    imagebutton:
        idle "images/rpg/ui/icon/attack.png"
        hover "images/rpg/ui/icon/attack_hover.png"
        focus_mask True
        action Function(stage3_attack_selected_enemy)
    
    # Button Skill
    imagebutton:
        idle stage3_get_skill_image()
        hover stage3_get_skill_hover()
        focus_mask True
        action stage3_get_skill_action()


    # Player Health Bar
    bar:
        xpos 593
        ypos 774
        range stage3_player_max_health
        value stage3_player_health
        left_bar "images/rpg/ui/bar/player_bar.png"
        right_bar "images/rpg/ui/bar/bar_back.png"
        xysize(699, 60)
    text "[stage3_player_health]/[stage3_player_max_health]":
        xalign 0.5
        ypos 812
        size 18

    # Player Stamina Bar
    bar:
        xpos 593
        ypos 821
        range stage3_player_max_stamina
        value stage3_player_stamina
        left_bar "images/rpg/ui/bar/stamina_bar.png"
        right_bar "images/rpg/ui/bar/bar_back.png"
        xysize(699, 60)
    text "[stage3_player_stamina]/[stage3_player_max_stamina]":
        xalign 0.5
        ypos 861
        size 18

    # Musuh Health Bar
    if stage3_enemy_health > 0:
        bar:
            xpos 1280
            ypos 165
            range stage3_enemy_max_health
            value stage3_enemy_health
            left_bar "images/rpg/ui/bar/enemy_bar.png"
            right_bar "images/rpg/ui/bar/bar_back.png"
            xysize(300, 70)

    # Win Screen
    if stage3_player_health <= 0:
        use stage3_enemy_win

    if stage3_enemy_health <= 0:
        use stage3_player_win  # Panggil label yang menampilkan screen

    if stage3_target_enemy == "enemy3":
        image "images/rpg/ui/turn_enemy0_indicator.png"

    # Turn Bar
    text "[stage3_turn_count]":
        xalign 0.5
        yalign 0.08
        color "#ffffff"

screen stage3_player_win:
    # Pop Up Reward
    add "images/rpg/reward/stage3_popup_reward_3stars.png"

    # Ganti textbutton menjadi imagebutton
    imagebutton:
        idle "images/rpg/reward/next_stage.png"
        hover "images/rpg/reward/next_stage_hover.png"
        focus_mask True
        action [Jump("after_third_battle"), Function(renpy.hide_screen, "combat_stage3")]
    
    imagebutton:
        idle "images/rpg/reward/stage_try_again.png"
        hover "images/rpg/reward/stage_try_again_hover.png"
        focus_mask True
        action [
            Function(stage3_reset_battle_variables),  # Reset variabel pertarungan
            Jump("third_battle")  # Kembali ke label third_battle
        ]


screen stage3_enemy_win:
    # Pop Up Reward
    add "images/rpg/reward/popup_lose.png"

    # Imagebutton untuk mencoba ulang
    imagebutton:
        idle "images/rpg/reward/try_again.png"
        hover "images/rpg/reward/try_again_hover.png"
        focus_mask True
        action [
            Function(stage3_reset_battle_variables),  # Reset variabel pertarungan
            Jump("third_battle")  # Kembali ke label third_battle
        ]