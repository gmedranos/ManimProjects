from turtle import width
from manim import *
from numpy import *
from sqlalchemy import true

class CreateCircle(Scene):
    def construct(self):
        elipse = Ellipse(width=3.0, height=4.0, color=BLUE_B)  # create a circle
        elipse.shift(3*LEFT)

        dot = Dot(point=array([-3., 2., 0.]),  radius = 0.1).set_color(GRAY_B)
        text_dq = Tex(r"$dq$", font_size=40).next_to(dot)
        text_dq.shift(0.3*UP)
        text_dq.shift(0.2*LEFT)
        linha = Line(start=array([- 10., 0., 0.]), end=array([10., 0., 0.]), color=BLUE_E)

        self.play(Create(linha))
        self.play(Create(elipse))
        
        linha_angulo = Line(start=array([-3., 2., 0.]), end=array([3., -0., 0.]), color=GREEN_D)
        self.play(Create(linha_angulo))
        self.play(Create(dot))
        self.play(Create(text_dq), run_time=0.3)
        self.wait(1)
        
        #angulo = Angle(line1=linha, line2=linha_angulo, quadrant=(-1,-1), other_angle=true)
        #self.play(Create(angulo))

        #nome_angulo = Tex(r"$\alpha$", font_size=30)
        #nome_angulo.next_to(angulo, direction=array([-1., 0, 0.]))

        #def passa_circulo(mob):
        #    if(mob.get_slope() != 0):
        #        mob.become(Line(array([3., -0., 0.]), dot.get_center(), color=GREEN_D))

        #linha_angulo.add_updater(passa_circulo)
        # self.play(MoveAlongPath(dot, elipse), rate_func=linear, run_time = 10)

        text_eq_1 = MathTex(r"dV = \frac{kdq}{r}", font_size=60)
        text_eq_1.shift(3*UP)
        text_eq_1.shift(3*RIGHT)
        self.play(Transform(text_dq, text_eq_1))
        self.wait(1)

        text_eq_1 = MathTex(r"dV = \frac{kdq}{\sqrt{z^2 + R^2}}", font_size=60)
        text_eq_1.shift(3*UP)
        text_eq_1.shift(3*RIGHT)

        self.play(Transform(text_dq, text_eq_1))
        self.wait(1)

        text_eq_1 = MathTex(r"\int dV = \int \frac{kdq}{\sqrt{z^2 + R^2}}", font_size=60)
        text_eq_1.shift(3*UP)
        text_eq_1.shift(3*RIGHT)

        self.play(Transform(text_dq, text_eq_1))
        self.wait(1)

        text_eq_1 = MathTex(r"V = \int \frac{kdq}{\sqrt{z^2 + R^2}}", font_size=60)
        text_eq_1.shift(3*UP)
        text_eq_1.shift(3*RIGHT)

        self.play(Transform(text_dq, text_eq_1))
        self.wait(1)

        text_eq_1 = MathTex(r"V = \frac{k}{\sqrt{z^2 + R^2}}\int dq", font_size=60)
        text_eq_1.shift(3*UP)
        text_eq_1.shift(3*RIGHT)

        self.play(Transform(text_dq, text_eq_1))
        self.wait(1)

        text_eq_1 = MathTex(r"V = \frac{k}{\sqrt{z^2 + R^2}}\int_{0}^{2\pi} \lambda(\theta)R d\theta", font_size=60)
        text_eq_1.shift(3*UP)
        text_eq_1.shift(3*RIGHT)
        
        self.play(Transform(text_dq, text_eq_1))
        self.wait(1)

        self.wait(2)
