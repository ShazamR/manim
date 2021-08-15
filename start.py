from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity = 0.4)
        circle.set_stroke(BLUE_A, opacity = 0.8)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()

class Mingdao(Scene):
    def construct(self):
        ellipse_a1 = Ellipse(height = 2.0, width = 4.0)
        ellipse_a2 = Ellipse(height = 2.0, width = 6.0).rotate(0.2)
        circle_a1 = Circle(radius = 0.01)
        circle_a2= Circle(radius = 2.0)
        circle_b1 = Circle(radius = 0.01)
        circle_b2 = Circle(radius = 0.5)

        
        text_a = Text("明道中學合唱團")
        text_b = Text("When You Believe")

        self.play(Create(ellipse_a1), Create(circle_a1))
        self.play(Transform(ellipse_a1, ellipse_a2), Transform(circle_a1, circle_a2))
        self.play(MoveAlongPath(circle_b2, ellipse_a2), rate_func=smooth)
        self.play(Transform(ellipse_a2, text_a, text_b))
        self.wait()

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)