import arcade
import os
import math

RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

UPDATES_PER_FRAME = 10
NUM_TEXTURAS_ANDAR = 2


def load_texture_4dir(filename_lados, filename_up, filename_down):
    """
    Carga texturas en las 4 direcciones, siendo la seguna un versión espejo del
    primer argumento.
    """
    return [
        arcade.load_texture(filename_lados),
        arcade.load_texture(filename_lados, mirrored=True),
        arcade.load_texture(filename_up),
        arcade.load_texture(filename_down)
    ]


class Masked(arcade.Sprite):
    def __init__(self):
        """Constructor del sprite del jugador"""
        super().__init__()
        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_4dir("sprites_master/MASKED1.png", "sprites_master/MASKED10.png",
                                                "sprites_master/MASKED7.png")

        self.textura_andar = []
        for i in range(11, 12):
            texture = load_texture_4dir(f"sprites_master/MASKED{i - 6}.png", f"sprites_master/MASKED{i}.png",
                                        f"sprites_master/MASKED{i - 3}.png")
            self.textura_andar.append(texture)

        self.texture = self.textura_quieto[0]

        self.set_hit_box(self.texture.hit_box_points)

    def actualizar_animacion(self, delta_time: float = 1 / 60):

        # Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.textura_quieto[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]


class Skeleton(arcade.Sprite):
    def __init__(self):
        """Constructor del sprite del jugador"""
        super().__init__()

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_4dir("sprites_master/ESQUELETO1.png", "sprites_master/ESQUELETO10.png",
                                                "sprites_master/ESQUELETO7.png")

        self.textura_andar = []
        for i in range(11, 12):
            texture = load_texture_4dir(f"sprites_master/ESQUELETO{i - 6}.png", f"sprites_master/ESQUELETO{i}.png",
                                        f"sprites_master/ESQUELETO{i - 3}.png")
            self.textura_andar.append(texture)

        self.texture = self.textura_quieto[0]

        self.set_hit_box(self.texture.hit_box_points)

    def disparar(self, skeleton, velocidad_disparo):
        laser = arcade.Sprite("sprites_master/LASER.png")

    def actualizar_animacion(self, delta_time: float = 1 / 60):

        # Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.textura_quieto[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]


class Gasmasked(arcade.Sprite):
    def __init__(self):
        """Constructor del sprite del jugador"""
        super().__init__()

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_4dir("sprites_master/GASMASK1.png", "sprites_master/GASMASK10.png",
                                                "sprites_master/GASMASK7.png")

        self.textura_andar = []
        for i in range(11, 12):
            texture = load_texture_4dir(f"sprites_master/GASMASK{i - 6}.png", f"sprites_master/GASMASK{i}.png",
                                        f"sprites_master/GASMASK{i - 3}.png")
            self.textura_andar.append(texture)

        self.texture = self.textura_quieto[0]

        self.set_hit_box(self.texture.hit_box_points)

        self.sonido_disparar = arcade.load_sound("Sonidos/Ataque Gas.wav")

    def disparar(self, gasmasked, velocidad_disparo):

        proyectil_gaseoso = arcade.Sprite("sprites_master/GASATTACK.png")
        self.sonido_disparar.play()


    def actualizar_animacion(self, delta_time: float = 1 / 60):

        # Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]
