import json
#Константа - Constant
db = {
    '05.2021': {'total': 84946,
                'avans_h': 39630,
                'prize_h': 23445,
                'salary_h': 0,
                'seniority_h': 0,
                'prize_of_year_h': 0,
                'ndfl_h': 0,
                'vacation_pay_h': 0,
                'fin_assist_h': 0,
                'sick_pay_h': 0,
                'avans_w': 28770,
                'prize_w': 15473,
                'salary_w': 0,
                'seniority_w': 0,
                'prize_of_year_w': 0,
                'ndfl_w': 0,
                'vacation_pay_w': 0,
                'fin_assist_w': 0,
                'sick_pay_w': 0,
                'Ипотека': 15400,
                'Квартплата': 0,
                'Еда': 15000,
                'Алие': 0,
                'Яндекс_музыка_м': 169,
                'Icloud_m': 0,
                'Связь_м': 200,
                'Интернет_дом': 700,
                'Интернет_офис': 280,
                'Стрижка': 700,
                'Маникюр': 0,
                'Связь_ж': 200,
                'Apple_musik_w': 169,
                'Icloud_w': 0,
                'Автосигнализация': 100,
                'Бензин': 5000,
                'Автобус': 1980,
                'Электричка': 2288,
                'Метро': 1848,
                'Кредитка': 0,
                'Обучение': 0,
                'Путешествия': 0,
                'Ремонт_балкона': 0,
                'Стоматология': 80000,
                'Ипотека_ЧДП': 0,
                'ИИС': 0,
                'Валюта': 0,
                'Подушка_безопасности': 0,
                'На_беременность': 0,
                'Прочие_сбережения': 0,
                'Техника': 0,
                'Одежда': 0
                },
    '06.2021': {'total': 66230,
                'avans_h': 39630,
                'prize_h': 30341,
                'salary_h': 75297,
                'seniority_h': 11493,
                'prize_of_year_h': 0,
                'ndfl_h': 0,
                'vacation_pay_h': 0,
                'fin_assist_h': 0,
                'sick_pay_h': 0,
                'avans_w': 28770,
                'prize_w': 20024,
                'salary_w': 54663,
                'seniority_w': 0,
                'prize_of_year_w': 0,
                'ndfl_w': 0,
                'vacation_pay_w': 0,
                'fin_assist_w': 0,
                'sick_pay_w': 0,
                'Ипотека': 15400,
                'Квартплата': 5500,
                'Еда': 30000,
                'Алие': 10000,
                'Яндекс_музыка_м': 169,
                'Icloud_m': 59,
                'Связь_м': 200,
                'Интернет_дом': 700,
                'Интернет_офис': 280,
                'Стрижка': 700,
                'Маникюр': 2000,
                'Связь_ж': 200,
                'Apple_musik_w': 169,
                'Icloud_w': 59,
                'Автосигнализация': 100,
                'Бензин': 5000,
                'Автобус': 3960,
                'Электричка': 4576,
                'Метро': 3696,
                'Кредитка': 0,
                'Обучение': 0,
                'Путешествия': 0,
                'Ремонт_балкона': 120000,
                'Стоматология': 15000,
                'Ипотека_ЧДП': 0,
                'ИИС': 0,
                'Валюта': 0,
                'Подушка_безопасности': 0,
                'На_беременность': 25000,
                'Прочие_сбережения': 0,
                'Техника': 10000,
                'Одежда': 0
                },
    '07.2021': {'total': 73680,
                'avans_h': 39630,
                'prize_h': 30341,
                'salary_h': 75297,
                'seniority_h': 11493,
                'prize_of_year_h': 0,
                'ndfl_h': 0,
                'vacation_pay_h': 0,
                'fin_assist_h': 126420,
                'sick_pay_h': 0,
                'avans_w': 28770,
                'prize_w': 20024,
                'salary_w': 54663,
                'seniority_w': 0,
                'prize_of_year_w': 0,
                'ndfl_w': 0,
                'vacation_pay_w': 0,
                'fin_assist_w': 83433,
                'sick_pay_w': 0,
                'Ипотека': 15400,
                'Квартплата': 5500,
                'Еда': 30000,
                'Алие': 10000,
                'Яндекс_музыка_м': 169,
                'Icloud_m': 59,
                'Связь_м': 200,
                'Интернет_дом': 700,
                'Интернет_офис': 280,
                'Стрижка': 700,
                'Маникюр': 2000,
                'Связь_ж': 200,
                'Apple_musik_w': 169,
                'Icloud_w': 59,
                'Автосигнализация': 100,
                'Бензин': 5000,
                'Автобус': 3960,
                'Электричка': 4576,
                'Метро': 3696,
                'Кредитка': 0,
                'Обучение': 0,
                'Путешествия': 100000,
                'Ремонт_балкона': 0,
                'Стоматология': 15000,
                'Ипотека_ЧДП': 150000,
                'ИИС': 0,
                'Валюта': 0,
                'Подушка_безопасности': 0,
                'На_беременность': 25000,
                'Прочие сбережения': 0,
                'Техника': 10000,
                'Одежда': 0
                }
}
with open("data.json", "w") as write_file:
    json.dump(db, write_file)