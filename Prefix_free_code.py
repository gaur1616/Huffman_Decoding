import string

#Class definition of tree for generating a Prefix Free Code
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right
        self.freq = 0
        self.code =''

    def __str__(self):
        return str(self.cargo)
        
    def getLetter(self):
        return self.letter
        
    def setLetter(self,value):
        self.letter=value

    def getFreq(self):
        return self.freq
        
    def setFreq(self,value):
        self.freq=value
    
    def getCode(self):
        return self.code
        
    def setCode(self,value):
        self.code=value

#Stack definition to sort and store the created trees/symbols
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

#Sort and Store in Stack:
def sortedInsert(S, element):
    if (S.isEmpty() or element.freq < S.peek().freq):
	S.push(element)
    else:
	temp = S.pop()
	sortedInsert(S, element)
	S.push(temp)

#To visualise the tree:     
def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print '         ' * level + str(tree.cargo) + ' ' + str(tree.code)
    print_tree_indented(tree.left, level+1)

#Code Assignment for the generated prefix free tree:
def update_code(tree, appcode):
    if tree == None: return
    update_code(tree.right, appcode+'1')
    tree.code=tree.code+ appcode
    update_code(tree.left, appcode+'0')

#Codebook Creation for encoding:
def create_codebook(tree):
    if tree == None: return
    create_codebook(tree.right)
    if len(tree.cargo)==1:
        wf.write(tree.cargo+' , '+tree.code+'\n')
    create_codebook(tree.left)
    
#File Handling: Open and Reading the text in the file:
rf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Input Text.txt','r')
para=rf.read()
rf.close()

#Length of the Paragraph read:
length_para=float(len(para))

#Creating a dictionary:
dictionary= string.ascii_lowercase + string.ascii_uppercase + string.punctuation + ' ' + string.digits

#Relative Frequency of each symbol:
codebook=[];

for i in range(len(dictionary)):
    letter_count=string.count(para,dictionary[i])
    codebook.append([dictionary[i],letter_count])

sym_tocode=Stack()

#Stack of all alphabets and punctuations with non zero frequency in a sorted manner 
for element in codebook:
    if element[1]!=0:
        newNode=Tree(element[0]);
        newNode.freq=element[1]
        sortedInsert(sym_tocode, newNode)

#Prefix free code tree generation
while sym_tocode.size()>1:
    t1=sym_tocode.pop()
    t2=sym_tocode.pop()
    mytree=Tree('(N)', t2, t1)
    mytree.freq=t1.freq+t2.freq
    sortedInsert(sym_tocode, mytree)
print_tree_indented(sym_tocode.peek())

#Code generation for the generated tree
update_code(sym_tocode.peek(), '')

#Generating Prefix Free Code Documentation for the provided text:
wf=open('D:\Documents\UB Course\Subjects\ITC\Homework\Exercise 4\Prefix Free Code.txt','w')
create_codebook(sym_tocode.peek())
wf.close()




