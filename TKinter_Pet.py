from tkinter import *
display = Tk()
display.geometry("500x500")
icon = BitmapImage(file=r"C:\NavObjectEdit\peaky-pro\Python\resources\Ball 4 Stars.ico")
display.iconbitmap(True, icon)

display.title("Pet Habit")
display.config(background= "skyblue")
frame = Frame(display, background="white", width=300, height=300)
frame.pack(pady=30)
frame.pack_propagate(False)

gif_image = PhotoImage(file=r"C:\NavObjectEdit\peaky-pro\Python\resources\piccolo-440-161921.mp4")
gif_label = Label(frame, image=gif_image, background= "white")
gif_label.pack(expand=True)

frames = []
i = 0
try:
    while True:
        gif = PhotoImage(
            file=r"C:\NavObjectEdit\peaky-pro\Python\resources\piccolo-440-161921.mp4",
            format=f"gif -index {i}"
        )
        frames.append(gif)
        i += 1
except TclError:
    pass
frame_index = 0
def animate():
    global frame_index
    gif_label.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    display.after(100, animate)
if frames:
    animate()
else:
    print("GIF not loaded")               
                     
display.mainloop()