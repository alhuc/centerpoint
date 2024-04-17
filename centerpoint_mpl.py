from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import itertools
from scipy.spatial import ConvexHull

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

def main(): 
    plt.figure()
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    pt_set = create_pts(plt)
    hspace_cond = 2/3 * len(pt_set)
    pt_permutations = list(itertools.permutations(pt_set))
    valid_sets = []
    for perm in pt_permutations: 
        # perm denotes convex closure
        # discard perms that fail to meet 2/3 * n 
        if len(perm) < hspace_cond: 
            continue
        # normal equations in 2D list:
        # [ x, y, offset] 
        hull_eq = ConvexHull(perm).equations
        
        # find family of compact convex sets C that satisfy hspace_cond
        # eq (hyperplane) = line in 2D = [ x , y , offset]
        ## line test
        for eq in hull_eq: 
            a, b, c = eq
            eq_count = 0 
            for pt in (set(pt_set) - set(perm)):
                x, y = pt 
                if (a*x + b*y <= c):
                    eq_count += 1
            if eq_count == 0 and (eq not in valid_sets):
                valid_sets.append(eq)
        #print(hull_eq)
        #break
    plt.show()

# FIXME: This is for drawing convex closures
# Example: plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'r', lw=2)

if __name__ == '__main__': 
    main()