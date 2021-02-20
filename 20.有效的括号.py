"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true


提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        pass
# ts 解法
# function isValid(s: string): boolean {
#     const stack: string[] = []
#     const hashMap: { [index: string]: string } = {
#         ')': '(',
#         '}': '{',
#         ']': '[',
#     }
#     for (const v of s) {
#         // 遇到了结束符
#         if (hashMap[v]) {
#             // 合法的出栈
#             if (hashMap[v] === (stack.slice(-1)[0])) {
#                 stack.pop()
#                 continue
#             } else {
#                 // 不合法的退出方法
#                 return false
#             }
#         }
#         // 入栈
#         stack.push(v)
#     }
#     return stack.length === 0
# }
