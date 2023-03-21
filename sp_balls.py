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
