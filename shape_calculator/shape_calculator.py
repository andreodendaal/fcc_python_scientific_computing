class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.area = 0
        self.perimeter = 0
        self.diagonal = 0

    
    def __str__(self) -> str:
        # if an instance of a Rectangle is represented as a string, it should look like: 
        # Rectangle(width=5, height=10)
        return_string = "Rectangle(width={0}, height={1})".format(self.width, self.height) 
        return return_string       

    def set_width(self, width):
        self.width = width

    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        # area (width * height)
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        # Returns perimeter (2 * width + 2 * height) 
        self.perimeter = (2 * self.width + 2 * self.height)
        return self.perimeter
    
    def get_diagonal(self):
        # Returns diagonal ((width ** 2 + height ** 2) ** .5) 
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return self.diagonal
    
    def get_picture(self): 
        # Returns a string that epresents the shape using lines of "*". 
        # The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. 
        # There should be a new line (\n) at the end of each line. 
        # If the width or height is larger than 50, this should return the string: "Too big for picture.".

        if self.height > 50 or self.width >50:
            return_string = "Too big for picture."
            return return_string
        
        self.matrix_height = self.height
        self.matrix_width = self.width

        matrix = [['*' for x in range(self.matrix_width)] for x in range(self.matrix_height)]
        x=0
        return_string = ''
        for x in range(self.matrix_height):    
            line = ''
            for y in range(self.matrix_width):
                value = matrix[x][y]       
                line = line + value 

            line = line + '\n'
            return_string = return_string + line

        return return_string
        

    def get_amount_inside(self, shape):
        # Takes another shape (square or rectangle) as an argument. 
        # Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
        # For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.\
        area_self = self.get_area()
        area_shape = shape.get_area()
        number_inside = area_self//area_shape 
        return number_inside


class Square(Rectangle):
    def __init__(self, width, height=0):
        super().__init__(width, height=width)
        self.width = width
        self.height = width
        self.side = self.width
    
    def __str__(self) -> str:
        # if an instance of a Rectangle is represented as a string, it should look like: 
        # Rectangle(width=5, height=10)
        return_string = "Square(side={0})".format(self.width) 
        return return_string

    def set_side(self, side):
        #self.side = side
        self.width = side
        self.height = side

