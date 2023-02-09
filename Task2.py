# №4.2[27]. Дана строка, состоящая из слов. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Слово не зависит от регистра написания букв.
# Определите, сколько различных слов содержится в этом тексте.
# Примеры/Тесты:
#     Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
#     Output: 14
#     Input: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a tellus ut arcu gravida porta eget a lacus. Curabitur ornare varius turpis, ultricies mollis sem convallis in. Nunc scelerisque lacinia risus sit amet aliquam.
#     Output: 31
# [*]  Усложнение. Выведите кол-во слов с учетом регистра и без учета регистра




text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(text.split())
new_text = text.upper() # верхний регистр
# print(new_text.upper())
# new_text1 = text.split()  # нижний регистр
# print(new_text1.split())

print(len(set(text.split())))
print(len(set(new_text.split())))
# print(len(set(new_text1.split())))



# 2 VARIANT
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
result = []
result1 = []
text = text.split()
# print(text)
for i in text:
    if i.lower() not in result: # нижний регистр
        result.append(i)
    elif i.upper() not in result1: # верхний регистр
        result1.append(i)
print(len(result))
print(len(result1))