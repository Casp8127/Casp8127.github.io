from datetime import datetime

time_now_is = datetime.now()
day_now = datetime.weekday(time_now_is)

pers_is_work_now = {1: 'Кирилл',
                    2: 'Алишер',
                    3: 'Кенан'}

#if day_now <= 2:
#    print(pers_is_work_now[1])
#elif day_now > 2 and day_now < 6:
#    print(pers_is_work_now[2])
#else:
#    print(pers_is_work_now[3])

#if day_of_week_skript.day_now <= 2:
#    await call.message.answer(text=day_of_week_skript.pers_is_work_now[1])
#elif day_of_week_skript.day_now > 2 and day_of_week_skript.day_now <= 5:
#    await call.message.answer(text=day_of_week_skript.pers_is_work_now[2])
#else:
#    await call.message.answer(text=day_of_week_skript.pers_is_work_now[3])