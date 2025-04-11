from graph_utils import *
from matrix_utils import *

n1 = 4
n2 = 2
n3 = 1
n4 = 7

n = n3 + 4

k = 1.0 - n3 * 0.01 - n4 * 0.005 - 0.05

dir = get_dir(n, k)

undir = get_undir(dir)
print_matrix(undir, "Undirected Graph")

B = get_B(n)
print_matrix(B, "B Matrix", 3)

C = get_C(undir, B)
print_matrix(C, "C Matrix", 3)

D = get_D(C)
print_matrix(D, "D Matrix")

H = get_H(D)
print_matrix(H, "H Matrix")

W = get_W(C, D, H)
print_matrix(W, "W Matrix", 3)

draw_graph(undir, directed=False, title="Undirected Graph", weight_matrix=W)
