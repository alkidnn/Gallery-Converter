import customtkinter as ctk
from converter import convert_gallery

class GalleryConverterApp:
    def __init__(self):
        # Настройки темы оформления
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Создание главного окна
        self.app = ctk.CTk()
        self.app.title("Gallery Converter v0.5")
        self.app.geometry("900x780")  # Немного увеличили высоту для кнопки очистки

        # Инициализируем интерфейс и привязываем горячие клавиши
        self.create_widgets()
        self.bind_hotkeys()

    def create_widgets(self):
        # Заголовок приложения
        self.label = ctk.CTkLabel(self.app, text="Multi-Gallery HTML Converter", font=("Arial", 20, "bold"))
        self.label.pack(pady=10)

        # --- СЕКЦИЯ ВВОДА ---
        self.input_label = ctk.CTkLabel(self.app, text="Вставьте исходный HTML код сюда:")
        self.input_label.pack(anchor="w", padx=20)
        
        self.input_box = ctk.CTkTextbox(self.app, width=860, height=200)
        self.input_box.pack(pady=5, padx=20)

        # Кнопка для быстрой вставки мышкой
        self.paste_button = ctk.CTkButton(
            self.app, 
            text="📋 Paste from Clipboard", 
            fg_color="gray", 
            hover_color="#555555", 
            command=self.paste_input
        )
        self.paste_button.pack(anchor="e", padx=20, pady=5)

        # --- КНОПКИ УПРАВЛЕНИЯ ---
        # Кнопка конвертации
        self.convert_button = ctk.CTkButton(
            self.app, 
            text="🚀 Convert", 
            font=("Arial", 14, "bold"),
            command=self.convert
        )
        self.convert_button.pack(pady=10)

        # Кнопка очистки всех полей
        self.clear_button = ctk.CTkButton(
            self.app, 
            text="🗑️ Clear All", 
            fg_color="#A83232",       # Красный оттенок для кнопки удаления/очистки
            hover_color="#822222", 
            font=("Arial", 12, "bold"),
            command=self.clear_fields
        )
        self.clear_button.pack(pady=5)

        # --- СЕКЦИЯ ВЫВОДА ---
        self.output_label = ctk.CTkLabel(self.app, text="Результат для Blogger:")
        self.output_label.pack(anchor="w", padx=20)
        
        self.output_box = ctk.CTkTextbox(self.app, width=860, height=200)
        self.output_box.pack(pady=5, padx=20)
        
        # Кнопка для быстрого копирования мышкой
        self.copy_button = ctk.CTkButton(
            self.app, 
            text="🖨️ Copy Result", 
            fg_color="gray", 
            hover_color="#555555", 
            command=self.copy_output
        )
        self.copy_button.pack(anchor="e", padx=20, pady=5)

        # --- СТРОКА СТАТУСА ---
        self.status_label = ctk.CTkLabel(self.app, text="Готов к работе", font=("Arial", 12, "italic"))
        self.status_label.pack(pady=10)

    def convert(self):
        html_input = self.input_box.get("1.0", "end-1c")
        
        if not html_input.strip():
            self.status_label.configure(text="Поле ввода пусто! Вставьте HTML.")
            return

        result, count = convert_gallery(html_input)

        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", result)
        self.status_label.configure(text=f"Успешно обработано изображений: {count}")

    def paste_input(self):
        try:
            clipboard = self.app.clipboard_get()
            self.input_box.delete("1.0", "end")
            self.input_box.insert("1.0", clipboard)
            self.status_label.configure(text="Текст успешно вставлен из буфера")
        except:
            self.status_label.configure(text="Буфер обмена пуст или не содержит текст")

    def copy_output(self):
        text = self.output_box.get("1.0", "end-1c")
        if text.strip():
            self.app.clipboard_clear()
            self.app.clipboard_append(text)
            self.status_label.configure(text="Результат скопирован в буфер обмена!")
        else:
            self.status_label.configure(text="Нечего копировать, поле вывода пусто")

    def clear_fields(self):
        """Функция очистки всех текстовых полей и сброса статуса"""
        self.input_box.delete("1.0", "end")
        self.output_box.delete("1.0", "end")
        self.status_label.configure(text="Поля успешно очищены. Готов к работе.")

    def bind_hotkeys(self):
        """Универсальная привязка горячих клавиш через keycode"""
        widgets = [self.input_box, self.output_box]
        for widget in widgets:
            widget.bind("<KeyPress>", lambda event, w=widget: self.handle_global_shortcuts(event, w))

    def handle_global_shortcuts(self, event, widget):
        """Обработчик нажатий по кодам клавиш (65=A, 67=C, 86=V)"""
        ctrl_pressed = (event.state & 0x0004) != 0
        
        if ctrl_pressed:
            if event.keycode == 65:  # Ctrl + A
                return self.select_all_shortcut(widget)
            elif event.keycode == 67:  # Ctrl + C
                return self.copy_shortcut(widget)
            elif event.keycode == 86:  # Ctrl + V
                return self.paste_shortcut(widget)

    def paste_shortcut(self, widget):
        try:
            if widget.tag_ranges("sel"):
                widget.delete("sel.first", "sel.last")
            widget.insert("insert", self.app.clipboard_get())
        except:
            pass
        return "break"

    def copy_shortcut(self, widget):
        try:
            selected_text = widget.get("sel.first", "sel.last")
            if selected_text:
                self.app.clipboard_clear()
                self.app.clipboard_append(selected_text)
        except:
            pass
        return "break"

    def select_all_shortcut(self, widget):
        widget.tag_add("sel", "1.0", "end")
        widget.mark_set("insert", "end")
        return "break"

    def run(self):
        self.app.mainloop()