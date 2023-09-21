class Water():
    def __init__(self, groundMap :list[list[str]], waterSize :int):
        self.map = groundMap
        self.waterMarkedMap = groundMap
        self.waterSize = waterSize-1


    def isMoveable(self, row :int, col :int) -> bool:
        '''Checks if the next position is a " " if it is returns True, if not returns False'''
        #print(row <= len(self.map) and col <= len(self.map[0]) and self.waterMarkedMap[row][col] == " ")
        return(row <= len(self.map) and col <= len(self.map[0]) and self.waterMarkedMap[row][col] == " ")

    def waterMovement(self, row :int, col :int):
        '''The recursive function going to modify waterMarkedMap by marking where the water moved with ~'''


        if (row == len(self.map) and col == len(self.map) and self.waterMarkedMap[row][col] == "~"):
            return True

        if self.isMoveable(row, col):
            self.waterMarkedMap[row][col] = "~"
            if self.waterSize == 0:
                return True
            self.waterSize -= 1

            #Look up
            if self.waterMovement(row+1, col):
                return True
            #Look right
            if self.waterMovement(row, col+1):
                return True
            #Look down
            if self.waterMovement(row-1, col):
                return True
            #Look left
            if self.waterMovement(row, col-1):
                return True
            
            return False
        
        return False
    
    def printWater2(self, row :int, col :int) -> list:
        if self.waterMovement(row, col):
            for i in self.waterMarkedMap:
                print(i)
            print("Flood Complete")
            return self.waterMarkedMap
        else:
            for i in self.waterMarkedMap:
                print(i)
            print("Flood Complete")
            return None