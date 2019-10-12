for i in range(1,101):
	if i % 7 == 0:		#整除7
		continue
	if i % 10 == 7: 	#个位是7
		continue
	if i // 10 == 7:	#十位是7
		continue
	else:
		print(i)
