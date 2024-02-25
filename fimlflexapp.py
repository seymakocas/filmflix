import sqlite3
import tkinter as tk
from tkinter import messagebox

# Veritabanı bağlantısı oluşturma
conn = sqlite3.connect('filmflix.db')
c = conn.cursor()

# CRUD işlevleri
def add_record():
    title = input("Enter the title of the film: ")
    year_released = input("Enter the year the film was released: ")
    rating = input("Enter the rating of the film: ")
    duration = input("Enter the duration of the film (in minutes): ")
    genre = input("Enter the genre of the film: ")
    
    c.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)", (title, year_released, rating, duration, genre))
    conn.commit()
    messagebox.showinfo("Success", "Record added successfully.")

def delete_record():
    record_id = input("Enter the ID of the record to delete: ")
    c.execute("DELETE FROM tblfilms WHERE filmID=?", (record_id,))
    conn.commit()
    messagebox.showinfo("Success", "Record deleted successfully.")

def update_record():
    record_id = input("Enter the ID of the record to update: ")
    new_title = input("Enter the new title of the film: ")
    new_year_released = input("Enter the new year the film was released: ")
    new_rating = input("Enter the new rating of the film: ")
    new_duration = input("Enter the new duration of the film (in minutes): ")
    new_genre = input("Enter the new genre of the film: ")
    
    c.execute("UPDATE tblfilms SET title=?, yearReleased=?, rating=?, duration=?, genre=? WHERE filmID=?", (new_title, new_year_released, new_rating, new_duration, new_genre, record_id))
    conn.commit()
    messagebox.showinfo("Success", "Record updated successfully.")

def read_all_records():
    c.execute("SELECT * FROM tblfilms")
    records = c.fetchall()
    for record in records:
        print(record)

# Tkinter arayüzü oluşturma
def main_menu():
    root = tk.Tk()
    root.title("FilmFlix")

    add_button = tk.Button(root, text="Add a record", command=add_record)
    add_button.pack()

    delete_button = tk.Button(root, text="Delete a record", command=delete_record)
    delete_button.pack()

    update_button = tk.Button(root, text="Update a record", command=update_record)
    update_button.pack()

    print_button = tk.Button(root, text="Print all records", command=read_all_records)
    print_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main_menu()

