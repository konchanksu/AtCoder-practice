class SegmentTree: 
    def __init__(self, n, first_status):
        """
        :param n: 要素数
        :param INF: 初期値（入りうる要素より十分に大きな数）
        """
        n2 = 1 << (n - 1).bit_length()
        self.offset = n2
        self.tree = [INF] * (n2 << 1)
        self.INF = INF
 
    def update(self, i, x):
        """
        i番目の値をxに更新
        :param i: index(0-indexed)
        :param x: update value
        """
        i += self.offset
        self.tree[i] = x
        while i > 1:
            y = self.tree[i ^ 1]
            if y <= x:
                break
            i >>= 1
            self.tree[i] = x
 
    def get_min(self, a, b):
        """
        [a, b)の最小値を得る
        :param a: index(0-indexed)
        :param b: index(0-indexed)
        """
        result = self.INF
 
        l = a + self.offset
        r = b + self.offset
        while l < r:
            if r & 1:
                result = min(result, self.tree[r - 1])
            if l & 1:
                result = min(result, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
 
        return result

N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(Q)]
