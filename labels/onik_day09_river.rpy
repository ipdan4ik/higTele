$ save_name = "Глава о Похищенных Демонами.\nДень Девятый, ночь после фестиваля"
scene black
n "Зачарованно пялясь на реку, я как-то пропустил тот миг, когда Рэна рядом уже не стояла."
nvl clear
n "Никогда не думал, что почувствую себя настолько беспомощным."
n "Раз уж я теперь здешний,"
extend " надо бы получше узнать окрестности..."
nvl clear
n "Лучше подождать здесь, нежели бродить по округе."
n "Уверен, кто-либо из любителей ночной прохлады меня вскоре найдёт."
nvl clear
n "...Вдруг послышалась знакомая речь."
extend " Голос Томитаке-сана."
n "Я пошёл к нему."
nvl clear
scene bg 247
show tomi si_def at sprava
n "\"Как дела, Томитаке-сан? Много хороших снимков наснимали?\""
n "\"Да, немало! Спасибо!\""
n "С Томитаке-саном была какая-то женщина."
extend " \n......Стало слегка неловко за то, что им помешал."
nvl clear
show takano si_def at sleva
n "\"О, Кейти-кун, и как тебе фестиваль?"
extend " Понравился ли?\""
n "Судя по речи, она местная, из Хинамидзавы."
n "......Пожалуй, лица уже стоит запоминать..."
n "Как там её зовут-то?....."
nvl clear
n "\"Ну......... э... ну, понравилось.\""
n "Должно быть, по напряжённому лицу стало понятно, как мучительно я пытался вспомнить её имя. Женщина хихикнула."
nvl clear
show tomi si_wa
n "\"А, так ты ж недавно сюда переехал?"
extend " Ты, как погляжу, так сдружился с другими детьми, что в подобное сложно поверить.\""
n "Ежели действительно похоже на то со стороны, то всё благодаря Рэне, Мион и остальным."
nvl clear
n "\"Скажи-ка, после завершения фестиваля не подумалось ли тебе: «Я стал частичкой Хинамидзавы»?..\""
n "\".........Да{w=0.3}... как сказать.\""
show tomi si_def
n "\"Ого. Не похоже на тебя, Кейти-кун.\""
n "Я уже принял решение влиться в Хинамидзаву."
n "Однако... здесь всё ещё чересчур много вещей, о которых у меня знания нет."
n "Например, с кем я пересекаюсь на улице, вот как сейчас."
extend " ......Или то, что случалось в прошлом."
nvl clear
n "\"...Да ладно?"
extend " И ты только потому чувствуешь себя посторонним?\""
n "\"Нет, «посторонний» — преувеличение."
extend " Просто... как бы сказать...\""
nvl clear
n "Мне хотелось знать больше о серьёзных событиях в жизни деревни,"
extend " навроде строительства дамбы и войны, развернувшейся вокруг него."
n "...Или о том жестоком преступлении, про что даже на вопросы не отвечают."
n "Хоть с той поры утекло много времени... Раз уж я собирался жить в Хинамидзаве, мне нужно знать не только её светлую сторону, но также и тёмную."
nvl clear
show tomi si_wa
n "\"Если знание поможет тебе понять...... я расскажу всё, что знаю.\""
n "Улыбка Томитаке-сана внушала доверие, как никогда."
n "Но я не ожидал, что мне пойдут навстречу, и потому никак не мог собраться с мыслями."
n "...Мне хотелось расспросить о многом, об очень многом."
nvl clear
n "\"Хорошо, тогда...... расскажите, пожалуйста, о строительстве дамбы."
extend " Она, говорят, потопила бы Хинамидзаву, а потому вокруг ней кипел большой переполох, верно?..\""
show tomi si_uh
n "\"Думаю, местные тебе лучше расскажут..."
extend " Ну, впрочем, и я могу кое-чем поделиться"
extend " — правда, всё вычитано из газет.\""
n "Глядя вдаль, Томитаке-сан повёл свой рассказ."
nvl clear
scene bg 238
n "\"Проект строительства дамбы родился около семи-восьми лет тому назад."
extend " Она обещала стать огромной, второй в стране после дамбы Куробэ.\""
nvl clear
show black
n "В то время перед Японией стояли три важные цели:"
n "Достроить сеть дорог, соединяющую острова; обеспечить растущие потребности в электроэнергии;"
extend " наконец, совладать с половодьем."
n "{nw}"
n "Среди всех способов решения заметно выделялись гидроэлектростанции, способные управлять речными потоками, добывать электричество и приносить огромный доход одновременно."
n "Повальное строительство ГЭС пришло и сюда, и на Хинамидзаву пала стрела с белым пером."
nvl clear
hide black
n "\"Рассчитанная площадь образовавшегося бы после завершения работ озера покрывала значительное пространство."
extend " Всё — от Хинамидзавы до Яготи вверх по течению — погрузилось бы под воду.\""
n "\"...Но... зачем понадобилось возводить плотину во столь населённых местах?"
extend " Разве не могли построить её где-нибудь, где никто не живёт?\""
n "\"Хммм... Не знаю точно, однако ж... я слыхал, что здешний ландшафт для постройки плотины подходил идеально.\""
nvl clear
n "Конечно, население Хинамидзавы противилось."
n "{nw}"
n "Помнится, Рика-тян говорила, что «все сражались как один», — можно понять, КАК яростно сопротивлялись жители."
nvl clear
n "\"Дело дошло до суда, затем до Парламента."
extend " О нём писали даже в токийских газетах.\""
n "Мион что-то такое упоминала."
n "Уверен, вся Хинамидзава поднялась против дамбы единым духом."
n "{nw}"
n "...Наверняка именно из-за схватки между жителями такие прочные узы."
nvl clear
scene bg 247
show tomi si_def at sprava
n "\"Тогда-то и вскрылись политические скандалы, многих обвинили во взяточничестве."
extend " Правительству пришлось остановить стройку.\""
nvl clear
n "Пожалуй, только сейчас я смогу задать вопрос об убийстве."
n "Всё-таки пацану моего возраста привлекательны всякие там загадочные преступления."
n "{nw}"
n "Пусть Рэны с Мион рядом нет, мне всё так же неловко показывать свою заинтересованность в подобных вещах."
n "{nw}"
n "Но раз я зашёл так далеко, лишний вопрос не повредит."
extend " Может быть, ответ на него успокоит моё разбушевавшееся любопытство."
nvl clear
n "\"Эм...... то убийство с расчленением трупа... оно произошло на самом деле?\""
n "\"Да, не сомневайся."
extend " Тогда я как раз находился в Хинамидзаве,"
extend " потому очень хорошо всё помню.\""
n "Томитаке-сан отозвался охотно, без малейшего признака недовольства."
nvl clear
n "\"......Насколько помню, оно произошло ровно четыре года назад,"
extend " в день фестиваля Ватанагаси.\""
n "Произошло в последние дни повстанческого движения, когда проект уже увяз в грязи, готовясь вот-вот закрыться."
n "{nw}"
n "...Именно преступление и добило постройку."
nvl clear
scene bg 239
n "Насколько известно, на стройплощадке разразилась пьяная драка, закончившаяся убийством."
n "Боясь обнаружения, шестеро нападавших расчленили труп на шесть частей, чтобы каждому досталось зарыть свою."
nvl clear
n "В итоге пятеро из шести, будучи неспособными выдержать угрызений совести, сдались полиции, однако шестой из убийц по-прежнему в бегах."
n "Правая рука, которую он должен был закопать, не найдена до сих пор."
nvl clear
n "Всё то же самое, что и в статье."
n "{nw}"
n "Да, преступление кошмарное, но...... не настолько страшное, чтоб Рэне и Мион понадобилось его скрывать."
n "Возможно, им просто не хотелось представлять Хинамидзаву в плохом свете тому, кто лишь только сюда переехал..."
n "{nw}"
n "Будучи благодарен им за внимательность, я в то же время жалел, что не могу заткнуть любопытство."
nvl clear
scene bg 247
show tomi si_wa at sprava
n "\"Оно случилось как раз в последние дни вызванного дамбой смятения."
extend " Народ поднял большой шум, назвав его «Проклятием Оясиро-сама».\""
nvl clear
n "\"Проклятие Оясиро-сама?..\""
n "{nw}"
n "Помнится, «Оясиро-сама» — бог, которому посвящено святилище, где проходил сегодняшний фестиваль."
nvl clear
n "Понятно теперь."
n "Все поверили, что их бог наслал божественное проклятие для защиты Хинамидзавы от злой силы, проекта строительства дамбы."
nvl clear
show takano si_wa at sleva
n "\"Молодёжь, похоже, так не считала, однако..."
extend " старики не сомневались — то было Проклятие Оясиро-сама.\""
n "Так сказала с озорным смешком спутница Томитаке-сана."
n "Томитаке-сан тоже усмехнулся, что, в свою очередь, заразило смехом и меня."
nvl clear
show takano si_def
n "\"...Но вот что любопытно... как нынче оно?"
extend " Возможно, среди молодёжи тоже многие"
extend " верят.\""
n "\"Верят... во что?\""
show tomi si_def
n "\"...В Проклятие Оясиро-сама,"
extend " конечно.\""
n "Томитаке-сан и его подруга, как и раньше, улыбались, но из глаз улыбки пропали."
nvl clear
n "\"С того самого случая..."
extend " каждый год оно разражалось."
extend " ......На тот же самый день.\""
n "\"Разражалось?.. Что разражалось?\""
n "Томитаке-сан малость помолчал, словно для пущей важности. Оглядевшись, он приглушённо продолжил."
nvl clear
show tomi si_uh
n "\"Каждый год... в день фестиваля Ватанагаси...{nw}"
extend " {w=1.5}...кто-то погибает.\""
nvl clear
n "\"Через год после убийства с расчленением, в день Ватанагаси..."
n "Поехав тем днём на прогулку, семейная пара, жившая в Хинамидзаве, но поддерживавшая строительство дамбы, упала со скал в горную реку."
extend " Муж умер, а тело жены не нашёл никто.\""
n "{nw}"
n "\"Даже являясь жителями Хинамидзавы, они одобряли постройку."
extend " Старые люди шептались, что их настигло Проклятие Оясиро-сама.\""
n "{nw}"
n "Женщина снова хихикнула."
nvl clear
n "\"Ещё через год,"
extend " вечером Ватанагаси."
extend " В тот раз неожиданно умер от странной, никому не известной хвори синтоистский священник."
extend " Той же ночью жена его, бросившись в болото, покончила жизнь самоубийством.\""
n "\"Синтоистский священник... священник нашего храма?\""
n "Женщина кивнула."
nvl clear
n "\"Среди жителей поползли слухи, что тот попросту не сумел смягчить гнев Оясиро-сама.\""
n "{nw}"
n "\"Следующий год. Вечером дня Ватанагаси"
extend " нашли местную домохозяйку, забитую до смерти.\""
nvl clear
n "...Домохозяйку?"
n "Но до сих пор все загадочные смерти так или иначе были связаны либо с плотиной, либо с Оясиро-сама?"
n "Никак... и домохозяйка с ними какую-то связь имела..."
nvl clear
show takano si_wa
n "\"В точку.\""
n "Женщина шутливо{w=0.8}... нет, жестокосердно подтвердила моё подозрение."
nvl clear
n "\"Супруг жертвы...{w=0.8} приходился младшим братом человеку, который упал со скалы двумя годами раньше, — стороннику дамбы.\""
show tomi si_def
n "\"Сам брат, по слухам, жив и здоров."
extend " Но, конечно... такие события заставили его волноваться, и он покинул деревню, переехав жить в квартиру в соседнем городе.\""
nvl clear
show black
n "...Моя челюсть отвисла от изумления."
nvl clear
n "Сначала — смертная битва против постройки."
n "Затем — случившееся посреди неё зверское расчленение."
n "{nw}"
n "Про них я знал, и только про них я хотел расспросить."
nvl clear
n "А там... оказалось, что случаев больше."
n "{nw}"
n "Убийство."
extend " Расчленение и сокрытие трупа."
extend " Смерть в результате несчастного случая."
extend " Смерть от незнакомой болезни."
extend " Самоубийство."
extend " Избиение до смерти."
nvl clear
n "...Как дитя современного века..."
n "Я действительно не хотел верить во что-то наподобье проклятий..."
n "{nw}"
n "...И всё же... каждый год — и всякий раз в день Ватанагаси — происходят странные смерти, а умершие всегда оказываются причастны к строительству дамбы?!..."
nvl clear
n "Легко сказать, что на всё воля случая, что всё произошло по стечению обстоятельств."
n "Однако... коли несколько лет подряд всякий год кто-то гибнет......{w=0.8} скептикам становится всё неуютнее защищать свою точку зрения..."
nvl clear
show takano si_def
hide black
n "Я не верю в проклятия."
extend " ...Но...... нельзя отрицать, что некая «сила» желает, чтобы каждый год в день Ватанагаси...{w=0.3} что-то произошло."
nvl clear
n "Похоже, поняв, что у меня на уме, женщина негромко хихикнула."
n "Словно собираясь спросить: «Ох, не слишком ли мы тебя напугали?»"
n "Неловко и раздражённо я попросил Томитаке-сана продолжать, застыдившись того, что мой страх открылся."
nvl clear
n "\"И?"
extend " Стало быть, кто-то умер и на следующий Ватанагаси, правда ведь?.."
extend " Кто же?\""
show tomi si_wa
n "\"Ну, хм{cps=6.0}.........{/cps} Кейти-кун, а ты как считаешь?\""
n "\"Ч...... эээээ?!\""
n "В его тоне отчётливо прозвучала издёвочка. Он что, надо мной смеётся?!!"
n "\"Эй, пожалуйста, не уклоняйтесь от ответа на мой вопрос!.. Я серьёзно!..\""
n "\"...Ну-ну, Кейти-кун, успокойся.\""
n "Мягко и спокойно произнесла женщина. Тут я понял, что слишком погорячился."
nvl clear
show tomi si_def
n "\"Кейти-кун, я не уклоняюсь от вопроса."
extend " Просто...... «следующий Ватанагаси», он, так сказать...\""
nvl clear
show takano si_fu
n "\"Сегодня.\"{w=0.5}"
n "Она легко выдала ответ, покончив с мучениями Томитаке-сана."
n "......Вдруг подул тёплый, сырой ветер, обдав холодной испариной."
nvl clear
n "\"Никто не скажет вслух, но...... все размышляют о том, случится ли что-нибудь и сегодня вечером.\""
n "\"Д-Даже несмотря на праздничную толпу?!\""
nvl clear
n "\"Ну, видишь ли, жертва прошлого лета, домохозяйка, не отличалась особой верой."
extend " На фестиваль Хлопковых Корабликов она не пришла.\""
n "\"По слухам, если в этом году не пойдёшь на Ватанагаси... тебя может коснуться гнев Оясиро-сама."
extend " ...Кейти-кун, ты ведь слыхал про такое?\""
n "Ни разу не слышал."
nvl clear
n "\"...Зна-значит, все, пришедшие на праздник...... просто боялись Проклятия?!\""
n "\"Кто знает, кто знает..."
extend " В этом году на Ватанагаси народу пришло необычно много.\""
n "\"И, разумеется, их всех устрашило"
extend " Проклятие Оясиро-сама.\""
n "\"..................\""
n "Потеряв дар речи, я мог только стоять столбом..."
nvl clear
hide takano
hide tomi
show black
n "Мы в эре Сёва. Во второй половине 20-го столетия по западному календарю."
n "Во всех областях познания мы достигли выдающихся успехов, осветив тьму невежества и страх неведомого."
n "Чёрно-белые телевизоры вымерли, а ракеты доставили человечество на Луну."
n "{nw}"
n "И всё же..."
extend " даже в сегодняшнем обществе?.."
nvl clear
n "\"Значительное число детских кружков пригласили из близлежащих деревень и посёлков, чтоб создать впечатление живости,"
extend " но, как и следовало ждать, у многих «появились неотложные дела»... и они не приехали."
n "Мне довелось услышать, как старейшины из деревенского совета жаловались, что слишком трудно собрать людей.\""
n "\"Пускай полиция вроде бы не считает прошлые преступления связанными друг с другом..."
extend " сколько-то полицейских в штатском выделили на обеспечение охраны фестиваля.\""
nvl clear
n "Понемногу я начал понимать, почему Рэна с Мион отмалчивались."
n "Если на Ватанагаси в нынешнем году ничего не случится, мне знать ничего не надо, всё пойдёт хорошо и так."
nvl clear
n "......Если ничего не случится,"
extend " говорить мне — лишь вызывать беспочвенные опасения."
n "Тогда лучше притвориться, что мне до сих пор ничего не известно."
extend " Девочки, со своей стороны, поведут себя так, словно ничего и не случалось вообще."
n "{nw}"
n "...И всё пойдёт обычно, точь-в-точь как раньше."
nvl clear
show takano si_wa at sprava
hide black
n "\"...Не слишком ли страшные для него разговоры?\""
n "Женщина вздохнула, медленно расчёсывая волосы."
n "\"Н-Нет... совсем,{w=0.3} совсем нет...\""
nvl clear
n "Я-то собирался показать свою сильную волю, а вместо этого показал свои слабость и замешательство."
hide takano
n "Томитаке-сан, похоже, начал раскаиваться, что вообще мне такое рассказал."
n "Тяжко вздохнув, он заговорил веселее."
nvl clear
show tomi si_wa at sleva
n "\"Кейти-кун, ты же не веришь в проклятия, правда?\""
n "\"...Ну-у-у.......\""
n "\"Да, будь они до сих пор загадками — я бы тоже подумал о стоящем за ними проклятии."
n "Но в нашем случае подобного нет."
extend " Полиция тщательно расследовала и раскрыла каждое преступление.\""
nvl clear
n "От слова «полиция» мне значительно полегчало."
n "Неплохой антоним для слова «проклятие»."
nvl clear
show tomi si_def
n "\"......К примеру, убийство с расчленением, самое первое дело."
extend " Помнишь?"
extend " Полиция схватила почти всех, кроме одного."
extend " Когда схватят и его — \nвопрос лишь времени."
extend " Что до причины — они сами признались, что развязали потасовку, будучи пьяны."
extend " Как видишь, проклятия никакого нет."
extend " ...Сам как считаешь?\""
n "{nw}"
n "Верно... если не брать в расчёт, что преступление произошло в день Ватанагаси, то никто в здравом уме не связал бы его с проклятием..."
nvl clear
n "\"Смерть четы сторонников дамбы в следующем году такова же."
extend " Раз они умудрились навлечь на себя враждебность других жителей, полиция расследовала дело с особым вниманием."
extend " И объявила, что то был несчастный случай,"
extend " а не убийство.\""
n "\"Но...... он же произошёл в день Ватанагаси?..\""
nvl clear
show tomi si_wa
n "\"Ха-ха-ха."
extend " Подумай сам, Кейти-кун."
extend " ...Ты думаешь, они бы так взяли да пришли на фестиваль, где собралась толпа их врагов?"
n "С их точки зрения, Ватанагаси — далеко не лучшее время для пребывания в деревне."
n "Так почему б им не отправиться в путешествие куда-нибудь подальше отсюда?\""
n "{nw}"
n "Объяснение меня не то чтоб устроило, но суть его слов понятна."
nvl clear
n "Потому я решил спросить начистоту, чтобы прогнать сомнения."
n "\"Так, Томитаке-сан... что насчёт священника, погибшего на следующий год?"
extend " Который от неведомой болезни помер."
extend " ...И опять же на день Ватанагаси...\""
nvl clear
show tomi si_def
n "\"Случай со священником объяснить ещё легче."
extend " Для него фестиваль Хлопковых Корабликов был главным событием в году, потому он мог просто заработаться и устать сверх всякой меры."
extend " Или же хроническая болезнь его подточила.\""
n "\"Но ведь недуг-то никому не известен?"
extend " Как он мог умереть по «неизвестной» причине в сегодняшний век, с нашей-то медициной?..\""
nvl clear
n "\"Все любят привирать."
extend " Сплетни, просто сплетни."
n "Если два года подряд происходят убийства, любой начнёт бояться собственной тени."
extend " ......Конечно, внезапная смерть сама по себе неестественна, оно так."
n "Полиция провела вскрытие..."
extend " и ничего сверхъестественного, насколько помню, не нашла?"
extend " Так сошлись обстоятельства, что смерть кажется странноватой.\""
nvl clear
n "\"...Но ведь жена священника убила себя, верно?"
extend " Что на её счёт?\""
n "\"Как я уже объяснял."
extend " Три года несчастий запугали местных."
extend " Набожные люди быстро поверили в проклятие..."
extend " и жена священника не стала исключением."
n "Судя по найденной записке{cps=*0.4}......{/cps} она желала смягчить самопожертвованием гнев Оясиро-сама.\""
nvl clear
n "\"Хорошо, хорошо...... а что скажете про убийство домохозяйки?"
extend " Опять на Ватанагаси!\""
n "\"Преступник, попавшись, признался в содеянном."
extend " Псих, очарованный Проклятием Хинамидзавы, решил его возродить.\""
nvl clear
n "\"Ладно, ладно, верю! ...И что с проклятием следующего лета?!{w=0.3} ...А, то есть...\""
n "Верно. Следующее лето — нынешнее лето."
n "Томитаке-сан ослепительно заулыбался."
nvl clear
n "\"Ничего не случится."
extend " Только не теперь."
extend " ...«Проклятия Оясиро-сама» не было никогда."
extend " Те, кто в него верят, просто играют на серии случайностей, распространяя слухи о том, что всё случилось из-за проклятия.\""
nvl clear
n "...Процессор в мозгу наконец остыл, вернувшись к нормальной работе."
n "Мне уже неловко — увлекаемый дурным ребячеством, я почти растерял хладнокровие..."
nvl clear
n "\"Кейти-кун, я понимаю, как тебе нравится Хинамидзава."
extend " ......Если б даже и существовало Проклятие Оясиро-сама,"
extend " тебя оно не затронет, ручаюсь.\""
nvl clear
n "С души словно камень упал."
n "Лучше поскорее забыть о том, что я сегодняшней ночью слышал."
n "Завтра на наших — с Рэной, Мион и остальными — лицах, как всегда, заиграют улыбки."
n "{nw}"
n "Единственное моё желание — жить дальше без тревог, стоит пройти сегодняшней ночи без происшествий."
nvl clear
n "Словно увидев мою решимость, подруга Томитаке-сана, сидевшая на большом камне, слушая нас, потянулась и встала."
nvl clear
show takano si_def at sprava
n "\"......Что ж."
extend " Мне пора.\""
n "\"Ох!.. Вот чёрт, заболтался!\""
n "Толпа истончилась; под вечерним небом оставалось лишь несколько семей."
n "{nw}"
n "Часы говорят, что... мы почти целый час пробеседовали."
nvl clear
n "\"Кейти-кун, ты же с друзьями пришёл, не так ли?"
extend " Они тебя ищут небось?\""
n "\"...И правда!.."
extend " Меня, наверно, все ищут!\""
n "\"Ха-ха-ха-ха!"
extend " Тебя разыскивают девочки? Во ты негодник!\""
show takano si_wa
n "\"Что же, спокойной ночи, Кейти-кун."
extend " И вам, Дзиро-сан. До встречи.\""
n "...Да и вы, Томитаке-сан, ещё тот негодник. (Хм, она же назвала его «Дзиро-саном»...)"
nvl clear
hide takano
n "Женщина охлопала пыль с ягодиц и направилась к святилищу, где торговцы собирали палатки."
nvl clear
$ save_name = "Глава о Похищенных Демонами.\nДень Девятый, наказание фотографа"
scene bg 246
show rena si ko_a1 at sprava
n "\"Кейти-кууун!!!"
extend " Простиии!!!\""
n "Вместо неё прибежала Рэна."
n "За ней виднелись остальные."
n "Помяни чёрта, называется."
nvl clear
show mion si wink_a1 at sleva
n "\"Звиняй-звиняй, Кей-тян!.."
extend " Мы в разговоре забылись!\""
n "Со мной то же самое, так что мы квиты."
hide rena
show satoko si aku_a1 at sprava
n "\"О, так вы пребывали здесь с Томитаке-саном!"
extend " Чудесно!!!\""
show rika miko de_a1 at central behind satoko
n "\"Подведём итоги сегодняшнего соревнования по стрельбе.\""
scene bg 246
show tomi si_uh at central
n "\"Ох, да... в-верно!.."
extend " Так я сыграл хуже всех?\""
nvl clear
scene black
scene bg 015
show rika miko de_a1 at central
n "После моей впечатляющей победы в тире счастья попытала Рика-тян, однако большинство целей успели сбить."
n "...Хоть мишени кое-какие остались, но только труднодоступные."
n "Она тщательно целилась, но все три выстрела попали «в молоко», так что, по-хорошему, ей надо бы поделить последнее место с Томитаке-саном."
nvl clear
show rika miko ko_a1
n "...Но, начав хныкать своё «мии-мии», она поразила владельца в самое сердце."
n "И тот дал ей жевательных конфет в качестве утешительного приза."
n "Так Рика-тян избежала звания главной неудачницы."
nvl clear
scene bg 247
n "\"......По-моему, в Рике-тян добрая часть от тануки.\""
show rika miko ni_a1 at sprava
n "\"Ума не приложу, о чём ты говоришь, Кейти.\""
show satoko si aku_a1 at sleva
n "\"И потому главным неудачником объявляется Томитаке-сан!!!\""
n "С радостными воплями все громко захлопали. Томитаке-сан осторожно улыбнулся, не понимая, что происходит."
nvl clear
scene bg 247
show mion si tk_a2 at sprava
n "\"Ну чтооо, Томитаке-сан, вы готовы к... штрафной игре?!!\""
show tomi si_uh at sleva behind mion
n "\"А? Опа...... я уж и забыл!!!\""
n "Как неумно, Томитаке-сан. Именно из-за штрафных игр мы не можем проигрывать..."
nvl clear
n "Мион вынула из кармана маркер."
extend " ......Ах-ха, то самое."
nvl clear
n "\"Мион, прояви толику сострадания."
extend " Хотя бы смываемый маркер возьми."
extend " Вечный слишком тяжело отскрести.\""
show mion si wink_a1
n "\"Аха-ха, нет, нам нужны несмываемые чернила."
extend " Так они не сойдут и со стиркой.\""
n "\"Э, э! Что, что вы творите?!"
extend " Полегче, прошу вас!!!\""
nvl clear
n "Мы свели Томитаке-сану руки за спину, и Мион подошла к нему с маркером."
n "\"Скрип-скрип-скрип, вот и всё!\""
n "{nw}"
n "Мион водила маркером не по лицу Томитаке-сана, но по его майке."
nvl clear
show black
hide mion
n "{i}«Выйди на большую арену в этом году! — Мион».{/i}"
nvl clear
n "Следующей маркер получила Рэна, написав: {i}«Пожалуйста, покажите мне свои снимки в следующий раз! {font=DejaVuSans.ttf}☆{/font} — Рэна»{/i}."
n "{nw}"
n "Трогательно. С лица не сходит, продолжая расти, улыбка."
nvl clear
hide black
show satoko si aku_a1 at sprava
n "\"Ха-ха, да это же скорее прощальные пожелания, чем штрафная игра.\""
n "\"Хо-хо-хо! Я вам не такая мягкосердечная!"
extend " Надлежит свято соблюсти устои наказаний!\""
nvl clear
show rika miko de_a1 at sprava
show black
hide satoko
n "{i}«Эй, Неудачник! — Сатоко».{/i}"
n "{nw}"
n "{i}«Старайся в следующий раз. — Рика».{/i}"
nvl clear
hide black
n "\"Твой черёд, Кейти-сан.\""
nvl clear
hide rika
n "Не знаю даже, что написать, но...... да, для нынешнего штрафа — самое то."
nvl clear
n "{i}«Возвращайтесь, поиграете с нами. — Кейти».{/i}"
n "{nw}"
n "Томитаке-сан долго не произносил ни слова."
n "Сначала он выглядел озадаченным, но постепенно его выражение переменилось."
nvl clear
show tomi si_def at sprava
n "\"Мне придётся носить её до самого Токио... как часть наказания?\""
show mion si wa_a2 at sleva
n "\"Всё тааак! Поедешь домой в таком виде!\""
hide mion
show rena si wa_b1 at sleva
n "\"А-ха-ха-ха, вы и в следующий раз приедете в ней, надеюсь?"
extend " ...надеюсь!\""
n "{nw}"
n "Томитаке-сан растроган."
n "Его лицо покраснело от неловкости вперемешку с другими эмоциями."
nvl clear
hide rena
show tomi si_wa
n "\"Принял. В следующий раз обязательно приеду в ней."
extend " Даю слово!\""
n "Все радостно захлопали, загалдели."
n "Для отбывающего нынче друга то был самый лучший прощальный подарок."
nvl clear
n "Я заметил стоящую перед храмом подругу Томитаке-сана."
n "Томитаке-сан, тоже увидавший её, понял, что пришло время прощаться."
nvl clear
show mion si aku_a1 at sleva
n "\"Разве не ждёт вас подруга?"
extend " Не пора ль вам идти?"
extend " Ммм?\""
show tomi si_uh
n "\"А,{w=0.2} хм, видать, да... ха ха.\""
nvl clear
hide tomi
n "Томитаке-сан пошёл к ней, извиняясь за ожидание."
nvl clear
hide mion
n "Мы все по-своему с ним прощались."
n "{nw}"
n "Всякий раз Томитаке-сан оборачивался и махал рукой."
n "{nw}"
n "......И вот его силуэт растворился в темноте ночи."
nvl clear
n "Относительно лёгкое и простое прощание."
n "Для остальных оно не впервые."
n "Они уже много раз через него проходили."
nvl clear
show rena si def_a1 at sleva
n "\"...Ушёл.\""
show mion si wink_a2 at sprava
n "\"Что ж, пора и нам валить!\""
n "Рика-тян осталась в храме — как сказала, для собрания с исполнительным комитетом. Сатоко, понятное дело, туда же."
n "Я направился домой вместе со своей привычной командой."
nvl clear
scene black
scene bg 254
n "Весь путь мы провели в болтовне о сегодняшних битвах."
n "Нужно было сделать то, ах, как мы облажались тогда, всё такое."
nvl clear
scene bg 249
n "После расставания с Мион мы с Рэной остались наедине."
n "{nw}"
n "Дойдя до своего дома, простился и с Рэной."
nvl clear
n "\"Ты точно дойдёшь одна в такой поздний час?\""
show rena si wa_a1
n "\"Угу, очень даже!"
extend " Мой домик недалеко, и я пробегу всю дорогу.\""
n "\"...Увидишь тёмную личность — кричи громко!\""
show rena si hau_a1
n "\"А если я закричу... ты придёшь? ......придёшь?\""
n "\"Да, коль заслышу.\""
n "\"Хау!..{w=0.3} ..........Х-Хорошо!"
extend " Закричу так, что ты услышишь!\""
nvl clear
hide rena
n "Рэна весело ускакала, что-то напевая под нос и размахивая руками."
n "Ничего с ней не случится. В таком состоянии самый сильный взрослый не станет для неё помехой."
nvl clear
n "После ухода жизнерадостной Рэны вернулась тишина."
n "Я припомнил услышанное о проклятии, про которое ни одна из подруг даже слова не пожелала бросить."
extend " ......Чем больше я знаю, тем беспокойнее, учитывая сегодняшнюю дату, становлюсь."
nvl clear
scene bg 118
n "Никто ни в чём не проявил беспокойства, но оно есть..."
n "Впрочем, если ничего не случится сегодня, смысла в тревоге нет."
n "Ничего не случится. Ничего зловещего, ничего ужасного. Ничего."
nvl clear
n "\"Что ты там стоишь, Кейти?"
extend " ...Давай заходи, не то хочешь простудиться?\""
n "То моя мама."
n "\"Мам,"
extend " ты ходила на фестиваль Ватанагаси?\""
n "\"Не смогла"
extend " — твой отец так и не проснулся."
extend " К сожалению.\""
n "Мама, очевидно расстроенная, показала язык."
nvl clear
show cinema
show title02
#scene black
#show tips_received
#show text "Несчастный случай с четой сторонников дамбы\nОт загадочной болезни погибает\nсвященник храма Фурудэ\n\nУбийство домохозяйки\nЗаписанные радиопереговоры"
#hide tips_received
#hide text
$ day_result = "onik_day10"
call screen day_completed(tips="onikakusi")
jump onik_day10
