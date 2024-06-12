import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Veri dosyasını yükle
data = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")

# Ana pencere oluştur
root = tk.Tk()
root.title("Data Table Interface")
root.geometry("400x250")  # Ana pencerenin boyutunu ayarla

# Çerçeve oluştur
frame = ttk.Frame(root, width=400, height=250)
frame.pack_propagate(False)  # Çerçevenin boyutunu içeriğine göre değiştirmeyi durdur
frame.pack(padx=50, pady=50)  # Çerçevenin etrafına biraz boşluk ekle

# Veri tablosunu gösteren bir fonksiyon
def show_data_table():
    # Veri tablosu penceresi oluştur
    data_table_window = tk.Toplevel(root)
    data_table_window.title("Data Table")

    # Veri tablosu widget'ını oluştur
    data_table = ttk.Treeview(data_table_window)
    data_table.pack(fill="both", expand=True)

    # Sütunlar için başlık ayarlayın (Geçersiz sütunları atla)
    valid_columns = [col for col in data.columns if col != "Unnamed: 0"]
    data_table["columns"] = valid_columns
    for col in valid_columns:
        data_table.heading(col, text=col)

    # Veriyi tabloya ekle
    for index, row in data.iterrows():
        # Geçersiz sütunu atla
        values = [row[col] for col in valid_columns]
        data_table.insert("", "end", values=values)

# Eksik değer işleyici butonu için fonksiyon
def handle_missing_values():
    messagebox.showinfo("Info", "Missing value handler clicked!")

# "Show Data Table" butonunu oluştur
show_data_button = ttk.Button(frame, text="Show Data Table", command=show_data_table)
show_data_button.pack(pady=10)  # Dikey boşluk ekle

# "Missing Value Handler" butonunu oluştur
missing_value_button = ttk.Button(frame, text="Missing Value Handler", command=handle_missing_values)
missing_value_button.pack(pady=10)  # Dikey boşluk ekle

# Pencereyi çalıştır
root.mainloop()
