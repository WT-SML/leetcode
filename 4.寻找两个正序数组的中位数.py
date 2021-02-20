"""
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
通过次数335,540提交次数846,990
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

# ts 解法
# /**
#  * @param {number[]} nums1
#  * @param {number[]} nums2
#  * @return {number}
#  */
# const findMedianSortedArrays = function (nums1, nums2) {
#     let arr = [...nums1, ...nums2]
#     const quickSort = (array) => {
#         const sort = (arr, left = 0, right = arr.length - 1) => {
#             if (left >= right) {//如果左边的索引大于等于右边的索引说明整理完毕
#                 return
#             }
#             let i = left
#             let j = right
#             const baseVal = arr[j] // 取无序数组最后一个数为基准值
#             while (i < j) {//把所有比基准值小的数放在左边大的数放在右边
#                 while (i < j && arr[i] <= baseVal) { //找到一个比基准值大的数交换
#                     i++
#                 }
#                 arr[j] = arr[i] // 将较大的值放在右边如果没有比基准值大的数就是将自己赋值给自己（i 等于 j）
#                 while (j > i && arr[j] >= baseVal) { //找到一个比基准值小的数交换
#                     j--
#                 }
#                 arr[i] = arr[j] // 将较小的值放在左边如果没有找到比基准值小的数就是将自己赋值给自己（i 等于 j）
#             }
#             arr[j] = baseVal // 将基准值放至中央位置完成一次循环（这时候 j 等于 i ）
#             sort(arr, left, j - 1) // 将左边的无序数组重复上面的操作
#             sort(arr, j + 1, right) // 将右边的无序数组重复上面的操作
#         }
#         const newArr = array.concat() // 为了保证这个函数是纯函数拷贝一次数组
#         sort(newArr)
#         return newArr
#     }
#     arr = quickSort(arr)
#     console.log(arr)
#     if (arr.length % 2 === 0) {
#         let i = arr.length / 2
#         return (arr[i] + arr[i - 1]) / 2
#     } else {
#         return arr[(arr.length - 1) / 2]
#     }
# }
