import PyPDF2
import customtkinter
import os
from PIL import Image
from CTkMessagebox import CTkMessagebox

merger = PyPDF2.PdfMerger()
file_array = []


def open_file(frame_file):
    frame_file.after(0, lambda: delayed_open_file(frame_file))


def delayed_open_file(frame_file):
    file_path = customtkinter.filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF files", "*.pdf")],
    )

    if len(file_path) != 0:
        file_array.append(file_path)
        update_file_labels(frame_file)


def update_file_labels(frame_file):
    for widget in frame_file.winfo_children():
        widget.destroy()

    for i, file_path in enumerate(file_array):
        file_name = os.path.basename(file_path)
        label_text = f"{file_name}"

        label = customtkinter.CTkLabel(frame_file, text=label_text)
        label.grid(row=i, column=0, pady=3, sticky="new", ipadx=10, ipady=5)

        delete_btn = customtkinter.CTkButton(
            frame_file,
            width=20,
            height=20,
            text="",
            image=delete_icon,
            fg_color="#fc0303",
            hover_color="#960000",
            command=lambda idx=i: delete_file(idx, frame_file),
        )
        delete_btn.grid(
            row=i, column=1, pady=3, padx=5, sticky="nsew", ipadx=5, ipady=2
        )

    for i in range(len(file_array)):
        frame_file.grid_rowconfigure(i, weight=1)


def delete_file(index, frame_file):
    del file_array[index]
    update_file_labels(frame_file)


def open_location_output():
    output_path = customtkinter.filedialog.askdirectory()

    if len(output_path) != 0 and len(file_array) > 0:
        merge_pdfs(output_path)


def merge_pdfs(output_path):
    for file in file_array:
        merger.append(file)

    output = f"{output_path}/output.pdf"
    merger.write(output)
    CTkMessagebox(
        message="Merger PDF successfully",
        icon="check",
        option_1="OK",
    )


delete_icon = customtkinter.CTkImage(
    dark_image=Image.open(
        os.path.join(os.path.dirname(__file__), "assets/delete_icon.png")
    ),
    size=(15, 15),
)
