from manim import *
config.verbosity = "WARNING" 
class Hellys(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Tex(r'Helly\textquotesingle s Theorem', color = GREY, font_size = 16).move_to([0,3.5,0])
        self.add(title)
        title2 = Tex(r'Helly\textquotesingle s Theorem $\rightarrow$ \textbf{Radon\textquotesingle s Lemma}', color = GREY_D, font_size = 16).move_to([0,3.5,0])

        #self.play(title.animate.move_to([0,3.5,0]))
        thm1 = Tex(r'Let $C_1, \ldots, C_n$ be convex sets in $\mathbb{R}^d$, n $\geq$ d+1.', color=BLACK, font_size= 32)
        self.play(thm1.animate.move_to(UP).next_to(title, DOWN))
        self.wait(1)
        self.next_section()

        pent = Polygon([-2,0,0], [0,1,0],[2,0,0],[2,-2,0], [-2, -2,0], color=BLUE_A)
        sq = Polygon([-3,1,0], [-2,-1,0], [0,0,0], [-1,2,0], color=RED_A)
        tr = Polygon([-2,1,0], [1,1,0], [1, -2.5,0], color=GREEN)
        hexa = Polygon([0,1.5,0],[-1,0,0],[0,-2,0],[2,-2,0],[2.5,0,0],[2,1.5,0], color=PURPLE)

        li = [pent, sq, tr, hexa]
        self.show_sets(li)
        self.remove(thm1)
        thm2 = Tex(r'Suppose that the intersection of every d+1 of these sets is nonempty.', color=BLACK, font_size=32).move_to([0,3.2,0])
        self.play(ReplacementTransform(thm1, thm2))
        self.wait(2)
        self.next_section()

        itxs, itx_sets = self.show_intersections(li)
        thm3 = Tex(r'Then the intersection of all the $C_i$ is nonempty.', color=BLACK, font_size=32).move_to([0,3.2,0]) 
        self.play(ReplacementTransform(thm2, thm3))
        self.wait(2)
        self.play(thm3.animate.move_to([0,3, 0]).set_color(RED).scale(.75))
        self.wait(.5)
        for i in itxs:
            self.remove(i)
        self.wait(2)
        set_pos = [[-3,2,0], [-3,-2,0], [3,2,0], [3, -2,0]]
        proof1 = Tex(r'For each $d+1$ set, fix point $a_i$ at it\textquotesingle s intersection.', color=BLACK, font_size=32).move_to([0,3.2,0])
        self.play(ReplacementTransform(thm3, proof1))
        a_is = VGroup()
        targets = [[1.5,1.5,0], [-1.5,1.5,0], [-1.5,-1.5,0], [1.5,-1.5,0]]
        for shape_set, pos in zip(itx_sets, range(len(set_pos))):
            self.play(Create(shape_set.scale(.5).shift(set_pos[pos])))
            a_i = Dot(shape_set.get_center(), color=LOGO_BLACK)  
            a_is.add(a_i)
            self.play(Create(a_i))
            self.wait(.5)
        for shape_set in itx_sets: 
            self.remove(shape_set)
        #self.play(a_is.animate.shift(LEFT))
        move_ai = [ApplyMethod(a_i.move_to,loc) for a_i,loc in zip(a_is,targets)]
        proof2 = Tex(r'Collecting $a_i$, Radon\'s allows partition into $I_1, I_2$', color=BLACK, font_size=32).move_to([0,3.2,0]) # TODO pick an x, show I_n
        self.play(ReplacementTransform(proof1, proof2))
        self.play(*move_ai)

        self.play(ReplacementTransform(title, title2))
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
            self.play(Create(inter))
            set_grp = VGroup()
            for obj1 in subli: 
                set_grp.add(obj1.copy())
                self.remove(obj1)
            d1_sets.append(set_grp)
            self.wait(1)
        return itxs, d1_sets