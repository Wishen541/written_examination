'''
首先，我们使用二分搜索来找到最小可能的 k 值。二分搜索的左边界为 1，右边界为所有箱子中小球数的最大值。
我们定义一个 min_k 变量，它表示能够找到特殊小球的最小 k 值。如果无论 k 为多少都不能一定找到特殊小球，则 min_k 保持为 -1。
在每次二分搜索中，我们计算中间值 mid 并将每个箱子中最多可以取出的球数设为 mid。
我们计算出每个箱子最多能被取出多少次，然后将这些次数加起来，以得到在最多 m 次机会中，可以从所有箱子中取出多少个球。
如果这个值大于等于 m，则我们可以在当前的 mid 值下找到特殊小球，因此我们更新 min_k 的值并继续在更大的 mid 值中搜索。否则，我们需要在更小的 mid 值中搜索。
'''

class Solution:
    def Function(self, n: int, m: int, boxes: List[int]) -> int:
        # 计算最小可能的 k 值
        left = 1
        right = max(boxes)
        min_k = -1
        
        while left <= right:
            mid = (left + right) // 2
            count = 0
            
            for box in boxes:
                count += (box // mid)
                if count >= m:
                    min_k = mid
                    break
            
            if count >= m:
                left = mid + 1
            else:
                right = mid - 1
        
        return min_k
