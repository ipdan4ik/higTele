    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play ambient lsys17
    $ renpy.pause(2.0)
    stop ambient fadeout 0.01
    n "\"Прошу прощения за столь поздний звонок..."
    extend " Звонит Кимиёси, могу ли я говорить с главой дома?"
    extend " ......Да!"
    extend " Нет-нет, это вам спасибо."
    extend " Замечательно."
    extend "........ Так это..."
    extend " весьма жаль, шо приходится вас беспокоить..."
    extend " но не захаживал ли к вам наш дедушка?"
    extend "......... Ясненько!"
    extend " Разумеется!"
    extend " Ешшо раз прошу прощения, шо беспокою так поздно."
    extend " Всего вам хорошего."
    extend " Прошу извинить......\""
    nvl clear
    play ambient lsys13
    n "{i}Дзынь{/i}."
    nvl clear
    n "\"Ну и?"
    extend " Ничего?\""
    n "\"Ну дела..."
    extend " Играть он, конечно, страсть любит... но звонит-то всегда!\""
    n "\"Товарищей по го всех обзвонил?\""
    nvl clear
    stop ambient fadeout 1.0
    play music lsys17
    n "{b}{i}*Дрррррриииинь*{/i}{/b}!!..."
    nvl clear
    stop music fadeout 0.01
    play ambient lsys13
    if persistent.matsuri:
        scene bg 122 with Dissolve(1.0)
    n "\"Да!"
    extend " Кимиёси слушает.\""
    n "\"Звонит Сонодзаки."
    extend " Что у вас?"
    extend " Нашли старосту?\""
    n "\"А-а, Мион-тян."
    extend " Мы усех обзвонили, ничагошеньки..."
    extend " Как в воду канул..."
    extend " Совсем бяда!.."
    extend " И куды ж он запропастился!..\""
    nvl clear
    n "\"Мы тоже многим названивали{w=0.8}... ничего.\""
    n "\".................................\""
    n "\"Потолковала с бабулей — говорит, надо собрать молодёжную бригаду на поиски.\""
    nvl clear
    n "\"В-В такое-то время?.."
    extend " Мы даже не уверены, пропал он вообще или нет...\""
    play sound wa_026
    n "\"С Ватанагаси прошли всего сутки."
    extend " Тут никакая предосторожность не помешает."
    extend " Если за ночь его не отыщем, завтра звоним в полицию."
    extend " Найдём, не найдём — лишняя морока от полицейских нам ни к чему.\""
    nvl clear
    n "\"...Так Орё-сан сказала?\""
    n "\"Да."
    extend " Если на слово не верится, может, мне дать ей трубку?\""
    n "\"Н-нет, не надо!.."
    extend " Хорошо,"
    extend " соберём уж тады молодёжную бригаду."
    extend " А ежли за ночь его не найдут... позвоним в полицию.\""
    nvl clear
    n "\"Благодарю. Объявите сбор по бригаде."
    extend " Я буду исполнять бабушкины обязанности.\""
    n "\"С-Спасибо."
    extend " Тотчас же всех соберу...\""
    n "\"Ага,"
    extend " бывайте.\""
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_wata
    return
