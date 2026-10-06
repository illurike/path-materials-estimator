def get_positive_number(message):
    while True:
        try:
            value = float(input(message).replace(",", "."))
            if value > 0:
                return value
            print("Введите число больше нуля.")
        except ValueError:
            print("Ошибка: введите число, например 12.5")


print("Калькулятор материалов для дорожки")

length = get_positive_number("Длина дорожки, м: ")
width = get_positive_number("Ширина дорожки, м: ")

sand_thickness_cm = get_positive_number("Толщина песка, см: ")
gravel_thickness_cm = get_positive_number("Толщина щебня, см: ")

sand_price = get_positive_number("Цена песка, руб./т: ")
gravel_price = get_positive_number("Цена щебня, руб./т: ")

reserve_percent = get_positive_number("Запас материалов, %: ")

area = length * width
reserve = 1 + reserve_percent / 100

sand_volume = area * (sand_thickness_cm / 100) * reserve
gravel_volume = area * (gravel_thickness_cm / 100) * reserve

sand_density = 1.6
gravel_density = 1.45

sand_weight = sand_volume * sand_density
gravel_weight = gravel_volume * gravel_density

sand_cost = sand_weight * sand_price
gravel_cost = gravel_weight * gravel_price
total_cost = sand_cost + gravel_cost

print("\n--- РЕЗУЛЬТАТ РАСЧЁТА ---")
print(f"Площадь дорожки: {area:.2f} м²")
print(f"Песок: {sand_volume:.2f} м³ / {sand_weight:.2f} т")
print(f"Щебень: {gravel_volume:.2f} м³ / {gravel_weight:.2f} т")
print(f"Стоимость песка: {sand_cost:,.0f} руб.".replace(",", " "))
print(f"Стоимость щебня: {gravel_cost:,.0f} руб.".replace(",", " "))
print(f"ИТОГО: {total_cost:,.0f} руб.".replace(",", " "))

int test