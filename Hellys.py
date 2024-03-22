from manim import * 
class Hellys(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Tex(r'Helly\'s Theorem', color = GREY, font_size = 24)
        self.play(title.animate.move_to([0,3.5,0]))
        thm1 = Tex(r'Let $C_1, \ldots, C_n$ be convex sets in $\mathbb{R}^d$, n $\geq$ d+1.', color=BLACK, font_size= 32)
        self.play(thm1.animate.move_to([0,3, 0]))
        self.wait(1)
        self.next_section()
        
        sq = Square(color=BLACK)
        pent = RegularPolygon(n = 5, color = BLUE).scale(2)
        poly = RegularPolygon(n = 6, color = ORANGE)
        tr = Triangle(color = GREEN).scale(1.5)
        li = [sq, pent, poly, tr]
        self.show_sets(li)
        self.remove(thm1)
        thm2 = Tex(r'Suppose that the intersection of every d+1 of these sets is nonempty.', color=BLACK, font_size=32).move_to([0,3,0])
        self.play(ReplacementTransform(thm1, thm2))
        self.wait(2)
        self.next_section()

        
        sq.move_to([-1.5,0,0])
        pent.move_to([-.5,-.25,0])
        poly.move_to([0,0,-.5])
        tr.move_to([0,.5,.25])
        intx_li, intx_points = self.show_intersections(li)
        thm3 = Tex(r'Then the intersection of all the $C_i$ is nonempty.', color=BLACK, font_size=32).move_to([0,3,0]) 
        self.play(ReplacementTransform(thm2, thm3))
        self.wait(2)
        self.play(thm3.animate.move_to([0,3, 0]).set_color(RED).scale(.75))
        self.wait(2)
        self.next_section()
        
        points_text = TeX(r'Following supposition, for each $d+1$, not empty set, choose $a_i$ from their intersection')
        self.play(points_text)

        ## TODO: intx_li (line 30) should be a list of VGroups, for each VGroup
        ##          place in 2 x 2 grid,
        ##          display the 4 sets, use intersections

    def show_sets(self, li):
        for shape, i in zip(li, range(1,5)):
            self.play(Create(shape), run_time=.25)
            c_i = Tex(f"$C_{i}$", font_size=28, color=GREY).next_to(shape)
            self.play(Create(c_i), run_time=0)
            self.wait(1)
            self.remove(shape)
            self.remove(c_i)

    def show_intersections(self, li):
        colors = [BLUE, RED, GREEN, ORANGE]
        intersection_points = []
        d1_intersecting_sets = [] ## list of VGroups
        for obj, col in zip(li, colors):
            subli = list(set(li) - set(obj))
            vg = VGroup()
            vg.add(*[ele for ele in subli])
            for obj1 in subli:
                self.play(Create(obj1), run_time=.25)
                self.wait(.5)
            inter = Intersection(*[obj for obj in subli], color = col, fill_opacity=0.5 )
            intersection_points.append(inter.get_center)
            self.play(Create(inter))
            for obj1 in subli: 
                self.remove(obj1)
            self.wait(1)
        return d1_intersecting_sets, intersection_points