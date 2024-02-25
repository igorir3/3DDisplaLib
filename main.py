from tkinter import Tk, Canvas, PhotoImage, mainloop
import math
import time
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

class xyMatrix():
    def __init__(self, x_max : int = 320, y_max : int = 320):
        self.x_max, self.y_max = x_max, y_max
        self.datamatrix = []
        for i in range(x_max):
            tempmatrix = []
            for j in range(y_max):
                tempmatrix.append(None)
            self.datamatrix.append(tempmatrix)
    def get(self, x : int, y : int):
        return self.datamatrix[x][y]
    def set(self, x : int, y : int, data):
        self.datamatrix[x][y] = data
    def clear(self):
        self.datamatrix = []
        for i in range(self.x_max):
            tempmatrix = []
            for j in range(self.y_max):
                tempmatrix.append(None)
            self.datamatrix.append(tempmatrix)
    def append(self, data, overflow_mode : str = "error"):
        for y in range(self.y_max):
            for x in range(self.x_max):
                if self.datamatrix[x][y] != None:
                    self.datamatrix[x-1][y] = data
                    return
        if overflow_mode == "error":
            raise ValueError("Overflow!")
        elif overflow_mode == "ignore":
            return
        elif overflow_mode == "strerror":
            return "Overflow"
        elif overflow_mode == "del":
            self.datamatrix[self.x_max-1][self.y_max-1] = data
        else:
            raise ValueError("Uncorectable overflow mode!")
    def str(self):
        return_str = ""
        for y in range(self.y_max):
            for x in range(self.x_max):
                if self.datamatrix[x][y] != None:
                    return_str = return_str + f" '{str(self.datamatrix[x][y])}' "
                else:
                    return_str = return_str + " "
        return_str = return_str + "\n"   
                
            
class display2D():
    def __init__(self, width : int = 320, height : int = 320, division_widht : int = 320, division_height : int = 320, display_mode : str = "normal", data_mode : str = "display"):
        self.WIDTH, self.HEIGHT = width, height
        self.division_widht, self.division_height = division_widht, division_height
        self.display_mode = display_mode
        self.data_mode = data_mode
        
        self.x_mod = self.WIDTH / self.division_widht
        self.y_mod = self.HEIGHT / self.division_height

        self.window = Tk()
        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg="#000000")
        self.canvas.pack()
        img = PhotoImage(width=self.WIDTH, height=self.HEIGHT)
        self.canvas.create_image((self.WIDTH/2, self.HEIGHT/2), image=img, state="normal")
        
        if data_mode == "display":
            self.data = xyMatrix(self.division_widht, self.division_height)
        if data_mode == "coordinates":
            self.data = []

    def update(self, fos : bool = False, fd : float = 0):
        if self.data_mode == "display":
            img = PhotoImage(width=self.WIDTH, height=self.HEIGHT)
            self.canvas.create_image((self.WIDTH/2, self.HEIGHT/2), image=img, state="normal")
            for x in range(self.division_widht):
                for y in range(self.division_height):
                    dt = self.data.get(x, y)
                    if dt != None:
                        if type(dt) == bool:
                            if dt == True:
                                img.put("#ffffff", (int(x * self.x_mod), int(y * self.y_mod)))
                                if self.x_mod > 1 or self.y_mod > 1:
                                    for o in range(int(self.x_mod) + 1):
                                        for p in range(int(self.y_mod) + 1):
                                            x_temp = (int(x * self.x_mod) - int(self.x_mod)) + o
                                            if x_temp < 0:
                                                x_temp = 0
                                            if x_temp > self.WIDTH:
                                                x_temp = self.WIDTH
                                            y_temp = (int(y * self.y_mod) - int(self.y_mod)) + p
                                            if y_temp < 0:
                                                y_temp = 0
                                            if y_temp > self.HEIGHT:
                                                y_temp = self.HEIGHT
                                            img.put("#ffffff", (x_temp, y_temp))
                        elif type(dt) == int:
                            if dt > 255:
                                dt = 255
                            if dt > 0:
                                img.put(f"#{rgb_to_hex((dt, dt, dt))}", (int(x * self.x_mod), int(y * self.y_mod)))
                        elif type(dt) == float:
                            if dt > 1:
                                dt = 1.0
                            if dt > 0:
                                img.put(f"#{rgb_to_hex((255 * dt, 255 * dt, 255 * dt))}", (int(x * self.x_mod), int(y * self.y_mod)))
                        elif type(dt) == tuple:
                                img.put('#%02x%02x%02x' % dt, (int(x * self.x_mod), int(y * self.y_mod)))
                        if fos:
                            self.window.update()
                        if fd > 0:
                            time.sleep(fd)
            if not(fos):
                self.window.update()
    
    def setMatrix(self, matrix):
        self.data = matrix
    def getMatrix(self):
        return self.data
            
            
size = 10000
disp = display2D(width=1000, height=1000, division_widht = size, division_height = size)
while True:
    matrix = disp.getMatrix()
    data = []
    for i in range(size):
        matrix.set(i, int((size // 2) + (4096 * math.sin(i))), True)
        matrix.set(i, int((size // 2) + (4096 * math.cos(i))), True)
        matrix.set(i, size // 2, True)
        
        
    disp.setMatrix = matrix
    disp.update(fos=False)