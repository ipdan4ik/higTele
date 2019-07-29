    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play music msys09
    play sound wa_021
    scene bg 181 with Dissolve(1.0)
    centered "{space=24}— О Ватанагаси —"
    nvl clear
    play sound wa_021
    n "Теперь Ватанагаси всего лишь фестиваль, ежегодно проводимый в июне, однако, если обратить взор на его истоки, обнаруживается кровавый обряд."
    nvl clear
    play sound wa_021
    n "Вначале Ватанагаси был обычаем, в котором через установленные промежутки Оясиро-сама благословлял на «жертву»,"
    extend " которую затем ловила, расчленяла и впоследствии поедала по установленному порядку вся деревня."
    n "{nw}"
    n "(Порядок окутан множеством тайн,"
    extend " ибо промежутки между проведениями обряда весьма разнятся."
    extend " Некоторые считают, что устанавливаются они по расположению небесных тел, но такое звучит недостаточно убедительно.)"
    nvl clear
    play sound wa_021
    n "Жители древней деревни Онигафути крепко веровали, что являются наполовину людьми, наполовину демонами, а потому считали себя высшими созданиями по отношению к человеку."
    n "{nw}"
    n "Похищая и поедая людей, они просто доказывали своё вышестоящее положение в пищевой цепочке."
    nvl clear
    n "Хотя это всего лишь догадка, но, может быть, Ватанагаси проводился в качестве выхода недовольству, когда внутри жителей деревни его скапливалось достаточно — что есть последствие пребывания в рамках закрытого сообщества, которое представляла собой деревня,"
    extend " — и поэтому может считаться событием политического характера."
    n "Предположив, что проводился он именно для той цели, объяснить неравные промежутки легко."
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_wata
    return
