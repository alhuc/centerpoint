import time
from matplotlib.backend_bases import MouseButton
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
from scipy.spatial import ConvexHull
import math
def tellme(s):
    print(s)
    plt.suptitle(s, wrap=True)
    plt.draw()

def create_pts(plt):
    """
    Description
    
    Parameters 
    ----------
    plt:
        Description
    """
    pt_set = []
    tellme('Select $n$ points. Right click to remove last added. Press anything else to finish selection. Esc to start over')
    pt_set = np.asarray(plt.ginput(-1, timeout=-1, mouse_stop = MouseButton.MIDDLE))
    for i in pt_set:
        plt.scatter(x=i[0], y=i[1])
    return pt_set   

def gen_combinations(pt_set, hspace_cond):
    """
    Description
    
    Parameters 
    ----------
    pt_set : 
        Description
    hspace_cond:
        Description
    """
    filtered_combs = []
    """ignore any |combinations| < hspace_cond"""
    for i in range(math.ceil(hspace_cond), len(pt_set)+1):
        combo_r = combinations(pt_set, i)
        filtered_combs.extend([list(comb) for comb in combo_r])
    return filtered_combs

def find_compact_conv_sets(pt_set, pt_combinations):
    """
    Description
    
    Parameters 
    ----------
    pt_set : 
        Description
    pt_combinations:
        Description
    """
    valid_combs = []
    
    def _get_unique_combinations(combinations): 
        unique_valid_combs = []
        for comb in combinations:
            if not any(np.array_equal(comb, unique) for unique in unique_valid_combs):
                unique_valid_combs.append(comb)
        return unique_valid_combs 

    for comb in pt_combinations: 
        """normal equations in 2D list:[ x_norm, y_norm, offset] , ... , ]
               - x_norm, y_norm form a normal vector
               - offset : scalar multiple applied to [x, y] normal vector to get to origin
        """
        hull_eq = ConvexHull(comb).equations
        """find family of compact convex sets C that satisfy hspace_cond"""
        for eq in hull_eq: 
            """unpack -offset to account for """
            x_norm, y_norm, offset = eq
            offset = np.negative(offset)
            eq_count = 0
            pts_not_in_comb = pt_set[np.isin(pt_set, comb, invert=True).all(axis=1)] 
            for pt in pts_not_in_comb:
                x, y = pt 
                if x_norm*(x-x_norm*offset)+y_norm*(y-y_norm*offset) > 0 :
                    eq_count += 1
            if eq_count == 0:
                valid_combs.append(comb)

    compact_conv_sets = _get_unique_combinations(valid_combs) 
    return compact_conv_sets


def show_sets(c_sets, plt):
    ## viridis is just a standard uniform colormap
    cmap = plt.cm.get_cmap('viridis', len(c_sets))
    colors = cmap(np.linspace(0,1, len(c_sets)))
    new_map = ListedColormap(colors)
    for color, pt_comb in enumerate(c_sets):
        # assuming pt_comb are np.arrays
        pts = np.asarray(pt_comb)
        plt.fill(pts[:,0], pts[:,1], color = new_map(color), edgecolor='black', alpha = 0.1)

def on_key_press(event):
    if event.key == 'escape':
        update_plot()

def update_plot():
    plt.cla() 
    pt_set = create_pts(plt)
    hspace_cond = 2/3 * len(pt_set)
    pt_combinations = gen_combinations(pt_set, hspace_cond)
    compact_conv_sets = find_compact_conv_sets(pt_set, pt_combinations)
    print(compact_conv_sets)
    show_sets(compact_conv_sets, plt)
    plt.draw()  

def main(): 
    fig = plt.figure()
    plt.style.use('fast')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    cid = fig.canvas.mpl_connect('key_press_event', on_key_press)
    update_plot()
    plt.show()

if __name__ == '__main__': 
    main()
