from manim import *
import numpy as np

class Scena1(ThreeDScene):
    def construct(self):

        eixos = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=8,
            z_length=8,
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta= -60 * DEGREES)

        circulo = Circle()
        self.play(Create(eixos))
        self.wait()
        self.play(Create(circulo))

        linha_1 = Line(start=np.array([1, 0., 0.]), end=np.array([0., 0., 3.]), color=BLUE_E)
        dot = Dot(np.array([1, 0, 0]))

        def passa_circulo(mob):
            mob.become(Line(np.array([0., 0., 3.]), dot.get_center(), color=BLUE_E))

        self.play(Create(linha_1))
        self.play(Create(dot))
        self.wait(2)

        linha_1.add_updater(passa_circulo)
        self.play(MoveAlongPath(dot, circulo), rate_func=linear, run_time = 2.5)
