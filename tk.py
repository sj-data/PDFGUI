import tkinter as tk
from tkinter import filedialog
import os
from PyPDF2 import PdfReader, PdfWriter


# Create the main window
window = tk.Tk()
window.title("PDF tools")

# Create a label
label = tk.Label(text="Split, Merge, or Resize your PDF file")
label.pack()

def split_pdf(file_path):
    # Open the PDF file
    with open(file_path, "rb") as f:
        # Create a PDF file reader
        reader = PdfReader(f)
        # Get the number of pages in the file
        num_pages = len(reader.pages)
        # Iterate over the pages
        for i in range(num_pages):
            # Create PDF file writer
            writer = PdfWriter()
            # Get the i-th page
            page = reader.pages[i]
            # Add the page to the writer
            writer.add_page(page)
            # Generate a name for the page
            page_file_name = f"page{i+1}.pdf"
            # Create a new file for the page
            with open(page_file_name, 'wb') as page_f:
                # Write the page to the file
                writer.write(page_f)
            # Close the file
            page_f.close()
        #close original file
        f.close()
    
def on_browse_button_click():
  # This function will be called when the button is clicked
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    file_label.configure(text=file_path)
    run_button.configure(state="normal")

def on_run_button_click():
    # Called when run button clicked
    # Get the file path from the file label
    file_path = file_label.cget("text")
    #run the Python process on the selected file
    if file_path:
        split_pdf(file_path)
    else:
        print("no file selected")
        

# Create button to open file dialog
browse_button = tk.Button(text="Select PDF",
command=on_browse_button_click)
browse_button.pack()

# Create a label to display the selected file path
file_label = tk.Label(text="No file selected")

# Create a button
run_button = tk.Button(text="Split PDF", command=on_run_button_click)
run_button.pack()

# Run the main loop
window.mainloop()
