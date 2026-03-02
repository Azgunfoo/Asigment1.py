#Question1
def Valid_course (code):
    if len(code) != 6:
        return False
    for i in range(3):
        if not ('A' <= code[i] <= 'Z'):
            return False
    for i in range(3, 6):
        if not code[i].isdigit():
            return False
    return True
code = input("Enter course code: ")
print(Valid_course(code))

#Question2
def Valid_hex_color(color):
    if len(color) != 7:
        return False  
    if color[0] != '#':
        return False    
    for ch in color[1:]:
        if not (ch.isdigit() or 'A' <= ch <= 'F' or 'a' <= ch <= 'f'):
            return False
    return True
color = input("Enter hex color: ")
print(Valid_hex_color(color))

#Question3
def numbers_in_text(text):
    total = 0
    current_number = ""
    for ch in text:
        if ch.isdigit():
            current_number += ch
        else:
            if current_number != "":
                total += int(current_number)
                current_number = ""
    if current_number != "":
        total += int(current_number) 
    return total
text = input("Enter paragraph: ")
print(numbers_in_text(text))

#Question4
def redacted_phone_numbers(text):
    result = ""
    i = 0
    n = len(text)
    
    while i < n:
        if text[i:i+3] == "+84":
            j = i + 3
            while j < n and text[j].isdigit():
                j += 1
            result += "[REDACTED]"
            i = j
        
        elif i + 10 <= n and text[i:i+10].isdigit():
            result += "[REDACTED]"
            i += 10
        
        else:
            result += text[i]
            i += 1
    
    return result


text = input("Enter text: ")
print(redacted_phone_numbers(text))