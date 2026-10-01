from googletrans import Translator
import tkinter as tk

translator = Translator()

def translate_text():
    text_to_translate = text_input.get("1.0", tk.END).strip()

    if not text_to_translate:
        result_label.config(text="Escribe lo que deseas traducir primero.")
        return

    try:
        translation = translator.translate(
            text_to_translate, src="es", dest="ko"
        ).text

        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translation)
        output_box.config(state="disabled")

        result_label.config(text="Traducción exitosa.", fg="#d4839e")
    except Exception as e:
        result_label.config(text="Ocurrió un error de conexión.", fg="#e06d75")

window = tk.Tk()
window.title("Traductor Samgyeopsal con Mandioca")
window.geometry("450x520")
window.config(bg="#fff0f3")

title = tk.Label(
    window,
    text="Traductor Samgyeopsal con Mandioca",
    font=("Arial", 16, "bold"),
    bg="#fff0f3",
    fg="#b56576",
)
title.pack(pady=15)

instruction = tk.Label(
    window,
    text="Escribe en español lo que deseas traducir:",
    font=("Arial", 11),
    bg="#fff0f3",
    fg="#6d597a",
)
instruction.pack(anchor="w", padx=35)

text_input = tk.Text(
    window,
    height=5,
    font=("Arial", 11),
    bg="#ffffff",
    fg="#4a4e69",
    relief="solid",
    bd=1,
    padx=10,
    pady=10,
)
text_input.pack(pady=5, padx=30, fill="x")

translate_button = tk.Button(
    window,
    text="Traducir",
    font=("Arial", 12, "bold"),
    bg="#ffb5a7",
    fg="#ffffff",
    activebackground="#ff8fab",
    activeforeground="#ffffff",
    relief="flat",
    padx=15,
    pady=8,
    command=translate_text,
)
translate_button.pack(pady=12)

output_title = tk.Label(
    window,
    text="Traducción en coreano:",
    font=("Arial", 11),
    bg="#fff0f3",
    fg="#6d597a",
)
output_title.pack(anchor="w", padx=35)

output_box = tk.Text(
    window,
    height=5,
    font=("Arial", 12, "bold"),
    bg="#ffe5ec",
    fg="#b56576",
    relief="solid",
    bd=1,
    padx=10,
    pady=10,
)
output_box.pack(pady=5, padx=30, fill="x")
output_box.config(state="disabled")

result_label = tk.Label(
    window, text="", font=("Arial", 10, "italic"), bg="#fff0f3", fg="#b56576"
)
result_label.pack(pady=5)

window.mainloop()