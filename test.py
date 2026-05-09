from PIL import Image, ImageDraw

def generate_image_matrix(number_str, output_filename="cascade_matrix.png"):
    # Отфильтруем только цифры из ввода
    digits = [int(char) for char in str(number_str) if char.isdigit()]
    
    if not digits:
        print("Ошибка: В строке нет цифр.")
        return

    total_sum = sum(digits)
    salt = total_sum % 10
    
    filled_indices = [salt]
    
    for digit in digits:
        prev_col = filled_indices[-1]
        
        # (Цифра + Квадрат предыдущего столбца) % 10
        new_col = (digit + (prev_col ** 2)) % 10
        filled_indices.append(new_col)
        
    COLUMNS = 10
    ROWS = len(filled_indices)
    CELL_SIZE = 50     
    PADDING = 60      
    
    img_width = (COLUMNS * CELL_SIZE) + (PADDING * 2)
    img_height = (ROWS * CELL_SIZE) + (PADDING * 2)
    
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)
    
    m_x1, m_y1 = 15, 15
    m_x2, m_y2 = PADDING - 15, PADDING - 15
    
    draw.rectangle([m_x1, m_y1, m_x2, m_y2], fill="black")
    draw.rectangle([m_x1 + 6, m_y1 + 6, m_x2 - 6, m_y2 - 6], fill="white")
    draw.rectangle([m_x1 + 12, m_y1 + 12, m_x2 - 12, m_y2 - 12], fill="black")

    start_x = PADDING
    start_y = PADDING
    
    for row_idx, filled_col in enumerate(filled_indices):
        for col_idx in range(COLUMNS):
            x1 = start_x + (col_idx * CELL_SIZE)
            y1 = start_y + (row_idx * CELL_SIZE)
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            
            draw.rectangle([x1, y1, x2, y2], outline="black", width=2)
            
            if col_idx == filled_col:
                draw.rectangle([x1 + 6, y1 + 6, x2 - 6, y2 - 6], fill="black")
                
    img.save(output_filename)
    print("\n--- Отчет о генерации ---")
    print(f"Зашифрованное число: {''.join(map(str, digits))}")
    print(f"Сумма цифр: {total_sum}")
    print(f"Стартовый столбец: {salt}")
    print(f"Изображение успешно сохранено как '{output_filename}'.")

if __name__ == "__main__":
    user_input = input("Введите число для шифрования: ")
    generate_image_matrix(user_input)