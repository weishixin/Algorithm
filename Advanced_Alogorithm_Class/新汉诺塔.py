
def move( x , n , z ):
    if (x==0 and z ==2) or (x==2 and z ==0):
        return 2
    else:
        return 1

def hanoi( n , x , y , z ):
    count = 0
    if n == 1 :
        count +=move(x, n , z)
        return count
    else:
        count += hanoi( n-1 , x , y , z)#把n-1个盘子从x移动利用y移动到z上
        count += move(x , n , y)#把盘子n从x移动到y上
        count += hanoi(n - 1, z, y, x)#把n-1个盘子从z移动利用y移动到x上
        count += move(y, n, z)#把盘子n从y移动到z上
        count += hanoi(n-1 , x, y , z )
        return count


if __name__=='__main__':
    n = int(input())
    x=0
    y=1
    z=2
    print(hanoi(n,x,y,z))