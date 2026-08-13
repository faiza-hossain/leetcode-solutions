class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Each node stores:
        # left_char, right_char, prefix_len, suffix_len, best_len
        tree = [None] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1)
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            merge(node, l, r)

        def merge(node, l, r):
            a = tree[node * 2]
            b = tree[node * 2 + 1]

            lc1, rc1, pre1, suf1, best1 = a
            lc2, rc2, pre2, suf2, best2 = b

            mid = (l + r) // 2
            len1 = mid - l + 1
            len2 = r - mid

            left_char = lc1
            right_char = rc2

            prefix = pre1
            if pre1 == len1 and rc1 == lc2:
                prefix += pre2

            suffix = suf2
            if suf2 == len2 and rc1 == lc2:
                suffix += suf1

            best = max(best1, best2)

            if rc1 == lc2:
                best = max(best, suf1 + pre2)

            tree[node] = (
                left_char,
                right_char,
                prefix,
                suffix,
                best
            )

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            merge(node, l, r)

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][4])

        return ans
