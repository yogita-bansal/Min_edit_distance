'''
Name- Yogita Bansal
Roll No.- PhD18201
Assignment 1- Minimum Edit Distance
Date-16-08-2018
'''

# code for Minimum edit distance algorithm
import numpy as np
import sys

def ins_cost(c):
    return 1
    
def sub_cost(source_char,target_char):
    if source_char == target_char:
        return 0
    else:
        return 2

def del_cost(c):
    return 1
def min_edit_distance(source,target):

#     target='intention'
#     source='Execution'
#     dic={'s':"Substitution",'d':"Deletion",'l':"Insertion"}
    path=[]
    target=target.lower()
    source=source.lower()
    loc=[]
#     if source == target: return 0
#     elif len(source) == 0: return len(target)
#     elif len(target) == 0: return len(source)
#     if len(source)<len(target):
#         source, target = target, source
#     print(target,source)
    m=len(target)
    n=len(source)
    dist_mat=np.zeros((m+1,n+1))
    dist_mat_pointer=np.zeros((m+1,n+1),dtype=str)
    
    #print(dist_mat)
    #initialize the zeroth row and column to be the distance from the empty string
    dist_mat[0][0]=0
    for i in range(1,m+1):
        dist_mat[i][0]=dist_mat[i-1][0]+ins_cost(target[i-1])
    for j in range(1,n+1):
        dist_mat[0][j]=dist_mat[0][j-1]+ins_cost(source[j-1])
    for i in range(1,m+1):
        for j in range(1,n+1):
            insertion=dist_mat[i-1][j]+ins_cost(target[i-1])
            substitution=dist_mat[i-1][j-1]+sub_cost(source[j-1],target[i-1])
            deletion=dist_mat[i][j-1]+del_cost(source[j-1])
            val=min(insertion,substitution,deletion)
            loc=np.argmin([substitution,deletion,insertion])
            if loc==2:
#                 index=[i-1,j]
                pointer="l"
            elif loc==0:
#                 index=[i-1,j-1]
                pointer='s'
            elif loc==1:
#                 index=[i,j-1]
                pointer='d'
            dist_mat[i][j]=val
#             b=b=[str(x) for x in index]
#             pointer_string="_".join(b)
            dist_mat_pointer[i][j]=pointer
#             print(pointer_string)
#             dist_mat[i][j]=min(dist_mat[i-1][j]+ins_cost(target[i-1]),dist_mat[i-1][j-1]+
#             sub_cost(source[j-1],target[i-1]),dist_mat[i][j-1]+del_cost(source[j-1]))
# #             print(argmin([dist_mat[i-1][j]+ins_cost(target[i-1]),dist_mat[i-1][j-1]+sub_cost(source[j-1],target[i-1]),(dist_mat[i][j-1]+del_cost(source[j-1]))])
    #printing the path
    i=m
    j=n
    path.append(dist_mat_pointer[i][j])
    s_final=""
    t_final=""
    seq=""
    while(i>0 and j>0):
        if dist_mat_pointer[i][j]=='l':
            i=i-1
            s_final+="*"
            t_final+=target[i]
            path.append(dist_mat_pointer[i][j])
            seq+='d'
        if dist_mat_pointer[i][j]=='s':
            i=i-1
            j=j-1
            s_final+=source[j]
            t_final+=target[i]
            if source[j]==target[i]:
                seq+=" "
            else:
                seq+="s"
            path.append(dist_mat_pointer[i][j])
        if dist_mat_pointer[i][j]=='d':
            j=j-1
            s_final+=source[j]
            t_final+=("*")
            seq+='i'
            path.append(dist_mat_pointer[i][j])
#     print(s_final)
#     print(t_final)
#     print(i)
#     print(j)
    if(i!=0):
        while(i>0):
            i-=1
            t_final=t_final+target[i]
            s_final=s_final+'*'
            seq+='d'
    if(j!=0):
        while(j>0):
            j-=1
            s_final=s_final+source[j]
            t_final=t_final+"*"
            seq+='i'
    s_final=s_final[::-1]
    t_final=t_final[::-1]
    seq=seq[::-1]
    print("minimum edit distance between",source,"&",target,"=",dist_mat[m][n])
    print(s_final)
    print("|" * max(len(source),len(s_final)))
    print(t_final)
    print(seq)
    return(dist_mat[m][n])


if len (sys.argv) <3 :
    print ("Usage: python script.py word1 word2")
    print(sys.argv)
    sys.exit (1)
cost=min_edit_distance(source=sys.argv[1],target=sys.argv[2])
#print(cost,path)