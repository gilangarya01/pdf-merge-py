import PySimpleGUI as sg
import PyPDF2

file_types = [("PDF (*.pdf)", "*.pdf")]
merger = PyPDF2.PdfMerger()

def main():
    layout = [
        [
            sg.Text("PDF 1"),
            sg.Input(key="-FILE1-", do_not_clear=False),
            sg.FileBrowse(file_types=file_types),
        ],
        [
            sg.Text("PDF 2"),
            sg.Input(key="-FILE2-", do_not_clear=False),
            sg.FileBrowse(file_types=file_types),
        ],
        [
            sg.Text("Nama Output"),
            sg.Input(key="-OUTPUT-", do_not_clear=False),
        ],
        [
            sg.Button("Merge"),
        ]
    ]

    window = sg.Window("Merge PDF", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Merge":
            files = [values["-FILE1-"], values["-FILE2-"]]

            for file in files:
                merger.append(file)
            
            new_file = f"output/{values['-OUTPUT-']}.pdf"
            merger.write(new_file)

    window.close()

if __name__ == "__main__":
    main()
