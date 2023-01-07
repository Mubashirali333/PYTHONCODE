# "Quene"
# enquene add an item to the quene
# dequene remove an item form the element
#front get the front item
#rear get the last item

# l =[]
# while True:
#     c = int(input('''
#                  1 : Enquene
#                  2 : Dequene
#                  3 : Front
#                  4 : Rear
#                  5 : Display
#                  6 : Exit   :'''))
#     if c == 1:
#         n=input("Enter value : ")
#         l.append(n)
#         print(l)
#     elif c==2:
#         if len(l) ==0:
#             print("Empty Quene ")
#         else:
#             del l[0]
#     elif c==3:
#         print("Front value is ",l[0])
#     elif c==4:
#         print("Rear value is ",l[-1])    
#     elif c==5:
#         print("Display ",l)
#     elif c==6:
#         break
#     else:print("Invlaid")       

l=[]

while True:
    c=int(input('''
                  1 : Enquene
                  2 : Dequene 
                  3 : Front
                  4 : Rear
                  5 : Display
                  6 : Exit         :'''))
    if c==1:
        n=input("Enter value : ")
        l.append(n)
        print(l)
    elif c==2:
        del l[0]
    elif c==3:
        print("Front value is ",l[0])
    elif c==4:
        print("Rear value is ",l[-1])
    elif c==5:
        print("Display value is ",l)
    elif c==6:
        break        

