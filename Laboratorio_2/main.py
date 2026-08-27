from manim import *


class Laboratorio2(Scene):
    def construct(self):
        texto = Text("Laboratorio 2")

        self.play(Write(texto))
        self.wait(2)