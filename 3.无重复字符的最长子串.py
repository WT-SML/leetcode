"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
通过次数833,307提交次数2,288,439
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

# ts 解法
# /**
#  * @param {string} s
#  * @return {number}
#  */
# let lengthOfLongestSubstring = function(s) {
#   let l = 0, r = 0, ret = 0, set = new Set, n = s.length; //当前移动窗口的起止位置，返回结果，历史字符集合 ,子串长度
#   for (let i in s) { //遍历字符串
#     i *= 1 //转为 int
#     set.clear() //初始化set
#     l = i; //左边界递增
#     r = i; //右边界从左边界开始
#     while (r < n) {
#       if (set.has(s[r])) { //碰到重复的
#         break
#       }
#       set.add(s[r])//将当前字符存入set
#       ret = Math.max(ret, Array.from(set).length)
#       r++
#     }
#   }
#   return ret
# }
