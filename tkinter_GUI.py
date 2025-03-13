from customtkinter import *

app = CTk() # Main Window
app.geometry("400x400") # Window Size

label = CTkLabel(app, text="Hello World!") # Label Widget
label.pack(pady=20) # Vertical Padding

button = CTkButton(app, text="Click Me!", command=lambda: label.configure(text="Button Clicked!")) # Create Button, Update
button.pack(pady=20) # Vertical Padding

app.mainloop()