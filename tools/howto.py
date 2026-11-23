import sys; sys.path.insert(0, "tools")
from tr import build
RU = [
 ('"The trading screen" }', '"Торговый терминал" }'), ('"Your first trade" }', '"Первая сделка" }'),
 ('"Indicators and signals" }', '"Индикаторы и сигналы" }'), ('"Money management" }', '"Мани-менеджмент" }'),
 ('"Common mistakes" }', '"Типичные ошибки" }'),
 ('title="How to Trade on Pocket Option: Step-by-Step for Beginners"', 'title="Как торговать на Pocket Option: пошагово для новичков"'),
 ('description="Learn to trade on Pocket Option step by step: pick an asset, set time and amount, place your first trade, use indicators and manage risk on PocketOption."',
  'description="Как торговать на Pocket Option: выбор актива, время экспирации и сумма, первая сделка, индикаторы и мани-менеджмент. Пошаговая инструкция для новичков."'),
 ('h1="How to trade on Pocket Option"', 'h1="Как торговать на Pocket Option"'),
 ('lead="A practical walkthrough of the trading screen, your first trade and the habits that keep losses small. Follow along on the free demo."',
  'lead="Практический разбор терминала, первой сделки и привычек, которые помогают держать убытки под контролем. Повторяйте шаги на бесплатном демо-счёте."'),
 ('crumb="How to trade"', 'crumb="Как торговать"'),
 ('alt="Pocket Option trading screen with chart, time, amount and Buy/Sell buttons"', 'alt="Терминал Pocket Option: график, время, сумма и кнопки «Выше» и «Ниже»"'),
 ('The Pocket Option web platform: asset selector top left, chart in the centre, trade panel on the right.', 'Веб-платформа Pocket Option: выбор актива слева вверху, график в центре, панель сделок справа.'),
 ('<h2 id="screen">The trading screen</h2>', '<h2 id="screen">Торговый терминал</h2>'),
 ('''<strong>Asset selector</strong> (top left): pick a currency pair, crypto, stock, commodity or index. The payout
      percentage is shown next to each asset.''', '''<strong>Выбор актива</strong> (слева вверху): валютная пара, криптовалюта, акция, сырьё или индекс. Рядом с каждым
      активом указан процент выплаты.'''),
 ('<strong>Chart</strong> (centre): switch between candles, bars, line or area, and change the timeframe.', '<strong>График</strong> (в центре): японские свечи, бары, линия или область, плюс смена таймфрейма.'),
 ('''<strong>Trade panel</strong> (right): set the expiry time and the amount, then press <strong>Buy</strong> if you
      expect the price to rise or <strong>Sell</strong> if you expect it to fall.''', '''<strong>Панель сделок</strong> (справа): задайте время экспирации и сумму, затем нажмите <strong>«Выше»</strong>, если
      ждёте роста цены, или <strong>«Ниже»</strong>, если ждёте падения.'''),
 ('<strong>Trades</strong> (far right): open and closed positions with their results.', '<strong>Сделки</strong> (справа с краю): открытые и закрытые позиции с результатами.'),
 ('<h2 id="first">Your first trade</h2>', '<h2 id="first">Первая сделка</h2>'),
 ('      Open the{" "}\n', '      Откройте{" "}\n'), ('        demo account\n', '        демо-счёт\n'),
 ('<li>Choose a liquid asset such as EUR/USD.</li>', '<li>Выберите ликвидный актив, например EUR/USD.</li>'),
 ('<li>Set the chart to 1-minute candles and the expiry to 5 minutes.</li>', '<li>Поставьте минутные свечи (M1) и экспирацию 5 минут.</li>'),
 ('<li>Set the amount to $1 to $5, the same as you would on a small real account.</li>', '<li>Сумма сделки — $1–5, как на небольшом реальном счёте.</li>'),
 ('<li>Look at the trend over the last 30 to 60 candles. Press Buy or Sell only if the direction is clear.</li>', '<li>Оцените тренд по последним 30–60 свечам. Нажимайте «Выше» или «Ниже», только если направление очевидно.</li>'),
 ('''Wait for expiry. If your forecast is right, the stake plus the payout is added to your balance; if not, the stake
      is lost.''', '''Дождитесь экспирации. Если прогноз сыграл, на баланс вернётся ставка плюс выплата; если нет — ставка сгорает.'''),
 ('<h2 id="tools">Indicators and signals</h2>', '<h2 id="tools">Индикаторы и сигналы</h2>'),
 ('''Pocket Option includes the standard toolkit: moving averages, RSI, MACD, Bollinger Bands, Stochastic and more, plus
    drawing tools for trend lines and levels. Built-in signals suggest a direction and timeframe based on technical
    analysis.''', '''В Pocket Option есть стандартный набор: скользящие средние, RSI, MACD, полосы Боллинджера, стохастик и другие, а также
    инструменты для трендовых линий и уровней. Встроенные сигналы подсказывают направление и таймфрейм на основе
    технического анализа.'''),
 ('''Start with one trend tool (a moving average) and one momentum tool (RSI). Adding more indicators rarely improves
    results and makes charts harder to read. Treat signals as a second opinion, not an instruction.''', '''Начните с одного трендового индикатора (скользящая средняя) и одного осциллятора (RSI). Лишние индикаторы редко
    улучшают результат, зато мешают читать график. Сигналы — это второе мнение, а не команда к действию.'''),
 ('<h2 id="risk">Money management</h2>', '<h2 id="risk">Мани-менеджмент</h2>'),
 ('<th>Rule</th>\n        <th>Why it matters</th>', '<th>Правило</th>\n        <th>Зачем это нужно</th>'),
 ('<td>Risk 1–2% of your balance per trade</td>\n        <td>A losing streak will not wipe out your account.</td>', '<td>Риск 1–2% депозита на сделку</td>\n        <td>Серия убыточных сделок не обнулит депозит.</td>'),
 ('<td>Set a daily loss limit</td>\n        <td>Stops emotional trading after bad results.</td>', '<td>Дневной лимит убытков</td>\n        <td>Не даёт торговать на эмоциях после неудачного дня.</td>'),
 ('<td>Trade fixed amounts</td>\n        <td>Avoids doubling up to win back losses.</td>', '<td>Фиксированная сумма сделки</td>\n        <td>Защищает от удвоения ставок, чтобы отыграться.</td>'),
 ('<td>Check the payout first</td>\n        <td>At 80% payout you need to win about 56% of trades to break even.</td>', '<td>Сначала смотрите на выплату</td>\n        <td>При выплате 80% нужно закрывать в плюс около 56% сделок, чтобы выйти в ноль.</td>'),
 ('<h2 id="mistakes">Common mistakes</h2>', '<h2 id="mistakes">Типичные ошибки</h2>'),
 ('<li>Moving to real money after a few lucky demo trades.</li>', '<li>Переход на реал после пары удачных сделок на демо.</li>'),
 ('<li>Using very short expiries (5–30 seconds), where results are close to random.</li>', '<li>Сверхкороткие экспирации (5–30 секунд), где результат почти случаен.</li>'),
 ('<li>Martingale: doubling the stake after each loss.</li>', '<li>Мартингейл: удвоение ставки после каждого убытка.</li>'),
 ('<li>Trading during major news without a plan.</li>', '<li>Торговля на сильных новостях без плана.</li>'),
 ('<li>Ignoring the payout percentage, especially on OTC assets.</li>', '<li>Игнорирование процента выплаты, особенно на OTC-активах.</li>'),
 ('''Learn the platform first with the <a href="/demo-account/">demo account tips</a>, then read about{" "}
    <a href="/deposit-withdrawal/">deposits and withdrawals</a> when you are ready.''', '''Сначала освойте платформу с нашими <a href="/demo-account/">советами по демо-счёту</a>, а когда будете готовы —
    прочитайте про{" "}<a href="/deposit-withdrawal/">пополнение и вывод средств</a>.'''),
]
UA = [
 ('"The trading screen" }', '"Торговий термінал" }'), ('"Your first trade" }', '"Перша угода" }'),
 ('"Indicators and signals" }', '"Індикатори та сигнали" }'), ('"Money management" }', '"Мані-менеджмент" }'),
 ('"Common mistakes" }', '"Типові помилки" }'),
 ('title="How to Trade on Pocket Option: Step-by-Step for Beginners"', 'title="Як торгувати на Pocket Option: покроково для новачків"'),
 ('description="Learn to trade on Pocket Option step by step: pick an asset, set time and amount, place your first trade, use indicators and manage risk on PocketOption."',
  'description="Як торгувати на Pocket Option: вибір активу, час експірації та сума, перша угода, індикатори й мані-менеджмент. Покрокова інструкція для новачків."'),
 ('h1="How to trade on Pocket Option"', 'h1="Як торгувати на Pocket Option"'),
 ('lead="A practical walkthrough of the trading screen, your first trade and the habits that keep losses small. Follow along on the free demo."',
  'lead="Практичний розбір термінала, першої угоди та звичок, які допомагають тримати збитки під контролем. Повторюйте кроки на безкоштовному демо-рахунку."'),
 ('crumb="How to trade"', 'crumb="Як торгувати"'),
 ('alt="Pocket Option trading screen with chart, time, amount and Buy/Sell buttons"', 'alt="Термінал Pocket Option: графік, час, сума й кнопки «Вище» та «Нижче»"'),
 ('The Pocket Option web platform: asset selector top left, chart in the centre, trade panel on the right.', 'Вебплатформа Pocket Option: вибір активу ліворуч угорі, графік у центрі, панель угод праворуч.'),
 ('<h2 id="screen">The trading screen</h2>', '<h2 id="screen">Торговий термінал</h2>'),
 ('''<strong>Asset selector</strong> (top left): pick a currency pair, crypto, stock, commodity or index. The payout
      percentage is shown next to each asset.''', '''<strong>Вибір активу</strong> (ліворуч угорі): валютна пара, криптовалюта, акція, сировина чи індекс. Поруч із
      кожним активом указано відсоток виплати.'''),
 ('<strong>Chart</strong> (centre): switch between candles, bars, line or area, and change the timeframe.', '<strong>Графік</strong> (у центрі): японські свічки, бари, лінія чи область, плюс зміна таймфрейму.'),
 ('''<strong>Trade panel</strong> (right): set the expiry time and the amount, then press <strong>Buy</strong> if you
      expect the price to rise or <strong>Sell</strong> if you expect it to fall.''', '''<strong>Панель угод</strong> (праворуч): задайте час експірації й суму, потім натисніть <strong>«Вище»</strong>, якщо
      чекаєте зростання ціни, або <strong>«Нижче»</strong>, якщо чекаєте падіння.'''),
 ('<strong>Trades</strong> (far right): open and closed positions with their results.', '<strong>Угоди</strong> (праворуч із краю): відкриті й закриті позиції з результатами.'),
 ('<h2 id="first">Your first trade</h2>', '<h2 id="first">Перша угода</h2>'),
 ('      Open the{" "}\n', '      Відкрийте{" "}\n'), ('        demo account\n', '        демо-рахунок\n'),
 ('<li>Choose a liquid asset such as EUR/USD.</li>', '<li>Оберіть ліквідний актив, наприклад EUR/USD.</li>'),
 ('<li>Set the chart to 1-minute candles and the expiry to 5 minutes.</li>', '<li>Поставте хвилинні свічки (M1) та експірацію 5 хвилин.</li>'),
 ('<li>Set the amount to $1 to $5, the same as you would on a small real account.</li>', '<li>Сума угоди — $1–5, як на невеликому реальному рахунку.</li>'),
 ('<li>Look at the trend over the last 30 to 60 candles. Press Buy or Sell only if the direction is clear.</li>', '<li>Оцініть тренд за останніми 30–60 свічками. Натискайте «Вище» чи «Нижче», лише якщо напрямок очевидний.</li>'),
 ('''Wait for expiry. If your forecast is right, the stake plus the payout is added to your balance; if not, the stake
      is lost.''', '''Дочекайтеся експірації. Якщо прогноз зіграв, на баланс повернеться ставка плюс виплата; якщо ні — ставка згорає.'''),
 ('<h2 id="tools">Indicators and signals</h2>', '<h2 id="tools">Індикатори та сигнали</h2>'),
 ('''Pocket Option includes the standard toolkit: moving averages, RSI, MACD, Bollinger Bands, Stochastic and more, plus
    drawing tools for trend lines and levels. Built-in signals suggest a direction and timeframe based on technical
    analysis.''', '''У Pocket Option є стандартний набір: ковзні середні, RSI, MACD, смуги Боллінджера, стохастик та інші, а також
    інструменти для трендових ліній і рівнів. Вбудовані сигнали підказують напрямок і таймфрейм на основі технічного
    аналізу.'''),
 ('''Start with one trend tool (a moving average) and one momentum tool (RSI). Adding more indicators rarely improves
    results and makes charts harder to read. Treat signals as a second opinion, not an instruction.''', '''Почніть з одного трендового індикатора (ковзна середня) та одного осцилятора (RSI). Зайві індикатори рідко
    покращують результат, зате заважають читати графік. Сигнали — це друга думка, а не команда до дії.'''),
 ('<h2 id="risk">Money management</h2>', '<h2 id="risk">Мані-менеджмент</h2>'),
 ('<th>Rule</th>\n        <th>Why it matters</th>', '<th>Правило</th>\n        <th>Навіщо це потрібно</th>'),
 ('<td>Risk 1–2% of your balance per trade</td>\n        <td>A losing streak will not wipe out your account.</td>', '<td>Ризик 1–2% депозиту на угоду</td>\n        <td>Серія збиткових угод не обнулить депозит.</td>'),
 ('<td>Set a daily loss limit</td>\n        <td>Stops emotional trading after bad results.</td>', '<td>Денний ліміт збитків</td>\n        <td>Не дає торгувати на емоціях після невдалого дня.</td>'),
 ('<td>Trade fixed amounts</td>\n        <td>Avoids doubling up to win back losses.</td>', '<td>Фіксована сума угоди</td>\n        <td>Захищає від подвоєння ставок, щоб відігратися.</td>'),
 ('<td>Check the payout first</td>\n        <td>At 80% payout you need to win about 56% of trades to break even.</td>', '<td>Спершу дивіться на виплату</td>\n        <td>За виплати 80% треба закривати в плюс близько 56% угод, щоб вийти в нуль.</td>'),
 ('<h2 id="mistakes">Common mistakes</h2>', '<h2 id="mistakes">Типові помилки</h2>'),
 ('<li>Moving to real money after a few lucky demo trades.</li>', '<li>Перехід на реал після кількох вдалих угод на демо.</li>'),
 ('<li>Using very short expiries (5–30 seconds), where results are close to random.</li>', '<li>Надкороткі експірації (5–30 секунд), де результат майже випадковий.</li>'),
 ('<li>Martingale: doubling the stake after each loss.</li>', '<li>Мартингейл: подвоєння ставки після кожного збитку.</li>'),
 ('<li>Trading during major news without a plan.</li>', '<li>Торгівля на сильних новинах без плану.</li>'),
 ('<li>Ignoring the payout percentage, especially on OTC assets.</li>', '<li>Ігнорування відсотка виплати, особливо на OTC-активах.</li>'),
 ('''Learn the platform first with the <a href="/demo-account/">demo account tips</a>, then read about{" "}
    <a href="/deposit-withdrawal/">deposits and withdrawals</a> when you are ready.''', '''Спершу опануйте платформу з нашими <a href="/demo-account/">порадами щодо демо-рахунку</a>, а коли будете готові —
    прочитайте про{" "}<a href="/deposit-withdrawal/">поповнення та виведення коштів</a>.'''),
]
for L, pairs in [("ru", RU), ("ua", UA)]:
    build("src/pages/how-to-trade.astro", L, pairs, f"src/pages/{L}/how-to-trade.astro")
