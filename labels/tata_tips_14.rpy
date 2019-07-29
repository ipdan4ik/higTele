    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play music snow4
    t "XX июля 57 года эры Сёва{w=2.0}{nw}"
    t "{nw}"
    t "Первый отдел расследований полицейского участка Окиномия.{w=2.0}{nw}"
    t "Кому: уважаемому Такасуги, начальнику отдела{w=2.0}{nw}"
    t "{nw}"
    t "Штаб по борьбе с наркопреступностью префектуры XX{w=2.0}{nw}"
    t "От: XXXX, начальника подразделения города Шишибонэ{w=2.0}{nw}"
    t "{nw}"
    t "Тема: Не подлежащее разглашению дело под номером XX."
    nvl clear
    t "\nНастоящим уведомляю, что в расследуемом нашим подразделением случае появились показания о причастности к делу, не подлежащему разглашению{w=2.0}{nw}"
    extend " (полицейский участок Окиномия, \n№X — дело об убийстве домохозяйки в Хинамидзаве)."
    nvl clear
    t "X числа X месяца, во время допроса подозреваемого, задержанного за хранение наркотиков,{w=2.0}{nw}"
    extend " тот дал показания о причастности к вышеупомянутому делу, содержащие сведения, каковые мог знать лишь виновник.{w=2.0}{nw}"
    t "{nw}"
    t "По данной причине мы готовы переслать вам протокол допроса (копию) по первому требованию.{w=2.0}{nw}"
    t "{nw}"
    t "Если его показания достойны доверия, то более чем вероятно, что XXXX является исполнителем вышеупомянутого преступления."
    nvl clear
    t "Помимо того, следователь, допрашивавший подозреваемого, связался с полицейским участком Окиномия сразу по получении показаний,{w=2.0}{nw}"
    extend " однако сотрудник участка Окиномия неверно его понял из-за предписания начальника Главного полицейского управления префектуры о неразглашении некоторых расследований от 1 июля (Предписание И 1-12 от 57 года эры Сёва),{w=2.0}{nw}"
    extend " поэтому следователь не смог объяснить существование данного дела.{w=2.0}{nw}"
    t "{nw}"
    t "Из-за этого показания были по халатности сочтены нашим следователем не представляющими важности,{w=2.0}{nw}"
    extend " поэтому сердечно просим прощения, что до сего дня не предоставили данные сведения вашему отделу."
    nvl clear
    play sound wa_023
    t "\nДолжен добавить, что подозреваемый, XXXX, скончался в камере следственного изолятора X числа X месяца."
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_tata
    return
