# Lab #1 - Teoria de Errores

Animacion educativa sobre teoria de errores en mediciones fisicas.

---

## Contenido

| # | Seccion |
|---|---------|
| 1 | Por que existen errores en una medicion? |
| 2 | Teoria basica - magnitud, numero y unidad |
| 3 | Exactitud y precision |
| 4 | Error absoluto |
| 5 | Error relativo |
| 6 | Error porcentual |
| 7 | Ejemplo: medicion con regla |
| 8 | Ejemplo: medicion de tiempo |
| 9 | Ejemplo complejo: movimiento en liquidos |
| 10 | Conclusiones |

---

## Tecnologias

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje base |
| Manim Community | Motor de animacion matematica |

Documentacion de Manim: https://www.manim.community/

---

## Requisitos

```
Python >= 3.8
manim >= 0.18
```

Manim requiere LaTeX instalado en el sistema para renderizar formulas.
Guia de instalacion: https://docs.manim.community/en/stable/installation.html

---

## Instalacion

```bash
git clone https://github.com/CagoenFidel/Physics-1.git
cd Physics-1/lab#1

python -m venv .venv

.venv\Scripts\activate

pip install manim
```

---

## Uso

```bash
# Previsualizacion rapida
manim -pql main.py TeoriaErrores

# Render final
manim -pqh main.py TeoriaErrores
```

El video renderizado queda en media/videos/main/

---

## Notas

PD: no hice el informe por estar enfocado en esto.

Volver al repositorio: ../README.md
