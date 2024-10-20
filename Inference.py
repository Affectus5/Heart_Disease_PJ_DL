import joblib  # Для загрузки модели и скейлера
import pandas as pd  # Для работы с данными

# Загрузка подготовленных ранее модели и скейлера
model = joblib.load('models/model.joblib')
scaler = joblib.load('models/scaler.joblib')

# Загрузка тестовых данных
df = pd.read_csv("/content/drive/MyDrive/Heart_Disease_PJ_DL/data/test.csv")

# Удаление столбца с ID пациента
df.drop(columns=['ID'], inplace=True)

# Задаем список категориальных переменных
cat_list = [
    'sex',
    'chest',
    'fasting_blood_sugar',
    'resting_electrocardiographic_results',
    'exercise_induced_angina',
    'slope',
    'number_of_major_vessels',
    'thal'
]

# Преобразуем категориальные переменные в дамми-переменные
df_dum = pd.get_dummies(df, columns=cat_list, drop_first=True)

# Масштабирование данных
df_scaled = scaler.transform(df_dum)

# Предсказание параметров
predictions = model.predict(df_scaled)

# Вывод результатов предсказания
print(predictions)

try:
    # Загрузка данных и выполнение инференса
    df = pd.read_csv("/content/drive/MyDrive/Heart_Disease_PJ_DL/data/test.csv")
    df.drop(columns=['ID'], inplace=True)

    df_dum = pd.get_dummies(df, columns=cat_list, drop_first=True)
    df_scaled = scaler.transform(df_dum)

    predictions = model.predict(df_scaled)
    print(predictions)

except FileNotFoundError as e:
    print(f"Ошибка: {e}. Проверьте путь к файлу.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
