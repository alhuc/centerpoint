from matplotlib.backend_bases import MouseButton
from matplotlib.colors import ListedColormap
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
from shapely.geometry import Polygon, Point, GeometryCollection, MultiPolygon
from shapely import affinity
import shapely
from scipy.spatial import ConvexHull
import math

def tellme(s):
    print(s)
    plt.suptitle(s, wrap=True)
    plt.draw()

def create_pts(plt):
    pt_set = []
    tellme('Select $n$ points. Right click to remove last added. Press anything else to finish selection. Esc to start over')
    pt_set = np.asarray(plt.ginput(-1, timeout=-1, mouse_stop = MouseButton.MIDDLE))
    for i in pt_set:
        plt.scatter(x=i[0], y=i[1], zorder = 2)
    return pt_set   

def gen_combinations(pt_set, hspace_cond):
    filtered_combs = []
    """ignore any |combinations| < hspace_cond"""
    for i in range(math.floor(hspace_cond) + 1, len(pt_set)+1):
        combo_r = combinations(pt_set, i)
        filtered_combs.extend([list(comb) for comb in combo_r])
    return filtered_combs

def find_compact_conv_hulls(pt_set, pt_combinations):
    all_hull_vertices = []
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
        hull = ConvexHull(comb, qhull_options="Qx")
        """extract ccw-order of hull indices"""
        hull_vertices = hull.vertices
        hull_eq = hull.equations
        """find family of compact convex sets C that satisfy hspace_cond"""
        for eq in hull_eq: 
            """unpack -offset for orientation away from C_i """
            x_norm, y_norm, offset = eq
            offset = np.negative(offset)
            other_points_inside = 0
            pts_not_in_comb = pt_set[np.isin(pt_set, comb, invert=True).all(axis=1)] 
            for pt in pts_not_in_comb:
                x, y = pt 
                if x_norm*(x-x_norm*offset)+y_norm*(y-y_norm*offset) <= 0 :
                    other_points_inside += 1
            if other_points_inside == 0:
                all_hull_vertices.append([comb[i] for i in hull_vertices])
    compact_conv_hulls = _get_unique_combinations(all_hull_vertices) 
    return compact_conv_hulls



def show_sets(c_sets, plt):
    cmap = plt.cm.get_cmap('viridis', len(c_sets))
    colors = cmap(np.linspace(0,1, len(c_sets)))
    new_map = ListedColormap(colors)
    hatch_styles = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    for color, pt_comb in enumerate(c_sets):
        hatch_style = color % len(hatch_styles)
        pts = np.asarray(pt_comb)
        plt.fill(pts[:,0], pts[:,1], color = new_map(color), alpha = 0.08, zorder=1)

def on_key_press(event):
    if event.key == 'escape':
        update_plot()


def find_intersection(plt, vertex_set):
    polygons = [Polygon(conv_closure) for conv_closure in vertex_set]
    inter_object = polygons[0]
    delta = 10e-7
    wiggle_dir = [[0,delta], [delta,0], [0, -delta], [-delta, 0]]
    for i in polygons:
        all_wiggle_inters = []
        for dir in wiggle_dir:
            inter_object_dir = affinity.translate(inter_object, xoff=dir[0], yoff=dir[1])
            all_wiggle_inters.append(inter_object_dir)
        union_inters = shapely.union_all(all_wiggle_inters)
        inter_object = shapely.intersection(union_inters, i)
    show_intersection(inter_object, plt, delta)
    

def show_intersection(inter_object, plt, delta):
    colormap = plt.cm.get_cmap('cividis')
    tellme("Centerpoints WRITE SOMETHING HERE ")
    col = colormap(np.random.rand())
    if isinstance(inter_object, Polygon):
        minx, miny, maxx, maxy = inter_object.bounds
        print("x: ", maxx-minx)
        print("y: ", maxy-miny)
        if(maxx-minx <= delta * 10 and maxy-miny <= delta * 10):
            show_intersection(Point((maxx+minx)/2, (maxy+miny)/2), plt, delta)
        x, y = inter_object.exterior.coords.xy
        plt.fill(x,y, color = col, hatch='\|', alpha = .24)
    if isinstance(inter_object, GeometryCollection):
        for i in inter_object.geoms:
            show_intersection(i, plt, delta)
    if isinstance(inter_object, MultiPolygon):
        for i in inter_object.geoms:
            show_intersection(i, plt, delta)
    if isinstance(inter_object, Point):
        plt.scatter(inter_object.x, inter_object.y, s = 100, color = col)

def update_plot():
    plt.clf() 
    plt.style.use('fast')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    pt_set = create_pts(plt)
    hspace_cond = 2/3 * len(pt_set)
    pt_combinations = gen_combinations(pt_set, hspace_cond)
    compact_conv_hulls = find_compact_conv_hulls(pt_set, pt_combinations)
    show_sets(compact_conv_hulls, plt)
    intersection = find_intersection(plt, compact_conv_hulls)
    plt.draw()


def main(): 
    fig = plt.figure()
    cid = fig.canvas.mpl_connect('key_press_event', on_key_press)
    update_plot()
    plt.show()

if __name__ == '__main__': 
    main()
