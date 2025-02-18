init python:
    
    def stage2_reset_battle_variables():
        global stage2_player_health, stage2_player_stamina, stage2_cooldown_turns, stage2_cooldown_turns_health
        global stage2_enemy1_health, stage2_enemy2_health, stage2_turn, stage2_turn_count

        # Reset player stats
        stage2_player_health = player_max_health
        stage2_player_stamina = player_max_stamina
        stage2_cooldown_turns = 0
        stage2_cooldown_turns_health = 0

        # Reset enemy stats
        stage2_enemy1_health = stage2_enemy1_max_health
        stage2_enemy2_health = stage2_enemy2_max_health

        # Reset turn indicator
        stage2_turn = "stage2_player"
        stage2_turn_count = 1

# Function Action Select Musuh
    def stage2_select_enemy(target):
        global stage2_target_enemy
        stage2_target_enemy = target  # Simpan target yang dipilih
### Function Action Select Musuh

# Function Enemy 1 - Attack Player
    def stage2_enemy1_attack_player():
        global stage2_enemy1_damage, stage2_enemy1_health, stage2_enemy2_health, stage2_enemy2_health, stage2_player_defense_up, stage2_player_defense, stage2_player_health
        if stage2_enemy1_health <= 0 and stage2_enemy2_health > 0:
            stage2_enemy2_attack_player()
        if stage2_enemy2_health <= 0:
            damage = stage2_enemy1_damage
            stage2_player_health = max(0, stage2_player_health - damage)
            renpy.play("images/rpg/sound/gun/gun.mp3")
            renpy.show_screen("stage2_enemy1_fire_animation")
            renpy.show_screen("stage2_delay_screen_enemy1", 0.3, Function(stage2_turn_of, "stage2_player"))
        if stage2_enemy1_health > 0 and stage2_enemy2_health > 0:
            damage = stage2_enemy1_damage
            stage2_player_health = max(0, stage2_player_health - damage)
            renpy.play("images/rpg/sound/gun/gun.mp3")
            renpy.show_screen("stage2_enemy1_fire_animation")
            renpy.show_screen("stage2_delay_screen_enemy1", 0.3, Function(stage2_enemy2_attack_player))

    stage2_target_enemy = None  # Target awal belum ditentukan
### Function Enemy 1 - Attack Player

# Function Enemy 2 - Attack Player
    def stage2_enemy2_attack_player():
        global stage2_enemy2_damage, stage2_enemy2_health, stage2_player_defense_up, stage2_player_defense, stage2_player_health
        if stage2_enemy2_health <= 0 and stage2_enemy1_health > 0:
            stage2_enemy1_attack_player()
        if stage2_enemy1_health <= 0 and stage2_enemy2_health > 0:
            damage = stage2_enemy2_damage
            stage2_player_health = max(0, stage2_player_health - damage)
            renpy.play("images/rpg/sound/gun/gun.mp3")
            renpy.show_screen("stage2_enemy2_fire_animation")
            renpy.show_screen("stage2_delay_screen_enemy2", 0.3, Function(stage2_turn_of, "stage2_player"))
        if stage2_enemy2_health > 0 and stage2_enemy1_health > 0:
            damage = stage2_enemy2_damage
            stage2_player_health = max(0, stage2_player_health - damage)
            renpy.play("images/rpg/sound/gun/gun.mp3")
            renpy.show_screen("stage2_enemy2_fire_animation")
            renpy.show_screen("stage2_delay_screen_enemy2", 0.3, Function(stage2_turn_of, "stage2_player"))

    stage2_target_enemy = None  # Target awal belum ditentukan
### Function Enemy 2 - Attack Player

# Function Action Basic Attack
    def stage2_attack_selected_enemy():
        global stage2_target_enemy, stage2_player_damage, stage2_enemy1_health, stage2_enemy2_health, stage2_player_stamina, stage2_player_max_stamina
        if stage2_target_enemy == "enemy1":
            damage = stage2_player_damage
            stage2_enemy1_health = max(0, stage2_enemy1_health - damage)
            stage2_player_stamina = min(stage2_player_stamina + 7, stage2_player_max_stamina)  # Menambahkan stamina
            if stage2_enemy1_health <= 0 and stage2_enemy2_health <= 0:
                # renpy.show_screen("attack_enemy1_animation")
                renpy.hide_screen("attack_enemy1_animation")
                # renpy.show_screen("stage2_delay_screen", 0.3, NullAction())
            if stage2_enemy1_health <= 0 and stage2_enemy2_health > 0:
                renpy.play("images/rpg/sound/slash/basic_attack.mp3")
                renpy.show_screen("attack_enemy1_animation")
                renpy.show_screen("stage2_delay_screen", 0.3, Function(stage2_enemy2_attack_player))
            if stage2_enemy1_health > 0:
                renpy.play("images/rpg/sound/slash/basic_attack.mp3")
                renpy.show_screen("attack_enemy1_animation")
                renpy.show_screen("stage2_delay_screen", 0.3, Function(stage2_enemy1_attack_player))
        
        if stage2_target_enemy == "enemy2":
            damage = stage2_player_damage
            stage2_enemy2_health = max(0, stage2_enemy2_health - damage)
            stage2_player_stamina = min(stage2_player_stamina + 7, stage2_player_max_stamina)  # Menambahkan stamina
            if stage2_enemy2_health <= 0 and stage2_enemy1_health <= 0:
                renpy.show_screen("stage2_delay_screen", 0.3, NullAction())
            if stage2_enemy2_health <= 0 and stage2_enemy1_health > 0:
                renpy.play("images/rpg/sound/slash/basic_attack.mp3")
                renpy.show_screen("attack_enemy2_animation")
                renpy.show_screen("stage2_delay_screen", 0.3, Function(stage2_enemy1_attack_player))
            if stage2_enemy2_health > 0:
                renpy.play("images/rpg/sound/slash/basic_attack.mp3")
                renpy.show_screen("attack_enemy2_animation")
                renpy.show_screen("stage2_delay_screen", 0.3, Function(stage2_enemy1_attack_player))
        
        # Setelah menyerang, reset target dan hilangkan indikator
        stage2_target_enemy = None
### Function Action Basic Attack

# Function Action Kemampuan Health
    def stage2_kemampuan_health():
        global stage2_enemy1_health, stage2_target_enemy, stage2_player_kemampuan, stage2_player_health, stage2_player_max_health, stage2_player_stamina, stage2_cooldown_turns_health

        # Cek apakah ada cooldown
        if stage2_cooldown_turns_health > 0:
            return  # Tidak lakukan apa-apa jika cooldown belum selesai
        
        if stage2_player_stamina >= 40:
            renpy.play("images/rpg/sound/health/health.mp3")
            renpy.show_screen("health_animation")
            stage2_player_stamina = max(0, stage2_player_stamina - 40)
            stage2_player_health = min(stage2_player_health + 40, stage2_player_max_health)
            stage2_cooldown_turns_health = 5
            if stage2_enemy1_health > 0:
                renpy.show_screen("stage2_delay_screen", 2.8, Function(stage2_enemy1_attack_player))
            if stage2_enemy1_health <= 0:
                renpy.show_screen("stage2_delay_screen", 2.8, Function(stage2_enemy2_attack_player))
    
    # Setelah Health, reset indikator
        stage2_target_enemy = None
### Function Action Kemampuan Health

# Function Image Button Health
    def stage2_get_health_image():
        if stage2_player_stamina >= 40 and stage2_cooldown_turns_health == 0:
            return "images/rpg/ui/icon/skill_health.png"
        else:
            return "images/rpg/ui/icon/skill_health_disable.png"

    def stage2_get_health_hover():
        if stage2_player_stamina >= 40 and stage2_cooldown_turns_health == 0:
            return "images/rpg/ui/icon/skill_health_hover.png"
        else:
            return None  # Tidak ada efek hover jika kemampuan sedang cooldown

    def stage2_get_health_action():
        if stage2_player_stamina >= 40 and stage2_cooldown_turns_health == 0:
            return Function(stage2_kemampuan_health)
        else:
            return NullAction()  # Tidak melakukan apa-apa jika cooldown belum selesai
### Function Image Button Health

# Function Action Kemampuan Pangeran
    def stage2_kemampuan_selected_enemy():
        global stage2_target_enemy, stage2_player_kemampuan, stage2_enemy1_health, stage2_enemy2_health, stage2_player_stamina, stage2_cooldown_turns

        # Cek apakah ada cooldown
        if stage2_cooldown_turns > 0:
            return  # Tidak lakukan apa-apa jika cooldown belum selesai
        
        if stage2_target_enemy == "enemy1":
            damage = stage2_player_kemampuan
            stage2_player_stamina = max(0, stage2_player_stamina - 35)
            stage2_enemy1_health = max(0, stage2_enemy1_health - damage)
            stage2_cooldown_turns = 3
            if stage2_enemy1_health <= 0 and stage2_enemy2_health <= 0:
                renpy.hide_screen("slash_enemy1_animation")
            if stage2_enemy1_health <= 0 and stage2_enemy2_health > 0:
                renpy.play("images/rpg/sound/slash/skill_attack.mp3")
                renpy.show_screen("slash_enemy1_animation")
                renpy.show_screen("stage2_delay_screen", 0.5, Function(stage2_enemy2_attack_player))
            if stage2_enemy1_health > 0:
                renpy.play("images/rpg/sound/slash/skill_attack.mp3")
                renpy.show_screen("slash_enemy1_animation")
                renpy.show_screen("stage2_delay_screen", 0.5, Function(stage2_enemy1_attack_player))

        if stage2_target_enemy == "enemy2":
            damage = stage2_player_kemampuan
            stage2_player_stamina = max(0, stage2_player_stamina - 35)
            stage2_enemy2_health = max(0, stage2_enemy2_health - damage)
            stage2_cooldown_turns = 3
            if stage2_enemy2_health <= 0 and stage2_enemy1_health <= 0:
                renpy.show_screen("stage2_delay_screen", 0.5, NullAction())
            if stage2_enemy2_health <= 0 and stage2_enemy1_health > 0:
                renpy.play("images/rpg/sound/slash/skill_attack.mp3")
                renpy.show_screen("slash_enemy2_animation")
                renpy.show_screen("stage2_delay_screen", 0.5, Function(stage2_enemy1_attack_player))
            if stage2_enemy2_health > 0:
                renpy.play("images/rpg/sound/slash/skill_attack.mp3")
                renpy.show_screen("slash_enemy2_animation")
                renpy.show_screen("stage2_delay_screen", 0.5, Function(stage2_enemy1_attack_player))
    
        # Setelah menyerang, reset target dan hilangkan indikator
        stage2_target_enemy = None
### Function Action Kemampuan Pangeran

# Function Image Slash Button
    def stage2_get_skill_image():
        if stage2_player_stamina >= 35 and stage2_cooldown_turns == 0:
            return "images/rpg/ui/icon/skill_slash.png"
        else:
            return "images/rpg/ui/icon/skill_slash_disable.png"

    def stage2_get_skill_hover():
        if stage2_player_stamina >= 35 and stage2_cooldown_turns == 0:
            return "images/rpg/ui/icon/skill_slash_hover.png"
        else:
            return None  # Tidak ada efek hover jika kemampuan sedang cooldown

    def stage2_get_skill_action():
        if stage2_player_stamina >= 35 and stage2_cooldown_turns == 0:
            return Function(stage2_kemampuan_selected_enemy)
        else:
            return NullAction()  # Tidak melakukan apa-apa jika cooldown belum selesai
### Function Image Slash Button

# Function Turn Count
    def stage2_turn_of(stage2_entity):
        global stage2_turn, stage2_turn_count, stage2_cooldown_turns, stage2_cooldown_turns_health

        # Kurangi cooldown setiap turn
        if stage2_cooldown_turns > 0:
            stage2_cooldown_turns -= 1

        if stage2_cooldown_turns_health > 0:
            stage2_cooldown_turns_health -= 1

        # Update turn dan stage2_turn_count
        stage2_turn = stage2_entity
        stage2_turn_count += 1

        renpy.show_screen("stage2_delay_count", 0.3, NullAction())  # Contoh, tergantung giliran yang diinginkan
### Function Turn Count

# Player Stats Stage 2
define stage2_player_max_health = 100
define stage2_player_health = 100
define stage2_player_max_stamina = 100
define stage2_player_stamina = 100
define stage2_cooldown_turns = 0
define stage2_cooldown_turns_health = 0
define stage2_player_damage = 13
define stage2_player_kemampuan = 30
define stage2_player_defense = 8
define stage2_player_defense_up = False
### Player Stats Stage 2

# Enemy 1 Stats
define stage2_enemy1_max_health = 100
define stage2_enemy1_health = 100
define stage2_enemy1_damage = 8
define stage2_enemy1_defense = 5
define stage2_enemy1_defense_up = False
### Enemy Stats

# Enemy 2 Stats
define stage2_enemy2_max_health = 100
define stage2_enemy2_health = 100
define stage2_enemy2_damage = 8
define stage2_enemy2_defense = 5
define stage2_enemy2_defense_up = False
### Enemy 2 Stats

# Turn & Turn Count Indicator
define stage2_turn = "stage2_player"
define stage2_turn_count = 1
### Turn & Turn Count Indicator

# player Animation
define stage2_pangeran_animation = Animation(
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

# Enemy 1 Animation Idle
define stage2_enemy1_animation = Animation(
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_00.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_01.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_02.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_03.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_04.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_05.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_06.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_07.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_08.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_09.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_10.png", 0.1,
    repeat=True
)

# Enemy 1 Animation Hover
define stage2_enemy1_animation_hover = Animation(
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_00.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_01.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_02.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_03.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_04.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_05.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_06.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_07.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_08.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_09.png", 0.1,
    "images/rpg/character/enemy1/animation/stage2_enemy1_animation_hover_10.png", 0.1,
    repeat=True
)

# Enemy 2 Animation Idle
define stage2_enemy2_animation = Animation(
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_00.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_01.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_02.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_03.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_04.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_05.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_06.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_07.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_08.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_09.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_10.png", 0.1,
    repeat=True
)

# Enemy 2 Animation Hover
define stage2_enemy2_animation_hover = Animation(
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_00.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_01.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_02.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_03.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_04.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_05.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_06.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_07.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_08.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_09.png", 0.1,
    "images/rpg/character/enemy2/animation/stage2_enemy2_animation_hover_10.png", 0.1,
    repeat=True
)

# Enemy 1 Fire Animation
define stage2_fire_animation_enemy1 = Animation(
    "images/rpg/effect/fire_animation/enemy1_fire_animation.png", 0.1
)

# Enemy 2 Fire Animation
define stage2_fire_animation_enemy2 = Animation(
    "images/rpg/effect/fire_animation/enemy2_fire_animation.png", 0.1
)

# Basic Attack Animation To Enemy 1
define stage2_player_attack_enemy1_animation = Animation(
    "images/rpg/character/enemy1/stage2_attack_animation_enemy1/stage2_attack_animation_enemy1_01.png", 0.1,
    "images/rpg/character/enemy1/stage2_attack_animation_enemy1/stage2_attack_animation_enemy1_02.png", 0.1,
    "images/rpg/character/enemy1/stage2_attack_animation_enemy1/stage2_attack_animation_enemy1_03.png", 0.1
)

# Skill Attack Animation To Enemy 1
define stage2_player_slash_enemy1_animation = Animation(
    "images/rpg/character/enemy1/stage2_slash_animation_enemy1/stage2_slash_animation_enemy1_01.png", 0.1,
    "images/rpg/character/enemy1/stage2_slash_animation_enemy1/stage2_slash_animation_enemy1_02.png", 0.1,
    "images/rpg/character/enemy1/stage2_slash_animation_enemy1/stage2_slash_animation_enemy1_03.png", 0.1,
    "images/rpg/character/enemy1/stage2_slash_animation_enemy1/stage2_slash_animation_enemy1_04.png", 0.1,
    "images/rpg/character/enemy1/stage2_slash_animation_enemy1/stage2_slash_animation_enemy1_05.png", 0.1
)

# Basic Attack Animation To Enemy 2
define stage2_player_attack_enemy2_animation = Animation(
    "images/rpg/character/enemy2/stage2_attack_animation_enemy2/stage2_attack_animation_enemy2_1.png", 0.1,
    "images/rpg/character/enemy2/stage2_attack_animation_enemy2/stage2_attack_animation_enemy2_2.png", 0.1,
    "images/rpg/character/enemy2/stage2_attack_animation_enemy2/stage2_attack_animation_enemy2_3.png", 0.1
)

# Skill Attack Animation To Enemy 2
define stage2_player_slash_enemy2_animation = Animation(
    "images/rpg/character/enemy2/stage2_slash_animation_enemy2/stage2_slash_animation_enemy2_1.png", 0.1,
    "images/rpg/character/enemy2/stage2_slash_animation_enemy2/stage2_slash_animation_enemy2_2.png", 0.1,
    "images/rpg/character/enemy2/stage2_slash_animation_enemy2/stage2_slash_animation_enemy2_3.png", 0.1,
    "images/rpg/character/enemy2/stage2_slash_animation_enemy2/stage2_slash_animation_enemy2_4.png", 0.1,
    "images/rpg/character/enemy2/stage2_slash_animation_enemy2/stage2_slash_animation_enemy2_5.png", 0.1
)

# Skill Health Animation
define stage2_player_health_animation = Animation(
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

# Screen Delay and Hide Screen
screen stage2_delay_screen(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("stage2_enemy1_fire_animation"):
        $ renpy.hide_screen("stage2_enemy1_fire_animation")
    if renpy.get_screen("stage2_enemy2_fire_animation"):
        $ renpy.hide_screen("stage2_enemy2_fire_animation")
    if renpy.get_screen("health_animation"):
        $ renpy.hide_screen("health_animation")

screen stage2_delay_screen_enemy1(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("attack_enemy1_animation"):
        $ renpy.hide_screen("attack_enemy1_animation")
    if renpy.get_screen("slash_enemy1_animation"):
        $ renpy.hide_screen("slash_enemy1_animation")
    if renpy.get_screen("stage2_delay_screen"):
        $ renpy.hide_screen("stage2_delay_screen")
    if renpy.get_screen("health_animation"):
        $ renpy.hide_screen("health_animation")
    if renpy.get_screen("stage2_enemy1_fire_animation"):
        $ renpy.hide_screen("stage2_enemy1_fire_animation")

screen stage2_delay_screen_enemy2(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("attack_enemy2_animation"):
        $ renpy.hide_screen("attack_enemy2_animation")
    if renpy.get_screen("slash_enemy2_animation"):
        $ renpy.hide_screen("slash_enemy2_animation")
    if renpy.get_screen("stage2_delay_screen"):
        $ renpy.hide_screen("stage2_delay_screen")
    if renpy.get_screen("health_animation"):
        $ renpy.hide_screen("health_animation")
    if renpy.get_screen("stage2_enemy2_fire_animation"):
        $ renpy.hide_screen("stage2_enemy2_fire_animation")

screen stage2_delay_count(delay, next_action):
    timer delay action next_action
    if renpy.get_screen("attack_enemy1_animation"):
        $ renpy.hide_screen("attack_enemy1_animation")
    if renpy.get_screen("attack_enemy2_animation"):
        $ renpy.hide_screen("attack_enemy2_animation")
    if renpy.get_screen("slash_enemy1_animation"):
        $ renpy.hide_screen("slash_enemy1_animation")
    if renpy.get_screen("slash_enemy2_animation"):
        $ renpy.hide_screen("slash_enemy2_animation")
    if renpy.get_screen("stage2_delay_screen"):
        $ renpy.hide_screen("stage2_delay_screen")
    if renpy.get_screen("stage2_delay_screen_enemy1"):
        $ renpy.hide_screen("stage2_delay_screen_enemy1")
    if renpy.get_screen("stage2_delay_screen_enemy2"):
        $ renpy.hide_screen("stage2_delay_screen_enemy2")
    if renpy.get_screen("health_animation"):
        $ renpy.hide_screen("health_animation")

# Image Battle Background
image stage2_battle_background = "images/rpg/background/battle_forest_background.png"


# Label Start
label second_battle:
    $ quick_menu = False 
    scene stage2_battle_background
    
    python:
        stage2_reset_battle_variables()

    play music "images/rpg/sound/historical_environment/battle_music.mp3" loop
        
    call screen combat_stage2

screen attack_enemy1_animation():
    add stage2_player_attack_enemy1_animation align (0.5, 0.5)

screen slash_enemy1_animation():
    add stage2_player_slash_enemy1_animation align (0.5, 0.5)

screen attack_enemy2_animation():
    add stage2_player_attack_enemy2_animation align (0.5, 0.5)

screen slash_enemy2_animation():
    add stage2_player_slash_enemy2_animation align (0.5, 0.5)

screen stage2_health_animation():
    add stage2_player_health_animation align (0.5, 0.5)

screen stage2_enemy1_fire_animation():
    add stage2_fire_animation_enemy1 align (0.5, 0.5)

screen stage2_enemy2_fire_animation():
    add stage2_fire_animation_enemy2 align (0.5, 0.5)

screen combat_stage2:
    # Battle Status
    image "images/rpg/ui/battle_status.png"

    imagebutton:
        idle stage2_pangeran_animation

    # Image Enemy 1
    if stage2_enemy1_health > 0:  # Menampilkan tombol hanya jika kesehatan lebih dari 0
        imagebutton:
            idle stage2_enemy1_animation
            hover stage2_enemy1_animation_hover
            focus_mask True
            action Function(stage2_select_enemy, "enemy1")

    # Health Bar Enemy 1
    if stage2_enemy1_health > 0:
        bar:
            xpos 1243
            ypos 87
            range stage2_enemy1_max_health
            value stage2_enemy1_health
            left_bar "images/rpg/ui/bar/enemy_bar.png"
            right_bar "images/rpg/ui/bar/bar_back.png"
            xysize(300, 70)

    # Image Enemy 2
    if stage2_enemy2_health > 0:  # Menampilkan tombol hanya jika kesehatan lebih dari 0
        imagebutton:
            idle stage2_enemy2_animation
            hover stage2_enemy2_animation_hover
            focus_mask True
            action Function(stage2_select_enemy, "enemy2")

    # Health Bar Enemy 2
    if stage2_enemy2_health > 0:  # Menampilkan tombol hanya jika kesehatan lebih dari 0
        bar:
            xpos 1472
            ypos 222
            range stage2_enemy2_max_health
            value stage2_enemy2_health
            left_bar "images/rpg/ui/bar/enemy_bar.png"
            right_bar "images/rpg/ui/bar/bar_back.png"
            xysize(300, 70)

    # Button Health
    imagebutton:
        idle stage2_get_health_image()
        hover stage2_get_health_hover()
        focus_mask True
        action stage2_get_health_action()

    # Button Attack (Hanya Berfungsi Jika Target Dipilih)
    imagebutton:
        idle "images/rpg/ui/icon/attack.png"
        hover "images/rpg/ui/icon/attack_hover.png"
        focus_mask True
        action Function(stage2_attack_selected_enemy)

    # Button Skill
    imagebutton:
        idle stage2_get_skill_image()
        hover stage2_get_skill_hover()
        focus_mask True
        action stage2_get_skill_action()

    # Stage 2 Player Health Bar
    bar:
        xpos 593
        ypos 774
        range stage2_player_max_health
        value stage2_player_health
        left_bar "images/rpg/ui/bar/player_bar.png"
        right_bar "images/rpg/ui/bar/bar_back.png"
        xysize(699, 60)
    text "[stage2_player_health]/[stage2_player_max_health]":
        xalign 0.5
        ypos 812
        size 18
    
    # Stage 2 Player Stamina Bar
    bar:
        xpos 593
        ypos 821
        range stage2_player_max_stamina
        value stage2_player_stamina
        left_bar "images/rpg/ui/bar/stamina_bar.png"
        right_bar "images/rpg/ui/bar/bar_back.png"
        xysize(699, 60)
    text "[stage2_player_stamina]/[stage2_player_max_stamina]":
        xalign 0.5
        ypos 861
        size 18

    if stage2_target_enemy == "enemy1":
        image "images/rpg/ui/turn_enemy1_indicator.png"
    
    if stage2_target_enemy == "enemy2":
        image "images/rpg/ui/turn_enemy2_indicator.png"

    # Turn Bar
    text "[stage2_turn_count]":
        xalign 0.5
        yalign 0.08
        color "#ffffff"

    if stage2_enemy1_health <= 0 and stage2_enemy2_health <= 0:
        use stage2_player_win  # Panggil label yang menampilkan screen

    if stage2_player_health <= 0:
        use stage2_enemy_win


screen stage2_player_win:
    # Pop Up Reward
    add "images/rpg/reward/stage2_popup_reward_3stars.png"

    # Ganti textbutton menjadi imagebutton
    imagebutton:
        idle "images/rpg/reward/next_stage.png"
        hover "images/rpg/reward/next_stage_hover.png"
        focus_mask True
        action [Jump("after_second_battle"), Function(renpy.hide_screen, "combat_stage2")]
    
    imagebutton:
        idle "images/rpg/reward/stage_try_again.png"
        hover "images/rpg/reward/stage_try_again_hover.png"
        focus_mask True
        action [
            Function(stage2_reset_battle_variables),  # Reset variabel pertarungan
            Jump("second_battle")  # Kembali ke label second_battle
        ]

screen stage2_enemy_win:
    # Pop Up Reward
    add "images/rpg/reward/popup_lose.png"

    # Imagebutton untuk mencoba ulang
    imagebutton:
        idle "images/rpg/reward/try_again.png"
        hover "images/rpg/reward/try_again_hover.png"
        focus_mask True
        action [
            Function(stage2_reset_battle_variables),  # Reset variabel pertarungan
            Jump("second_battle")  # Kembali ke label first_battle
        ]