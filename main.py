# 1. Função de Salto
def on_a_pressed():
    # Só salta se estiver no fundo do ecrã (simulando o chão)
    if mySprite.y >= 110:
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# 2. Lógica de Comer
def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.set_position(randint(10, 150), randint(80, 110))
    music.play(music.melody_playable(music.ba_ding), music.PlaybackMode.UNTIL_DONE)

sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

# --- CONFIGURAÇÃO ---

# Criar o Herói (Alien)
mySprite = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . 7 7 7 7 . . . . . .
    . . . . . 7 7 7 7 7 7 . . . . .
    . . . . 7 7 1 7 7 1 7 7 . . . .
    . . . . 7 7 7 7 7 7 7 7 . . . .
    . . . . 7 7 f f f f 7 7 . . . .
    . . . . 7 7 7 7 7 7 7 7 . . . .
    """), SpriteKind.player)

# Mover apenas esquerda/direita. O salto é no botão A (Espaço)
controller.move_sprite(mySprite, 100, 0)

# Impedir o boneco de cair fora do ecrã
mySprite.set_stay_in_screen(True)

# Aplicar Gravidade
mySprite.ay = 500

# Criar a Comida
comida = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . 2 2 2 2 2 2 . . . . .
    . . . . 2 2 2 2 2 2 2 2 . . . .
    . . . . f f f f f f f f . . . .
    . . . . 2 2 2 2 2 2 2 2 . . . .
    """), SpriteKind.food)