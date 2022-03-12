class RotateCube:
    init_cube = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    def __init__(self):
        self._cube = self.init_cube
        self._length = len(self._cube)

    def form(self, cube, turn):
        str = f"{turn}\n-------------"
        for i in range(len(cube)):
            str += "\n|"
            for j in range(len(cube)):
                str += f" {cube[i][j]} |"
            str += "\n-------------"
        return str + "\n"

    def __changePosition(self):
        new_form = [list() for _ in range(self._length)]
        for i in range(self._length):
            for j in range(self._length):
                new_form[i].append(self._cube[j][i])
        return new_form

    def start(self):
        return self.form(self._cube, "initial position")

    def clockwise(self):
        new_form = self.__changePosition()
        for i in range(self._length):
            new_form[i].reverse()
        self._cube = new_form
        return self.form(self._cube, "after clockwise turn")

    def counter_clockwise(self):
        new_form = self.__changePosition()
        new_form.reverse()
        self._cube = new_form
        return self.form(self._cube, "afer counter clockwise turn")
        

cube = RotateCube()
print(cube.start())
print(cube.clockwise())
print(cube.counter_clockwise())
print(cube.counter_clockwise())
print(cube.counter_clockwise())
print(cube.counter_clockwise())
print(cube.counter_clockwise())

print(cube.start())
print(cube.counter_clockwise())
print(cube.clockwise())
print(cube.clockwise())
print(cube.clockwise())
print(cube.clockwise())
print(cube.clockwise())


