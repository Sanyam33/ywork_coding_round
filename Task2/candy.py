rating=[1,2,1]
candy=[0,0,0]


for i in range(0,len(rating)):
    if i==0:
        if rating[i]>rating[i+1]:
            candy[i]+=2
        else:
            candy[i]=1
            
    elif i==len(rating)-1:
        if rating[i]>rating[i-1]:
            candy[i]= candy[i]+2
        else:
            candy[i]=1
    
    elif rating[i]>rating[i-1] or rating[i]>rating[i+1]:
        candy[i]+=2
    
    else:
        candy[i]+=1
        
        
print(f'ratting: {rating}')    
print(f'candy: {candy}')
print(f'candy: {sum(candy)}')