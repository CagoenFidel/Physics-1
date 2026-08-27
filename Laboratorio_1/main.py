from manim import *
import numpy as np


class TeoriaErrores(Scene):

    def construct(self):
        self.portada()
        self.porque_existen_errores()
        self.teoria_basica()
        self.exactitud_precision()
        self.error_absoluto()
        self.error_relativo()
        self.error_porcentual()
        self.ejemplo_regla()
        self.ejemplo_tiempo()
        self.experimento_liquidos()
        self.conclusion()

    # ========================================================
    # 1. PORTADA
    # ========================================================

    def portada(self):
        titulo      = Text("TEORÍA DE ERRORES", font_size=52)
        fisica      = Text("Física 1", font_size=36)
        grupo       = Text("Grupo Z6", font_size=30)
        autor       = Text("Autor: Marcos", font_size=28)
        subtitulo   = Text("Medir también es aprender a estimar", font_size=25)
        herramienta = Text("Hecho en Python  ·  Manim", font_size=22)

        contenido = VGroup(
            titulo, fisica, grupo, autor, subtitulo, herramienta
        ).arrange(DOWN, buff=0.35)

        self.play(Write(titulo))
        self.play(FadeIn(fisica,      shift=UP))
        self.play(FadeIn(grupo,       shift=UP))
        self.play(FadeIn(autor,       shift=UP))
        self.play(FadeIn(subtitulo,   shift=UP))
        self.play(FadeIn(herramienta, shift=UP))

        self.wait(3)
        self.play(FadeOut(contenido))

    # ========================================================
    # 2. ¿POR QUÉ EXISTEN LOS ERRORES?
    # ========================================================

    def porque_existen_errores(self):
        titulo = Text(
            "¿Por qué existen errores en una medición?",
            font_size=38
        )
        self.play(Write(titulo))
        self.wait(2)
        self.play(titulo.animate.to_edge(UP))

        regla = NumberLine(x_range=[0, 10, 1], length=10)
        self.play(Create(regla))

        punto = Dot(regla.n2p(5))
        self.play(Create(punto))

        medicion = MathTex(r"x = 5.0\text{ cm}")
        medicion.next_to(punto, UP)
        self.play(Write(medicion))

        self.wait(2)

        texto = Text(
            "Pero toda medición tiene una incertidumbre.",
            font_size=28
        )
        texto.to_edge(DOWN)
        self.play(FadeIn(texto))

        self.wait(3)
        self.play(
            FadeOut(titulo), FadeOut(regla), FadeOut(punto),
            FadeOut(medicion), FadeOut(texto)
        )

    # ========================================================
    # 3. TEORÍA BÁSICA
    # ========================================================

    def teoria_basica(self):
        titulo = Text("Teoría básica", font_size=42)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        definicion = Text(
            "Una medición es una comparación entre una magnitud",
            font_size=27
        )
        definicion2 = Text("y una unidad de referencia.", font_size=27)

        grupo = VGroup(definicion, definicion2).arrange(DOWN, buff=0.25)
        self.play(Write(grupo))
        self.wait(3)
        self.play(FadeOut(grupo))

        magnitud = MathTex(r"\text{Magnitud} = \text{número} \times \text{unidad}")
        self.play(Write(magnitud))
        self.wait(3)
        self.play(FadeOut(magnitud), FadeOut(titulo))

    # ========================================================
    # 4. EXACTITUD Y PRECISIÓN
    # ========================================================

    def exactitud_precision(self):
        titulo = Text("Exactitud y precisión", font_size=42)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        centro   = Dot(ORIGIN)
        objetivo = Circle(radius=2)
        objetivo.set_stroke(width=2)
        self.play(Create(objetivo))

        # PRECISIÓN
        puntos_precisos = VGroup()
        for pos in [[0.7, 0.6, 0], [0.85, 0.55, 0], [0.65, 0.8, 0], [0.75, 0.7, 0]]:
            puntos_precisos.add(Dot(np.array(pos)))

        texto = Text("Precisión: resultados muy cercanos entre sí", font_size=24)
        texto.to_edge(DOWN)
        self.play(LaggedStart(*[Create(p) for p in puntos_precisos], lag_ratio=0.2))
        self.play(Write(texto))
        self.wait(3)
        self.play(FadeOut(puntos_precisos), FadeOut(texto))

        # EXACTITUD
        puntos_exactos = VGroup()
        for pos in [[0.05, 0.08, 0], [-0.1, 0.05, 0], [0.08, -0.08, 0], [-0.05, -0.1, 0]]:
            puntos_exactos.add(Dot(np.array(pos)))

        texto2 = Text("Exactitud: resultados cercanos al valor real", font_size=24)
        texto2.to_edge(DOWN)
        self.play(LaggedStart(*[Create(p) for p in puntos_exactos], lag_ratio=0.2))
        self.play(Write(texto2))
        self.wait(3)

        self.play(
            FadeOut(objetivo), FadeOut(centro), FadeOut(puntos_exactos),
            FadeOut(texto2), FadeOut(titulo)
        )

    # ========================================================
    # 5. ERROR ABSOLUTO
    # ========================================================

    def error_absoluto(self):
        titulo = Text("Error absoluto", font_size=42)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        linea = NumberLine(x_range=[0, 10, 1], length=10)
        linea.shift(UP * 0.5)
        self.play(Create(linea))

        real   = Dot(linea.n2p(5))
        medido = Dot(linea.n2p(5.3))

        real_text   = MathTex(r"x_r=5.0")
        medido_text = MathTex(r"x_m=5.3")
        real_text.next_to(real, DOWN)
        medido_text.next_to(medido, UP)

        self.play(Create(real))
        self.play(Write(real_text))
        self.play(Create(medido))
        self.play(Write(medido_text))

        distancia = BraceBetweenPoints(real.get_center(), medido.get_center())
        self.play(GrowFromCenter(distancia))
        self.wait(2)

        formula = MathTex(r"E_a=|x_m-x_r|")
        formula.move_to(DOWN * 2.0)
        self.play(Write(formula))

        resultado = MathTex(r"E_a=|5.3-5.0|=0.3")
        resultado.next_to(formula, DOWN, buff=0.4)
        self.play(Write(resultado))
        self.wait(4)

        self.play(
            FadeOut(linea), FadeOut(real), FadeOut(medido),
            FadeOut(real_text), FadeOut(medido_text), FadeOut(distancia),
            FadeOut(formula), FadeOut(resultado), FadeOut(titulo)
        )

    # ========================================================
    # 6. ERROR RELATIVO
    # ========================================================

    def error_relativo(self):
        titulo = Text("Error relativo", font_size=42)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        explicacion = Text(
            "Comparamos el error con el valor de referencia.",
            font_size=27
        )
        explicacion.move_to(UP * 1.5)
        self.play(Write(explicacion))
        self.wait(2)

        formula = MathTex(r"E_r=\frac{E_a}{|x_r|}")
        formula.move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(2)

        ejemplo = MathTex(r"E_r=\frac{0.3}{5.0}=0.06")
        ejemplo.move_to(DOWN * 1.8)
        self.play(Write(ejemplo))
        self.wait(3)

        self.play(
            FadeOut(titulo), FadeOut(explicacion),
            FadeOut(formula), FadeOut(ejemplo)
        )

    # ========================================================
    # 7. ERROR PORCENTUAL
    # ========================================================

    def error_porcentual(self):
        titulo = Text("Error porcentual", font_size=42)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        formula = MathTex(r"E_\%=E_r\times100")
        formula.move_to(UP * 0.5)
        self.play(Write(formula))
        self.wait(2)

        ejemplo = MathTex(r"E_\%=0.06\times100=6\%")
        ejemplo.next_to(formula, DOWN, buff=0.6)
        self.play(Write(ejemplo))
        self.wait(3)

        self.play(FadeOut(titulo), FadeOut(formula), FadeOut(ejemplo))

    # ========================================================
    # 8. EJEMPLO 1 — MEDICIÓN CON REGLA
    # ========================================================

    def ejemplo_regla(self):
        titulo = Text("Ejemplo 1: medición con una regla", font_size=38)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        regla = NumberLine(x_range=[0, 10, 1], length=11)
        regla.shift(UP * 0.5)
        self.play(Create(regla))

        valor_real   = Dot(regla.n2p(7))
        valor_medido = Dot(regla.n2p(7.2))
        self.play(Create(valor_real))
        self.play(Create(valor_medido))

        etiquetas = VGroup(
            MathTex(r"x_r=7.0\text{ cm}"),
            MathTex(r"x_m=7.2\text{ cm}")
        )
        etiquetas[0].next_to(valor_real,   DOWN)
        etiquetas[1].next_to(valor_medido, UP)
        self.play(Write(etiquetas))

        formula = MathTex(r"E_a=|7.2-7.0|=0.2\text{ cm}")
        formula.move_to(DOWN * 2.2)
        self.play(Write(formula))
        self.wait(4)

        self.play(
            FadeOut(titulo), FadeOut(regla), FadeOut(valor_real),
            FadeOut(valor_medido), FadeOut(etiquetas), FadeOut(formula)
        )

    # ========================================================
    # 9. EJEMPLO 2 — MEDICIÓN DE TIEMPO
    # ========================================================

    def ejemplo_tiempo(self):
        titulo = Text("Ejemplo 2: medición de tiempo", font_size=40)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        reloj = Circle(radius=1.5)
        reloj.shift(UP * 0.3)

        numero = DecimalNumber(0, num_decimal_places=2)
        numero.next_to(reloj, DOWN)

        self.play(Create(reloj))
        self.play(Write(numero))
        self.wait(1)

        tiempos = [2.41, 2.36, 2.44, 2.39]
        for tiempo in tiempos:
            nuevo = DecimalNumber(tiempo, num_decimal_places=2)
            nuevo.next_to(reloj, DOWN)
            self.play(Transform(numero, nuevo), run_time=0.6)

        promedio = sum(tiempos) / len(tiempos)
        promedio_texto = MathTex(rf"\bar{{t}}={promedio:.3f}\text{{ s}}")
        promedio_texto.move_to(DOWN * 2.8)
        self.play(Write(promedio_texto))
        self.wait(4)

        self.play(
            FadeOut(titulo), FadeOut(reloj),
            FadeOut(numero), FadeOut(promedio_texto)
        )

    # ========================================================
    # 10. EXPERIMENTO COMPLEJO — LÍQUIDOS
    # ========================================================

    def experimento_liquidos(self):
        titulo = Text("Ejemplo complejo: movimiento en líquidos", font_size=36)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        tubo_agua   = Rectangle(width=1.4, height=4.5)
        tubo_aceite = Rectangle(width=1.4, height=4.5)
        tubos = VGroup(tubo_agua, tubo_aceite).arrange(RIGHT, buff=1.2)
        tubos.shift(LEFT * 2.5 + DOWN * 0.2)
        self.play(Create(tubos))

        agua   = Text("Agua",   font_size=24)
        aceite = Text("Aceite", font_size=24)
        agua.next_to(tubo_agua,   DOWN, buff=0.2)
        aceite.next_to(tubo_aceite, DOWN, buff=0.2)
        self.play(Write(agua), Write(aceite))

        punto_A = Dot(tubo_agua.get_top()    + DOWN * 0.5)
        punto_B = Dot(tubo_agua.get_bottom() + UP   * 0.5)
        letra_A = Text("A", font_size=22)
        letra_B = Text("B", font_size=22)
        letra_A.next_to(punto_A, LEFT, buff=0.15)
        letra_B.next_to(punto_B, LEFT, buff=0.15)
        self.play(Create(punto_A), Create(punto_B), Write(letra_A), Write(letra_B))

        distancia = MathTex(r"d=0.50\text{ m}", font_size=32)
        distancia.next_to(tubos, LEFT, buff=0.5)
        self.play(Write(distancia))
        self.wait(2)

        texto = Text(
            "Se mide el tiempo que tarda\nel objeto en recorrer A → B",
            font_size=22,
            line_spacing=1.2
        )
        texto.move_to(RIGHT * 3.5 + UP * 1.5)
        self.play(Write(texto))
        self.wait(3)
        self.play(FadeOut(texto), FadeOut(distancia))

        tiempos_agua   = [1.21, 1.18, 1.23, 1.20, 1.19]
        tiempos_aceite = [2.41, 2.35, 2.46, 2.39, 2.43]

        tabla_titulo = Text("Mediciones experimentales", font_size=26)
        tabla_titulo.to_edge(DOWN).shift(UP * 0.1)
        self.play(Write(tabla_titulo))

        datos_agua = VGroup()
        for i, t in enumerate(tiempos_agua):
            datos_agua.add(MathTex(rf"t_{{agua,{i+1}}}={t:.2f}\text{{ s}}", font_size=28))
        datos_agua.arrange(DOWN, buff=0.22)
        datos_agua.next_to(tubo_agua, RIGHT, buff=0.35)
        self.play(LaggedStart(*[Write(x) for x in datos_agua], lag_ratio=0.15))

        datos_aceite = VGroup()
        for i, t in enumerate(tiempos_aceite):
            datos_aceite.add(MathTex(rf"t_{{aceite,{i+1}}}={t:.2f}\text{{ s}}", font_size=28))
        datos_aceite.arrange(DOWN, buff=0.22)
        datos_aceite.next_to(tubo_aceite, RIGHT, buff=0.35)
        self.play(LaggedStart(*[Write(x) for x in datos_aceite], lag_ratio=0.15))

        self.wait(4)

        promedio_agua   = sum(tiempos_agua)   / len(tiempos_agua)
        promedio_aceite = sum(tiempos_aceite) / len(tiempos_aceite)

        self.play(
            FadeOut(datos_agua), FadeOut(datos_aceite), FadeOut(tabla_titulo)
        )

        resultados = VGroup(
            MathTex(rf"\bar{{t}}_{{agua}}={promedio_agua:.3f}\text{{ s}}",   font_size=34),
            MathTex(rf"\bar{{t}}_{{aceite}}={promedio_aceite:.3f}\text{{ s}}", font_size=34)
        ).arrange(DOWN, buff=0.5)
        resultados.move_to(RIGHT * 3.0 + UP * 0.5)
        self.play(Write(resultados))
        self.wait(3)

        velocidad = MathTex(r"v=\frac{d}{t}", font_size=34)
        velocidad.move_to(RIGHT * 3.0 + UP * 1.8)
        self.play(Write(velocidad))

        velocidades = VGroup(
            MathTex(rf"v_{{agua}}=\frac{{0.50}}{{{promedio_agua:.3f}}}",   font_size=30),
            MathTex(rf"v_{{aceite}}=\frac{{0.50}}{{{promedio_aceite:.3f}}}", font_size=30)
        ).arrange(DOWN, buff=0.45)
        velocidades.move_to(RIGHT * 3.0 + DOWN * 1.2)
        self.play(Write(velocidades))
        self.wait(4)

        conclusion = Text("El medio modifica el movimiento del objeto.", font_size=26)
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(4)

        self.play(
            FadeOut(titulo), FadeOut(tubos), FadeOut(agua), FadeOut(aceite),
            FadeOut(punto_A), FadeOut(punto_B), FadeOut(letra_A), FadeOut(letra_B),
            FadeOut(resultados), FadeOut(velocidad), FadeOut(velocidades),
            FadeOut(conclusion)
        )

    # ========================================================
    # 11. CONCLUSIÓN
    # ========================================================

    def conclusion(self):
        titulo = Text("Conclusiones", font_size=44)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))

        puntos = VGroup(
            Text("• Toda medición tiene incertidumbre.",                     font_size=27),
            Text("• El error permite cuantificar la diferencia.",            font_size=27),
            Text("• Repetir mediciones permite analizar la dispersión.",     font_size=27),
            Text("• Los errores pueden ser aleatorios o sistemáticos.",      font_size=27),
            Text("• El análisis de errores permite evaluar un experimento.", font_size=27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        self.play(LaggedStart(*[Write(p) for p in puntos], lag_ratio=0.3))
        self.wait(5)

        autor = Text("Física 1 — Grupo Z6 — Marcos", font_size=25)
        autor.to_edge(DOWN)
        self.play(FadeIn(autor))

        pd = Text(
            "PD: no hice el informe por estar en esta vaina",
            font_size=20
        )
        pd.next_to(autor, UP, buff=0.2)
        self.play(FadeIn(pd))

        self.wait(4)##FUNCIONA JUEPUTA