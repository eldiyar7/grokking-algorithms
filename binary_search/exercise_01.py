# Time:  O(logn)
# Space: O(1)
#
# You are a product manager and currently leading a team to
# develop a new product. Unfortunately, the latest version of
# your product fails the quality check. Since each version is
# developed based on the previous version, all the versions
# after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to
# find out the first bad one, which causes all the following
# ones to be bad.
#
# You are given an API bool isBadVersion(version) which will
# return whether version is bad. Implement a function to find
# the first bad version. You should minimize the number of
# calls to the API.
#

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution():
    def __init__(self, versions, badVersions):
        self.versions =  versions
        self.badVersions = badVersions

    def isBadVersion(self, mid):
        if mid in self.badVersions:
            return True
        else:
            return False

    def firstBadVersion(self):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = len(self.versions)
        while left <= right:
            mid = int((left + right) / 2)
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

instance_1 = Solution([1,2,5,6,7,8,9,10], [6,7,8,9,10])
print (instance_1.firstBadVersion())