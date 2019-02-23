l=range(1,101)
print(l)
l1=[]
i=0
for k in l:
	print(k)
	if(k%6==0):
		print("shuchu:%d" %k)
		l1.append(k)	
		l.remove(k)
		print("qudiaole:%d" %k)
		i=0
		print(l)
