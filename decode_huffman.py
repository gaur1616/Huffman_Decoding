#File Handling: Refering to the Prefix Free Code Lookup Table for encoding
rf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Prefix Free Code.txt','r');
codestring = rf.read().split('\n')
rf.close()

#File Handling: Refering to the Prefix Free Code Lookup Table for encoding
rf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Encoded text.txt','r');
en_text = rf.read()
rf.close()

codebook = []
for i in range(len(codestring)-1):
    codebook.append([codestring[i].split(' , ')[0], codestring[i].split(' , ')[1]])
    
codebook=sorted(codebook, key=lambda x: len(x[1]))

index = 0
wf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Decoded Text.txt','w')
while index<len(en_text):
    for i in range(len(codebook)):
        if en_text[index:index+len(codebook[i][1]):1] == codebook[i][1]:
            wf.write(codebook[i][0])
            index += len(codebook[i][1])
            break
wf.close()

#File Handling: Open and Reading the input text in the file:
rf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Input Text.txt','r')
para=rf.read()
rf.close()

#File Handling: Open and Reading the input text in the file:
rf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Decoded Text.txt','r')
de_para=rf.read()
rf.close()

#Error comparison between the input text and decoded text:
if de_para == para:
    print 'Good'
else:
    print 'Bad'