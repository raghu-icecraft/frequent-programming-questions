def remove_overlap(rs):
        rs.sort()
        def process (rs,deviation):
                start = len(rs) - deviation - 1
                if start < 1:
                        return rs
                if rs[start][0] > rs[start-1][1]:
                        return process(rs,deviation+1)
                else:
                        rs[start-1] = ((rs[start][0],rs[start-1][0])[rs[start-1][0] < rs[start][0]],(rs[start][1],rs[start-1][1])[rs[start-1][1] > rs[start][1]])
                        del rs[start]
                        return process(rs,0)
        return process(rs,0)
r = [(1,7),(4,9),(3,5),(5,13),(3,7),(14,78)]
l=remove_overlap(r)
print(l)

#Input : [(1,7),(4,9),(3,5),(5,13),(3,7),(14,78)]
#Output : [(1, 13), (14, 78)]
