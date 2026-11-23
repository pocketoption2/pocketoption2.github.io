import sys; sys.path.insert(0, "tools")
from tr import build
RU = [
 ('"Types of bonuses" }', '"Виды бонусов" }'), ('"How promo codes work" }', '"Как работают промокоды" }'),
 ('"Bonus rules to know" }', '"Правила бонусов" }'), ('"Is a bonus worth it?" }', '"Стоит ли брать бонус?" }'),
 ('title="Pocket Option Promo Code & Bonus 2026: How They Work"', 'title="Промокод Pocket Option и бонусы 2026: как они работают"'),
 ('description="Pocket Option promo codes and deposit bonuses explained: bonus sizes, cashback, tournaments and the turnover rules to meet before you can withdraw."',
  'description="Промокоды и бонусы на депозит Pocket Option: размер бонуса, кэшбэк, турниры и условия отыгрыша, которые нужно выполнить до вывода."'),
 ('h1="Pocket Option promo codes and bonuses"', 'h1="Промокоды и бонусы Pocket Option"'),
 ('lead="Deposit bonuses, cashback, tournaments and achievements can add value, but every bonus comes with conditions. Read these before you enter a code."',
  'lead="Бонусы на депозит, кэшбэк, турниры и достижения могут быть выгодны, но у каждого бонуса есть условия. Прочитайте их, прежде чем вводить промокод."'),
 ('crumb="Bonus & promo codes"', 'crumb="Бонусы и промокоды"'),
 ('<h2 id="types">Types of bonuses</h2>', '<h2 id="types">Виды бонусов</h2>'),
 ('<th>Bonus</th>\n        <th>What it does</th>', '<th>Бонус</th>\n        <th>Что даёт</th>'),
 ('<td>Deposit promo code</td>\n        <td>Adds a percentage on top of your deposit as bonus funds.</td>', '<td>Промокод на депозит</td>\n        <td>Начисляет процент сверху депозита бонусными средствами.</td>'),
 ('<td>Cashback</td>\n        <td>Returns part of your losses over a period to your balance.</td>', '<td>Кэшбэк</td>\n        <td>Возвращает на баланс часть убытков за определённый период.</td>'),
 ('<td>Risk-free trades</td>\n        <td>Refunds the stake of a set number of losing trades.</td>', '<td>Безрисковые сделки</td>\n        <td>Возвращает сумму ставки по заданному числу убыточных сделок.</td>'),
 ('<td>Tournaments</td>\n        <td>Separate balance with prize pools; some are free to enter.</td>', '<td>Турниры</td>\n        <td>Отдельный баланс и призовой фонд; в некоторых участие бесплатное.</td>'),
 ('<td>Achievements</td>\n        <td>Experience levels that unlock extra perks as you trade.</td>', '<td>Достижения</td>\n        <td>Уровни опыта, которые по мере торговли открывают дополнительные привилегии.</td>'),
 ('''Offers change often and differ by account. The <strong>Promo codes</strong> and <strong>Market</strong> sections of
    your account show what is available to you right now.''', '''Акции часто меняются и у всех разные. Что доступно именно вам сейчас, видно в разделах <strong>«Промокоды»</strong> и
    <strong>«Маркет»</strong> личного кабинета.'''),
 ('<h2 id="promo">How promo codes work</h2>', '<h2 id="promo">Как работают промокоды</h2>'),
 ('Open <strong>Finance → Deposit</strong> and choose a method.', 'Откройте <strong>«Финансы» → «Пополнение»</strong> и выберите способ оплаты.'),
 ('<li>Enter the promo code in the field before confirming the payment.</li>', '<li>Введите промокод в специальное поле до подтверждения платежа.</li>'),
 ('The bonus is credited with your deposit and its progress appears under <strong>Promo codes</strong>.', 'Бонус зачислится вместе с депозитом, а прогресс отыгрыша появится в разделе <strong>«Промокоды»</strong>.'),
 ('''You can also tick a bonus offer shown on the deposit screen instead of typing a code. Only one deposit bonus can be
    active at a time.''', '''Вместо ввода кода можно просто отметить бонусное предложение на экране пополнения. Одновременно может быть активен
    только один бонус на депозит.'''),
 ('<h2 id="rules">Bonus rules to know</h2>', '<h2 id="rules">Правила бонусов</h2>'),
 ('<strong>Turnover:</strong> a deposit bonus must be traded a set number of times before it can be withdrawn.', '<strong>Отыгрыш:</strong> бонус на депозит нужно прокрутить определённое количество раз, прежде чем его можно вывести.'),
 ('''<strong>Withdrawing early:</strong> if you withdraw while the bonus is still active, the bonus amount is deducted
      from your balance.''', '''<strong>Ранний вывод:</strong> если вывести деньги, пока бонус активен, его сумма спишется с баланса.'''),
 ('<strong>Expiry:</strong> unused codes and bonuses can expire.', '<strong>Срок действия:</strong> неиспользованные промокоды и бонусы могут сгореть.'),
 ('<strong>Declining:</strong> you can always deposit without a bonus. Many traders prefer this for full flexibility.', '<strong>Отказ:</strong> пополнять счёт без бонуса можно всегда. Многие трейдеры так и делают, чтобы выводить в любой момент.'),
 ('''Check the turnover multiplier shown with each offer. A higher bonus percentage usually comes with a higher turnover
    requirement.''', '''Смотрите на множитель отыгрыша в каждом предложении. Чем больше процент бонуса, тем обычно выше требования к обороту.'''),
 ('<h2 id="worth">Is a bonus worth it?</h2>', '<h2 id="worth">Стоит ли брать бонус?</h2>'),
 ('''A bonus helps if you plan to trade actively for a while and are comfortable with the turnover rule. If you want the
    option to withdraw at any time, deposit without one. Either way, practise first on the{" "}
    <a href="/demo-account/">free demo</a>.''', '''Бонус имеет смысл, если вы планируете активно торговать какое-то время и вас устраивают условия отыгрыша. Если
    важно выводить деньги в любой момент, пополняйте без бонуса. В любом случае сначала потренируйтесь на{" "}
    <a href="/demo-account/">бесплатном демо-счёте</a>.'''),
 ('See the current offers in your Pocket Option account →', 'Актуальные предложения в личном кабинете Pocket Option →'),
]
UA = [
 ('"Types of bonuses" }', '"Види бонусів" }'), ('"How promo codes work" }', '"Як працюють промокоди" }'),
 ('"Bonus rules to know" }', '"Правила бонусів" }'), ('"Is a bonus worth it?" }', '"Чи варто брати бонус?" }'),
 ('title="Pocket Option Promo Code & Bonus 2026: How They Work"', 'title="Промокод Pocket Option і бонуси 2026: як вони працюють"'),
 ('description="Pocket Option promo codes and deposit bonuses explained: bonus sizes, cashback, tournaments and the turnover rules to meet before you can withdraw."',
  'description="Промокоди й бонуси на депозит Pocket Option: розмір бонусу, кешбек, турніри та умови відпрацювання, які треба виконати до виведення."'),
 ('h1="Pocket Option promo codes and bonuses"', 'h1="Промокоди та бонуси Pocket Option"'),
 ('lead="Deposit bonuses, cashback, tournaments and achievements can add value, but every bonus comes with conditions. Read these before you enter a code."',
  'lead="Бонуси на депозит, кешбек, турніри й досягнення можуть бути вигідними, але кожен бонус має умови. Прочитайте їх, перш ніж вводити промокод."'),
 ('crumb="Bonus & promo codes"', 'crumb="Бонуси та промокоди"'),
 ('<h2 id="types">Types of bonuses</h2>', '<h2 id="types">Види бонусів</h2>'),
 ('<th>Bonus</th>\n        <th>What it does</th>', '<th>Бонус</th>\n        <th>Що дає</th>'),
 ('<td>Deposit promo code</td>\n        <td>Adds a percentage on top of your deposit as bonus funds.</td>', '<td>Промокод на депозит</td>\n        <td>Нараховує відсоток понад депозит бонусними коштами.</td>'),
 ('<td>Cashback</td>\n        <td>Returns part of your losses over a period to your balance.</td>', '<td>Кешбек</td>\n        <td>Повертає на баланс частину збитків за певний період.</td>'),
 ('<td>Risk-free trades</td>\n        <td>Refunds the stake of a set number of losing trades.</td>', '<td>Безризикові угоди</td>\n        <td>Повертає суму ставки за визначеною кількістю збиткових угод.</td>'),
 ('<td>Tournaments</td>\n        <td>Separate balance with prize pools; some are free to enter.</td>', '<td>Турніри</td>\n        <td>Окремий баланс і призовий фонд; у деяких участь безкоштовна.</td>'),
 ('<td>Achievements</td>\n        <td>Experience levels that unlock extra perks as you trade.</td>', '<td>Досягнення</td>\n        <td>Рівні досвіду, які в міру торгівлі відкривають додаткові привілеї.</td>'),
 ('''Offers change often and differ by account. The <strong>Promo codes</strong> and <strong>Market</strong> sections of
    your account show what is available to you right now.''', '''Акції часто змінюються й у всіх різні. Що доступно саме вам зараз, видно в розділах <strong>«Промокоди»</strong> і
    <strong>«Маркет»</strong> особистого кабінету.'''),
 ('<h2 id="promo">How promo codes work</h2>', '<h2 id="promo">Як працюють промокоди</h2>'),
 ('Open <strong>Finance → Deposit</strong> and choose a method.', 'Відкрийте <strong>«Фінанси» → «Поповнення»</strong> й оберіть спосіб оплати.'),
 ('<li>Enter the promo code in the field before confirming the payment.</li>', '<li>Введіть промокод у спеціальне поле до підтвердження платежу.</li>'),
 ('The bonus is credited with your deposit and its progress appears under <strong>Promo codes</strong>.', 'Бонус зарахується разом із депозитом, а прогрес відпрацювання з’явиться в розділі <strong>«Промокоди»</strong>.'),
 ('''You can also tick a bonus offer shown on the deposit screen instead of typing a code. Only one deposit bonus can be
    active at a time.''', '''Замість введення коду можна просто позначити бонусну пропозицію на екрані поповнення. Одночасно може бути активним
    лише один бонус на депозит.'''),
 ('<h2 id="rules">Bonus rules to know</h2>', '<h2 id="rules">Правила бонусів</h2>'),
 ('<strong>Turnover:</strong> a deposit bonus must be traded a set number of times before it can be withdrawn.', '<strong>Відпрацювання:</strong> бонус на депозит треба прокрутити певну кількість разів, перш ніж його можна вивести.'),
 ('''<strong>Withdrawing early:</strong> if you withdraw while the bonus is still active, the bonus amount is deducted
      from your balance.''', '''<strong>Раннє виведення:</strong> якщо вивести гроші, поки бонус активний, його сума спишеться з балансу.'''),
 ('<strong>Expiry:</strong> unused codes and bonuses can expire.', '<strong>Термін дії:</strong> невикористані промокоди й бонуси можуть згоріти.'),
 ('<strong>Declining:</strong> you can always deposit without a bonus. Many traders prefer this for full flexibility.', '<strong>Відмова:</strong> поповнювати рахунок без бонусу можна завжди. Багато трейдерів так і роблять, щоб виводити будь-коли.'),
 ('''Check the turnover multiplier shown with each offer. A higher bonus percentage usually comes with a higher turnover
    requirement.''', '''Дивіться на множник відпрацювання в кожній пропозиції. Що більший відсоток бонусу, то зазвичай вищі вимоги до обороту.'''),
 ('<h2 id="worth">Is a bonus worth it?</h2>', '<h2 id="worth">Чи варто брати бонус?</h2>'),
 ('''A bonus helps if you plan to trade actively for a while and are comfortable with the turnover rule. If you want the
    option to withdraw at any time, deposit without one. Either way, practise first on the{" "}
    <a href="/demo-account/">free demo</a>.''', '''Бонус має сенс, якщо ви плануєте активно торгувати якийсь час і вас влаштовують умови відпрацювання. Якщо
    важливо виводити гроші будь-коли, поповнюйте без бонусу. У будь-якому разі спершу потренуйтеся на{" "}
    <a href="/demo-account/">безкоштовному демо-рахунку</a>.'''),
 ('See the current offers in your Pocket Option account →', 'Актуальні пропозиції в особистому кабінеті Pocket Option →'),
]
for L, pairs in [("ru", RU), ("ua", UA)]:
    build("src/pages/bonus-promo-code.astro", L, pairs, f"src/pages/{L}/bonus-promo-code.astro")
