from typing import List
class Solution:

  def maxDepthAfterSplit(self, seq: str) -> List[int]:
    depth = 0
    ans = []
    for c in seq:
      if c == "(":
        depth += 1
        ans.append(depth % 2)
      else:
        ans.append(depth % 2)
        depth -= 1
    return ans