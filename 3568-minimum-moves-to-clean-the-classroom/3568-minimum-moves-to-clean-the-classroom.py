from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        litter = []
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        L = len(litter)
        litter_id = {pos: k for k, pos in enumerate(litter)}
        full_mask = (1 << L) - 1
        E = energy + 1  

        def mask_of(r, c, mask):
            if (r, c) in litter_id:
                return mask | (1 << litter_id[(r, c)])
            return mask

        def idx(r, c, mask, e):
            return ((r * n + c) * (full_mask + 1) + mask) * E + e

        start_mask = mask_of(sr, sc, 0)
        if start_mask == full_mask:
            return 0

        size = m * n * (full_mask + 1) * E
        visited = bytearray(size)
        visited[idx(sr, sc, start_mask, energy)] = 1

        queue = deque([(sr, sc, start_mask, energy)])
        moves = 0

        while queue:
            moves += 1
            for _ in range(len(queue)):
                r, c, mask, e = queue.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    if e == 0:
                        continue

                    ne = energy if classroom[nr][nc] == 'R' else e - 1
                    nmask = mask_of(nr, nc, mask)

                    if nmask == full_mask:
                        return moves

                    i = idx(nr, nc, nmask, ne)
                    if visited[i]:
                        continue
                    visited[i] = 1
                    queue.append((nr, nc, nmask, ne))

        return -1