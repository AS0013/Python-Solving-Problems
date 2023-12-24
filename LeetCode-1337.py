# LeetCode Easy: 1337. The K Weakest Rows in a Matrix.

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # contains no. of soldiers and row number
        temp = []

        for i,m in enumerate(mat):
            temp.append([sum(m),i])
        # sorting by first element of each list
        temp.sort()

        return [temp[i][1] for i in range(k)]
    

