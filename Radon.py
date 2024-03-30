from manim import *
config.verbosity = "WARNING" 
class Radon(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Tex(r'Radon$\textquotesingle$s Theorem', color = GREY, font_size = 24)
        self.play(title.animate.move_to([0,3.5,0]))
        thm1 = Tex(r'Let $A$ be a set of $d+2$ points in $\mathbb{R}^d$.', color = BLACK, font_size = 32)
        self.play(thm1.animate.move_to([0,3,0]))
        self.wait(1)
        
        dimensions = Tex(r'Dimension: $d$', color = BLACK, font_size = 32)
        self.play(dimensions.animate)
        example_dimension = Tex(r'Let$\textquotesingle$s look at 2-D for example', color = BLACK, font_size = 32)
        example_dimension.move_to([0,1,0])
        self.play(example_dimension.animate)
        dimensions_two = Tex(r'Dimension: $2$', color = BLACK, font_size = 32)
        self.play(ReplacementTransform(dimensions, dimensions_two))
        points = Tex(r'Points:', color = BLACK, font_size = 32)
        points.move_to([0,-1,0])
        self.play(points.animate)
        d_plus_two_points = Tex(r'$d + 2$', color = BLUE_E, font_size = 32)
        two_plus_two_points = Tex(r'$2 + 2$', color = BLUE_E, font_size = 32)
        four_points = Tex(r'$4$', color = BLUE_E, font_size = 32)
        d_plus_two_points.move_to([1,-1,0])
        two_plus_two_points.move_to([1,-1,0])
        four_points.move_to([1,-1,0])
        self.play(d_plus_two_points.animate)
        self.play(ReplacementTransform(d_plus_two_points, two_plus_two_points))
        self.play(ReplacementTransform(two_plus_two_points, four_points))
        vg = VGroup()
        vg.add(points)
        vg.add(four_points)
        self.remove(example_dimension)
        self.remove(dimensions_two)
        self.play(vg.animate.move_to([-4,-3,0]))
        self.wait(1)
        
        GRID_SIZE = 4
        grid_background = Square(side_length=GRID_SIZE)
        grid_background.set_fill(BLACK, opacity=1)
        grid_background.set_stroke(color=BLUE_E, width=20)
        grid_background.move_to([-4,0,0])
        number_plane = NumberPlane(
            x_length=GRID_SIZE,
            y_length=GRID_SIZE,
            x_range=(-GRID_SIZE/2, GRID_SIZE/2, 1),
            y_range=(-GRID_SIZE/2, GRID_SIZE/2, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        number_plane.move_to([-4,0,0])
        self.play(grid_background.animate)
        self.play(number_plane.animate)
        
        d1 = Dot(color=RED, radius=0.1).move_to([-5,1,0])
        d2 = Dot(color=RED, radius=0.1).move_to([-3,1,0])
        d3 = Dot(color=RED, radius=0.1).move_to([-5,-1,0])
        d4 = Dot(color=RED, radius=0.1).move_to([-3,-1,0])
        self.play(d1.animate)
        self.play(d2.animate)
        self.play(d3.animate)
        self.play(d4.animate)
        
        subsets = Tex(r'Then there exist two disjoint subsets $A_1, A_2 \subset A$ such that:', color = BLACK, font_size = 28).move_to([3,2,0])
        intersection = Tex(r'$conv(A_1)\cap conv(A_2) \neq \varnothing$', color = BLACK, font_size = 28).move_to([3,1.5,0])
        self.play(subsets.animate)
        self.play(intersection.animate)
        self.wait(2)
        
        e1 = Ellipse(width = 1, height = 3.4, color = GREEN)
        e2 = e1.copy()
        A1 = DashedVMobject(e1, num_dashes=15, dashed_ratio=.25).rotate(PI/4)
        A1lbl = Tex(r'$A_1$', color=BLUE, font_size=28).move_to([-5,1.5,0])
        A2 = DashedVMobject(e2, num_dashes=15, dashed_ratio=.25).rotate(-PI/4)
        A2lbl = Tex(r'$A_2$', color=BLUE, font_size=28).move_to([-3,1.5,0])
        A1.move_to([-4,0,0])
        A2.move_to([-4,0,0])
        self.play(A1.animate, A1lbl.animate)
        self.play(A2.animate, A2lbl.animate)
        
        A1conv = Line(d2, d3)
        self.play(A1conv.animate)
        A2conv = Line(d1, d4)
        self.play(A2conv.animate)
        mid = Dot(color=ORANGE, radius=0.1).move_to([-4,0,0])
        midlbl = Tex(r'$\textbf{x}$', color=ORANGE, font_size=32).move_to([-4,0.3,0])
        self.play(mid.animate, midlbl.animate)
        
        arr = Arrow(start=DOWN*1.8, end=UP*.75, color = ORANGE).move_to([-4,-1.3,0])
        arrlbl = Tex(r'$conv(A_1)\cap conv(A_2) \neq \varnothing$', color=BLACK, font_size=28).move_to([-4,-2.5,0])
        radonpointlbl = Tex(r'$x$ is a \underline{Radon point}', color=BLACK, font_size=28).move_to([-4,-2.5,0])
        self.play(arr.animate, arrlbl.animate)
        self.play(ReplacementTransform(arrlbl, radonpointlbl))
        self.wait(2)