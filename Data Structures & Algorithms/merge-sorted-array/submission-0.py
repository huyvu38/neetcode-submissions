class Solution:
    def merge(self, nums1, m, nums2, n):

        p1 = m - 1
        p2 = n - 1

        insert = m + n - 1

        while p1 >= 0 and p2 >= 0:

            if nums1[p1] > nums2[p2]:
                nums1[insert] = nums1[p1]
                p1 -= 1
            else:
                nums1[insert] = nums2[p2]
                p2 -= 1

            insert -= 1

        # leftover nums2
        while p2 >= 0:
            nums1[insert] = nums2[p2]
            p2 -= 1
            insert -= 1