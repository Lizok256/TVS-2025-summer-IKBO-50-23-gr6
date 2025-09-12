import tkinter as tk
from tkinter import messagebox


class LandCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор участка")
        self.root.geometry("400x450")


        tk.Label(root, text="Калькулятьр готов!", font=("Arial", 14)).pack(pady=10)


        tk.Label(root, text="Выберите команду:").pack()
        self.command_var = tk.StringVar(value="1")
        self.command_menu = tk.OptionMenu(
            root,
            self.command_var,
            "1", "2", "3", "4", "5",
            command=self.update_form
        )
        self.command_menu.pack()
        tk.Label(root, text="1 - рассчитать стоимость участка\n2 - перевести площадь в сотки\n3 - рассчитать площадь\n4 - макс. площадь застройки\n5 - стоимость ограждения").pack()


        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)


        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)


        tk.Button(root, text="Рассчитать", command=self.calculate).pack()


        self.update_form("1")

    def update_form(self, value):

        for widget in self.input_frame.winfo_children():
            widget.destroy()


        if value == "1":
            tk.Label(self.input_frame, text="Длина (м):").pack()
            self.length_entry = tk.Entry(self.input_frame)
            self.length_entry.pack()
            tk.Label(self.input_frame, text="Ширина (м):").pack()
            self.width_entry = tk.Entry(self.input_frame)
            self.width_entry.pack()
        elif value == "2":
            tk.Label(self.input_frame, text="Площадь (кв.м):").pack()
            self.area_entry = tk.Entry(self.input_frame)
            self.area_entry.pack()
        elif value == "3":
            tk.Label(self.input_frame, text="Площадь (кв.м):").pack()
            self.area_entry = tk.Entry(self.input_frame)
            self.area_entry.pack()
            tk.Label(self.input_frame, text="Стоимость кв.м (руб):").pack()
            self.cost_entry = tk.Entry(self.input_frame)
            self.cost_entry.pack()
        elif value == "4":
            tk.Label(self.input_frame, text="Длина (м):").pack()
            self.length_entry = tk.Entry(self.input_frame)
            self.length_entry.pack()
            tk.Label(self.input_frame, text="Ширина (м):").pack()
            self.width_entry = tk.Entry(self.input_frame)
            self.width_entry.pack()
        elif value == "5":
            tk.Label(self.input_frame, text="Длина (м):").pack()
            self.length_entry = tk.Entry(self.input_frame)
            self.length_entry.pack()
            tk.Label(self.input_frame, text="Ширина (м):").pack()
            self.width_entry = tk.Entry(self.input_frame)
            self.width_entry.pack()
            tk.Label(self.input_frame, text="Стоимость метра ограждения (руб):").pack()
            self.fence_cost_entry = tk.Entry(self.input_frame)
            self.fence_cost_entry.pack()

    def calculate(self):
        try:
            command = self.command_var.get()
            if command == "1":
                length = self.length_entry.get()
                width = self.width_entry.get()
                res = length * width
                self.result_label.config(text=f"Площадь: {res:.2f} кв.м")
            elif command == "2":
                try:
                    area_str = self.area_entry.get().strip()
                    if not area_str:
                        raise ValueError("Введите значение площади")
                    area = float(area_str)

                    if area <= 0:
                        raise ValueError("Площадь должна быть больше нуля")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return
                res = area / 10000
                self.result_label.config(text=f"Участок: {res:.2f} соток")
            elif command == "3":
                try:
                    area_str = self.area_entry.get().strip()
                    cost_str = self.cost_entry.get().strip()
                    if not area_str or not cost_str:
                        raise ValueError("Введите значения")
                    area = float(area_str)
                    cost = float(cost_str)

                    if area <= 0 or cost <= 0:
                        raise ValueError("Значения должны быть больше нуля")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

                res = area * cost
                self.result_label.config(text=f"Стоимость: {cost:.2f} руб")
            elif command == "4":

                try:
                    length_str = self.length_entry.get().strip()
                    width_str = self.width_entry.get().strip()
                    if not length_str or not width_str:
                        raise ValueError("Введите значения")
                    length = float(length_str)
                    width = float(width_str)

                    if length <= 0 or width <= 0:
                        raise ValueError("Значения должны быть больше нуля")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return
                area = length * width
                max_building_area = area * 0.3
                self.result_label.config(text=f"Макс. площадь застройки: {max_building_area:.2f} кв.м")
            elif command == "5":

                try:
                    length_str = self.length_entry.get().strip()
                    width_str = self.width_entry.get().strip()
                    fence_cost_str = self.fence_cost_entry.get().strip()
                    if not length_str or not width_str or not fence_cost_str:
                        raise ValueError("Введите значения")
                    length = float(length_str)
                    width = float(width_str)
                    fence_cost = float(fence_cost_str)

                    if length <= 0 or width <= 0 or fence_cost <= 0:
                        raise ValueError("Значения должны быть больше нуля")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return


                perimeter = 2 * (length + width)
                total_fence_cost = perimeter * fence_cost
                self.result_label.config(text=f"Стоимость ограждения: {total_fence_cost:.2f} руб")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e) if str(e) != "" else "Введите корректные числа")


if __name__ == "__main__":
    root = tk.Tk()
    app = LandCalculator(root)
    root.mainloop()

