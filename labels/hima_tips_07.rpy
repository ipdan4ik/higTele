    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    scene bg 034 with dissolve_04
    play music msys06
    show irie doc def_a1 at sprava with dissolve_04
    n "\"Давление практически в норме."
    extend " В ваши годы, да такая воля к жизни... нет-нет, я лишь восхищаюсь."
    n "Орё-сан, думаю, вы спокойно доживёте до ста, а то и двухсот лет.\""
    nvl clear
    n "Молодой врач в белом халате, улыбаясь, разговаривал с лежащей в кровати старой женщиной, попутно снимая с её руки липучки тонометра."
    nvl clear
    n "\"Шутник вы, дохтур Ириэ..."
    extend " Не дело мне заживатися, чаго мешать молодым..."
    extend " Хо-хо-хо-хо...\""
    n "Та усмехнулась и тихо прыснула."
    n "Затем, повернув лицо к раздвижной двери, властно крикнула."
    nvl clear
    n "\"Симико-сан, Таэко-сан, хде вы там?"
    extend " Принеситя Ириэ-сэнсэю ячменного чаю!\""
    nvl clear
    n "За дверью простучал быстрый топоток, и та отодвинулась."
    n "В проёме стояла девочка."
    extend " ...По всей видимости, её внучка."
    nvl clear
    if not persistent.matsuri:
        show mion si def_a2 at sleva with left_03
    n "\"Симико-сан уже домой ушла."
    extend " Что-то нужно?\""
    n "\"Мион, принеси-ка Ириэ-сэнсэю ячменного чаю.\""
    nvl clear
    n "\"Лады, сделаю."
    extend " А тебе, бабуль?"
    extend " Может, чёрного?"
    extend " С кучей сахара, сливок, да?\""
    n "\"Не, я сама разбавлю."
    extend " Гляди не забудь принести сахарницу и сливки!\""
    if not persistent.matsuri:
        show mion si wink_a1 with dissolve_02
    n "\"Слушаюсь.\""
    if not persistent.matsuri:
        hide mion with right_03
    n "Вежливо отвечала девочка Мион своей неизменно требовательной бабушке, после чего вышла за дверь."
    nvl clear
    n "\"Эй, дохтуру чай в стакан для гостей, поняла?!"
    extend " И подушку захватить не забудь!"
    extend " И стакан допрежь насухо вытри, слышишь?!\""
    n "\"...ышу, ышу я..."
    extend " Неча орать...\""
    n "Прилетел из коридора нахальный выкрик."
    n "{nw}"
    n "Как всегда. Никакого почтения к старшим."
    extend " Бабушка горько усмехнулась с выражением, говорящим: «Она безнадёжна»."
    nvl clear
    n "\"Ну от шо с нею делать?"
    extend " Зовсем от рук отбилась девчонка...\""
    show irie doc def_a2 with dissolve_02
    n "\"Орё-сан, Орё-сан, м-м-м-м... я б-бы т-так не сказал."
    extend " Мион-тян старается как может.\""
    nvl clear
    n "\"У ней и мать така же беспутна була."
    extend " Вылитая она!\""
    show irie doc warai with dissolve_02
    n "\"А-ха-ха-ха-ха."
    extend " Тогда, полагаю, и мать её матери в этом плане нисколько им обеим не уступает?\""
    n "Его собеседница зашлась громким смехом."
    extend " Лицо её казалось вполне весёлым."
    nvl clear
    n "\"Ириэ-сэнсэй."
    extend " Сделайтя милость, откроитя он ту дверь?"
    extend " Ветерочку бы.\""
    n "{nw}"
    n "Через узкую щель между створок раздвижной двери в комнату проникало пение хигураси."
    nvl clear
    n "Поднявшись, Ириэ чуть пошире раздвинул створки."
    nvl clear
    scene bg 035 zakat with right_03
    play ambient lsys11
    n "...Освежающий ветер ворвался в комнату, прогоняя застоявшийся воздух."
    nvl clear
    show irie doc def_a2 at sleva with left_03
    n "\"Днём теперь такая жара... но зато как прохладно утром и вечером."
    extend " Вчера под вечер даже зябко было.\""
    n "\"М-м......"
    extend " Вот вам ишшо причина любить Хинамидзаву.\""
    n "Тепло улыбнувшись в ответ, Ириэ вернулся и присел на подушку рядом с нею."
    n "{nw}"
    n "Несколько минут они сидели молча, услаждая слух пением вечерних цикад...{w=2.0}"
    nvl clear
    stop music fadeout 1.0
    n "\"Знать не знаю, доживу ли до ста, но пока помирать не собираюсь......"
    extend " Покеда не разберусь с плотиной, у гробу меня нихто не закроеть.\""
    show irie doc def_a1 with dissolve_02
    n "\"......Тяжело, наверное, заставить правительство отказаться от своего...\""
    n "\"Это правительство, оно всегда как будто жёрнов ворочаеть."
    extend " Здоровый причём такой.\""
    nvl clear
    show irie doc maji_a1 with dissolve_02
    n "\"...Жёрнов?\""
    n "\"Ну. Шо, не слыхав?"
    extend " Жёрнов.\""
    show irie doc def_a2 with dissolve_02
    n "«Нет-нет-нет, конечно, знаю-знаю», — поспешил успокоить её Ириэ."
    n "{nw}"
    n "Он знал — Орё не любит, когда её так перебивают."
    nvl clear
    n "\"И евонный жёрнов хучь шо покрошит в труху."
    extend " Запросто."
    extend " Токмо тяжёлый он больно, и запросто с места иво не стронешь."
    extend " Надо, шоб разом потянуло много-много народу, от тады стронется. Вот какой это жёрнов.\""
    n "Ириэ слушал, не раскрывая рта."
    nvl clear
    if not persistent.matsuri:
        show mion si def_a1 at sprava with right
    n "Неся поднос со стаканами чая, вернулась Мион."
    n "Мигом заметив увлечённость, с которою говорила Орё, она тихонько, стараясь не помешать, подсела и подала обоим чай."
    nvl clear
    n "\"От п-таму, када его всё же свернёшь, вдруг не остановишь."
    extend " ......А всего тяжелее — как раз толкнуть его, шоб сам пошёл."
    extend " Вот там не хотят этого, поэтому и ворочають его без передыху.\""
    if not persistent.matsuri:
        show mion si wa_a2 with dissolve_02
    n "\"А, знаю, ты про силу трения?"
    extend " Да, бабуля, похоже на правду.\""
    n "\"Дык вот,"
    extend " ежли жёрнов энтот вдруг станет... снова его запустить сможеть лишь могучая сила, от так.\""
    nvl clear
    scene bg 036 zakat with dissolve_04
    n "\".........Ваша правда. Если проект остановить, потребуется немало сил, чтобы его продолжить.\""
    n "\"Остановить крутящийся жёрнов непросто......"
    extend " Но раз останови его — и не тронется больше."
    extend " Такой это жёрнов.\""
    nvl clear
    n "\"Найти бы ещё подходящий способ остановить его...\""
    n "Как только Ириэ так сказал, пожилая женщина с Мион вдруг замолчали..."
    nvl clear
    n "Ириэ догадался, что ляпнул не то, и, волнуясь, заторопился искать слова для заглаживания оплошности."
    n "Однако они молчали не из-за того, что доктор оговорился."
    nvl clear
    scene black with dissolve_04
    n "......Потому что на лицах обеих появились насмешливые улыбки."
    nvl clear
    n "\".................................\""
    n "\"...........................\""
    n "Внезапно комнатный воздух застыл. Ириэ перестал соображать, что творится."
    n "Им целиком завладел испуг, что ухмылки выражают недовольство допущенной им оплошностью."
    nvl clear
    scene bg 036 zakat with dissolve_04
    n "\".....................\""
    n "\"....................................\""
    n "\"...............Ха, ха... Ха ха ха ха ха ха ха...\""
    n "Молчание длилось не так уж долго."
    n "Но Ириэ не мог выдержать ни секунды больше и потому нервно рассмеялся, пытаясь разрядить обстановку."
    nvl clear
    n "...Через пару секунд Мион со старой женщиной вторили ему,"
    extend " и вскоре комнату заполнил несколько холодный,"
    extend " непонятно на что направленный смех."
    n "{nw}"
    n ".........Не смеялись только цикады. Они безразлично продолжили выводить всё те же рулады..."
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_hima
    return
