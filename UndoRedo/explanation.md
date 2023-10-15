Code Explanation

**Introduction:**
- We have a Python class called `UndoRedo` that represents an "Undo-Redo" functionality, like the feature you find in text editors or image editing applications. It allows us to keep track of changes to data and undo or redo those changes.

**Initialization:**
- In the `__init__` method, we set up the initial state of the `UndoRedo` object.
- We have two essential attributes: `history` and `current_state`.
- `history` is an empty list that will store previous states of the data.
- `current_state` is also initialized as an empty list, representing the current state of the data.

**Doing an Action (do method):**
- The `do` method is used to perform an action, which can be thought of as making a change to our data. It takes a parameter called `data` that represents the new state of the data.
- When an action is performed using the `do` method, it resets the `history` by setting it to an empty list.
- It also updates the `current_state` to the new data. It essentially saves the new state of the data.

**Undoing an Action (undo method):**
- The `undo` method allows us to go back one step in time to a previous state of the data.
- It checks if there's anything in the `history`. If there is, it means there's something to undo.
- It takes the last item from the `history` (the most recent past state) and sets it as the `current_state`.

**Redoing an Action (redo method):**
- The `redo` method helps us move forward in time to a state we were at just before undoing.
- It first checks if there's anything in the `history`. If there is, it removes the last item from the `history` (which is the current state we're in) to prepare for redoing.
- If there's another state left in the `history` (meaning we have undone at least once before), it sets the `current_state` to the last item in the `history`.

**Getting the Current State (currentstate method):**
- The `currentstate` method simply returns the current state of the data.

**Demonstration:**
- We demonstrate how this works by creating an instance of the `UndoRedo` class.
- We start with an initial list: `[5, 3, 2.1, 4.8]`.
- We perform several actions like sorting and reversing the list and adding elements.
- At each step, we can undo and redo to see how the data changes, and we print the current state of the data to observe the effects of undo and redo operations.

**Conclusion:**
- In summary, the `UndoRedo` class is a useful tool for tracking and managing changes to data, making it easy to undo or redo actions, similar to how we can revert or replay changes in text or image editing applications.