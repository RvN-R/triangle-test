'''gen_matrix returns a list that contains all the x,y values that make up a 8x8 matrix display. 
The third value is a state value, 0 LED off 1 LED is on, at default its set to 0 creating a blank matrix display'''

def gen_matrix():
    plot = 8
    list = []
    for x in range(plot):
        for y in range(plot):
            list.append((x,y,0))
    
    return list
 
'''Unsure if this is nessary but I've created a variable called gen_matrix allowing me to interate over the list created in gen_matrix function'''
gen_matrix = gen_matrix()

'''below is a print statement that illustrates the x,y and LED state values that make up an 8x8 matrix display'''
print(gen_matrix)


'''amend_matrix takes a tuple generated from a font bitmap directory. Goal here is to loop through the tuple and change the relevant state values created in gen_matrix function to 1 turning the LED on, depending on the third value of each item in the tuple. For example the third value is 80 so state of LED for the x and y coordinate assocaited with 80 should be 1 and not 0. amend_matrix then returns an updated list of x,y and state values to pass through the set_let_state() API call to display the ascii character '''

'''I've began the process below but I wasn't able to figure out how to iterate over gen_matrix the way I wanted. I would need to use indexs to recall the correct x and y coordinate, and I couldn't figure out a way of doing that. I think in highsight I should of used a dictionarie in gen_matrix function instead of settling on using a list containing all the x,y values that make up a 8x8 matrix display. This would be easier for me to iternate over in amend_matrix using a for loop'''

def amend_matrix(tuple):
    # print(tuple)
    # print(gen_matrix[1])
    for x in range(len(tuple)):
        if tuple[x][2] == 80:
            print("LED ON")
        else:
            print("LED OFF")
    
    
amend_matrix(((0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0, "x","F8")))