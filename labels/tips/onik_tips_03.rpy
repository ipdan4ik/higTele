scene black
scene bg 108
show mion se wink_a1 at sleva
n "\"Кей-тян, а ты точно не богач?\""
n "\"С чего вдруг такие вопросы?"
extend " Когда это я в школу на лимузине приезжал?\""
nvl clear
show mion se wink_b1
n "\"Ну а сколько тебе дают на карманные расходы в месяц?\""
n "\"Тысячу йен.\""
show satoko se aku_a1 at sprava
n "\"Ого. Вполне себе средненько.\""
show rika se de_a1 at central
n "\"...И приносит он вполне обычную пищу."
extend " Не похож на богатого.\""
nvl clear
scene bg 109
n "Да чё это с ними?!"
n "Сначала спросили, сколько мне дают денег в месяц, а теперь обсуждают наше благосостояние!"
nvl clear
show rena se wa_a1 at sprava
n "\"А-ха-ха-ха-ха. Прости, прости!\""
n "Рэна поймала мой недоумевающий взгляд и звонко рассмеялась."
show mion se wa_a1 at sleva
n "{nw}"
n "\"Уж больно дом у тебя здоровый, понимаешь?"
extend " Стало быть, ещё с начала работ он слыл в деревне как «Особняк Маэбара».\""
n "О-Особняк Маэбара-а?!"
show rena se def_a1
n "\"Дом вышел большой, и мы всё гадали, что за богатей к нам приедет.\""
n "{nw}"
n "А, вот оно как."
extend " Понимаю."
n "......Мой дом и вправду большой,"
extend " этого не отнимешь."
nvl clear
scene bg 108
show satoko se aku_b1 at sleva
n "\"Полагаю, потративши все деньги на постройку дома, они в конце концов стали бедняками!\""
show rika se wa_a1 at sprava
n "\"......Так ты обнищал, бедненький ты, бедняжечка.\""
n "...Рика-тян сочувственно погладила меня по голове."
extend " Ну вообще блеск — то я богач, то в бедняки записывают, моргнуть не успеешь..."
nvl clear
n "\"Не хочется обрывать полёт вашего воображения, но моя семья ни богата ни бедна."
extend " Мы — самая обычная семья со средним достатком.\""
hide satoko
show mion se tk_b2 at sleva
n "\"Ну да, как же! С таким-то домишком, да так мы и поверили!"
extend " Парадное — во какое, а через ворота вполне проедет хоть дорогое авто, хоть грузовик!!!"
extend " Для меня это никакая не «обычность»!\""
n "То есть чем больше дом, тем богаче владелец?"
nvl clear
scene bg 119
n "Наш дом так велик из-за папиной мастерской."
n "Вместе со стоящими повсюду картинами она занимает значительное пространство..."
extend " Очень значительное."
n "{nw}"
n "Короче говоря, жилого пространства там не больше трети от всего дома."
nvl clear
n "Батя мечтает в будущем устраивать у себя дома художественные выставки, потому и построены широкие ворота, чтоб как люди могли пройти, так и машины."
n "......А упомянутое Мион парадное ведёт в мастерскую отца, посему оно практически всегда закрыто."
n "Мы же пользуемся самым что ни на есть обыкновеннейшим входом."
n "{nw}"
n "Хороший, полагаю, пример поговорки: «По обложке книгу не судят»."
nvl clear
scene bg 110
show mion se def_a1 at sleva
n "\"А-а-а, хотела бы я как-нибудь порыскать в доме Кей-тяна."
extend " Он заявляет, что не богат, живя в таких-то хоромах!"
extend " Только представьте, что там может быть спрятано!\""
show rena se hau_a1 at sprava
n "\"Н-надеюсь, что-нибудь миииленькое! Хау-у-у!\""
hide mion
show satoko se aku_b1 at sleva
n "\"Я б ожидала пустых комнат, ведь они же не могут себе позволить покупку мебели!\""
show rika se wa_a1
n "\"......А я бы хотела поваляться на большом ковре.\""
n "\"О-о-о! Отличная задумка, Рика-тян, отличная задумка! Рэна тоже поваляться хооочет!\""
nvl clear
n "...Да им же просто нравится дразнить воображение..."
n "Ну что ж... думаю, стоит когда-нибудь их к себе пригласить."
n "{nw}"
n "...Мой отец питает слабость к таким девочкам, потому он может и показать им свою мастерскую."
nvl clear
scene bg 093
n "Цикады кричат всё громче, а небо стоит в недосягаемой вышине."
n "Жара. И пахнет она ранним летом."
nvl clear
scene black
call screen tips_onik
return
