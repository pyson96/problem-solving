class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if(len(nums1) > len(nums2)) : 
            return self.findMedianSortedArrays(nums2, nums1)
        l = 0
        r = len(nums1) 
        mid = (l + r) // 2
        while l <= r :
            conditionValue = self.checkCondition(nums1,nums2,mid)
            if conditionValue == 1 :
                r = mid - 1
                mid = (l + r) // 2
            if conditionValue == 2 :
                l = mid + 1
                mid= (l + r) // 2
            if conditionValue == 0 :
                return self.getAnswer(nums1,nums2,mid)
        return 0

    def checkCondition(self,nums1,nums2,mid) :
        total = len(nums1) + len(nums2)
        mid2 = (total + 1 ) // 2 - mid
        leftValue1 = nums1[mid-1] if mid-1 >= 0 else float('-inf')
        rightValue1 = nums1[mid] if mid < len(nums1) else float('inf')
        leftValue2 = nums2[mid2-1] if mid2-1 >= 0 else float('-inf')
        rightValue2 = nums2[mid2] if mid2 < len(nums2) else float('inf')
        if leftValue1 > rightValue2 :
            return 1
        if leftValue2 > rightValue1 :
            return 2
        return 0
    def getAnswer(self,nums1,nums2,mid) :
        total = len(nums1) + len(nums2)
        mid2 = (total + 1 ) // 2 - mid
        leftValue1 = nums1[mid-1] if mid-1 >= 0 else float('-inf')
        rightValue1 = nums1[mid] if mid < len(nums1) else float('inf')
        leftValue2 = nums2[mid2-1] if mid2-1 >= 0 else float('-inf')
        rightValue2 = nums2[mid2] if mid2 < len(nums2) else float('inf')
        if total % 2 == 0 :
            return ( max(leftValue1, leftValue2) + min(rightValue1, rightValue2) ) / 2
        else  :
            return max(leftValue1, leftValue2)
s = Solution()
s.findMedianSortedArrays([1,2], [3,4])