"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
通过次数449,004提交次数1,145,158
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass

# ts 解法
# function longestCommonPrefix(strs: string[]): string {
#     if (strs.length === 0) {
#         return ""
#     }
#     for (const i in strs[0].split("")) {
#         for (const j in strs) {
#             if (strs[j][i] !== strs[0][i]) {
#                 return strs[0].slice(0, parseInt(i))
#             }
#         }
#     }
#     return strs[0]
#
# }
