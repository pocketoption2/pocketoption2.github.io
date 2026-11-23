import sys; sys.path.insert(0, "tools")
from tr import build
RU = [
 ('"Verdict" }', '"Вердикт" }'), ('"Company and availability" }', '"Компания и доступность" }'),
 ('"Platform and trading" }', '"Платформа и торговля" }'), ('"Costs and payouts" }', '"Комиссии и выплаты" }'),
 ('"Deposits and withdrawals" }', '"Пополнение и вывод" }'), ('"Is Pocket Option safe?" }', '"Можно ли доверять Pocket Option?" }'),
 ('"Who it suits" }', '"Кому подойдёт" }'),
 ('title="Pocket Option Review 2026: Is PocketOption Legit & Safe?"', 'title="Обзор Pocket Option 2026: отзывы, надёжность, плюсы и минусы"'),
 ('description="Our Pocket Option review for 2026: regulation, payouts, fees, deposits, withdrawals and the demo account, plus the pros, cons and risks before you sign up."',
  'description="Честный обзор Pocket Option 2026: регулирование, выплаты, комиссии, пополнение, вывод и демо-счёт, плюсы, минусы и риски до регистрации."'),
 ('h1="Pocket Option review: is it worth your money?"', 'h1="Обзор Pocket Option: стоит ли доверять свои деньги?"'),
 ('lead="We tested the platform on the demo and went through the account, deposit and withdrawal rules. Here is what Pocket Option does well, where it falls short and who it is for."',
  'lead="Мы протестировали платформу на демо и разобрали правила по аккаунту, пополнению и выводу. Рассказываем, в чём Pocket Option хорош, где проседает и кому подойдёт."'),
 ('crumb="Review"', 'crumb="Обзор"'),
 ('<h2 id="verdict">Verdict</h2>', '<h2 id="verdict">Вердикт</h2>'),
 ('''Pocket Option is one of the easiest brokers to start with: a <strong>$5 minimum deposit</strong>,{" "}
    <strong>$1 trades</strong> and a demo account that opens without registration. The web platform is fast and clean,
    payment options are unusually broad, and social trading is built in.''', '''Pocket Option — один из самых простых брокеров для старта: <strong>минимальный депозит $5</strong>,{" "}
    <strong>сделки от $1</strong> и демо-счёт без регистрации. Веб-платформа быстрая и аккуратная, выбор способов оплаты
    необычно широкий, а копитрейдинг встроен прямо в терминал.'''),
 ('''The trade-off is regulation. Pocket Option is an offshore broker, and short-term fixed-time trading is high risk by
    design. It is a reasonable choice for practising and trading small amounts, not a place to park savings.''', '''Обратная сторона — регулирование. Pocket Option — офшорный брокер, а краткосрочная торговля с фиксированным временем
    рискованна по своей природе. Это разумный выбор, чтобы учиться и торговать небольшими суммами, но не место для
    хранения сбережений.'''),
 ('<th>Area</th>\n        <th>Our take</th>', '<th>Критерий</th>\n        <th>Наша оценка</th>'),
 ('<td>Ease of use</td>\n        <td>Excellent. One-click demo, clear interface on web and mobile.</td>', '<td>Удобство</td>\n        <td>Отлично. Демо в один клик, понятный интерфейс в браузере и на телефоне.</td>'),
 ('<td>Costs</td>\n        <td>No deposit or withdrawal commission from Pocket Option. Payouts up to 92% per trade.</td>', '<td>Комиссии</td>\n        <td>Pocket Option не берёт комиссию за ввод и вывод. Выплата до 92% за сделку.</td>'),
 ('<td>Payments</td>\n        <td>170+ methods including cards, e-wallets, mobile money and crypto.</td>', '<td>Платежи</td>\n        <td>170+ способов: карты, электронные кошельки, мобильные платежи и крипта.</td>'),
 ('<td>Tools</td>\n        <td>Indicators, signals, copy trading, pending and express trades.</td>', '<td>Инструменты</td>\n        <td>Индикаторы, сигналы, копитрейдинг, отложенные и экспресс-сделки.</td>'),
 ('<td>Regulation</td>\n        <td>Offshore. Not overseen by a tier-1 regulator.</td>', '<td>Регулирование</td>\n        <td>Офшор. Нет надзора регулятора первого уровня.</td>'),
 ('<h2 id="company">Company and availability</h2>', '<h2 id="company">Компания и доступность</h2>'),
 ('''Pocket Option launched in 2017. By its own figures it passed one million users in 2018 and more than 10 million
    registered users in 2019. The site and platform are available in over 40 languages.''', '''Pocket Option работает с 2017 года. По данным самой компании, в 2018 году у неё был уже миллион пользователей, а в
    2019-м — более 10 миллионов зарегистрированных. Сайт и платформа доступны более чем на 40 языках, включая русский.'''),
 ('''The broker does not accept clients from the{" "}
    <strong>EEA, the USA, the UK, Israel, Japan, the Philippines and Brazil</strong>. If you live in one of these
    countries, you will not be able to open a real account, and you should not try to work around the restriction.''', '''Брокер не принимает клиентов из{" "}
    <strong>стран ЕЭЗ, США, Великобритании, Израиля, Японии, Филиппин и Бразилии</strong>. Если вы живёте в одной из
    этих стран, открыть реальный счёт не получится, и обходить ограничение не стоит.'''),
 ('<h2 id="platform">Platform and trading</h2>', '<h2 id="platform">Платформа и торговля</h2>'),
 ('''Everything runs in the browser, so there is nothing to install on a desktop. The same account works on the{" "}
    <a href="/app/">Android app, the iPhone web app and the Telegram bot</a>. Charts load quickly, and switching assets
    or timeframes takes a click.''', '''Всё работает в браузере, поэтому на компьютер ничего ставить не нужно. Тот же аккаунт работает в{" "}
    <a href="/app/">приложении для Android, веб-приложении для iPhone и Telegram-боте</a>. Графики грузятся быстро, а
    сменить актив или таймфрейм можно в один клик.'''),
 ('<h3>Trade types</h3>', '<h3>Типы сделок</h3>'),
 ('''<strong>Quick trading:</strong> forecast whether the price will be higher or lower after a set time, from a few
      seconds to several hours.''', '''<strong>Быстрая торговля:</strong> прогноз, будет ли цена выше или ниже через заданное время — от нескольких
      секунд до нескольких часов.'''),
 ('<strong>Pending trades:</strong> open a position automatically when the price or time you set is reached.', '<strong>Отложенные сделки:</strong> позиция открывается автоматически при достижении заданной цены или времени.'),
 ('<strong>Express trades:</strong> combine several forecasts; all must be correct, and the payout can reach 218%.', '<strong>Экспресс-сделки:</strong> несколько прогнозов в одной сделке; сыграть должны все, зато выплата доходит до 218%.'),
 ('<strong>Social trading:</strong> copy the trades of other users automatically.', '<strong>Копитрейдинг:</strong> автоматическое копирование сделок других трейдеров.'),
 ('<h3>Assets</h3>', '<h3>Активы</h3>'),
 ('''More than 100 instruments: major and minor currency pairs, cryptocurrencies, stocks such as Apple and Tesla,
    commodities like gold and oil, and indices. OTC versions of popular assets remain open on weekends, with prices
    quoted by the broker rather than an exchange.''', '''Более 100 инструментов: основные и второстепенные валютные пары, криптовалюты, акции вроде Apple и Tesla, сырьё —
    золото и нефть, а также индексы. OTC-версии популярных активов торгуются и в выходные, но котировки на них даёт
    брокер, а не биржа.'''),
 ('<h2 id="costs">Costs and payouts</h2>', '<h2 id="costs">Комиссии и выплаты</h2>'),
 ('''Pocket Option does not charge commission on deposits or withdrawals, although your bank or payment provider may. The
    broker earns from the difference between what traders win and lose, which is why the payout on a correct forecast is
    less than 100% of the stake.''', '''Pocket Option не берёт комиссию за пополнение и вывод, хотя её может удержать ваш банк или платёжная система.
    Брокер зарабатывает на разнице между выигрышами и проигрышами трейдеров, поэтому выплата за верный прогноз меньше
    100% от ставки.'''),
 ('''Payouts vary by asset and time of day, typically between 70% and 92% on major pairs. OTC assets and quieter hours
    tend to pay less. Always check the figure shown above the Buy and Sell buttons before opening a trade.''', '''Процент выплаты зависит от актива и времени суток: на основных парах обычно от 70% до 92%. На OTC-активах и в
    спокойные часы платят меньше. Перед сделкой всегда смотрите на цифру над кнопками «Выше» и «Ниже».'''),
 ('<h2 id="money">Deposits and withdrawals</h2>', '<h2 id="money">Пополнение и вывод</h2>'),
 ('''The minimum deposit is $5 for most methods. Deposits are usually credited within minutes. Withdrawals require a
    verified account and are paid back to a method you used to deposit, in line with anti-money-laundering rules. Pocket
    Option sets no minimum withdrawal amount when no deposit bonus is active. Our{" "}
    <a href="/deposit-withdrawal/">deposits and withdrawals page</a> explains each step.''', '''Минимальный депозит — $5 для большинства способов, деньги обычно зачисляются за несколько минут. Для вывода нужен
    верифицированный аккаунт, а деньги по правилам AML уходят тем же способом, которым вы пополняли счёт. Если активного
    бонуса нет, минимальной суммы вывода нет. Каждый шаг разобран на странице{" "}
    <a href="/deposit-withdrawal/">пополнение и вывод средств</a>.'''),
 ('<h2 id="safety">Is Pocket Option safe?</h2>', '<h2 id="safety">Можно ли доверять Pocket Option?</h2>'),
 ('''Pocket Option has a long track record and millions of users, and most user complaints we found concern bonus
    conditions or verification delays rather than missing funds. That said, offshore brokers offer less protection than
    regulated ones: there is no investor compensation scheme, and disputes are handled by the company itself.''', '''У Pocket Option долгая история и миллионы пользователей, а большинство негативных отзывов, которые мы нашли, касаются
    условий бонусов или затянутой верификации, а не пропавших денег. При этом офшорный брокер защищает клиента слабее
    регулируемого: фонда компенсаций нет, а споры решает сама компания.'''),
 ('''Practical rule: verify your account before your first deposit, avoid bonuses you do not fully understand, and never
    trade money you need for living costs.''', '''Практическое правило: пройдите верификацию до первого депозита, не берите бонусы, условия которых вам непонятны, и
    никогда не торгуйте деньгами, нужными на жизнь.'''),
 ('<h2 id="who">Who it suits</h2>', '<h2 id="who">Кому подойдёт</h2>'),
 ('''<strong>Good fit:</strong> beginners who want to learn on a free demo, traders with small budgets, and users in
      regions where local payment methods matter.''', '''<strong>Подойдёт:</strong> новичкам, которые хотят учиться на бесплатном демо, трейдерам с небольшим депозитом и тем,
      кому важны местные способы оплаты.'''),
 ('''<strong>Poor fit:</strong> anyone who needs a tier-1 regulated broker, long-term investors, and residents of the
      restricted countries listed above.''', '''<strong>Не подойдёт:</strong> тем, кому нужен брокер с регулятором первого уровня, долгосрочным инвесторам и жителям
      перечисленных выше стран.'''),
 ('    The fastest way to decide is to{" "}\n', '    Быстрее всего определиться —{" "}\n'),
 ('      try the demo\n', '      попробовать демо\n'),
 ('. It costs nothing, and you will know within an hour whether the platform suits you.', '. Это бесплатно, и уже через час станет ясно, подходит ли вам платформа.'),
]
UA = [
 ('"Verdict" }', '"Вердикт" }'), ('"Company and availability" }', '"Компанія та доступність" }'),
 ('"Platform and trading" }', '"Платформа й торгівля" }'), ('"Costs and payouts" }', '"Комісії та виплати" }'),
 ('"Deposits and withdrawals" }', '"Поповнення і виведення" }'), ('"Is Pocket Option safe?" }', '"Чи можна довіряти Pocket Option?" }'),
 ('"Who it suits" }', '"Кому підійде" }'),
 ('title="Pocket Option Review 2026: Is PocketOption Legit & Safe?"', 'title="Огляд Pocket Option 2026: відгуки, надійність, плюси й мінуси"'),
 ('description="Our Pocket Option review for 2026: regulation, payouts, fees, deposits, withdrawals and the demo account, plus the pros, cons and risks before you sign up."',
  'description="Чесний огляд Pocket Option 2026: регулювання, виплати, комісії, поповнення, виведення й демо-рахунок, плюси, мінуси та ризики до реєстрації."'),
 ('h1="Pocket Option review: is it worth your money?"', 'h1="Огляд Pocket Option: чи варто довіряти свої гроші?"'),
 ('lead="We tested the platform on the demo and went through the account, deposit and withdrawal rules. Here is what Pocket Option does well, where it falls short and who it is for."',
  'lead="Ми протестували платформу на демо й розібрали правила щодо акаунта, поповнення та виведення. Розповідаємо, у чому Pocket Option сильний, де просідає і кому підійде."'),
 ('crumb="Review"', 'crumb="Огляд"'),
 ('<h2 id="verdict">Verdict</h2>', '<h2 id="verdict">Вердикт</h2>'),
 ('''Pocket Option is one of the easiest brokers to start with: a <strong>$5 minimum deposit</strong>,{" "}
    <strong>$1 trades</strong> and a demo account that opens without registration. The web platform is fast and clean,
    payment options are unusually broad, and social trading is built in.''', '''Pocket Option — один із найпростіших брокерів для старту: <strong>мінімальний депозит $5</strong>,{" "}
    <strong>угоди від $1</strong> і демо-рахунок без реєстрації. Вебплатформа швидка й охайна, вибір способів оплати
    напрочуд широкий, а копітрейдинг вбудовано просто в термінал.'''),
 ('''The trade-off is regulation. Pocket Option is an offshore broker, and short-term fixed-time trading is high risk by
    design. It is a reasonable choice for practising and trading small amounts, not a place to park savings.''', '''Зворотний бік — регулювання. Pocket Option — офшорний брокер, а короткострокова торгівля з фіксованим часом
    ризикована за своєю природою. Це розумний вибір, щоб навчатися й торгувати невеликими сумами, але не місце для
    зберігання заощаджень.'''),
 ('<th>Area</th>\n        <th>Our take</th>', '<th>Критерій</th>\n        <th>Наша оцінка</th>'),
 ('<td>Ease of use</td>\n        <td>Excellent. One-click demo, clear interface on web and mobile.</td>', '<td>Зручність</td>\n        <td>Відмінно. Демо в один клік, зрозумілий інтерфейс у браузері й на телефоні.</td>'),
 ('<td>Costs</td>\n        <td>No deposit or withdrawal commission from Pocket Option. Payouts up to 92% per trade.</td>', '<td>Комісії</td>\n        <td>Pocket Option не бере комісію за введення й виведення. Виплата до 92% за угоду.</td>'),
 ('<td>Payments</td>\n        <td>170+ methods including cards, e-wallets, mobile money and crypto.</td>', '<td>Платежі</td>\n        <td>170+ способів: картки, електронні гаманці, мобільні платежі й крипта.</td>'),
 ('<td>Tools</td>\n        <td>Indicators, signals, copy trading, pending and express trades.</td>', '<td>Інструменти</td>\n        <td>Індикатори, сигнали, копітрейдинг, відкладені й експрес-угоди.</td>'),
 ('<td>Regulation</td>\n        <td>Offshore. Not overseen by a tier-1 regulator.</td>', '<td>Регулювання</td>\n        <td>Офшор. Немає нагляду регулятора першого рівня.</td>'),
 ('<h2 id="company">Company and availability</h2>', '<h2 id="company">Компанія та доступність</h2>'),
 ('''Pocket Option launched in 2017. By its own figures it passed one million users in 2018 and more than 10 million
    registered users in 2019. The site and platform are available in over 40 languages.''', '''Pocket Option працює з 2017 року. За даними самої компанії, у 2018 році в неї вже був мільйон користувачів, а у
    2019-му — понад 10 мільйонів зареєстрованих. Сайт і платформа доступні понад 40 мовами, зокрема українською.'''),
 ('''The broker does not accept clients from the{" "}
    <strong>EEA, the USA, the UK, Israel, Japan, the Philippines and Brazil</strong>. If you live in one of these
    countries, you will not be able to open a real account, and you should not try to work around the restriction.''', '''Брокер не приймає клієнтів із{" "}
    <strong>країн ЄЕЗ, США, Великої Британії, Ізраїлю, Японії, Філіппін і Бразилії</strong>. Якщо ви живете в одній із
    цих країн, відкрити реальний рахунок не вийде, і обходити обмеження не варто.'''),
 ('<h2 id="platform">Platform and trading</h2>', '<h2 id="platform">Платформа й торгівля</h2>'),
 ('''Everything runs in the browser, so there is nothing to install on a desktop. The same account works on the{" "}
    <a href="/app/">Android app, the iPhone web app and the Telegram bot</a>. Charts load quickly, and switching assets
    or timeframes takes a click.''', '''Усе працює в браузері, тож на комп’ютер нічого встановлювати не треба. Той самий акаунт працює в{" "}
    <a href="/app/">застосунку для Android, вебзастосунку для iPhone і Telegram-боті</a>. Графіки вантажаться швидко, а
    змінити актив чи таймфрейм можна в один клік.'''),
 ('<h3>Trade types</h3>', '<h3>Типи угод</h3>'),
 ('''<strong>Quick trading:</strong> forecast whether the price will be higher or lower after a set time, from a few
      seconds to several hours.''', '''<strong>Швидка торгівля:</strong> прогноз, чи буде ціна вищою або нижчою через заданий час — від кількох секунд
      до кількох годин.'''),
 ('<strong>Pending trades:</strong> open a position automatically when the price or time you set is reached.', '<strong>Відкладені угоди:</strong> позиція відкривається автоматично, коли досягнуто заданої ціни чи часу.'),
 ('<strong>Express trades:</strong> combine several forecasts; all must be correct, and the payout can reach 218%.', '<strong>Експрес-угоди:</strong> кілька прогнозів в одній угоді; зіграти мають усі, зате виплата сягає 218%.'),
 ('<strong>Social trading:</strong> copy the trades of other users automatically.', '<strong>Копітрейдинг:</strong> автоматичне копіювання угод інших трейдерів.'),
 ('<h3>Assets</h3>', '<h3>Активи</h3>'),
 ('''More than 100 instruments: major and minor currency pairs, cryptocurrencies, stocks such as Apple and Tesla,
    commodities like gold and oil, and indices. OTC versions of popular assets remain open on weekends, with prices
    quoted by the broker rather than an exchange.''', '''Понад 100 інструментів: основні та другорядні валютні пари, криптовалюти, акції на кшталт Apple і Tesla, сировина —
    золото й нафта, а також індекси. OTC-версії популярних активів торгуються й у вихідні, але котирування на них дає
    брокер, а не біржа.'''),
 ('<h2 id="costs">Costs and payouts</h2>', '<h2 id="costs">Комісії та виплати</h2>'),
 ('''Pocket Option does not charge commission on deposits or withdrawals, although your bank or payment provider may. The
    broker earns from the difference between what traders win and lose, which is why the payout on a correct forecast is
    less than 100% of the stake.''', '''Pocket Option не бере комісію за поповнення й виведення, хоча її може утримати ваш банк чи платіжна система.
    Брокер заробляє на різниці між виграшами та програшами трейдерів, тому виплата за правильний прогноз менша за 100%
    від ставки.'''),
 ('''Payouts vary by asset and time of day, typically between 70% and 92% on major pairs. OTC assets and quieter hours
    tend to pay less. Always check the figure shown above the Buy and Sell buttons before opening a trade.''', '''Відсоток виплати залежить від активу й часу доби: на основних парах зазвичай від 70% до 92%. На OTC-активах і в
    спокійні години платять менше. Перед угодою завжди дивіться на цифру над кнопками «Вище» та «Нижче».'''),
 ('<h2 id="money">Deposits and withdrawals</h2>', '<h2 id="money">Поповнення і виведення</h2>'),
 ('''The minimum deposit is $5 for most methods. Deposits are usually credited within minutes. Withdrawals require a
    verified account and are paid back to a method you used to deposit, in line with anti-money-laundering rules. Pocket
    Option sets no minimum withdrawal amount when no deposit bonus is active. Our{" "}
    <a href="/deposit-withdrawal/">deposits and withdrawals page</a> explains each step.''', '''Мінімальний депозит — $5 для більшості способів, гроші зазвичай зараховуються за кілька хвилин. Для виведення потрібен
    верифікований акаунт, а гроші за правилами AML ідуть тим самим способом, яким ви поповнювали рахунок. Якщо активного
    бонусу немає, мінімальної суми виведення немає. Кожен крок розібрано на сторінці{" "}
    <a href="/deposit-withdrawal/">поповнення та виведення коштів</a>.'''),
 ('<h2 id="safety">Is Pocket Option safe?</h2>', '<h2 id="safety">Чи можна довіряти Pocket Option?</h2>'),
 ('''Pocket Option has a long track record and millions of users, and most user complaints we found concern bonus
    conditions or verification delays rather than missing funds. That said, offshore brokers offer less protection than
    regulated ones: there is no investor compensation scheme, and disputes are handled by the company itself.''', '''Pocket Option має довгу історію й мільйони користувачів, а більшість негативних відгуків, які ми знайшли, стосуються
    умов бонусів або затягнутої верифікації, а не зниклих грошей. Водночас офшорний брокер захищає клієнта слабше за
    регульованого: фонду компенсацій немає, а суперечки вирішує сама компанія.'''),
 ('''Practical rule: verify your account before your first deposit, avoid bonuses you do not fully understand, and never
    trade money you need for living costs.''', '''Практичне правило: пройдіть верифікацію до першого депозиту, не беріть бонуси, умови яких вам незрозумілі, і
    ніколи не торгуйте грошима, потрібними на життя.'''),
 ('<h2 id="who">Who it suits</h2>', '<h2 id="who">Кому підійде</h2>'),
 ('''<strong>Good fit:</strong> beginners who want to learn on a free demo, traders with small budgets, and users in
      regions where local payment methods matter.''', '''<strong>Підійде:</strong> новачкам, які хочуть навчатися на безкоштовному демо, трейдерам із невеликим депозитом і тим,
      кому важливі місцеві способи оплати.'''),
 ('''<strong>Poor fit:</strong> anyone who needs a tier-1 regulated broker, long-term investors, and residents of the
      restricted countries listed above.''', '''<strong>Не підійде:</strong> тим, кому потрібен брокер із регулятором першого рівня, довгостроковим інвесторам і
      мешканцям перелічених вище країн.'''),
 ('    The fastest way to decide is to{" "}\n', '    Найшвидше визначитися —{" "}\n'),
 ('      try the demo\n', '      спробувати демо\n'),
 ('. It costs nothing, and you will know within an hour whether the platform suits you.', '. Це безкоштовно, і вже за годину стане зрозуміло, чи підходить вам платформа.'),
]
for L, pairs in [("ru", RU), ("ua", UA)]:
    build("src/pages/review.astro", L, pairs, f"src/pages/{L}/review.astro")
