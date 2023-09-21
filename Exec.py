from WaterMovement import Water
class Exec():
    def __init__(self, fileName):
        self.file = fileName
        self.map = []
        self.waterSize = 0


    def readFile(self):
        with open(self.file) as f:
            self.Coordinates = [next(f) for i in range(1)]
            self.Coordinates.append(self.Coordinates.pop().strip())
            self.waterSize = [next(f) for i in range(1, 2)]
            self.waterSize.append(self.waterSize.pop().strip())
            for line in f:
                line_list = list(line.strip('\n'))
                self.map.append(line_list)
        row, col = self.Coordinates[0].split()
        row = int(row)
        col = int(col)
        if row > len(self.map) or col > len(self.map[0]):
            exit("Invalid Starting Position")
        elif row < 0 or col < 0:
            exit("Rows and coloumns cannot be set to a value below 0")
        size = int(self.waterSize[0])
        print("Size: {0}, {1}".format(len(self.map), len(self.map[0])))
        print("Starting position: {0}, {1}".format(row, col))
        Flood = Water(self.map, size)
        Flood.printWater2(row, col)