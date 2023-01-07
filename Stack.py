# Stack

# push : insert an element
# pop : delete an last element
# peek : display last element
# display dislay list


# l=[]

# while True:
#     c=int(input('''
#                 1 : Push
#                 2 : Pop
#                 3 : Peek
#                 4 : Display
#                 5 : Exit :'''))
#     if c==1:
#         n=input("Enter value : ")
#         l.append(n)
#         print(l)
#     elif c==2:
#         if len(l)==0:
#             print("Empty stack")
#         else:l.pop()
#     elif c==3:       
#         if len(l)==0:
#             print("Emppty stack")
#         else:
#             print("Peek value is ",l[-1])
#     elif c==4:
#         print("Display value is ",l)
#     elif c==5:
#         break                 
#     else:
#         print("Invalid")


l=[]

while True:
    c=int(input('''
                   1 : Push
                   2 : Pop
                   3 : Peek
                   4 : Display
                   5 : Exit    '''))

    if c==1:
        n=input("Enter value : ")
        l.append(n)
    elif c==2:
        l.pop()
    elif c==3:
        print("Peek value is ",l[-1])
    elif c==4 :
        print("Display is ",l)
    elif c==5:
        break
    else:
        print("Invalid ")                               