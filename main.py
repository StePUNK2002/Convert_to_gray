from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def convert_to_RGB(path):
    try:
        # Открываем изображение
        image = Image.open(path)

        # Создаем копию изображения и переводим ее в формат RGB
        rgb_image = image.copy().convert('RGB')
        pixel_values = rgb_image.getpixel((0, 0))
        width, height = image.size
        for i in range(0, height):
            for j in range(0, width):
                R = rgb_image.getpixel((j, i))[0]
                G = rgb_image.getpixel((j, i))[1]
                B = rgb_image.getpixel((j, i))[2]
                color = int(0.299 * R + 0.587 * G + 0.114 * B)
                rgb_image.putpixel((j, i), (color, color, color))
        rgb_image.save(f"{os.path.dirname(path)}/answer.png")
        image.close()
        rgb_image.close()
    except Exception as e:
        print(f"{e}")
# Создаем главное окно
root = tk.Tk()

# Задаем заголовок окна
root.title("Перевод в отенки серого")
root.geometry("500x300")

def load_image(file_path):
    # Открываем изображение с помощью модуля PIL
    image = Image.open(file_path)

    # Ограничиваем размеры изображения до 500x500 с сохранением соотношения сторон
    image.thumbnail((500, 500))

    # Возвращаем объект изображения
    return image

# Функция для выбора файла
def choose_file():
    root.attributes('-topmost', True)  # устанавливаем окно поверх других окон
    file_path = filedialog.askopenfilename(parent=root)
    if file_path != "":
        print("Выбранный файл:", file_path)
        convert_to_RGB(file_path)
        image = Image.open(f"{os.path.dirname(file_path)}/answer.png")
        image.thumbnail((500, 500), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.create_image(0, 0, image=photo_image, anchor='nw')
        canvas.image = photo_image
    else:
        pass


# Создаем кнопку для выбора файла
button = tk.Button(root, text="Выбрать файл", command=choose_file)
button.pack(pady=10)
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Запускаем цикл обработки событий
root.mainloop()