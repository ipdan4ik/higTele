$ save_name = "Глава о Похищенных Демонами.\nДень Последний, полицейский участок"
scene okinomiya
scene black
scene bg 112
n "Сигаретный дым повис над курилкой."
nvl clear
n "Как понимаю, вся эта куча дорогой хрени для очистки воздуха просто жужжит вроде выгорающей лампочки, никакой пользы не принося."
nvl clear
n "Почему курильщиков запихивают в самый тёмный конец коридора?"
n "...Слыхал как-то, что налог с продажи табака даёт где-то с десяток процентов от всех местных налогов..."
n "{nw}"
n "Могли бы и получше к нам относиться, раз мы столько налогов уплачиваем..."
nvl clear
scene black
scene bg 112
show kuma si_uh at sleva
n "\"......Хм-м, а зачем избавляться от пятёрки {i}ман{/i}?"
extend " Разве так победить не сложнее?\""
n "{nw}"
n "Мой младший напарник уставился в колонку журнала про маджонг, идущую под заголовком «Следующий Ход»."
nvl clear
show ooishi si def_a1 at sprava
n "\"{i}Тэмпаю{/i} без пятёрки {i}ман{/i} беды особой не будет.\""
n "\"Но если собрался поставить на {i}Хай-тэй{/i}, не лучше ли подождать {i}рянмэн{/i}?\""
show ooishi si wa_a1
n "\"Кума-тян, глянь-ка ты на неигровые плитки."
extend " Все остальные выбросили свои пятёрки {i}ман{/i}, опасности в том никакой."
extend " Тому же, кто, стремясь к {i}Кей-тэну{/i} в конце игры, не спешит объявлять {i}тэмпай{/i}, исход всяко не понравится.\""
nvl clear
n "Тот задумчиво помычал, вертя в пальцах окурок, затем вытащил новую сигарету."
nvl clear
n "\"...Я всё смысла не вижу..."
extend " Особенно потому, что выиграть станет сложнее.\""
show ooishi si def_a1
n "\"Кстати говоря, ты не сможешь объявить {i}рон{/i}, если даже выигрывающего свалят завершающим ходом.\""
n "\"Э-э?! С чего бы?!\""
nvl clear
n "И тут с другого конца коридора прозвучал голос."
nvl clear
n "\"Ооиси-сан, вы там?"
extend " Вам поступил внешний вызов.\""
show ooishi si wa_a1
n "\"А, благодарю. Скоро вернусь, Кума-тян!\""
nvl clear
scene black
n "\"П-Почему я не могу объявить {i}рон{/i}?!"
extend " П-Постойте секундочку, Ооиси-сааан!\""
nvl clear
scene bg 192
n "Парень за столом напротив размахивал телефонною трубкой."
n "\"Внешняя линия,"
extend " таксофон.\""
nvl clear
scene bg 011
n "\"О, премного благодарю!"
extend " ...Простите за ожидание, Ооиси у телефона."
extend " Алло?\""
nvl clear
n "{b}\"О-Ооиси-сан?!{/b}"
extend " {b}Алло?!\"{/b}"
n "\"О, да это же Маэбара-сан?"
extend " Рад, рад вас услышать!..\""
n "В голосе Маэбары-куна отчётливо звучало нечто нехорошее."
nvl clear
n "...Маэбара-кун первый раз мне сюда звонит."
n "И притом с таксофона."
nvl clear
n "\"Прошу вас, успокойтесь."
extend " Что произошло?\""
n "{b}\"Ну, э,{w=0.8} вот...{w=1.0}... ыаах!!!.....\"{/b}"
nvl clear
n "Из телефона доносилась бессвязная речь. Было ясно, что про спокойствие говорить не приходилось."
n "Я прикрыл рот рукой, чтобы никто не подслушал, и тихо шепнул в трубку."
nvl clear
n "\"В чём дело?!\""
n "{b}\"Ыуаааххх... я... я, я......\"{/b}"
n "\"...Успокойтесь, Маэбара-сан!"
extend " Я сразу вышлю к вам ближайший патруль"
extend " и сам как можно скорее приеду!\""
n "{b}\"......Боюсь{cps=3.0}......{/cps} это уже, скорее всего{w=1.0}...... бесполезно.\"{/b}"
nvl clear
n "Испуг и, наряду с ним, отрешённость..."
n "{nw}"
n "......Его что, прямо сейчас, пока он звонит, окружают?!{w=3.0}"
nvl clear
scene bg 192
n "\"Маэбара-сан, вы же звоните с таксофона?"
extend " Где вы?!\""
n "Посторонних звуков не доносится, слышен один только голос Маэбары-куна."
n "Звонит, стало быть, из телефонной будки."
nvl clear
n "Я торопливо зачеркал на бумажке и показал её сидевшему напротив сотруднику."
n "{nw}"
n "«ХИНАМИДЗАВА — ТЕЛЕФОННАЯ БУДКА!!»"
n "{nw}"
n "Тот понял с первого взгляда и тут же начал набирать внутренний номер."
nvl clear
scene bg 011
n "\"...Маэбара-сан, прошу, спокойнее!"
extend " Что у вас происходит?!...\""
n "Не самая лучшая мысль — подгонять того, кто и так перепуган до смерти... но сейчас не время любезничать."
n "{nw}"
n "...Маэбара-кун, должно быть, подвергся опасности, но успел убежать и сделать звонок."
n "......И прямо сейчас ему может грозить очередная беда!.."
nvl clear
n "Но... сколько бы я ни пытался разговорить его, Маэбара-кун лишь всё более волновался."
n "{nw}"
n "Подозреваю, Маэбара-кун позвонил не только ради подмоги."
n "...Он звонит, желая нечто мне рассказать."
n "{nw}"
n "И рассказать он хочет нечто такое......"
extend " что, считает, никогда уже поведать не сможет, если звонок пропадёт впустую!.."
nvl clear
scene bg 192
n "Товарищ протянул записку."
n "«{i}В Хинамидзаве будка одна.{/i}"
extend " {i}Отправил патруль.{/i}"
extend " {i}5 минут{/i}»."
n "\"Слишком долго!"
extend " Сколько наших в машине?\""
n "\"Двое.\""
nvl clear
n "Двоих не хватит."
n "{nw}"
n "......Если я всё правильно представляю... Маэбару-куна окружили со всех сторон."
n "И он пяти минут не продержится!"
nvl clear
n "\"Вы звонили участковому в Хинамидзаве?!\""
n "\"Сейчас он по расписанию в патруле."
extend " Семьи дома нет, дозвониться не можем.\""
n "\"Чёрт!!"
extend " Кума-тян, заводи машину.\""
show kuma si_def at sprava
n "\"Есть!!!\""
nvl clear
hide kuma si_def
n "{b}\"...Алло?{/b}"
extend " {b}Ооиси-сан?..{/b}"
extend " {b}КХА, КХА, АГХК!!\"{/b}"
n "\"Алло!"
extend " Не волнуйтесь,"
extend " я здесь и слушаю!\""
nvl clear
n "Речь Маэбары-куна звучит странно..."
n "Кашель какой-то нехороший."
n "{nw}"
n "......Его рвёт?"
n "Или же... кровь?!"
n "Он уже ранен?!"
nvl clear
$ save_name = "Глава о Похищенных Демонами.\nДень Последний, только не говорите..."
scene bg 011
n "\"Маэбара-сан, полицейская машина уже в пути."
extend " Они доберутся до вас в несколько минут, поэтому, прошу вас, держитесь!"
extend " Алло?!"
extend " Вы меня слышите?!"
extend " Маэбара-сан?!\""
n "Из трубки донёсся жестокий кашель."
n "{nw}"
n "......В мозгу пронеслась худшая из догадок."
nvl clear
n "\"Маэбара-сан!!!"
extend " Кто на вас нападает?!"
extend " Сколько их?!\""
n "{b}\"......Я...{w=1.5} Я тоже{w=1.0}...... сначала думал, что это люди......{w=1.0} Ы-гхе!!!\"{/b}"
n "Хрип, не похожий ни на отрыжку, ни на кашель."
nvl clear
n "\"Вы в порядке?! Маэбара-сан!!\""
n "{b}\"До того я считал,{w=1.0} что преступники — люди, Проклятие Оясиро-сама никакое не настоящее...{/b}"
extend " {b}До недавнего времени.{/b}"
extend " {b}Но теперь{cps=*0.2}......{/cps} я...... знаю...{w=1.0} КХА, КККХА!!...\"{/b}"
n "Мучительный кашель,"
extend " за ним рвота."
nvl clear
n "\"......Но теперь{w=0.8}... я думаю{w=0.8}... Оясиро-сама{w=0.8}...... есть... на самом деле..."
extend " Нет, оно сейчас прямо здесь..."
extend " здесь... и сейчас.\""
n "\"Маэбара-сан, прошу, вам надо успокоиться...\""
n "\"Мне казалось, что-то не так..."
extend " Оно шло за мной, шло ВСЁ ВРЕМЯ!!..."
n "Я бежал и бежал, бежал и бежал!!!....."
extend " А оно гналось за мной тенью!!"
extend " И мало-помалу... шажок за шажочком..."
extend " подбиралось всё ближе и ближе... к моей спине......\""
nvl clear
n "\"......Маэбара-сан{cps=*0.3}{w=1.0}... а оно, случаем......{/cps}... {b}сейчас не...{w=1.0} .........за... вами?{/b}\""
nvl clear
n "\"............Да..."
extend " оно...... прямо...... за мной.........\""
n "\"Пожалуйста, Маэбара-сан."
extend " ......Вам страшно, я знаю."
extend " Но скажите, умоляю!!!"
extend " {b}......Кто... позади вас?!{/b}\""
nvl clear
n "\"Я не могу... повернуться..."
extend " Если я повернусь...... меня{w=0.8}...... меня...\""
n "\"Вам страшно, я знаю!!!"
extend " Но вы обязаны мне сказать!!"
extend " Просто поверните слегка голову!!!"
extend " {b}Маэбара-сан, кто......{w=1.0} там за вами?!!{/b}\""
nvl clear
n "В ответ послышалась громкая рвота, и затем"
extend " тошнотворный звук."
nvl clear
n "{i}\"...Маэбара-сан...{/i}"
extend " {i}...только не говорите, что вы{/i}"
extend "... {i}вы же не... раздираете себе глотку?..\"{/i}"
nvl clear
n "Ответа не последовало."
n "...Только... скребущий, царапающий звук......"
nvl clear
scene black
n "Оглушительный грохот."
nvl clear
n "...Похоже, Маэбара-кун выронил трубку."
n "На другом конце провода слышались приглушённые стоны со рвотой, а затем... чудной повторяющийся шум."
nvl clear
scene bg 011
n "{b}\"Алло!{/b}"
extend " {b}Алло?!{/b}"
extend " {b}Маэбара-сан?!{/b}"
extend " {b}Прошу вас, ответьте?!!\"{/b}"
n "Мой голос ему слышится сейчас очень, очень далёким."
n "{nw}"
n "Но... я не мог не кричать."
nvl clear
n "И затем из телефона... донеслось бормотание."
nvl clear
n "Не разберу его слов."
n "......Судя по голосу... он говорит сам с собой?"
n "Или... с кем-то с ним рядом?"
nvl clear
n "\"Алло?.."
extend " ..................Маэбара... сан?..\""
n "Не столько бормотание...... сколько некая начитываемая буддистская сутра, нечто, повторяемое на один лад."
n "Я напрягся, пытаясь уловить..."
n "{nw}"
n "Что произносит он?....."
n "Что...... чёрт побери... пытается он сказать!!!......."
nvl clear
scene black
n "{b}*Кррах*!{/b}"
nvl clear
n "Звонок вдруг оборвался."
extend " ......Что, время на 10 йен уже истекло?!"
n "Грёбаные таксофоны!!..."
nvl clear
n "\"............А.\""
nvl clear
n "Потому что звонок столь внезапно закончился..."
n "Его последние слова ясно пришли на ум."
nvl clear
scene bg 192
show kuma si_def at sprava
else
scene bg 192
n "\"Ооиси-сан, машина готова!!!"
extend " Ооиси-сан?!...\""
nvl clear
n "\"{i}......Простите меня{/i}, н-да.\""
n "\"Ооиси-сан??.....\""
nvl clear
n "Маэбара-кун повторял одно и то же."
n "{nw}"
n "...«Простите меня»........."
nvl clear
n "\nТогда я понял..."
n ".........Можно было уже не спешить."
nvl clear
hide kuma
n "......Только тогда я расслышал доносившийся из раскрытого окна... стрёкот вечерних цикад."
nvl clear
n "{i}*Чирик-чиииииирк-чирик-чирик-чирик*.......{/i}"
nvl clear
n "Полагаю, слышал его всё время,"
extend " но внимания не обращал."
n "Почему сейчас он меня вдруг так озаботил?"
nvl clear
n "{i}*Чирик-чииирк-чирииик-чирик-чирик*.......{/i}"
nvl clear
n "Они пытаются что-то мне сообщить?"
n "Такое чувство, что......"
extend " знали только поющие на закате цикады."
nvl clear
scene white
scene black
$ save_name = "Глава о Похищенных Демонами.\nЭпилог."
t "Июнь 58 года эры Сёва.{w=2.0}{nw}"
t "{nw}"
t "В деревушке Хинамидзава, входящей в состав города Шишибонэ одноимённой префектуры, произошло убийство двух школьниц.{w=2.0}{nw}"
t "{nw}"
t "Подозреваемый — Маэбара Кейти (1X лет).{w=2.0}{nw}"
nvl clear
scene bg 119 zakat
t "Подозреваемый пригласил к себе домой двух своих одноклассниц{w=2.0}{nw}"
extend " (имена — Рюгу Рэйна и Сонодзаки Мион), которых затем избил до смерти металлической битой.{w=4.0}{nw}"
nvl clear
scene black
scene bg 080
t "Место преступления — комната подозреваемого на втором этаже.{w=2.0}{nw}"
t "{nw}"
t "Комната забрызгана ужасающим количеством крови, также имеются признаки борьбы с жертвами.{w=2.0}{nw}"
t "{nw}"
t "Кроме самого места преступления, разгромлены оказались прихожая, гостиная комната и кухня.{w=4.0}{nw}"
nvl clear
scene bg 022 _day
t "В прихожей сохранились вмятины от ударов на стенах и на ящике из-под обуви.{w=2.0}{nw}"
t "{nw}"
t "Подтверждается, что удары нанесла та же самая бита, которая послужила орудием убийства.{w=2.0}{nw}"
t "Так как во вмятинах крови не найдено, полиция заключает, что удары нанесены до убийства.{w=2.0}{nw}"
t "{nw}"
t "Есть вероятность, что подозреваемый таким образом предупреждал своих жертв от побега.{w=4.0}{nw}"
nvl clear
scene bg 170
t "Ковёр в гостиной нашли перевёрнутым и отброшенным.{w=2.0}{nw}"
t "{nw}"
t "Едва ли это произошло в ходе борьбы с жертвами, но причина того неясна.{w=4.0}{nw}"
nvl clear
scene bg 115
t "В кухне оказался разорван мешок из-под мусора, его содержимое рассыпалось по полу.{w=2.0}{nw}"
t "{nw}"
t "На разбросанном по полу мусоре нашлись отпечатки ладоней, принадлежащие, по-видимому, подозреваемому.{w=2.0}{nw}"
t "{nw}"
t "Похоже на то, что подозреваемый вынул мусор и хлопал по нему ладонями.{w=2.0}{nw}"
t "{nw}"
t "Смысл его действий неясен.{w=4.0}{nw}"
nvl clear
t "Кроме того, на холодильнике обнаружилась прикреплённая записка с надписью: «Иголки не было?»{w=2.0}{nw}"
t "{nw}"
t "Значение записи неизвестно.{w=2.0}{nw}"
t "Полиция на всякий случай просмотрела мусор, но иголку найти не смогла.{w=4.0}{nw}"
nvl clear
scene black
t "Гаражные двери, хотя и не обнаружили признаков повреждений, будучи в раскрытом состоянии со времени переезда семьи, оказались закрытыми.{w=2.0}{nw}"
t "{nw}"
t "На них обнаружены отпечатки пальцев подозреваемого.{w=2.0}{nw}"
t "{nw}"
t "Смысл его действий неясен.{w=4.0}{nw}"
nvl clear
t "\nПодозреваемый сбежал с места преступления,{w=2.0}{nw}"
extend " но патрульные (с Хинамидзавского участка) нашли его лежащим в телефонной будке.{w=3.0}{nw}"
nvl clear
t "Ко времени обнаружения подозреваемый находился в бессознательном, критическом состоянии.{w=2.0}{nw}"
t "{nw}"
t "Он был без промедления доставлен в деревенскую клинику, однако сутки спустя скончался, не приходя в сознание.{w=4.0}{nw}"
nvl clear
scene bg 188
t "Вскрытие показало, что причиной смерти стал геморрагический шок.{w=2.0}{nw}"
t "{nw}"
t "Было заключено, что он расцарапал ногтями собственное горло, а последующая потеря крови привела к его смерти.{w=4.0}{nw}"
nvl clear
t "Потому как смерть весьма-таки напоминала загадочную гибель Томитаке-си неделей ранее, полиция начала расследование на предмет любых возможных связей.{w=2.0}{nw}"
t "{nw}"
t "(По настоятельной просьбе местных жителей велось без огласки.){w=2.0}{nw}"
t "{nw}"
t "Полиция заподозрила, что в смерти повинен какой-то наркотик, но, как и в случае с Томитаке-си, ничего не обнаружилось.{w=4.0}{nw}"
nvl clear
t "Загадочность происшествия вначале привела к заключению о непродуманности и внезапности преступления.{w=2.0}{nw}"
t "{nw}"
t "Однако заключение поменялось, когда одна за другой открылись странности в поведении подозреваемого, возникшие перед самым совершением преступления.{w=4.0}{nw}"
nvl clear
t "Он отдалился от ближайших друзей. Закрылся ото всех. Начал поступать непонятным образом.{w=2.0}{nw}"
t "{nw}"
t "За несколько дней до преступления стал носить с собой металлическую биту.{w=2.0}{nw}"
t "{nw}"
t "Его часто видели огрызающимся, враждебно себя проявляющим и разговаривающим с самим собой, кое-что слышали одноклассники.{w=4.0}{nw}"
nvl clear
t "За два дня до преступления он даже намекал родителям на собственную смерть.{w=2.0}{nw}"
t "{nw}"
t "Исходя из тех наблюдений, полиция начала новое расследование в предположении, что преступление произошло не внезапно, но намеренно, будучи продуманным за несколько дней до того.{w=4.0}{nw}"
nvl clear
scene bg 219
t "Позднее{w=1.5}{nw}"
extend " в комнате подозреваемого нашлась записка его почерком.{w=2.0}{nw}"
t "{nw}"
t "Записку составили две части разлинованной тетрадной страницы размера B5,{nw}"
extend " примотанные к задней крышке часов, {w=0.05}б{w=0.05}у{w=0.05}д{w=0.05}т{w=0.05}о{w=0.05} {w=0.05}б{w=0.05}ы{w=0.05} {w=0.05}к{w=0.05}т{w=0.05}о{w=0.05}-{w=0.05}т{w=0.05}о{w=0.05} {w=0.05}п{w=0.05}ы{w=0.05}т{w=0.05}а{w=0.05}л{w=0.05}с{w=0.05}я{w=0.05} {w=0.05}и{w=0.05}х{w=0.05} {w=0.05}с{w=0.05}п{w=0.05}р{w=0.05}я{w=0.05}т{w=0.05}а{w=0.05}т{w=0.05}ь{w=0.05}.{w=4.0}{nw}"
nvl clear
t "Содержимое записки см. в приложении.{w=2.0}{nw}"
nvl clear
scene bg 203
t "\nПолиция обратила особое внимание на близкую связанность записки с преступлением.{w=2.0}{nw}"
extend "\n{nw}"
t "Расследование пошло в сторону вероятной принадлежности подозреваемого к некого рода сговору.{w=2.0}{nw}"
extend "\n{nw}"
t "Однако, не обнаружив других зацепок, полиция поставила под сомнение саму достоверность записки.{w=2.0}{nw}"
extend "\n{nw}"
t "Намеренное преступление или случайность?{w=1.0}{nw}"
extend " С неясной истиной и отсутствием развития дело, казалось, решения не найдёт.{w=4.0}{nw}"
nvl clear
scene black
t "Однако... спустя несколько лет{w=1.0}{nw}"
extend " появилось новое предположение насчёт записки.{w=3.0}{nw}"
nvl clear
t "Предполагалось, что два клочка тетрадной бумаги — не разорванная пополам страница размера B5...{w=2.0}{nw}"
t "{nw}"
t "На деле записка изначально представляла собой цельный листок бумаги B5.{w=2.0}{nw}"
t "{nw}"
t "Но кто-то порвал её в двух местах,{w=1.5}{nw}"
extend " «чтобы убрать несколько строк в середине».{w=4.0}{nw}"
nvl clear
t "Предположительно вырваны две или три строки, судя по размерам почерка и вырванного куска.{w=2.0}{nw}"
t "{nw}"
t "Скорее всего, их убрал кто-то другой, но не сам подозреваемый.{w=2.0}{nw}"
t "{nw}"
t "И множественные следы клейкой ленты на задней стенке часов натолкнули полицию на мысль,{w=2.0}{nw}"
extend " что «к записке было примотано что-то ещё».{w=4.0}{nw}"
nvl clear
t "Первым из детективов на место преступления попал Ооиси Кураудо, по слухам, связанный с происшествием.{w=2.0}{nw}"
t "{nw}"
t "По собственному согласию его расспросили, но всякую причастность к повреждению записки он отрицал.........{w=4.0}{nw}"
nvl clear
scene bg 220
t "Нижеследующее — записка подозреваемого.{w=4.0}{nw}"
nvl clear
t "{b}Я, Маэбара Кейти, нахожусь во смертельной опасности.{/b}{w=2.0}{nw}"
t "{b}Я не знаю, кто пытается меня убить и за что.{/b}{w=2.0}{nw}"
t "{nw}"
t "{b}Всё, что я знаю, — здесь как-то запутано Проклятие Оясиро-сама.{/b}{w=2.0}{nw}"
t "{nw}"
t "{b}Рэна и Мион состоят в заговоре с преступниками.{/b}{w=1.0}{nw}"
extend " {b}Ещё четверо или пять взрослых.{/b}{w=1.0}{nw}"
extend " {b}У них есть белый фургон.{/b}{w=2.0}{nw}"
t "{nw}"
t "(Здесь кончается первый обрывок, оборванный строго по горизонтали в нижней части.){w=4.0}{nw}"
nvl clear
scene bg 221
t "(Дальше начинается вторая часть записки, оборванная сверху строго по горизонтали.){w=2.0}{nw}"
t "{nw}"
t "{b}Я не знаю, почему всё так получилось.{/b}{w=2.0}{nw}"
t "{nw}"
t "{b}К тому времени, как вы это прочтёте, я, скорее всего, уже буду мёртв.{/b}{w=2.0}{nw}"
extend " {b}...Найдено моё тело или нет — разница небольшая.{/b}{w=4.0}{nw}"
nvl clear
t "{b}Кто бы ни читал это, прошу — раскройте правду.{/b}{w=2.0}{nw}"
extend " {b}Это всё, чего я желаю.{/b}{w=2.0}{nw}"
t "\n\n\n\n\n{space=400}{b}Маэбара Кейти{/b}"
nvl clear
scene white
scene end_1
scene end_2
scene end_3
scene black
#jump otsukaresama_onikakushi
