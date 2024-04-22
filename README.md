# Centerpoint Theorem
Spring 2024 CSC591 Computational Geometry Project on the Centerpoint Theorem.

We base our implementation on Matoušek's proof in Section 1.4 of [*Lectures on Discrete Geometry*](https://link.springer.com/book/10.1007/978-1-4613-0039-7).

We calculate the compact convex closures $C_i$ of points set $P$ such that $|C_i| > \frac{n}{d+1}$, where $d$ = dimension, $n = |P|$.

We find the intersection of all $C_i$, showing the center region. Any point within this region is a valid center point. The center region may be a single point, as in the case of a quadrilateral. 

## What is a centerpoint?
A [centerpoint](https://en.wikipedia.org/wiki/Centerpoint_(geometry)) $c$ of a set $X$ of $n$ points  in $d$ dimensions is defined as a point such that any hyperplane that goes through $c$ divides the point set $X$ such that at least $\frac{n}{d+1}$ points are on either side of the hyperplane. In 2-dimensions, the number of dimensions that this program visualizes, this means that any line through a centerpoint has $\frac{2}{3}*n$ points on either side.

The center region $R = \Set{c \mid \text{c is a centerpoint}}$. In other words, the center region is the region that contains only the centerpoints.

## How to find the centerpoints
The center region can be equivalently defined as the intersection of all halfspaces that contain at least $\frac{n}{d+1}$ points. In this program, we find the convex closures of every subset of $X$ containing at minimum this many points that can be separated from the rest of the set by a halfspace, to show the centerpoint theorem. Then, since every $d+1$ of the subsets must have an intersection, by [Helly's Theorem](https://en.wikipedia.org/wiki/Helly%27s_theorem) there must exist an intersection between all these convex closures. This intersection between all the convex closures is the center region. For more details on this proof see Matoušek's proof in Section 1.4 of [*Lectures on Discrete Geometry*](https://link.springer.com/book/10.1007/978-1-4613-0039-7).

## Implementation details 
1. $|P|$, length of input set, should be $> 2$
2. See `requirements.txt` for required packages 
3. There are many more efficient algorithms to find the centerpoint. Our program only shows the center region via the method described in the proof.
