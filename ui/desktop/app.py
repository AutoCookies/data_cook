from gui import DataViewerApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = DataViewerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
