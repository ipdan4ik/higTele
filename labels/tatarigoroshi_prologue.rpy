$ save_name = "Глава о Смертоносном Проклятии.\nПролог"
$ mouse_visible = False
$ _game_menu_screen = None
scene black
scene si_tatarigorosi
scene black
show text "{font=times.ttf}В стремлении защищать не было лжи.{/font}" at truecenter
hide text
show text "{font=times.ttf}Желанию ценить и беречь не должно было быть равных.{/font}" at truecenter
hide text
show text "{font=times.ttf}Но заботливость породила тёмное чувство,\nставшее жаждой убийства,{/font}"
show text "{font=times.ttf}и когда-то белоснежные мысли\nокрасились в красный и чёрный.{/font}" as text2
hide text
hide text2
show text "{font=times.ttf}При этом он понимал, что разрушает мирную жизнь,{/font}"
show text "{font=times.ttf}которую хотел уберечь.{/font}" as text2
scene chapter 3
scene chapter tata_1
scene chapter tata_2
scene black
show text "{font=times.ttf}Что же пошло не так?{/font}" at truecenter
hide text
show text "{font=times.ttf}В поисках ответа трагедия идёт дальше.{/font}" at truecenter
hide text
scene tyuui_disclaimer
scene black
scene tyuui_s58
scene black
$ _game_menu_screen = "game_menu"
$ mouse_visible = True
scene white
scene bg 203
n "Жара..."
nvl clear
n "Даже малейшего ветерка нет... и мало жарищи, так ещё и лето выдалось на редкость влажное."
n "На многих окнах висит, просушиваясь, бельё, но свежестью от него не веет — наоборот, его унылый вид раздражает."
nvl clear
scene black
n "С обеих сторон улочку обступили скособочившиеся частные домишки вперемежку с невысокими многоквартирными."
n "{nw}"
n "И без того узенькая дорога становилась ещё уже, муторнее и жарче от клумб и горшков с никнущими цветами, от велосипедов, мотороллеров и мотоциклов."
nvl clear
n "Никому бы не захотелось побывать в подобном местечке в такое время."
n "...И всё же как раз тогда, после обеда, по дороге проехал мотоцикл..."
nvl clear
scene bg 133
n "Он затормозил у двухэтажного многоквартирного дома, который даже из лести нельзя было назвать ухоженным."
nvl clear
n "С мотоцикла слез мужчина весьма почтенного возраста. Лицо его избороздили морщины."
n "...Приметив его, развешивавшая бельё хозяйка поздоровалась."
nvl clear
n "\"А-а, здоровенько-о!"
extend " Страх жарко-то нонче, ага?\""
n "\"Да-а, есть такое дело!"
extend " Мене будто прям живьём варять."
extend " Хе-хе-хе!\""
nvl clear
n "\"Ах да, гражданин управляющий,"
extend " я вам кой-шо сказать хотела.\""
n "\"Ээээ, да-да, знаю, знаю!"
extend " Ртутные светильники, так?"
extend " Совсем запамятовал!"
extend " Э-хе-хе!\""
n "\"Та ни, вы шо, не слышите?"
extend " С самого утра"
extend " чем-то несёт, я уж не можу больше.\""
n "\".........Ох, ну и ну."
extend " И верно, шо за вонь!"
extend " Видать, канал-от опять засорился.\""
nvl clear
n "\"Будьтя ласка, сделайте шо-нить."
extend " С утра нос коробится.\""
n "\"Хе-хе-хе!"
extend " Ну, вы от того токмо красивше выйдете, хе-хе-хе!\""
nvl clear
scene black
n "Позади дома шла сточная канава."
n "{nw}"
n "Её решётку забивали опавшие листья и ветки, собиравшие собой мусор и летом жутко вонявшие."
nvl clear
n "\"Вот, можа, побалакаете с чановниками об этом?"
extend " Нехай вообще усю канаву закапывают!\""
n "\"Н-да-а."
extend " Решётку совсем забило."
extend " Палкой бы какой потолкать, глядишь, снова вода пойдёт.\""
n "{nw}"
n "Мужчина перебрался через заборчик, ограждавший канаву, и поднял с земли валявшуюся рядом палку для развешивания белья."
n "Никак, попробует расчистить ею решётку."
nvl clear
scene bg 203
n "\"Э-эй, э-эй, постойте!"
extend " Оно ишшо сильнее вонять почнёт,"
extend " ежли разворошить!\""
n "\"Э-хе-хе, дак оно воняет и кады забивает канаву, и коли его шевелить."
extend " Шо ж мене остаётся?"
extend " Хе-хе-хе!\""
n "Он ткнул палкой в кучу мусора, скопившуюся у решётки."
n "......Нечего и говорить, что с накопившимся мусором от этого ничего не сделалось."
nvl clear
n "\"О-ох..."
extend " Гляньте-ко, мёртвая кошка."
extend " Надоть отдел охраны здоровья сюды привлечь.\""
n "\"Мёртвые кошки-собачки дюже на вонь здоровы..."
extend " Не знаю, шо тут с одной палкой поделаю.\""
nvl clear
n "\"Эвона понакидали — мусорные мешки, одёжка старая..."
extend " Ишшо и горшок-уточка для детишков?"
extend " ...Таперь понятно, чего такая вонища."
extend " Шо ж за люди-то!\""
nvl clear
scene black
n "Какая разница — добавить мусора, не добавить, — канал и так уж давно как помойка."
n "{nw}"
n "...Многие нерадивые люди так думают, вот благодаря им канава и стала помойкой."
nvl clear
n "Палка ткнулась в кучу старых вещей, плававшую в грязной водице, и та, испустив облачко чёрного дыма, немного разошлась."
n "{nw}"
n "От открывшегося взору непонятного и жуткого зрелища оба непроизвольно нахмурились..."
nvl clear
n "\"О-о... глядитя-ка, личинки так и кишать."
extend " Верно, еду кто-то выкинул...\""
n "\"Ох...... г-гражданин управляющий..."
extend " Ш-што там такое?\""
nvl clear
n "\"Э, шо только не выбрасывають......\""
n "\"......В-вы... вы поглядите... это же!!.....\""
n "\"М-м{w=1.0}......... Ох.{w=0.8} ......ОООООО-О-О-ОХ ЖЕЕЕ Ж!!\""
nvl clear
scene white
scene bg 133
n "\"А, проходите!"
extend " Здравия желаю.\""
n "\"Ох-х, ну и вонища!"
extend " Эй!"
extend " Сверху тоже простынкой накройте!"
extend " Со второго этажа всё видно!\""
nvl clear
n "\"Личность пока не установили."
extend " Пол женский."
extend " Возраст — от двадцати пяти до сорока."
extend " Предполагаю, скончалась два-три дня тому назад."
extend " \nА потом кто-то бросил её труп сюда.\""
n "\"Причём голой."
extend " Да уж, легко мы её не опознаем."
extend " Посмотрите, не приходило ли в управление жизнеобеспечения объявление о пропаже.\""
nvl clear
n "\"Скорее всего, в канал её скинули с привязанным грузом."
extend " Похоже, груз отвязался, вот она и всплыла."
extend " ...Только почему её решили кинуть сюда, в сточную канаву?"
extend " Могли бы и получше-то место выбрать — где-нибудь под автострадой, ну, в горах, что ли.\""
n "\"Хочешь сказать, лучше бы тело нашли не на нашем участке?"
extend " Ну, кто бы это ни совершил, прятать тело точно не собирался.\""
nvl clear
n "\"Значит, убийца {i}рассчитывал{/i}, что тело найдут, — хотел преподать кому-то какой-то урок?\""
nvl clear
scene black
n "\"У неё живот разодран, и я не думаю, что здесь водится настолько зубастая рыба."
extend " Кто-то вспорол ей живот и вытащил внутренности."
extend " Перед убийством её жестоко пытали."
extend " Прямо как старые порядки китайской мафии, правда?"
extend " Поспрошай Сигэ-сана из четвёртого отдела, не знает ли он о каких волнениях, связанных с бандами.\""
n "\"Есть!\""
nvl clear
n "\"Всё-таки... вот уж труп так труп."
extend " Поглядите-ка на эти кишки, они вам не напоминают о салате в Кёя?"
extend " Вон, глянь-ка, оттуда словно лапша вылезет, если палочками поворошить, не так ли?\""
scene ryuuketu
n "\"......М-м!"
extend " П-пожалуйста, перестаньте...\""
nvl clear
n "\"Кха-ха-ха-ха!"
extend " Итак, живот выпотрошен, уши с носом отрезаны."
extend " Никому бы не понравилось так умирать."
extend " А особенно неприятный видок у пальцев."
extend " По нескольку здоровых гвоздей в каждом пальце на обеих руках."
extend " Что ж это за пытка такая?\""
nvl clear
scene black
show title at truecenter
scene black
jump tata_day01
