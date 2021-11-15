ranked_count=int(input())

ranked_string=input().split()

ranked=[]

for i in ranked_string:
	ranked.append(int(i))

player_count=int(input())

player_string=input().split()
player=[]

for i in player_string:
	player.append(int(i))

ranked_final=[]

for i in ranked:
	if i not in ranked_final:
		ranked_final.append(i)

ans=[]

for i in player:
	ranked_final.append(i)
	ranked_final.sort(reverse=True)
	ans.append(ranked_final.index(i)+1)
	ranked_final.remove(i)

for i in ans:
	print(i)

# 100 90 80 50
# 95 70 50
# 100 95 90 80 70 50
