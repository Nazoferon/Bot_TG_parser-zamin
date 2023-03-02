import shedule, tg
from datetime import datetime

def formatChanges(chg, grp):
    message = ""
    for change in chg[grp]:
        message += f"Пара №{change['num']} - {change['name']}\n"
    return message

nazar = 5900123750

data = datetime.now().strftime("%d.%m %T")

bot = tg.Tg("5982028350:AAHmLCVVvX0t5ZNwY4CShrehfqlXtMERfUw", nazar)

groups = ["43-ІП"]

myshedule = shedule.Shedule()
oldchanges = myshedule.getGroupsChanges(groups)

txt = ""
for group in oldchanges:
    if formatChanges == None:
        txt = "Помилка на сайті парсингу - перевірте сайт - https://rcnubip.org.ua/studentu/zmini-do-rozkladu/"
    else: txt += f"\n===========================\nГрупа: {group}\nЗаміни:\n"+formatChanges(oldchanges, group)+"==========================="
bot.say(f"Поточний стан на {data}:\n"+txt)
print(f"Запис за {data}")

while True:
    try:
        myshedule.update()
        changes = myshedule.getGroupsChanges(groups)

        if changes != oldchanges:
            message = ""
            for group in changes:
                if changes[group] != oldchanges[group]:
                    message += f"Зафіксовані зміни в розкладі {group}:\n"
                    message += formatChanges(changes, group)
            bot.say(message)

            oldchanges = changes

    except KeyboardInterrupt:
        print("Ок, на перекур")
        quit()
