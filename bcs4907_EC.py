#Benjamin Stanelle
#1001534907
#4/21/2020
#windows 10 pro x64, Python 3.7 
def main():
    fName= input("Enter the file name and extension: ")
    file1= open(fName, "r");
    lines=file1.readlines();    #reads each line and puts in list
    file1.close();
    if fName =="input_RPN_EC.txt":
        i=0
        print("Algebraic Expressions converted to RPN: ")
        for r in lines:
            i+=1
            print(i,")", end='')
            algebraicToRPN(r.split())
    elif fName == "input_RPN.txt":
        print("The RPN expressions when evaluated: ")
        for x in lines:
            calculate(x.split())        #splits on space 
            
def calculate(expr):        
    stack=[] 
    for x in expr:      #loops through each character, with spaces removed

        if x.isdigit():       #if its a digit add to the stack  
            stack.append(x)
        if x== '*':             #if not a digit pop two, which are numbers
            mult1=int(stack.pop()) #multiply second one popped * the first one popped
            mult2=int(stack.pop())
            stack.append(mult2*mult1) #append the new number to the stack
        elif x== '+':
            add1=int(stack.pop())
            add2=int(stack.pop())
            stack.append(add2+add1)
        elif x== '/':
            div1=int(stack.pop())
            div2=int(stack.pop())
            stack.append(div2/div1)
        elif x== '-':
            sub1=int(stack.pop())
            sub2=int(stack.pop())
            stack.append(sub2-sub1)
    
    print("=", int(stack.pop()))     #print the final number on the stack and empty

def algebraicToRPN(expr):   #expr is a algebraic expression with no spaces
    operators= "+-*/"       #list of operators in order of precedence; least to greatest
    postfix= ""             #result postfix string
    stack=[]
    stack.append('#')       #to check if the stack is empty, could have used stack.isEmpty()
    for x in expr:          #loop through each char in that expression
        if x.isdigit():     #if its a digit add it to the result string
            postfix+=x      
        elif x=='(':        #if open bracket add to the stack
            stack.append(x)
        elif operators.find(x) != -1:     #if its in operators string 
            #while the stack is not empty and the current opperator has less precedence
            #than the top item on the stack
            while stack[-1] != '#' and operators.find(x)<=operators.find(stack[-1]):
                    postfix+=stack[-1]  #add the top item from the stack to the result string
                    stack.pop()     #could have done postfix+= stack.pop()
            stack.append(x)     #add the operator to the stack
        elif x==')':        
            while stack[-1] != '#' and stack[-1] != '(':    #stack not empty and top of stack is not `(`
                postfix+= stack[-1]     #concatenate result string with item on top of stack
                stack.pop()     #pop stack 
            stack.pop()     #pop stack to get rid of '('
            
        else:
            continue   #if the character is not one of the specified chars, skip it
    while stack[-1] != '#':   #while stack is not empty 
        postfix+=stack[-1]    #pop the top of the stack and put in result string
        stack.pop()
    print(" ",postfix)
    calculate(postfix)      #after conversion is done, calculate(new RPN expression)
        
            
            
    

main()