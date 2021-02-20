"""
7. 整数反转
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0


提示：

-231 <= x <= 231 - 1
通过次数585,381提交次数1,674,526
"""


class Solution:
    def reverse(self, x: int) -> int:
        pass

# ts 解法
# function reverse(x: number): number {
#     const minus = "-";
#     let arr = (x + "").split("").reverse();
#     if (arr[arr.length - 1] === minus) {
#         arr.pop();
#         arr.unshift(minus);
#     }
#     let ret = Number(arr.join(""));
#     return ret >= (-2) ** 31 && ret <= 2 ** 31 - 1 ? ret : 0;
# }
