# Centerpoint Theorem
Spring 2024 CSC591 Computational Geometry Project on the Centerpoint Theorem.

We base our implementation on Matoušek's proof in Section 1.4 of [*Lectures on Discrete Geometry*](https://link.springer.com/book/10.1007/978-1-4613-0039-7).

We calculate the compact convex closures $C_i$ of points set $P$ such that $|C_i| > \frac{n}{d+1}$, where $d$ = dimension, $n = |P|$.

We find the intersection of all $C_i$, showing the center region. Any point within this region is a valid center point. The center region may be a single point, as in the case of a quadrilateral. 

## Implementation details 
1. $|P|$, length of input set, should be $> 2$
2. See `requirements.txt` for required packages 
