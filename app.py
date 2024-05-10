import streamlit as st
import pandas as pd
import os

# Функция для загрузки данных из Excel-файла
def load_data(file_name):
    return pd.read_excel(file_name)

# Путь к папке, содержащей файлы Excel
folder_path = 'D:/Lab_12_ex'  # Укажите путь к папке с файлами

# Получаем список всех файлов в папке
files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# Загрузка данных из всех файлов и объединение их в один датафрейм
data_frames = [load_data(file) for file in files]
df = pd.concat(data_frames)

# Заголовок страницы
st.title('Визуализация данных из нескольких Excel-файлов')

# Раздел для отображения данных в виде таблицы
st.header('Данные')
st.write(df)

# Раздел для отображения анализа данных
st.header('Анализ данных')

# Выберите колонку для визуализации
column = st.selectbox('Выберите колонку для анализа', df.columns)

# Выберите тип визуализации
plot_type = st.selectbox('Выберите тип визуализации', ['Гистограмма', 'Линейный график'])

# Создайте график в зависимости от выбранного типа
if plot_type == 'Гистограмма':
    st.bar_chart(df[column])
elif plot_type == 'Линейный график':
    st.line_chart(df[column])

# Можете добавить дополнительные визуализации и элементы пользовательского интерфейса
