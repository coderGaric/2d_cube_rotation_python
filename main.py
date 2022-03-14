from art import logo

class RotateCube:
    init_cube = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    def __init__(self):
        self.cube = self.init_cube
        self.length = len(self.cube)

    def form(self, cube):
        str = f"\n-------------"
        for i in range(len(cube)):
            str += "\n|"
            for j in range(len(cube)):
                str += f" {cube[i][j]} |"
            str += "\n-------------"
        return str + "\n"

    def changePosition(self):
        new_form = [list() for _ in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                new_form[i].append(self.cube[j][i])
        return new_form

    def start(self):
        return self.form(self.cube)

    def clockwise(self):
        new_form = self.changePosition()
        for i in range(self.length):
            new_form[i].reverse()
        self.cube = new_form
        return self.form(self.cube)

    def counter_clockwise(self):
        new_form = self.changePosition()
        new_form.reverse()
        self.cube = new_form
        return self.form(self.cube)
        
    def on(self):
        print(logo)
        print("^" * 35)
        print(self.start())
        print("Intruction:\n1 - rotate clockwise\n2 - rotate counter clockwise\n3 - exit")
        print("\n" + "^" * 35 + "\n")
        
        choice = False
        while not choice :
            turn = input("Your choice: ")
            if turn == "1":
                print(self.clockwise())
            elif turn == "2":
                print(self.counter_clockwise())
            elif turn == "3":
                print("\n" + "^" * 35 + "\n")
                print("Bye!")
                choice = True
                

cube = RotateCube()
cube.on()