# "Prime Palindrome Golf" downloaded: Sun Jul 31 18:29:28 2016
golf=lambda x:[i for i in range(x+1,7**6)if i==int(str(i)[::-1])and all(i%j>0for j in range(2,i))][0]
