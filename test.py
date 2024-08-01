txtfile = open("myfile.txt",'w')
for i in range (100):
    print("I love Python",sep = '',end = '\n',file = txtfile,flush = True)