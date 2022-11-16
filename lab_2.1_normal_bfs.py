#Lab-2___16th_November_Assignment_1
#Normal BFS:
q=[]
vis=[]
g={
    '1':['2','3','4'],
    '2':['5','6'],
    '3':[],
    '4':['7','8'],
    '5':['9','10'],
    '6':[],
    '7':['11','12'],
    '8':[],
    '9':[],
    '10':[],
    '11':[],
    '12':[]
}

def bfs(vis,g,node):
    vis.append(node)
    q.append(node)
    
    while q:
        #pop and then print!
        temp=q.pop(0)
        print(temp)
        
        #visit the unvisited and then put them in queue!
        for m in g[temp]:
            if m not in vis:
                vis.append(m)
                q.append(m)
                

bfs(vis,g,'1')
