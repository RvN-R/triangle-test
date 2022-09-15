"""Changing tactic and using a dictionarie instead of a list to create all the x,y values that make up a 8x8 matrix display
The third value is a state value, 0 LED off 1 LED is on, at default its set to 0 creating a blank matrix display"""
dict = {
    "row1": [(0,0,0), (0,1,0), (0,2,0), (0,3,0),(0,4,0), (0,5,0),(0,6,0), (0,7,0)],
    "row2": [(1,0,0), (1,1,0), (1,2,0), (1,3,0),(1,4,0), (1,5,0),(1,6,0), (1,7,0)],
    "row3": [(2,0,0), (2,1,0), (2,2,0), (2,3,0),(2,4,0), (2,5,0),(2,6,0), (2,7,0)],
    "row4": [(3,0,0), (3,1,0), (3,2,0), (3,3,0),(3,4,0), (3,5,0),(3,6,0), (3,7,0)],
    "row5": [(4,0,0), (4,1,0), (4,2,0), (4,3,0),(4,4,0), (4,5,0),(4,6,0), (4,7,0)],
    "row6": [(5,0,0), (5,1,0), (5,2,0), (5,3,0),(5,4,0), (5,5,0),(5,6,0), (5,7,0)],
    "row7": [(6,0,0), (6,1,0), (6,2,0), (6,3,0),(6,4,0), (6,5,0),(6,6,0), (6,7,0)],
    "row8": [(7,0,0), (7,1,0), (7,2,0), (7,3,0),(7,4,0), (7,5,0),(7,6,0), (7,7,0)]
}
# print(thisdict.get("row1"[1]))
# print(dict.get("row2")[0])


'''Tuple generated from a font bitmap directory'''
tuple = ((0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0,"x",80), (0, "x","F8"))


'''I've changed my approach from the master branch. I wasn't able to figure out how to iterate over gen_matrix the way I wanted. I felt I needed to use indexs to recall the correct x and y coordinate, and I couldn't figure out a way of doing that using a list so elected to use a dictionary instead.'''

'''amend_dict takes a dictionary generated above and a tuple generated from a font bitmap directory. Goal here is to loop through dictionary and tuple for the length of the dictionary itself. I've then used a if statement to change the relevant led_state values in the dictionary to 1 depending on the third value of each item in the tuple. For example if the third value is 80 then the led_state should be 1 and not 0 thus turning the LED on. amend_dict then returns an updated list of x,y and state values to pass through the set_let_state() to display the ascii characters correctly on the 8x8 led display '''

def amend_dict(dict,tuple):
    for x in range(len(dict)):
        txt = "row{}"
        row = txt.format(x + 1)
        xCoord = tuple[x][0]
        
        if tuple[x][2] == 80:
            dict[row][xCoord] = (x,xCoord,1)
        elif tuple[x][2] == "F8":
            dict[row] = [(7, 0, 1), (7, 1, 1), (7, 2, 1), (7, 3, 1), (7, 4, 1), (7, 5, 1), (7, 6, 1), (7, 7, 1)]
    return dict
amend_dict(dict,tuple)

'''Function takes the output of amend_dict and assigns x y and state data ready to mapped to 8x8 matrix display, still working this one out. Worth running function when coming back to this to figure out how best to store, x y and led_state values'''
def set_let_state(dict, tuple):
    x = []
    y = []
    led_state = []
        
    for z in range(len(dict)):
        txt = "row{}"
        row = txt.format(z+1)
        
        '''Still need to figure out how to loop throught the loops correctly'''
        
        '''Below prints out amended y value of row 2'''
        print(dict[row][2][0])
        '''Below prints  out amended x value of row 2'''
        print(dict[row][2][1])
        '''Below prints  out amended LED State value of row 2'''
        print(dict[row][2][2])
        
        '''Attempt to add assocaited values to lists above'''
        # y.append(dict[row][z][0])
        # x.append(dict[row][z][1])
        # led_state.append(dict[row][z][2])

    
    
set_let_state(dict, tuple)
