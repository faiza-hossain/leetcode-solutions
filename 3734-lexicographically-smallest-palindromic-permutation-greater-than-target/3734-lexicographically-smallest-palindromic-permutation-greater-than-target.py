class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half = n // 2
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd_chars = [i for i in range(26) if cnt[i] % 2 == 1]
        if n % 2 == 0:
            if odd_chars:
                return ""
            mid_char = ""
        else:
            if len(odd_chars) != 1:
                return ""
            mid_char = chr(odd_chars[0] + 97)

        half_cnt = [c // 2 for c in cnt]

        def build(h_chars):
            h = "".join(h_chars)
            return h + mid_char + h[::-1]

        # 1. Try exact match of target's first half
        temp = half_cnt[:]
        feasible = True
        for ch in target[:half]:
            idx = ord(ch) - 97
            if temp[idx] == 0:
                feasible = False
                break
            temp[idx] -= 1

        if feasible:
            t = build(list(target[:half]))
            if t > target:
                return t

        # 2. Try diverging at position i, from the end backward
        for i in range(half - 1, -1, -1):
            temp = half_cnt[:]
            ok = True
            for ch in target[:i]:
                idx = ord(ch) - 97
                if temp[idx] == 0:
                    ok = False
                    break
                temp[idx] -= 1
            if not ok:
                continue

            target_idx = ord(target[i]) - 97
            cand = -1
            for c in range(target_idx + 1, 26):
                if temp[c] > 0:
                    cand = c
                    break
            if cand == -1:
                continue

            temp[cand] -= 1
            rest = []
            for c in range(26):
                rest.append(chr(c + 97) * temp[c])
            h_chars = list(target[:i]) + [chr(cand + 97)] + list("".join(rest))
            return build(h_chars)

        return ""