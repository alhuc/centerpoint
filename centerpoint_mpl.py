from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
from scipy.spatial import ConvexHull
import math

def tellme(s):
    print(s)
    plt.title(s, fontsize=12)
    plt.draw()

def create_pts(plt):
    pt_set = []
    tellme('Select n of points, right click to remove recent, center click to finish ')
    pt_set = np.asarray(plt.ginput(-1, timeout=-1, mouse_stop = MouseButton.MIDDLE))
    for i in pt_set:
        plt.scatter(x=i[0], y=i[1])
    return pt_set   

def gen_combinations(pt_set, hspace_cond):
    filtered_combs = []
    """ignore any |combinations| < hspace_cond"""
    for i in range(math.ceil(hspace_cond), len(pt_set)):
        combo_r = combinations(pt_set, i)
        filtered_combs.extend([list(comb) for comb in combo_r])
    return filtered_combs

def main(): 
    plt.figure()
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    pt_set = create_pts(plt)
    hspace_cond = 2/3 * len(pt_set)
    pt_combinations = gen_combinations(pt_set, hspace_cond)
    valid_sets = []
    for comb in pt_combinations: 
        """normal equations in 2D list:[ x, y, offset] """
        hull_eq = ConvexHull(comb).equations
        
        """find family of compact convex sets C that satisfy hspace_cond
           eq (hyperplane) = line in 2D = [ x , y , offset]"""
        for eq in hull_eq: 
            a, b, c = eq
            eq_count = 0
            """subset pt_set: compare comb elements against pt_set, axis=1 groups by row ((x, y) pair)
                          ~ takes subset of entries that are false"""
            pts_not_in_comb = pt_set[np.isin(pt_set, comb, invert=True).all(axis=1)] 
            for pt in pts_not_in_comb:
                x, y = pt 
                ## line test
                if (a*x + b*y <= c):
                    eq_count += 1
            # FIXME: condition evaluation never adds an eq to valid_sets
            if eq_count == 0 and (len(valid_sets) != 0 and np.isin(valid_sets, eq, invert = True).all(axis = 1)):
                ## never entered
                print("inside append")
                valid_sets.append(eq)
        print(valid_sets)
        plt.show()
        return valid_sets

#This is for drawing convex closures
#Example: plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'r', lw=2)

if __name__ == '__main__': 
    valid_sets = main()
    print(valid_sets)
