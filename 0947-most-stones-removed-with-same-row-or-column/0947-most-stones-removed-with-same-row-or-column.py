class Solution(object):
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.rank = {}

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

        def add(self, x):
            if x not in self.parent:
                self.parent[x] = x
                self.rank[x] = 0

    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        uf = self.UnionFind()
        for x, y in stones:
            uf.add(x)
            uf.add(~y)  # Use ~y to distinguish columns from rows since -0 == 0
            uf.union(x, ~y)

        root_set = set()
        for x, y in stones:
            root_set.add(uf.find(x))
            root_set.add(uf.find(~y))

        return len(stones) - len(root_set)
        