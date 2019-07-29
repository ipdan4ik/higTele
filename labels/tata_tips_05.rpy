    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play music lsys12
    t "Ниже приведён отчёт о первоначальном осмотре тела жертвы."
    nvl clear
    t "{b}1) Жертва была скована{/b}{w=2.0}{nw}"
    t "{nw}"
    t "Судя по рубцам, нанесённым, по всей видимости, верёвками при попытках вырваться, жертву привязывали к специальному столу для пыток, чтобы ограничить ей свободу движения.{w=2.0}{nw}"
    t "Особенно туго стянули пальцы на обеих руках.{w=2.0}{nw}"
    t "{nw}"
    t "Судя по следам, более чем вероятно, что применённое снаряжение было сделано под заказ или в домашних условиях."
    nvl clear
    t "{b}2) Уши и нос жертвы отрезаны{/b}{w=2.0}{nw}"
    t "{nw}"
    t "Судя по рубцам, похоже, что жертву держал за шею по крайней мере один человек, пока другой отрезал ей уши и нос.{w=2.0}{nw}"
    t "{nw}"
    t "Вероятно, при этом использовалось несколько типов лезвий. В их числе с высокой вероятностью применены ножницы."
    nvl clear
    t "{b}3) Пальцы на обеих руках проткнуты гвоздями большого размера{/b}{w=2.0}{nw}"
    t "{nw}"
    t "В каждый сустав каждого пальца на обеих руках вбито по гвоздю большого размера, всего 30 (тридцать) гвоздей.{w=2.0}{nw}"
    t "Гвоздями к ладоням были прибиты квадратные дощечки со стороной 20 (двадцать) сантиметров. Предположительно, раньше они служили частью пыточного стола.{w=2.0}{nw}"
    t "{nw}"
    t "Вероятно, именно ради этой цели он и создан."
    nvl clear
    t "{b}4) Брюшная полость вскрыта, внутренние органы частично удалены{/b}{w=2.0}{nw}"
    t "{nw}"
    t "Брюшная стенка жертвы вскрыта острым \nпредметом — вероятно, с помощью медицинских познаний.{w=2.0}{nw}"
    t "По всей видимости, во время вскрытия жертва была ещё жива.{w=2.0}{nw}"
    t "{nw}"
    t "После того жертва подверглась извлечению и удалению органов, происходившему постепенно. Похоже, что смерть наступила во время него."
    nvl clear
    t "{b}5) Тело выброшено{/b}{w=2.0}{nw}"
    t "{nw}"
    t "После привязывания груза из трёх гантелей на собачий ошейник, надетый на шею жертвы, тело сбросили в канал Одзи.{w=2.0}{nw}"
    t "{nw}"
    t "Общий вес гантелей позволяет предположить, что для перемещения тела понадобилось не менее трёх взрослых мужчин."
    nvl clear
    play sound wa_021
    n "{i}Ооиси-сану.{/i}"
    n "{i}Вот копия отчёта о первоначальном осмотре тела из канала Одзи, которую вы просили.{/i}"
    n "{nw}"
    n "{i}Начальник отдела Сигэхару-сан считает, дело класса «С».{/i}"
    extend " {i}Ваше мнение?{/i}"
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_tata
    return
