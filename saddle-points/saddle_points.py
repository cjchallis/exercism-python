def saddle_points(mat):
    if not mat:
        return set()
    r = len(mat)
    c = len(mat[0])
    if any(len(row) != c for row in mat):
        raise ValueError('Not all rows are the same length.')

    return set([(i,j) for i in range(r) for j in range(c)
                      if all(mat[i][j] >= mat[i][k] for k in range(c))
                      if all(mat[i][j] <= mat[l][j] for l in range(r))
               ])
