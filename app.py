import customtkinter
import utils

customtkinter.deactivate_automatic_dpi_awareness()

app = customtkinter.CTk()
app.geometry("600x400")
app.title("PDF Merge")

title = customtkinter.CTkLabel(
    app,
    text="PDF Merge",
    fg_color="transparent",
    font=customtkinter.CTkFont(size=20, weight="bold"),
)
title.grid(row=0, column=0, columnspan=2, pady=20, sticky="new")

frame_file = customtkinter.CTkFrame(master=app, width=200, height=40)
frame_file.grid(row=1, column=0, rowspan=2, padx=20, sticky="new")

frame_file.grid_columnconfigure(0, weight=1)

frame_btn = customtkinter.CTkFrame(master=app)
frame_btn.grid(row=1, column=1, padx=20, sticky="new")


def browser_file():
    utils.open_file(frame_file)


browser_btn = customtkinter.CTkButton(
    frame_btn,
    text="Browser File",
    command=browser_file,
)
browser_btn.pack(pady=10)

merge_btn = customtkinter.CTkButton(
    frame_btn,
    text="Merge",
    fg_color="#ff6600",
    hover_color="#963c00",
    command=utils.open_location_output,
)
merge_btn.pack(pady=10)

app.grid_columnconfigure(0, weight=6)
app.grid_columnconfigure(1, weight=1)

app.mainloop()
