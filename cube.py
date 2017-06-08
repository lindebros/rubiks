# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:21:42 2017

@author: minit
"""

#cube color is determined by a [6*3][3]
# white, yellow, blue, green, orange, red
# color neighbors: (starting from top clockwise)
    # white: blue, red, green, orange
    # red: white, blue, yellow, green
    # yellow: blue, orange, green, red
    # orange: white, green, yellow, green
    # green: white, red, yellow, orange
    # blue: white, red, yellow, red

class Cube:
    colors = []
    
    def __init__(self):
        global colors
        for i in range(6*3):
            self.colors.append([int(i/3),int(i/3),int(i/3)])
        
        print(self.colors)
    
    def reset(self):
        global colors
        for i in range(6*3):
            self.colors[i] = [int(i/3),int(i/3),int(i/3)]
        print(self.colors)
    
    def rotateFace(self,i):
        #change corners
        tmp = self.colors[i][0]
        self.colors[i][0] = self.colors[i+2][0]
        self.colors[i+2][0] = self.colors[i+2][2]
        self.colors[i+2][2] = self.colors[i][2]
        self.colors[i][2] = tmp
        
        #change edges
        tmp = self.colors[i][1]
        self.colors[i][1] = self.colors[i+1][0]
        self.colors[i+1][0] = self.colors[i+2][1]
        self.colors[i+2][1] = self.colors[i+1][2]
        self.colors[i+1][2] = tmp       
        
    
    def white(self):
        print("white")
        
        #Change white face 
        self.rotateFace(0)        
        
        #Change other faces
        tmp = self.colors[6]
        self.colors[6] = self.colors[12]
        self.colors[12] = self.colors[9]
        self.colors[9] = self.colors[15]
        self.colors[15] = tmp
        
        print(self.colors)
        
        
    def yellow(self):
        print("yellow")
        
        #change yellow face
        self.rotateFace(3)
        
        #change other faces
        tmp = self.colors[8]
        self.colors[8] = self.colors[17]
        self.colors[17] = self.colors[11]
        self.colors[11] = self.colors[14]
        self.colors[14] = tmp
        
        print(self.colors)
        
    def blue(self):
        print("blue")
        #change blue face
        self.rotateFace(6)
        
        #Change other faces
        tmp1 = self.colors[0][0]
        tmp2 = self.colors[0][1]
        tmp3 = self.colors[0][2]
        
        self.colors[0][0] = self.colors[15][2]
        self.colors[15][2] = self.colors[3][0]
        self.colors[3][0] = self.colors[14][0]
        self.colors[14][0] = tmp1
        
        self.colors[0][1] = self.colors[16][2]
        self.colors[16][2] = self.colors[3][1]
        self.colors[3][1] = self.colors[13][0]
        self.colors[13][0] = tmp2
        
        self.colors[0][2] = self.colors[17][2]
        self.colors[17][2] = self.colors[3][2]
        self.colors[3][2] = self.colors[12][0]
        self.colors[12][0] = tmp3
    
        
        print(self.colors)
        
    def green(self):
        print("green")
        #change green face
        self.rotateFace(9)
        
        #change other faces
        tmp1 = self.colors[2][0]
        tmp2 = self.colors[2][1]
        tmp3 = self.colors[2][2]
        
        self.colors[2][0] = self.colors[14][2]
        self.colors[14][2] = self.colors[5][0]
        self.colors[5][0] = self.colors[15][0]
        self.colors[15][0] = tmp1
        
        self.colors[2][1] = self.colors[13][2]
        self.colors[13][2] = self.colors[5][1]
        self.colors[5][1] = self.colors[16][0]
        self.colors[16][0] = tmp2
        
        self.colors[2][2] = self.colors[12][2]
        self.colors[12][2] = self.colors[5][2]
        self.colors[5][2] = self.colors[17][0]
        self.colors[17][0] = tmp3
    
        print(self.colors)
        
        
    def orange(self):
        print("orange")
        
        #change orange face
        self.rotateFace(12)
        
        #change other faces
        tmp1 = self.colors[0][0]
        tmp2 = self.colors[1][0]
        tmp3 = self.colors[2][0]
        
        self.colors[0][0] = self.colors[8][2]
        self.colors[8][2] = self.colors[5][2]
        self.colors[5][2] = self.colors[11][0]
        self.colors[11][0] = tmp1
        
        self.colors[1][0] = self.colors[7][2]
        self.colors[7][2] = self.colors[4][2]
        self.colors[4][2] = self.colors[10][0]
        self.colors[10][0] = tmp2
        
        self.colors[2][0] = self.colors[6][2]
        self.colors[6][2] = self.colors[3][2]
        self.colors[3][2] = self.colors[9][0]
        self.colors[9][0] = tmp3
        
        print(self.colors)
        
    def red(self): 
        print("red")
        
        #change red face
        self.rotateFace(15)
        
        #change other faces
        tmp1 = self.colors[0][2]
        tmp2 = self.colors[1][2]
        tmp3 = self.colors[2][2]
        
        self.colors[0][2] = self.colors[9][2]
        self.colors[9][2] = self.colors[5][0]
        self.colors[5][0] = self.colors[8][0]
        self.colors[8][0] = tmp1
        
        self.colors[1][2] = self.colors[10][2]
        self.colors[10][2] = self.colors[4][0]
        self.colors[4][0] = self.colors[7][0]
        self.colors[7][0] = tmp2
        
        self.colors[2][2] = self.colors[11][2]
        self.colors[11][2] = self.colors[3][0]
        self.colors[3][0] = self.colors[6][0]
        self.colors[6][0] = tmp3
        
        print(self.colors)