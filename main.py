import sys
import inspect
from tkinter import *
from PIL import ImageTk, Image
import threading

from world import *
import maze_generators
import solvers


if __name__ == '__main__':
    # TODO: clean up the GUI code
    global world
    global labels
    global solvers_dict
    global generators_dict

    solvers_dict = {solver.__name__: solver for solver in solvers.Solver.__subclasses__()}
    generators_dict = {name: obj for name, obj in inspect.getmembers(maze_generators, inspect.isfunction)}

    def draw_world():
        global labels
        global world
        labels = []
        for _ in world.rows:
            labels.append([Label(maze_frame) for _ in world.cols])

        for row in world.rows:
            for col in world.cols:
                labels[row][col].config(bg=Legend.color[world[Position(row, col)]])
                labels[row][col].config(width=10, height=5)
                labels[row][col].grid(row=row, column=col)

    def create_click():

        creator = Toplevel()

        maze_menu_label = Label(creator, text="Choose maze")
        maze_menu_label.configure(padx=10, pady=10)
        maze_menu_label.grid(row=0, column=0)

        solve_menu_label = Label(creator, text='Choose solver')
        solve_menu_label.configure(padx=10, pady=10)
        solve_menu_label.grid(row=1, column=0)

        maze_chosen = StringVar()
        maze_menu = OptionMenu(creator, maze_chosen, *generators_dict.keys())
        maze_menu.grid(row=0, column=1)

        solver_chosen = StringVar()
        solve_menu = OptionMenu(creator, solver_chosen, *solvers_dict.keys())
        solve_menu.grid(row=1, column=1)

        confirm_button = Button(creator, text='Confirm')
        confirm_button.configure(command=lambda: create_world(maze_chosen.get(), solver_chosen.get(), creator))
        confirm_button.grid(row=2, column=1)
        cancel_button = Button(creator, text='Cancel', command=creator.destroy)
        cancel_button.grid(row=2, column=0)

    def create_world(maze_name, solver_name, window):
        global world
        world = World(generators_dict[maze_name], solvers_dict[solver_name])
        window.destroy()
        draw_world()
        solve_button.configure(state=NORMAL)
        reset_button.configure(state=NORMAL)

    def solve_click():
        solver = threading.Thread(target=world.solve_maze, args=[labels])
        solver.start()

    def reset_click():
        global world
        world.reset()
        draw_world()

    root = Tk()
    root.title("Maze World")
    root.iconbitmap('./images/icon.ico')

    bg_image = PhotoImage('./images/background_maze.png')
    bg_label = Label(root, image=bg_image)
    bg_label.pack()

    maze_frame = LabelFrame(root, padx=40, pady=40)
    maze_frame.pack(padx=10, pady=10)

    button_frame = LabelFrame(root, padx=5, pady=5)
    button_frame.pack()

    create_button = Button(button_frame, text="New maze", command=create_click)
    create_button.configure(padx=10, pady=10, bg="#983a94")
    create_button.grid(row=0, column=0, padx=10, pady=5)

    solve_button = Button(button_frame, text="Solve!", command=solve_click)
    solve_button.configure(state=DISABLED, padx=10, pady=10, bg="#84d6e0")
    solve_button.grid(row=0, column=1, padx=10, pady=5)

    reset_button = Button(button_frame, text="Reset", command=reset_click)
    reset_button.configure(state=DISABLED, padx=10, pady=10, bg="#444444")
    reset_button.grid(row=0, column=2, padx=10, pady=5)

    root.mainloop()



