import tkinter as tk
from tkinter import filedialog, ttk, Menu
from utils.csv_utils import load_csv
from utils.image_utils import load_image
from utils.video_utils import load_video

class DataViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Viewer - data_py")
        self.root.geometry("900x600")
        self.root.configure(bg="#F5F5F5")

        # 🔹 Menu Bar
        self.menu_bar = Menu(root)
        self.root.config(menu=self.menu_bar)

        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open File(s)", command=self.open_files)
        file_menu.add_command(label="Save File", command=self.save_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # 🔹 Notebook để hiển thị nhiều loại dữ liệu trong các tab
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.dfs = {}  # Lưu trữ dữ liệu CSV theo tên file
        self.video_captures = {}  # Lưu trữ đối tượng VideoCapture

    def open_files(self):
        """ Mở nhiều file (CSV, hình ảnh, video) và hiển thị nội dung trong các tab riêng biệt """
        file_paths = filedialog.askopenfilenames(
            filetypes=[("CSV Files", "*.csv"), ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("Video Files", "*.mp4 *.avi *.mkv")]
        )
        if not file_paths:
            return

        for file_path in file_paths:
            if file_path.lower().endswith(".csv"):
                self.dfs[file_path] = load_csv(file_path, self.notebook)
            elif file_path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                load_image(file_path, self.notebook)
            elif file_path.lower().endswith((".mp4", ".avi", ".mkv")):
                load_video(file_path, self.notebook, self.video_captures)

    def save_csv(self):
        """ Lưu file CSV đang được chọn trong tab hiện tại """
        current_tab = self.notebook.select()
        if not current_tab:
            return

        tab_text = self.notebook.tab(current_tab, "text")
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.dfs[tab_text].to_csv(file_path, index=False)

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = DataViewerApp(root)
    root.mainloop()