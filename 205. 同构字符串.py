"""
205. 同构字符串
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。



示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true


提示：

1 <= s.length <= 5 * 104
t.length == s.length
s 和 t 由任意有效的 ASCII 字符组成
通过次数185,198提交次数372,447
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dit = {}
        for _ in range(len(s)):
            s_c = s[_]
            t_c = t[_]
            if dit.get(s_c) is None:
                if list(dit.values()).count(t_c) > 0:
                    return False
                dit[s_c] = t_c
            elif dit[s_c] != t_c:
                return False
        return True


print(Solution().isIsomorphic("badc", "baba"))
