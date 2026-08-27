"""
parallelogram.py — Método del Paralelogramo de Vectores
Estilo 3Blue1Brown  ·  Manim Community Edition

══════════════════════════════════════════════════════
  RENDERIZADO
══════════════════════════════════════════════════════
  Preview rápido (480p):
    manim -pql parallelogram.py ParallelogramaVectorial

  Calidad media (720p):
    manim -pqm parallelogram.py ParallelogramaVectorial

  Alta calidad (1080p):
    manim -pqh parallelogram.py ParallelogramaVectorial

  4K:
    manim -pqk parallelogram.py ParallelogramaVectorial

  Solo un fotograma (preview):
    manim -s parallelogram.py ParallelogramaVectorial

══════════════════════════════════════════════════════
  ESTRUCTURA DE ESCENAS
══════════════════════════════════════════════════════
  ParallelogramaVectorial  ← animación completa (~2 min)
  SoloParalelogramo        ← solo la construcción (sin texto)
  SoloDiagonal             ← solo la diagonal suma
"""

from manim import *
import numpy as np


# ═══════════════════════════════════════════════════════
#  CONFIGURACIÓN  — cambia estos valores fácilmente
# ═══════════════════════════════════════════════════════

WAIT = 1.0           # multiplicador global de pausas (0.5 = todo más rápido)

BG_COLOR  = "#0D1117"   # fondo oscuro
COL_A     = "#FF6B6B"   # coral    → vector a
COL_B     = "#4ECDC4"   # teal     → vector b
COL_SUM   = "#FFE66D"   # dorado   → a + b
COL_DIFF  = "#C77DFF"   # lila     → a − b
COL_MUT   = "#8B949E"   # gris     → texto secundario, θ
COL_TXT   = "#C9D1D9"   # blanco   → texto principal
COL_GRID  = "#141920"   # rejilla menor
COL_AXIS  = "#1F2A38"   # ejes

# Coordenadas de los vectores (unidades Manim)
VEC_A = np.array([2.5,  1.0, 0])
VEC_B = np.array([0.8,  2.3, 0])


# ═══════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════

def solid_arrow(start, end, color, sw=5.0, tip_l=0.22):
    """Flecha sólida principal."""
    return Arrow(
        np.array(start), np.array(end),
        color=color, buff=0,
        stroke_width=sw,
        max_tip_length_to_length_ratio=0.12,
        tip_length=tip_l,
    )


def ghost_arrow(start, end, color, sw=2.8, ndashes=16):
    """Flecha punteada (copia fantasma del paralelogramo).

    Nota: DashedVMobject puede puntear también la punta.
    Si prefieres punta sólida, sustituye por DashedLine +
    un ArrowTip posicionado manualmente.
    """
    arr = Arrow(
        np.array(start), np.array(end),
        color=color, buff=0,
        stroke_width=sw,
        max_tip_length_to_length_ratio=0.09,
        tip_length=0.17,
    )
    return DashedVMobject(arr, num_dashes=ndashes, equal_lengths=True).set_color(color)


def label_vec(tex, color, font_size=42):
    return MathTex(tex, color=color, font_size=font_size)


def narration(text, color=COL_MUT, fs=26):
    mob = Text(text, font_size=fs, color=color)
    mob.to_edge(DOWN, buff=0.45)
    return mob


def make_plane():
    return NumberPlane(
        x_range=[-6, 6, 1],
        y_range=[-4, 4, 1],
        background_line_style={"stroke_color": COL_GRID, "stroke_width": 0.7},
        axis_config={
            "stroke_color": COL_AXIS,
            "stroke_width": 1.5,
            "include_numbers": False,
            "include_ticks": False,
        },
        faded_line_ratio=0,
    )


# ═══════════════════════════════════════════════════════
#  ESCENA COMPLETA
# ═══════════════════════════════════════════════════════

class ParallelogramaVectorial(Scene):
    """Animación didáctica completa del método del paralelogramo."""

    def construct(self):
        self.camera.background_color = BG_COLOR

        A = VEC_A
        B = VEC_B
        S = A + B       # suma  = diagonal principal
        # D = A - B     # diferencia = diagonal secundaria (B→A)

        # ── Secciones ──────────────────────────────────────────────
        self.sec_plano()
        self.sec_apertura()
        self.sec_vectores(A, B)
        self.sec_angulo(A, B)
        self.sec_copia_b(A, S)
        self.sec_copia_a(B, S)
        self.sec_relleno(A, B, S)
        self.sec_diagonal_suma(S)
        self.sec_componentes(A)
        self.sec_ley_coseno()
        self.sec_diagonal_diff(A, B)
        self.sec_cierre()

        # ── Fade final ─────────────────────────────────────────────
        self.play(FadeOut(Group(*self.mobjects.copy())), run_time=1.5)
        self.wait(0.5)

    # ───────────────────────────────────────────────────────────────
    #  Sección 0 — Plano coordenado
    # ───────────────────────────────────────────────────────────────
    def sec_plano(self):
        plane = make_plane()
        self.play(Create(plane), run_time=1.3)
        dot = Dot(ORIGIN, radius=0.07, color=COL_MUT)
        self.play(FadeIn(dot, scale=0.5))

    # ───────────────────────────────────────────────────────────────
    #  Sección 1 — Título de apertura
    # ───────────────────────────────────────────────────────────────
    def sec_apertura(self):
        title = Text("Método del Paralelogramo",
                     weight=BOLD, font_size=44, color=COL_TXT)
        sub = Text("suma de vectores · geometría pura",
                   font_size=22, color=COL_MUT)
        title.to_edge(UP, buff=0.3)
        sub.next_to(title, DOWN, buff=0.14)

        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.15))
        self.wait(1.8 * WAIT)
        self.play(FadeOut(title, sub), run_time=0.7)

    # ───────────────────────────────────────────────────────────────
    #  Sección 2 — Introducción de vectores a y b
    # ───────────────────────────────────────────────────────────────
    def sec_vectores(self, A, B):
        self.va = solid_arrow(ORIGIN, A, COL_A)
        self.vb = solid_arrow(ORIGIN, B, COL_B)

        self.la = label_vec(r"\vec{a}", COL_A)
        self.la.next_to(A, RIGHT + UP * 0.2, buff=0.18)

        self.lb = label_vec(r"\vec{b}", COL_B)
        self.lb.next_to(B, LEFT + UP * 0.1, buff=0.18)

        narr = narration("Dos vectores desde el mismo origen")

        self.play(GrowArrow(self.va), run_time=1.0)
        self.play(Write(self.la))
        self.play(GrowArrow(self.vb), run_time=1.0)
        self.play(Write(self.lb))
        self.play(Write(narr))
        self.wait(1.5 * WAIT)
        self.play(FadeOut(narr))

    # ───────────────────────────────────────────────────────────────
    #  Sección 3 — Ángulo θ entre los vectores
    # ───────────────────────────────────────────────────────────────
    def sec_angulo(self, A, B):
        a_ang = np.arctan2(A[1], A[0])
        b_ang = np.arctan2(B[1], B[0])
        start  = min(a_ang, b_ang)
        sweep  = abs(b_ang - a_ang)
        mid    = start + sweep / 2

        arc = Arc(radius=0.70, start_angle=start, angle=sweep,
                  color=COL_MUT, stroke_width=1.8)
        lbl_t = MathTex(r"\theta", color=COL_MUT, font_size=30)
        lbl_t.move_to(1.12 * np.array([np.cos(mid), np.sin(mid), 0]))

        self.play(Create(arc), Write(lbl_t))
        self.wait(0.9 * WAIT)

    # ───────────────────────────────────────────────────────────────
    #  Sección 4 — Copia de b desde la punta de a
    # ───────────────────────────────────────────────────────────────
    def sec_copia_b(self, A, S):
        narr = narration("Copiamos b desde la punta de a", color=COL_B)
        self.play(Write(narr))

        gb  = ghost_arrow(A, S, COL_B)
        gb.set_opacity(0.65)
        lbl = label_vec(r"\vec{b}", COL_B, font_size=30).set_opacity(0.65)
        lbl.next_to(gb.get_center(), RIGHT, buff=0.2)

        self.play(Create(gb), run_time=1.0)
        self.play(FadeIn(lbl, shift=RIGHT * 0.1))
        self.wait(0.8 * WAIT)

        note = narration(
            "lados opuestos iguales = definición de paralelogramo",
            fs=21
        )
        self.play(FadeOut(narr), Write(note))
        self.wait(1.2 * WAIT)
        self.play(FadeOut(note))

    # ───────────────────────────────────────────────────────────────
    #  Sección 5 — Copia de a desde la punta de b
    # ───────────────────────────────────────────────────────────────
    def sec_copia_a(self, B, S):
        narr = narration("Copiamos a desde la punta de b", color=COL_A)
        self.play(Write(narr))

        ga  = ghost_arrow(B, S, COL_A)
        ga.set_opacity(0.65)
        lbl = label_vec(r"\vec{a}", COL_A, font_size=30).set_opacity(0.65)
        lbl.next_to(ga.get_center(), UP + LEFT * 0.1, buff=0.2)

        self.play(Create(ga), run_time=1.0)
        self.play(FadeIn(lbl, shift=UP * 0.1))
        self.wait(0.8 * WAIT)

        note = narration("¡El paralelogramo está completo!")
        self.play(Transform(narr, note))
        self.wait(1.5 * WAIT)
        self.play(FadeOut(narr))

    # ───────────────────────────────────────────────────────────────
    #  Sección 6 — Relleno del paralelogramo
    # ───────────────────────────────────────────────────────────────
    def sec_relleno(self, A, B, S):
        fill = Polygon(
            ORIGIN, A, S, B,
            fill_color=COL_SUM,
            fill_opacity=0.0,
            stroke_width=0,
        )
        self.add(fill)
        self.play(fill.animate.set_fill(opacity=0.11), run_time=0.9)
        self.wait(0.6 * WAIT)

    # ───────────────────────────────────────────────────────────────
    #  Sección 7 — La diagonal principal es a + b
    # ───────────────────────────────────────────────────────────────
    def sec_diagonal_suma(self, S):
        narr = VGroup(
            Text("La diagonal es", font_size=26, color=COL_MUT),
            MathTex(r"\vec{a}+\vec{b}", color=COL_SUM, font_size=34),
        ).arrange(RIGHT, buff=0.15).to_edge(DOWN, buff=0.45)
        self.play(Write(narr))

        v_sum = solid_arrow(ORIGIN, S, COL_SUM, sw=5.5)
        lbl   = MathTex(r"\vec{a}+\vec{b}", color=COL_SUM, font_size=38)
        lbl.next_to(S * 0.46, LEFT + DOWN * 0.05, buff=0.15)

        self.play(GrowArrow(v_sum), run_time=1.3)
        # Flash en la punta — "¡esto es lo que buscamos!"
        self.play(
            Flash(S, color=COL_SUM, flash_radius=0.55,
                  num_lines=12, line_length=0.28)
        )
        self.play(Write(lbl))
        self.wait(1.8 * WAIT)
        self.play(FadeOut(narr))

    # ───────────────────────────────────────────────────────────────
    #  Sección 8 — Descomposición en componentes
    # ───────────────────────────────────────────────────────────────
    def sec_componentes(self, A):
        narr = narration("Las componentes x e y se suman por separado")
        self.play(Write(narr))

        ax = np.array([A[0], 0, 0])  # proyección sobre eje x

        cx = DashedLine(ORIGIN, ax, color=COL_A,
                        stroke_width=2.0, dash_length=0.12)
        cy = DashedLine(ax,     A,  color=COL_A,
                        stroke_width=2.0, dash_length=0.12)
        lx = MathTex(r"a_x", color=COL_A, font_size=26).next_to(cx, DOWN, buff=0.14)
        ly = MathTex(r"a_y", color=COL_A, font_size=26).next_to(cy, RIGHT, buff=0.12)

        self.play(Create(cx), Create(cy), run_time=0.9)
        self.play(Write(lx), Write(ly))
        self.wait(0.8 * WAIT)

        formula = VGroup(
            MathTex(r"\vec{a}+\vec{b}", color=COL_SUM, font_size=32),
            MathTex(r"= \bigl(a_x + b_x,\quad a_y + b_y\bigr)",
                    font_size=32, color=COL_TXT),
        ).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.38)

        self.play(Write(formula), run_time=1.5)
        self.wait(2.0 * WAIT)
        self.play(FadeOut(narr, formula, cx, cy, lx, ly))

    # ───────────────────────────────────────────────────────────────
    #  Sección 9 — Ley del coseno (magnitudes)
    # ───────────────────────────────────────────────────────────────
    def sec_ley_coseno(self):
        narr = narration("La magnitud sigue la ley del coseno:")
        self.play(Write(narr))

        law = MathTex(
            r"|\vec{a}+\vec{b}|^2 "
            r"= |\vec{a}|^2 + |\vec{b}|^2 "
            r"+ 2\,|\vec{a}|\,|\vec{b}|\,\cos\theta",
            font_size=32, color=COL_TXT,
        ).to_edge(UP, buff=0.38)
        self.play(Write(law), run_time=2.0)

        # Casos límite
        cases = MathTex(
            r"\theta=0^\circ\;\Rightarrow\;\text{máximo}",
            r"\qquad",
            r"\theta=90^\circ\;\Rightarrow\;\text{Pitágoras}",
            r"\qquad",
            r"\theta=180^\circ\;\Rightarrow\;\text{mínimo}",
            font_size=22, color=COL_MUT,
        ).next_to(law, DOWN, buff=0.28)

        self.play(Write(cases), run_time=1.5)
        self.wait(2.5 * WAIT)
        self.play(FadeOut(narr, law, cases))

    # ───────────────────────────────────────────────────────────────
    #  Sección 10 — La otra diagonal es a − b
    # ───────────────────────────────────────────────────────────────
    def sec_diagonal_diff(self, A, B):
        narr = VGroup(
            Text("La otra diagonal:", font_size=26, color=COL_MUT),
            MathTex(r"\vec{a}-\vec{b}", color=COL_DIFF, font_size=34),
        ).arrange(RIGHT, buff=0.15).to_edge(DOWN, buff=0.45)
        self.play(Write(narr))

        # La diferencia va de la punta de b a la punta de a
        v_diff = solid_arrow(B, A, COL_DIFF, sw=4.0)
        mid_d  = (A + B) / 2
        lbl    = MathTex(r"\vec{a}-\vec{b}", color=COL_DIFF, font_size=34)
        lbl.next_to(mid_d, RIGHT, buff=0.22)

        self.play(GrowArrow(v_diff), run_time=1.0)
        self.play(
            Flash(A, color=COL_DIFF, flash_radius=0.45,
                  num_lines=10, line_length=0.24)
        )
        self.play(Write(lbl))
        self.wait(1.8 * WAIT)
        self.play(FadeOut(narr))

    # ───────────────────────────────────────────────────────────────
    #  Sección 11 — Cuadro de cierre
    # ───────────────────────────────────────────────────────────────
    def sec_cierre(self):
        box = RoundedRectangle(
            width=9.0, height=2.1,
            corner_radius=0.25,
            fill_color="#0E1520",
            fill_opacity=0.96,
            stroke_color=COL_SUM,
            stroke_width=1.5,
        ).to_edge(DOWN, buff=0.2)

        linea1 = Text("Un solo paralelogramo contiene:", font_size=22, color=COL_MUT)
        linea2 = VGroup(
            MathTex(r"\vec{a}+\vec{b}", color=COL_SUM,  font_size=32),
            Text("· diagonal principal ·",  font_size=18, color=COL_MUT),
            MathTex(r"\vec{a}-\vec{b}", color=COL_DIFF, font_size=32),
            Text("· diagonal secundaria",   font_size=18, color=COL_MUT),
        ).arrange(RIGHT, buff=0.22)
        contenido = VGroup(linea1, linea2).arrange(DOWN, buff=0.24)
        contenido.move_to(box)

        self.play(FadeIn(box), Write(contenido), run_time=1.5)
        self.wait(3.0 * WAIT)
        self.play(FadeOut(box, contenido))


# ═══════════════════════════════════════════════════════
#  ESCENA MINIMALISTA — solo la construcción geométrica
# ═══════════════════════════════════════════════════════

class SoloParalelogramo(Scene):
    """
    Versión limpia sin narración: útil para thumbnails o shorts.
      manim -pqh parallelogram.py SoloParalelogramo
    """
    def construct(self):
        self.camera.background_color = BG_COLOR

        A = VEC_A
        B = VEC_B
        S = A + B

        plane = make_plane()
        self.play(Create(plane), run_time=0.8)

        # Vectores
        va = solid_arrow(ORIGIN, A, COL_A)
        vb = solid_arrow(ORIGIN, B, COL_B)
        la = MathTex(r"\vec{a}", color=COL_A, font_size=44).next_to(A, RIGHT + UP*0.2, buff=0.18)
        lb = MathTex(r"\vec{b}", color=COL_B, font_size=44).next_to(B, LEFT + UP*0.1, buff=0.18)

        self.play(GrowArrow(va), GrowArrow(vb), run_time=1.2)
        self.play(Write(la), Write(lb))
        self.wait(0.5)

        # Copias fantasma
        gb = ghost_arrow(A, S, COL_B); gb.set_opacity(0.6)
        ga = ghost_arrow(B, S, COL_A); ga.set_opacity(0.6)

        self.play(Create(gb), Create(ga), run_time=1.0)

        # Relleno
        fill = Polygon(ORIGIN, A, S, B,
                       fill_color=COL_SUM, fill_opacity=0, stroke_width=0)
        self.add(fill)
        self.play(fill.animate.set_fill(opacity=0.11), run_time=0.6)

        # Suma
        vs = solid_arrow(ORIGIN, S, COL_SUM, sw=5.5)
        ls = MathTex(r"\vec{a}+\vec{b}", color=COL_SUM, font_size=40)
        ls.next_to(S * 0.45, LEFT + DOWN*0.05, buff=0.15)
        self.play(GrowArrow(vs), run_time=1.0)
        self.play(Flash(S, color=COL_SUM, flash_radius=0.5, num_lines=12, line_length=0.3))
        self.play(Write(ls))

        # Diferencia
        vd = solid_arrow(B, A, COL_DIFF, sw=3.5)
        ld = MathTex(r"\vec{a}-\vec{b}", color=COL_DIFF, font_size=34)
        ld.next_to((A+B)/2, RIGHT, buff=0.22)
        self.play(GrowArrow(vd), run_time=0.9)
        self.play(Write(ld))

        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects.copy())), run_time=1.2)


# ═══════════════════════════════════════════════════════
#  ESCENA EDUCATIVA — componentes en detalle
# ═══════════════════════════════════════════════════════

class ComponentesDetalle(Scene):
    """
    Zoom sobre cómo las componentes se suman algebraicamente.
      manim -pqh parallelogram.py ComponentesDetalle
    """
    def construct(self):
        self.camera.background_color = BG_COLOR

        A = VEC_A
        B = VEC_B
        S = A + B

        plane = make_plane()
        self.play(Create(plane), run_time=0.9)

        va = solid_arrow(ORIGIN, A, COL_A)
        vb = solid_arrow(ORIGIN, B, COL_B)
        vs = solid_arrow(ORIGIN, S, COL_SUM, sw=5.5)

        self.play(GrowArrow(va), GrowArrow(vb), run_time=1.0)
        self.play(GrowArrow(vs), run_time=0.8)

        # ── Componentes de a ──────────────────────────────────────
        ax_proj = np.array([A[0], 0, 0])
        cx = DashedLine(ORIGIN, ax_proj, color=COL_A, stroke_width=2)
        cy = DashedLine(ax_proj, A,      color=COL_A, stroke_width=2)
        lx_a = MathTex(r"a_x", color=COL_A, font_size=26).next_to(cx, DOWN, buff=0.13)
        ly_a = MathTex(r"a_y", color=COL_A, font_size=26).next_to(cy, RIGHT, buff=0.12)

        self.play(Create(cx), Create(cy))
        self.play(Write(lx_a), Write(ly_a))
        self.wait(0.8)

        # ── Componentes de b ──────────────────────────────────────
        bx_proj = np.array([B[0], 0, 0])
        dx = DashedLine(ORIGIN, bx_proj, color=COL_B, stroke_width=2)
        dy = DashedLine(bx_proj, B,      color=COL_B, stroke_width=2)
        lx_b = MathTex(r"b_x", color=COL_B, font_size=26).next_to(dx, DOWN, buff=0.38)
        ly_b = MathTex(r"b_y", color=COL_B, font_size=26).next_to(dy, LEFT, buff=0.12)

        self.play(Create(dx), Create(dy))
        self.play(Write(lx_b), Write(ly_b))
        self.wait(0.8)

        # ── Fórmulas ──────────────────────────────────────────────
        eqs = VGroup(
            MathTex(r"(a_x + b_x,\; a_y + b_y)", font_size=30, color=COL_TXT),
            MathTex(
                r"= \left("
                + str(round(A[0], 1)) + r"+"
                + str(round(B[0], 1)) + r",\;"
                + str(round(A[1], 1)) + r"+"
                + str(round(B[1], 1))
                + r"\right)",
                font_size=28, color=COL_MUT,
            ),
            MathTex(
                r"= \left("
                + str(round(S[0], 1)) + r",\;"
                + str(round(S[1], 1))
                + r"\right)",
                font_size=30, color=COL_SUM,
            ),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        eqs.to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4)

        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
            self.wait(0.5)

        self.wait(2.0)
        self.play(FadeOut(Group(*self.mobjects.copy())), run_time=1.2)