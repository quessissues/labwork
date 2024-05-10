import streamlit as st
import pandas as pd

# Функция для загрузки данных из Excel-файла
def load_data(file_name):
    return pd.read_excel(file_name)

# Список файлов для загрузки
files = [
    'KGZ-2014.xlsx', 'KGZ-2015.xlsx', 'KGZ-2016.xlsx', 'KGZ-2017.xlsx',
    'KZ-2014.xlsx', 'KZ-2015.xlsx', 'KZ-2016.xlsx', 'KZ-2017.xlsx',
    'TJK-2014.xlsx', 'TJK-2015.xlsx', 'TJK-2016.xlsx', 'TJK-2017.xlsx',
    'UZB-2014.xlsx', 'UZB-2015.xlsx', 'UZB-2016.xlsx', 'UZB-2017.xlsx'
]

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

