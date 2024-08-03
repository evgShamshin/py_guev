mv_v1 = int(input())
mv_g1 = int(input())
mv_v2 = int(input())
mv_g2 = int(input())
if (mv_v1 - 1 == mv_v2 or mv_v1 + 1 == mv_v2 or mv_v1 == mv_v2) and (mv_g1 - 1 == mv_g2 or mv_g1 + 1 == mv_g2 or mv_g1 == mv_g2):
    print("YES")
else:
    print("NO")