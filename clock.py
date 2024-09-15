import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)

# Function to update the clock
def update_clock():
    current_time = time.strftime("%H:%M:%S %p")  # Format the time as HH:MM:SS AM/PM
    label.config(text=current_time)  # Update the label with the current time
    label.after(1000, update_clock)  # Call the update_clock function every second (1000 ms)

# Create a label to display the time
label = tk.Label(root, text="", font=("Helvetica", 48), bg="black", fg="cyan")
label.pack(expand=True)

# Start updating the clock
update_clock()

# Start the Tkinter event loop
root.mainloop()

