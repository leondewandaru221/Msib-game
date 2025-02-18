init python:

    def reset_battle_variables():
        global player_health, player_stamina, cooldown_turns, cooldown_turns_health
        global enemy_health, turn, turn_count

        # Reset player stats
        player_health = player_max_health
        player_stamina = player_max_stamina
        cooldown_turns = 0
        cooldown_turns_health = 0

        # Reset enemy stats
        enemy_health = enemy_max_health

        # Reset turn indicator
        turn = "player"
        turn_count = 1

    def attack_player():
        global enemy_damage, player_defense_up, player_defense, player_health
        damage = enemy_damage
        if player_defense_up:
            damage = max(0, enemy_damage - player_defense)
            player_defense_up = False
        
        player_health = max(0, player_health - damage)
        renpy.play("images/rpg/sound/gun/gun.mp3")
        renpy.show_screen("fire_animation")
        renpy.show_screen("delay_screen_enemy", 0.3, Function(turn_of, "player"))
        # turn_of("player")  # Kembali ke giliran player

    target_enemy = None  # Target awal belum ditentukan

# Function Action Select Musuh
    def select_enemy(target):
        global target_enemy
        target_enemy = target  # Simpan target yang dipilih
### Function Action Select Musuh


# Function Action Basic Serangan Pangeran
    def attack_selected_enemy():
        global target_enemy, player_damage, enemy_health, player_stamina, player_max_stamina
        if target_enemy == "enemy0":
            renpy.play("images/rpg/sound/slash/basic_attack.mp3")
            renpy.show_screen("attack_animation")
            damage = player_damage
            enemy_health = max(0, enemy_health - damage)
            player_stamina = min(player_stamina + 7, player_max_stamina)  # Menambahkan stamina tanpa melebihi batas maksimal
            if enemy_health <= 0:
                renpy.hide_screen("attack_animation")
            if enemy_health > 0 and player_health > 0:
                renpy.show_screen("delay_screen", 0.3, Function(attack_player))
        
        # Setelah menyerang, reset target dan hilangkan indikator
        target_enemy = None
### Function Action Basic Serangan Pangeran


# Function Action Kemampuan Pangeran
    def kemampuan_selected_enemy():
        global target_enemy, player_kemampuan, enemy_health, player_stamina, cooldown_turns

        # Cek apakah ada cooldown
        if cooldown_turns > 0:
            return  # Tidak lakukan apa-apa jika cooldown belum selesai
        
        if target_enemy == "enemy0":
            renpy.play("images/rpg/sound/slash/skill_attack.mp3")
            renpy.show_screen("slash_animation")
            damage = player_kemampuan
            player_stamina = max(0, player_stamina - 35)
            enemy_health = max(0, enemy_health - damage)
            cooldown_turns = 3
            if enemy_health <= 0:
                renpy.hide_screen("slash_animation")
            if enemy_health > 0 and player_health > 0:
                renpy.show_screen("delay_screen", 0.5, Function(attack_player))
    
        # Setelah menyerang, reset target dan hilangkan indikator
        target_enemy = None
### Function Action Kemampuan Pangeran


# Function Image Kemampuan Pangeran
    def get_skill_image():
        if player_stamina >= 35 and cooldown_turns == 0:
            return "images/rpg/ui/icon/skill_slash.png"
        else:
            return "images/rpg/ui/icon/skill_slash_disable.png"

    def get_skill_hover():
        if player_stamina >= 35 and cooldown_turns == 0:
            return "images/rpg/ui/icon/skill_slash_hover.png"
        else:
            return None  # Tidak ada efek hover jika kemampuan sedang cooldown

    def get_skill_action():
        if player_stamina >= 35 and cooldown_turns == 0:
            return Function(kemampuan_selected_enemy)
        else:
            return NullAction()  # Tidak melakukan apa-apa jika cooldown belum selesai
### Function Image Kemampuan Pangeran


# Function Action Kemampuan Health
    def kemampuan_health():
        global target_enemy, player_kemampuan, player_health, player_max_health, player_stamina, cooldown_turns_health

        # Cek apakah ada cooldown
        if cooldown_turns_health > 0:
            return  # Tidak lakukan apa-apa jika cooldown belum selesai
        
        if player_stamina >= 40:
            renpy.play("images/rpg/sound/health/health.mp3")
            renpy.show_screen("health_animation")
            player_stamina = max(0, player_stamina - 40)
            player_health = min(player_health + 40, player_max_health)
            cooldown_turns_health = 5
            
            if enemy_health > 0 and player_health > 0:
                renpy.show_screen("delay_screen", 2.8, Function(attack_player))
    
    # Setelah Health, reset indikator
        target_enemy = None
### Function Action Kemampuan Health


# Function Image Kemampuan Pangeran
    def get_health_image():
        if player_stamina >= 40 and cooldown_turns_health == 0:
            return "images/rpg/ui/icon/skill_health.png"
        else:
            return "images/rpg/ui/icon/skill_health_disable.png"

    def get_health_hover():
        if player_stamina >= 40 and cooldown_turns_health == 0:
            return "images/rpg/ui/icon/skill_health_hover.png"
        else:
            return None  # Tidak ada efek hover jika kemampuan sedang cooldown

    def get_health_action():
        if player_stamina >= 40 and cooldown_turns_health == 0:
            return Function(kemampuan_health)
        else:
            return NullAction()  # Tidak melakukan apa-apa jika cooldown belum selesai
### Function Image Kemampuan Pangeran


# Function Turn Count
    def turn_of(entity):
        global turn, turn_count, cooldown_turns, cooldown_turns_health

        # Kurangi cooldown setiap turn
        if cooldown_turns > 0:
            cooldown_turns -= 1

        if cooldown_turns_health > 0:
            cooldown_turns_health -= 1

        # Update turn dan turn_count
        turn = entity
        turn_count += 1

        renpy.show_screen("delay_count", 0.3, NullAction())  # Contoh, tergantung giliran yang diinginkan
### Function Turn Count


# Player Stats
define player_max_health = 100
define player_health = 100
define player_max_stamina = 100
define player_stamina = 100
define cooldown_turns = 0
define cooldown_turns_health = 0
define player_damage = 13
define player_kemampuan = 30
define player_defense = 8
define player_defense_up = False
### Player Stats

# Enemy Stats
define enemy_max_health = 75
define enemy_health = 75
define enemy_damage = 8
define enemy_defense = 5
define enemy_defense_up = False
### Enemy Stats


# Turn Turn Count Indicator
define turn = "player"
define turn_count = 1
### Turn Count Indicator

# player Animation
define pangeran_animation = Animation(
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
define enemy1_animation = Animation(
    "images/rpg/character/enemy/animation/enemy1_animation_00.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_01.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_02.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_03.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_04.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_05.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_06.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_07.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_08.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_09.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_10.png", 0.1,
    repeat=True
)

define enemy1_animation_hover = Animation(
    "images/rpg/character/enemy/animation/enemy1_animation_hover_00.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_01.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_02.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_03.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_04.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_05.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_06.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_07.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_08.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_09.png", 0.1,
    "images/rpg/character/enemy/animation/enemy1_animation_hover_10.png", 0.1,
    repeat=True
)

define fire_animation = Animation(
    "images/rpg/effect/fire_animation/fire_animation.png", 0.1
)

define player_attack_animation = Animation(
    "images/rpg/effect/attack_animation/attack_animation_1.png", 0.1,
    "images/rpg/effect/attack_animation/attack_animation_2.png", 0.1,
    "images/rpg/effect/attack_animation/attack_animation_3.png", 0.1
)

define player_slash_animation = Animation(
    "images/rpg/effect/slash_animation/slash_animation_1.png", 0.1,
    "images/rpg/effect/slash_animation/slash_animation_2.png", 0.1,
    "images/rpg/effect/slash_animation/slash_animation_3.png", 0.1,
    "images/rpg/effect/slash_animation/slash_animation_4.png", 0.1,
    "images/rpg/effect/slash_animation/slash_animation_5.png", 0.1
)

define player_health_animation = Animation(
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

screen delay_screen(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("delay_screen"):
        $ renpy.hide_screen("delay_screen")
    if renpy.get_screen("delay_screen_enemy"):
        $ renpy.hide_screen("delay_screen_enemy")
    if renpy.get_screen("fire_animation"):
        $ renpy.hide_screen("fire_animation")

screen delay_screen_enemy(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("attack_animation"):
        $ renpy.hide_screen("attack_animation")
    if renpy.get_screen("slash_animation"):
        $ renpy.hide_screen("slash_animation")
    if renpy.get_screen("delay_screen"):
        $ renpy.hide_screen("delay_screen")
    if renpy.get_screen("health_animation"):
        $ renpy.hide_screen("health_animation")
    if renpy.get_screen("fire_animation"):
        $ renpy.hide_screen("fire_animation")

screen delay_count(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("attack_animation"):
        $ renpy.hide_screen("attack_animation")
    if renpy.get_screen("slash_animation"):
        $ renpy.hide_screen("slash_animation")
    if renpy.get_screen("delay_screen"):
        $ renpy.hide_screen("delay_screen")
    if renpy.get_screen("delay_screen_enemy"):
        $ renpy.hide_screen("delay_screen_enemy")
    if renpy.get_screen("health_animation"):
        $ renpy.hide_screen("health_animation")
    if renpy.get_screen("fire_animation"):
        $ renpy.hide_screen("fire_animation")


# Image Background
image battle_background = "images/rpg/background/battle_forest_background.png"


label first_battle:
    $ quick_menu = False 
    scene battle_background
    hide bg_school_afternoon
    python:
        reset_battle_variables()

    play music "images/rpg/sound/historical_environment/battle_music.mp3" loop
    
    call screen combat_stage1

screen attack_animation():
    add player_attack_animation align (0.5, 0.5)

screen slash_animation():
    add player_slash_animation align (0.5, 0.5)

screen health_animation():
    add player_health_animation align (0.5, 0.5)

screen fire_animation():
    add fire_animation align (0.5, 0.5)
    

# Screen Stage 1
screen combat_stage1:

    # Battle Status
    image "images/rpg/ui/battle_status.png"
    

    imagebutton:
        idle pangeran_animation


    # Image Musuh
    if enemy_health > 0:
        imagebutton:
            idle enemy1_animation
            hover enemy1_animation_hover
            focus_mask True
            action Function(select_enemy, "enemy0")

    # Button Health
    imagebutton:
        idle get_health_image()
        hover get_health_hover()
        focus_mask True
        action get_health_action()
    
    # Button Attack (Hanya berfungsi jika target dipilih)
    imagebutton:
        idle "images/rpg/ui/icon/attack.png"
        hover "images/rpg/ui/icon/attack_hover.png"
        focus_mask True
        action Function(attack_selected_enemy)
    
    # Button Skill
    imagebutton:
        idle get_skill_image()
        hover get_skill_hover()
        focus_mask True
        action get_skill_action()


    # Player Health Bar
    bar:
        xpos 593
        ypos 774
        range player_max_health
        value player_health
        left_bar "images/rpg/ui/bar/player_bar.png"
        right_bar "images/rpg/ui/bar/bar_back.png"
        xysize(699, 60)
    text "[player_health]/[player_max_health]":
        xalign 0.5
        ypos 812
        size 18

    # Player Stamina Bar
    bar:
        xpos 593
        ypos 821
        range player_max_stamina
        value player_stamina
        left_bar "images/rpg/ui/bar/stamina_bar.png"
        right_bar "images/rpg/ui/bar/bar_back.png"
        xysize(699, 60)
    text "[player_stamina]/[player_max_stamina]":
        xalign 0.5
        ypos 861
        size 18

    # Musuh Health Bar
    if enemy_health > 0:
        bar:
            xpos 1280
            ypos 165
            range enemy_max_health
            value enemy_health
            left_bar "images/rpg/ui/bar/enemy_bar.png"
            right_bar "images/rpg/ui/bar/bar_back.png"
            xysize(300, 70)

    # Win Screen
    if player_health <= 0:
        use enemy_win

    if enemy_health <= 0:
        use player_win  # Panggil label yang menampilkan screen

    if target_enemy == "enemy0":
        image "images/rpg/ui/turn_enemy0_indicator.png"

    # Turn Bar
    text "[turn_count]":
        xalign 0.5
        yalign 0.08
        color "#ffffff"

screen player_win:
    # Pop Up Reward
    add "images/rpg/reward/popup_reward_3stars.png"

    # Ganti textbutton menjadi imagebutton
    imagebutton:
        idle "images/rpg/reward/next_stage.png"
        hover "images/rpg/reward/next_stage_hover.png"
        focus_mask True
        action [Jump("battle_conclusion"), Function(renpy.hide_screen, "combat_stage1")]
    
    imagebutton:
        idle "images/rpg/reward/stage_map.png"
        hover "images/rpg/reward/stage_map_hover.png"
        focus_mask True
        action NullAction()


screen enemy_win:
    # Pop Up Reward
    add "images/rpg/reward/popup_lose.png"

    # Imagebutton untuk mencoba ulang
    imagebutton:
        idle "images/rpg/reward/try_again.png"
        hover "images/rpg/reward/try_again_hover.png"
        focus_mask True
        action [
            Function(reset_battle_variables),  # Reset variabel pertarungan
            Jump("battle_conclusion")  # Kembali ke label first_battle
        ]