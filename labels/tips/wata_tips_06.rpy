scene black
n "\"...Мы встречаемся не впервые!"
extend " Кого ты, по-твоему, видел несколько дней подряд?\""
n "\"Ладно......"
extend " раз уж ты так говоришь, ладно.\""
nvl clear
n "Нас подобрал фургон, принадлежащий родне Шион."
n "{nw}"
n "Я попробовал отказаться, но Шион настояла, чтоб и мой велик прихватили."
nvl clear
scene bg 103
n "Машина мчалась по изрытой колдобинами дороге в Хинамидзаву."
n "Эта Шион... лицедейка явно не хуже Мион, а то и лучше — сколько её ни расспрашивай, на всё сыщет ответ."
nvl clear
n "\"Но, знаешь...... ты вылитая она."
extend " Скажи, а когда распускаешь волосы, становишься от неё неотличима?\""
show shion si wink_a1
else
show shion si wink_a1 at sprava
n "\"Хм-м."
extend " А что, вполне возможно?"
extend " Как-никак однояйцевые близнецы."
extend " Мы, бывало, менялись одёжкой, и никто нас не мог различить."
extend " Частенько так проделывали с сеструхой — обвели вокруг пальца кучу народа. Аха-ха-ха!\""
nvl clear
n "Немолодой водитель в чёрном костюме, смахивающий на дворецкого, протяжно вздохнул."
nvl clear
show shion si wa_a1
n "\"Касай, ты чего?"
extend " Что вздыхаешь?\""
n "\"Прошу прощения."
extend " Подумалось просто, что вы совершенно за все годы не изменились.\""
n "В зеркале заднего вида явственно отобразился тяжёлый груз его долгих лет."
nvl clear
show shion si def_b1
n "\"Впрочем, в какой стороне твой дом?"
extend " Касай хорошо знает в Хинамидзаве только дорогу в главное имение Сонодзаки,"
extend " гляди в оба — не то завезёт ещё куда-нибудь в Яготи, где и оставит.\""
n "\"О-ох, чёрт!.."
extend " Извините, не могли бы вы остановиться на той дорожке справа?"
extend " Дальше сам как-нибудь.\""
nvl clear
scene black
scene bg 249
n "Машина остановилась в указанной точке."
n "Касай-сан достал мне велик из отделения для багажа."
nvl clear
n "\"А... большое спасибо."
extend " Премного благодарю за то, что подбросили...\""
n "\"Кейти-сан"
extend " ваше имя?\""
n "\"Э... а, да.\""
n "\"......Думается, вам предстоят многие трудности, но — уверен — они рано или поздно пройдут. А до поры потерпите.\""
nvl clear
n "На его лице читалось большое сочувствие."
n "......Ему, видно, многое пришлось испытать с той поры, когда сестрички Сонодзаки ходили под стол пешком."
nvl clear
n "\"Но, как и в Мион-сан, есть в ней унутри доброта.\""
n "\"Хотите сказать, она, как Мион, способна наворотить кучу дел?..\""
n "{nw}"
n "Улыбка его застыла, он смолк."
extend " Эй, скажите хоть что-нибудь..."
nvl clear
show shion si wink_a1 at central
n "\"Пока, Кей-тян! Ещё встретимся."
extend " Передавай приветы сеструхе."
extend " Хотя, может, самой начать ходить в хинамидзавскую школу...\""
n "\"Не вздумай."
extend " Коли придёшь, я переведусь в Окиномию.\""
show shion si wa_b1
n "\"Фу, Кей-тян, какой грубый!..\""
nvl clear
hide shion
n "Раздался короткий гудок."
extend " Пожилой водитель призывно махал рукой."
nvl clear
n "Подняв облако пыли, машина умчалась в ночную мглу..."
n "{nw}"
n ".........Да уж...... ну и денёк выдался."
n "В памяти всплыла незабываемая физиономия Мион, увидевшей меня вместе с Шион, — как у голубя, получившего в зад гороховой пулькой из игрушечного ружья."
nvl clear
scene black
call screen tips_wata
return
