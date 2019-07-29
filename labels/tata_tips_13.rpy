    stop music fadeout 1.0
    stop ambient fadeout 1.0
    play music gear
    t "{b}Протокол Е2-3, номер 44{/b}{w=2.0}{nw}"
    t "{b}XX числа XX месяца 52 года эры Сёва{/b}{w=2.0}{nw}"
    t "{nw}"
    t "Имя:{w=2.0}{nw}"
    t "{b}Ходзё Сатоко (X лет){/b}{w=2.0}{nw}"
    t "{nw}"
    t "Место постоянного проживания: город Шишибонэ, деревня Хинамидзава, XXX."
    nvl clear
    t "\n{u}{b}1) Способ связи{/b}{/u}{w=2.0}{nw}"
    t "{nw}"
    t "Ребёнок сам позвонил на линию помощи при случаях жестокого обращения с детьми."
    nvl clear
    t "\n{u}{b}2) Обстоятельства жестокого обращения{/b}{/u}{w=2.0}{nw}"
    t "{nw}"
    t "Жалуется на физическое насилие со стороны отчима."
    nvl clear
    t "\n{u}{b}3) Состав семьи \n(обидчики отмечены звёздочками *){/b}{/u}{w=2.0}{nw}"
    t "{nw}"
    t "Отчим*, родная мать, старший брат, сама жертва.{w=2.0}{nw}"
    t "+ Мать вышла замуж за отчима в XX году эры Сёва.{w=2.0}{nw}"
    extend " Ребёнок рождён от прежнего мужа, с которым она развелась."
    nvl clear
    t "\n{u}{b}4) Действия, предпринятые Центром по вопросам воспитания{/b}{/u}{w=2.0}{nw}"
    extend "\n{nw}"
    t "После поступления звонка на телефон доверия в тот же день был произведён звонок в школу с целью выяснить состояние ребёнка.{w=2.0}{nw}"
    t "В тот же день сотрудник центра посетил дом ребёнка для выяснения обстоятельств.{w=2.0}{nw}"
    extend "\n{nw}"
    t "Отчим добросовестно выслушал указания и согласился посещать городские уроки по воспитанию.{w=2.0}{nw}"
    t "Принято решение наблюдать за его успехами и помогать советом в случае надобности."
    nvl clear
    t "\n{u}{b}5) Прочее{/b}{/u}{w=2.0}{nw}"
    t "{nw}"
    t "В результате разговоров с ребёнком в городском центре по вопросам воспитания и поддержки детей{w=2.0}{nw}"
    extend " выяснилось, что, вероятнее всего, причиной звонка явились чрезмерное недоверие ребёнка к отчиму и недостаток общения.{w=2.0}{nw}"
    t "{nw}"
    t "Как выяснилось, жестокого обращения не было. Ребёнок совершил ложный вызов, чтобы заставить отчима держаться подальше."
    nvl clear
    t "(Ниже — карандашная записка, сделанная дежурившим тогда сотрудником.){w=2.0}{nw}"
    t "{nw}"
    t "Как видно, проблема в дочери.{w=2.0}{nw}"
    t "Ф., старший агент городского центра воспитания и поддержки детей, отметил, что большая часть её заявлений о жестоком обращении надуманна.{w=2.0}{nw}"
    t "{nw}"
    t "По данной причине руководство впредь будет осуществляться над самим ребёнком.{w=2.0}{nw}"
    t "Не стоит ей особенно доверять."
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_tata
    return
