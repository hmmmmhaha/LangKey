import tkinter as tk
from tkinter import ttk

class MultilingualKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Multilingual Keyboard")

        # Set the icon for the windo

        # Text widget to display typed text
        self.text_widget = tk.Text(self.root, height=10, width=50)
        self.text_widget.grid(row=0, column=0, columnspan=15)

        # Supported languages and their keyboard layouts
        self.layouts = {
            "Romanian": [
                ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "\\"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
            ],
            "Swedish": [
                ["§", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "´"],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Å"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä"],
                ["<", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "-"]
            ],
            "German": [
                ["^", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "ß", "'"],
                ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "+"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "#"],
                ["<", "Y", "X", "C", "V", "B", "N", "M", ",", ".", "-"]
            ],
            "Czech": [
                [";", "+", "ě", "š", "č", "ř", "ž", "ý", "á", "í", "é", "=", "`"],
                ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "ú", ")"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", "ů", "§"],
                ["\\", "Y", "X", "C", "V", "B", "N", "M", ",", ".", "-"]
            ],
            "French": [
                ["²", "&", "é", "\"", "'", "(", "-", "è", "_", "ç", "à", ")", "="],
                ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "^", "$"],
                ["Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "ù", "*"],
                ["<", "W", "X", "C", "V", "B", "N", ",", ";", ":", "!"]
            ],
            "Vietnamese": [
                ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
                ["ă", "â", "ê", "ô", "ơ", "ư", "đ", "ạ", "ả", "ấ", "ầ", "ậ", "ấ"],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "\\"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
                ["f", "s", "r", "x", "j", "z"]
            ],
            "Thai": [
                ["ๅ", "/", "_", "ภ", "ถ", "ุ", "ึ", "ค", "ต", "จ", "ข", "ช"],
                ["ๆ", "ไ", "ำ", "พ", "ะ", "ั", "ี", "ร", "น", "ย", "บ", "ล"],
                ["ฟ", "ห", "ก", "ด", "เ", "้", "่", "า", "ส", "วง", "ร"],
                ["ผ", "ป", "แ", "อ", "ิ", "ื", "ท", "ม", "ใ", "ฝ"]
            ],
            "Burmese": [
                ["တ", "န", "မ", "အ", "ပ", "ခ", "ည", "ဟ", "အ", "င", "ဆ", "တ"],
                ["က", "ဂ", "စ", "ဆ", "ဘ", "တ", "ဖ", "ဒ", "ပ", "မ"],
                ["ဌ", "ည", "မ", "လ", "က", "ဆ", "ပ", "င", "သ", "စ"],
                ["ေ", "ဲ", "ိ", "ု", "ာ", "ု", "့", "ူ", "ဲ", "ျ"]
            ],
            "Russian": [
                ["ё", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
                ["Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ"],
                ["Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э"],
                ["Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ".", "/"]
            ],
            "English": [
                ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "\\"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
            ],
             "Greek": [
                ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
                ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν"],
                ["Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω", ",", ".", "/"],
            ],
            "Armenian": [
                ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
                ["ա", "բ", "գ", "դ", "ե", "զ", "է", "թ", "ժ", "ի", "լ", "խ"],
                ["ծ", "կ", "հ", "ձ", "ղ", "ճ", "մ", "յ", "ն", "շ", "ո"],
                ["տ", "ր", "ս", "վ", "տ", "պ", "ռ", "ց", "ւ", "ու", "և"]
            ],
            "Arabic": [
                ["ق", "و", "ع", "ر", "ت", "س", "ي", "ب", "ل", "ا", "ن", "م", "ك"],
                ["ض", "ص", "ث", "ق", "ف", "غ", "ع", "ه", "خ", "ح", "ج", "د"],
                ["ش", "س", "ي", "ب", "ل", "ا", "ت", "ن", "م", "ك", "ط", "ظ", "ش"],
                ["ي", "ب", "ل", "ا", "ت", "ن", "م", "ك", "ط", "ظ", "ف", "غ"]
            ]
        }

        self.shift_on = False
        self.caps_lock_on = False
        self.current_layout = "Romanian"
        self.create_buttons()

        # Dropdown menu to select the language
        self.language_var = tk.StringVar(value=self.current_layout)
        self.language_menu = ttk.OptionMenu(self.root, self.language_var, self.current_layout, *self.layouts.keys(), command=self.switch_language)
        self.language_menu.grid(row=1, column=0, columnspan=15, pady=10)

    def create_buttons(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.grid_forget()

        # Display the buttons for the current language layout
        layout = self.layouts[self.current_layout]

        # Add Shift and Caps Lock buttons
        row_offset = 2
        shift_button = tk.Button(self.root, text="Shift", width=5, command=self.toggle_shift)
        shift_button.grid(row=row_offset + len(layout), column=0)
        caps_lock_button = tk.Button(self.root, text="Caps Lock", width=5, command=self.toggle_caps_lock)
        caps_lock_button.grid(row=row_offset + len(layout), column=1)

        # Generate the keyboard layout buttons
        for row, keys in enumerate(layout, start=row_offset):
            for col, key in enumerate(keys):
                button = tk.Button(self.root, text=key, width=5, command=lambda k=key: self.insert_text(k))
                button.grid(row=row, column=col + 2)  # Shift layout to the right by 2 columns

    def switch_language(self, language):
        self.current_layout = language
        self.create_buttons()

    def toggle_shift(self):
        self.shift_on = not self.shift_on
        self.update_keys()

    def toggle_caps_lock(self):
        self.caps_lock_on = not self.caps_lock_on
        self.update_keys()

    def update_keys(self):
        for widget in self.root.grid_slaves():
            if isinstance(widget, tk.Button) and widget.cget("text") not in {"Shift", "Caps Lock"}:
                current_text = widget.cget("text")
                if self.caps_lock_on or (self.shift_on and not self.caps_lock_on):
                    widget.config(text=current_text.upper())
                else:
                    widget.config(text=current_text.lower())

    def insert_text(self, key):
        if self.caps_lock_on or (self.shift_on and not self.caps_lock_on):
            self.text_widget.insert(tk.END, key.upper())
        else:
            self.text_widget.insert(tk.END, key.lower())
        if self.shift_on:
            self.shift_on = False
            self.update_keys()

if __name__ == "__main__":
    root = tk.Tk()
    keyboard = MultilingualKeyboard(root)
    root.mainloop()
