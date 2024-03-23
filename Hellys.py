from manim import *
config.verbosity = "WARNING" 
class Hellys(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Tex(r'Helly\'s Theorem', color = GREY, font_size = 24)
        self.play(title.animate.move_to([0,3.5,0]))
        thm1 = Tex(r'Let $C_1, \ldots, C_n$ be convex sets in $\mathbb{R}^d$, n $\geq$ d+1.', color=BLACK, font_size= 32)
        self.play(thm1.animate.move_to([0,3, 0]))
        self.wait(1)
        self.next_section()

        ## FIXME: should define in terms of points
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
        itxs, itx_sets, itx_points = self.show_intersections(li)
        thm3 = Tex(r'Then the intersection of all the $C_i$ is nonempty.', color=BLACK, font_size=32).move_to([0,3,0]) 
        self.play(ReplacementTransform(thm2, thm3))
        self.wait(2)
        self.play(thm3.animate.move_to([0,3, 0]).set_color(RED).scale(.75))
        self.wait(.5)
        for i in itxs:
            self.remove(i)
        self.wait(2)
        set_pos = [[-3,3,0], [3,3,0], [-3,-3,0], [3, -3,0]]
        for shape_set, pos in zip(itx_sets, range(len(set_pos))):
            self.play(Create(shape_set))#*[s.scale(.5) for s in shape_set]))
            shape_set.shift(set_pos[pos])
            self.wait(2)
        self.wait(2)

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
        itxs = []
        itx_pts = []
        d1_sets = []
        for obj, col in zip(li, colors):
            subli = list(set(li) - set(obj))
            vg = VGroup()
            vg.add(*[ele for ele in subli])
            for obj1 in subli:
                self.play(Create(obj1), run_time=.25)
                self.wait(.5)
            inter = Intersection(*[obj for obj in subli], color = col, fill_opacity=0.5 )
            itxs.append(inter)
            itx_pts.append(inter.get_center)
            self.play(Create(inter))
            set_grp = VGroup()
            for obj1 in subli: 
                set_grp.add(obj1.copy())
                self.remove(obj1)
            d1_sets.append(set_grp)
            self.wait(1)
        return itxs, d1_sets, itx_pts