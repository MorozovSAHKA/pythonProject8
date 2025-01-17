import pandas as pd

df_excel = pd.read_excel('Годовые_оценки_для_пндас.xlsx')

for i in range(len(df_excel)):
    print(f"{i+1}. {df_excel.iloc[i]}")

choice = int(input("Введи номер строки, которую хотишь выбрать: "))

if choice <= len(df_excel):
    selected_row = df_excel.iloc[choice-1]
    print(f"Ваша выбранная строка:\n{selected_row}")
else:
    print("Неверный номер строки!")

# Посмотреть информацию о таблице
print(df_excel.info())



# df = pd.read_excel('output.xlsx')