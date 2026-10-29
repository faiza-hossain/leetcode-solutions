
class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: avoids recursion-depth errors.
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1

                parent[0][u] = u if p == -1 else p
                for k in range(1, LOG):
                    parent[k][u] = parent[k - 1][
                        parent[k - 1][u]
                    ]

                stack.append((u, p, 1))
                for v in reversed(graph[u]):
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def is_ancestor(u, v):
            return tin[u] <= tin[v] <= tout[u]

        def lca(u, v):
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v

            for k in range(LOG - 1, -1, -1):
                anc = parent[k][u]
                if not is_ancestor(anc, v):
                    u = anc

            return parent[0][u]

        # Fenwick tree supporting XOR updates and prefix XOR queries.
        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_update(left, right, value):
            add(left, value)
            if right + 1 < n:
                add(right + 1, value)

        # Each node's character is represented by one bit.
        masks = [1 << (ord(c) - ord('a')) for c in s]

        # Store each node's contribution over its Euler subtree.
        for u in range(n):
            range_update(tin[u], tout[u], masks[u])

        ans = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - ord('a'))

                delta = masks[u] ^ new_mask
                if delta:
                    range_update(tin[u], tout[u], delta)
                    masks[u] = new_mask

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                # Root-to-node masks, with the LCA counted once.
                path_mask = (
                    prefix(tin[u])
                    ^ prefix(tin[v])
                    ^ masks[w]
                )

                # At most one character may have odd frequency.
                ans.append(
                    (path_mask & (path_mask - 1)) == 0
                )

        return ans
