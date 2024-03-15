import tkinter as tk

database = []
changes_log = []

def track_changes(func):
    def wrapper(*args, **kwargs):
        global changes_log
        before_change = database.copy()
        result = func(*args, **kwargs)
        after_change = database.copy()
        changes_log.append({
            'function': func.__name__,
            'before_change': before_change,
            'after_change': after_change
        })
        return result
    return wrapper

@track_changes
def create_table(entry):
    global database
    database_dict = {name: value for name, value in zip(['title', 'price', 'category'], entry.get().split())}
    database.append(database_dict)
    entry.delete(0, tk.END)  # Очистка введенных данных
    read_database()

@track_changes
def update_database(entry_index, entry_key, entry_value):
    global database
    index_dict = int(entry_index.get())
    keys_dict = entry_key.get()
    value_dict = entry_value.get()
    database[index_dict][keys_dict] = value_dict
    entry_index.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    entry_value.delete(0, tk.END)
    read_database()

@track_changes
def delete_database(entry_index, entry_key):
    global database
    index_dict = int(entry_index.get())
    keys_dict = entry_key.get()
    value_dict = ''
    database[index_dict][keys_dict] = value_dict
    entry_index.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    read_database()

@track_changes
def read_database():
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    for item in database:
        result_text.insert(tk.END, str(item) + '\n')
    result_text.config(state=tk.DISABLED)

# Создание главного окна
root = tk.Tk()
root.title("Tkinter Database App")

# Ввод данных для create_table
create_label = tk.Label(root, text="Введите название товара, сумму и категорию через пробел:")
create_entry = tk.Entry(root)
create_button = tk.Button(root, text="Добавить в базу данных", command=lambda: create_table(create_entry))

create_label.pack()
create_entry.pack()
create_button.pack()

# Ввод данных для update_database
update_index_label = tk.Label(root, text="Индекс словаря для изменения:")
update_index_entry = tk.Entry(root)
update_key_label = tk.Label(root, text="Ключ (title, price, category):")
update_key_entry = tk.Entry(root)
update_value_label = tk.Label(root, text="Новое значение:")
update_value_entry = tk.Entry(root)
update_button = tk.Button(root, text="Обновить базу данных", command=lambda: update_database(update_index_entry, update_key_entry, update_value_entry))

update_index_label.pack()
update_index_entry.pack()
update_key_label.pack()
update_key_entry.pack()
update_value_label.pack()
update_value_entry.pack()
update_button.pack()

# Ввод данных для delete_database
delete_index_label = tk.Label(root, text="Индекс словаря для удаления:")
delete_index_entry = tk.Entry(root)
delete_key_label = tk.Label(root, text="Ключ (title, price, category):")
delete_key_entry = tk.Entry(root)
delete_button = tk.Button(root, text="Удалить из базы данных", command=lambda: delete_database(delete_index_entry, delete_key_entry))

delete_index_label.pack()
delete_index_entry.pack()
delete_key_label.pack()
delete_key_entry.pack()
delete_button.pack()

# Вывод базы данных
result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
result_text.pack()

# Запуск главного цикла
root.mainloop()
