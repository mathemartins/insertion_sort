class UndoRedo:
    def __init__(self):
        self.history = []
        self.current_state = []

    def do(self, data):
        self.history = []
        self.current_state = data.copy()

    def undo(self):
        if self.history:
            self.current_state = self.history.pop()

    def redo(self):
        if self.history:
            self.history.pop()  # Remove the current state from history
        if self.history:
            self.current_state = self.history[-1]

    def currentstate(self):
        return self.current_state


# Demonstrate UndoRedo behavior
def demonstrate_undo_redo():
    undo_redo = UndoRedo()
    initial_list = [5, 3, 2.1, 4.8]
    print("Initial List:", initial_list)

    undo_redo.do(initial_list)
    initial_list.sort()
    print("Sorted List:", initial_list)

    undo_redo.do(initial_list)
    initial_list.reverse()
    print("Reversed List:", initial_list)

    undo_redo.do(initial_list)
    initial_list.append(9)
    print("List with 9 added:", initial_list)

    undo_redo.undo()
    print("Undo to Reversed List:", undo_redo.currentstate())

    undo_redo.do(undo_redo.currentstate())
    initial_list.append(9)
    print("List with 9 added again:", initial_list)

    undo_redo.undo()
    print("Undo back to the original state:", undo_redo.currentstate())


demonstrate_undo_redo()
