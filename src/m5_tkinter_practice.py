"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Patrick Vedova.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    stuff = tkinter.Tk()
    # ------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(stuff, padding=20)
    frame1.grid()

    # ------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    button = ttk.Button(frame1, text='button')
    button.grid()


    # ------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button['command'] = (lambda: print('Hello'))


    # ------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entry_box = ttk.Entry(frame1)
    entry_box.grid()

    button_2 = ttk.Button(frame1, text='button_2')
    button_2.grid()

    def function1(entry):
        if entry.get() == 'ok':
            print('Hello')
        else:
            print('Goodbye')


    button_2['command'] = (lambda: function1(entry_box))

    # ------------------------------------------------------------------
    # Done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry_box2 = ttk.Entry(frame1)
    entry_box2.grid()

    button_3 = ttk.Button(frame1, text='button_3')
    button_3.grid()

    def function2(entry1, N):
        value1 = entry1.get()
        value2 = int(N.get())
        for k in range(value2):
            print(value1)

    button_3['command'] = (lambda: function2(entry_box, entry_box2))


    # ------------------------------------------------------------------
    # Done: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    stuff.mainloop()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
