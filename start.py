import shedule, tg

def formatChanges(chg, grp):
    message = ""
    for change in chg[grp]:
        message += f"Пара №{change['num']} - {change['name']}\n"
    return message

nazar = 5900123750

bot = tg.Tg("5982028350:AAHmLCVVvX0t5ZNwY4CShrehfqlXtMERfUw", nazar)

groups = ["43-ІП"]

myshedule = shedule.Shedule()
oldchanges = myshedule.getGroupsChanges(groups)

txt = ""
for group in oldchanges:
    txt += f"\n===========================\nГрупа: {group}\nЗаміни:\n"+formatChanges(oldchanges, group)+"==========================="
bot.say("Поточний стан:\n"+txt)

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
