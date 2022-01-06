a= [['g', 'f', 'g'],['i', 's'],['b', 'e', 's', 't']]
res = ''.join(ele for sub in a for ele in sub) 
print("The String after join : " + res)  