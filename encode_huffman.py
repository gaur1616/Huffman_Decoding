import string

#File Handling: Open and Reading the input text in the file:
rf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Input Text.txt','r')
para=rf.read()
rf.close()

#File Handling: Refering to the Prefix Free Code Lookup Table for encoding
rf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Prefix Free Code.txt','r');
codestring = rf.read().split('\n')
rf.close()

codebook = []
for i in range(len(codestring)-1):
    codebook.append([codestring[i].split(' , ')[0], codestring[i].split(' , ')[1]])

#Generating Encoded Text:
wf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Encoded Text.txt','w')
for ele in para:
    for i in range(len(codebook)):
        if ele == codebook[i][0]:
            wf.write(codebook[i][1])
wf.close()
