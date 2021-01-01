n=int(input())
#n=3
l=1
def moveTower(n, otkuda, kuda, withPole):
    if n >= 1:
        moveTower(n-1, otkuda, withPole, kuda)
        moveDisk(otkuda, kuda)
        global l
        l += 1
        moveTower(n-1, withPole, kuda, otkuda)

def moveDisk(fp,tp):
    #l=1
    print("nomer hoda:", l, ";otkuda:", fp, ";kuda:", tp)
moveTower(n,"A","B","C")