def main():
	print("hello world!!")

if __name__ == '__main__':
    main()

#faster and harder method
def climbingLeaderboard(scores, alice):

	#at the same time of giving every leaderboard score
	#we compare the leaderboard score with alice's score
	#in the reverse manner cuz alice's highest score is at the end
	#immediately append alice score in a new list
	#using list.pop() to reduce length of alice's list as
	#the compared score is no longer needed
	#a O(n) method
    alice_ranking = []
    for index, x in enumerate(scores):
        if index == 0:
            rank = 1 
        else :
            if x != scores[index-1]:
                rank += 1
        
        if len(alice) == 0:
            break
        else:
            while len(alice)>0 and alice[-1] >= x:
                alice_ranking.append(rank)
                alice.pop()
    
    last_rank = rank + 1
    if len(alice) != 0:
        for x in alice:
            alice_ranking.append(last_rank)
        
    alice_ranking.reverse()
    return alice_ranking

#slower and memory extensive method
def climbingLeaderboard2(scores, alice):

	#create a list that gives every score a ranking 1st
	ranked_scores = []
    for index, x in enumerate(scores):
        if index == 0:
            rank = 1
        else:
            if x != scores[index-1]:
                rank += 1
        ranked_scores.append(rank)

    #then iterate each alice's score and gives alice ranking
    #it's slow cuz alice's score list is descending
    #while the leaderboard score is ascending
    #means every iteration we will go to the end of leaderboard
    # to give alice ranking
    # looks like a O(n^2) or O(n^3) method
    alice_ranking = []
    for index, x in enumerate(alice):
        for index2, y in enumerate(scores):
            if x >= y :
                rank = ranked_scores[index2]
                alice_ranking.append(rank)
                break 
            
            if index2 == len(scores) - 1 and x < y:
                rank = ranked_scores[index2] + 1
                alice_ranking.append(rank)
                break
    return alice_ranking