class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for a, b in zip(s, target):
            cnt[ord(a) - 97] += 1
            cnt[ord(b) - 97] -= 1

        for i in range(len(target) - 1, -1, -1):
            x = ord(target[i]) - 97
            cnt[x] += 1

            if min(cnt) < 0:
                continue

            for y in range(x + 1, 26):
                if cnt[y]:
                    cnt[y] -= 1
                    return target[:i] + chr(y + 97) + ''.join(
                        chr(k + 97) * cnt[k] for k in range(26)
                    )

        return ""
