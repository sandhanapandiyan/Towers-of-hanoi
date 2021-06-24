# TowersofHanoi
def tower_of_hanoi(n, start, auxiliary, end):  
    if(n == 1):  
        print('Move disk 1 from rod {} to rod {}'.format(start, end))  
        return
    tower_of_hanoi(n - 1, start, end, auxiliary)  
    print('Move disk {} from rod {} to rod {}'.format(n, start, end))  
    tower_of_hanoi(n - 1, auxiliary, start, end)  
#Main
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')