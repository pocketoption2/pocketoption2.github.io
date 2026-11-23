import sys; sys.path.insert(0, "tools")
from tr import build
RU = [
 ('"Payment methods" }', '"Способы оплаты" }'), ('"How to deposit" }', '"Как пополнить счёт" }'),
 ('"Verification" }', '"Верификация" }'), ('"How to withdraw" }', '"Как вывести деньги" }'),
 ('"Fees and timing" }', '"Комиссии и сроки" }'), ('"If a payment is delayed" }', '"Если платёж задерживается" }'),
 ('title="Pocket Option Deposit & Withdrawal: Methods, Fees, Times"', 'title="Pocket Option: пополнение и вывод средств, комиссии и сроки"'),
 ('description="Deposit from $5 with 170+ payment methods and withdraw with no Pocket Option fees. Cards, e-wallets, crypto, verification and payout times explained."',
  'description="Пополнение от $5 через 170+ способов оплаты и вывод без комиссии Pocket Option. Карты, электронные кошельки, крипта, верификация и сроки выплат."'),
 ('h1="Pocket Option deposits and withdrawals"', 'h1="Пополнение и вывод средств в Pocket Option"'),
 ('lead="Deposits start at $5 and Pocket Option charges no commission either way. Here is how to fund your account, get verified and withdraw without delays."',
  'lead="Депозит — от $5, комиссии Pocket Option нет ни на ввод, ни на вывод. Разбираем, как пополнить счёт, пройти верификацию и выводить деньги без задержек."'),
 ('crumb="Deposits & withdrawals"', 'crumb="Пополнение и вывод"'),
 ('<h2 id="methods">Payment methods</h2>', '<h2 id="methods">Способы оплаты</h2>'),
 ('''Pocket Option lists more than 170 payment methods. What you see in your account depends on your country and
    currency.''', '''У Pocket Option более 170 способов оплаты. Какие из них доступны именно вам, зависит от страны и валюты счёта.'''),
 ('<strong>Cards:</strong> Visa, Mastercard and local card schemes.', '<strong>Банковские карты:</strong> Visa, Mastercard и местные платёжные системы.'),
 ('<strong>E-wallets:</strong> Jeton, Volet, WebMoney, Apple Pay, Google Pay, Paytm, GrabPay and more.', '<strong>Электронные кошельки:</strong> Jeton, Volet, WebMoney, Apple Pay, Google Pay, Paytm, GrabPay и другие.'),
 ('<strong>Bank transfers and QR:</strong> UPI, QRIS, DuitNow, VietQR, PSE and other local rails.', '<strong>Банковские переводы и QR:</strong> UPI, QRIS, DuitNow, VietQR, PSE и другие местные системы.'),
 ('<strong>Mobile money:</strong> M-Pesa, MTN, Airtel, Orange, Vodacom and others across Africa.', '<strong>Мобильные платежи:</strong> M-Pesa, MTN, Airtel, Orange, Vodacom и другие операторы Африки.'),
 ('<strong>Crypto:</strong> Bitcoin, Ethereum, USDT on several networks, Litecoin, Tron, Solana and more.', '<strong>Криптовалюта:</strong> Bitcoin, Ethereum, USDT в нескольких сетях, Litecoin, Tron, Solana и другие.'),
 ('<h2 id="deposit">How to deposit</h2>', '<h2 id="deposit">Как пополнить счёт</h2>'),
 ('Log in and open <strong>Finance → Deposit</strong>.', 'Войдите в аккаунт и откройте <strong>«Финансы» → «Пополнение»</strong>.'),
 ('<li>Choose a payment method and enter the amount, from $5 for most methods.</li>', '<li>Выберите способ оплаты и укажите сумму — для большинства способов от $5.</li>'),
 ('''Add a promo code if you have one. Read its conditions first, see{" "}
      <a href="/bonus-promo-code/">bonus and promo codes</a>.''', '''Если есть промокод, введите его, но сначала прочитайте условия — подробнее в разделе{" "}
      <a href="/bonus-promo-code/">бонусы и промокоды</a>.'''),
 ('<li>Confirm the payment with your provider. Most deposits are credited within minutes.</li>', '<li>Подтвердите платёж у своей платёжной системы. Обычно деньги зачисляются за несколько минут.</li>'),
 ('<h2 id="verify">Verification</h2>', '<h2 id="verify">Верификация</h2>'),
 ('''Verification protects your account and is required before you can withdraw. Pocket Option asks for your personal
    details, a photo ID and, in some cases, proof of address. Verifying right after registration saves time later.''',
  '''Верификация защищает аккаунт и обязательна перед первым выводом. Pocket Option попросит личные данные, фото
    документа и иногда подтверждение адреса. Лучше пройти её сразу после регистрации — потом сэкономите время.'''),
 ('''Use your real name and details from the start. A mismatch between your profile and your documents or payment method
    is the most common reason for a delayed withdrawal.''', '''Сразу указывайте настоящие имя и данные. Самая частая причина задержки вывода — расхождение между профилем,
    документами и платёжным методом.'''),
 ('<h2 id="withdraw">How to withdraw</h2>', '<h2 id="withdraw">Как вывести деньги</h2>'),
 ('Open <strong>Finance → Withdrawal</strong>.', 'Откройте <strong>«Финансы» → «Вывод»</strong>.'),
 ('<li>Select a method you used to deposit. Anti-money-laundering rules require funds to return the same way.</li>', '<li>Выберите способ, которым пополняли счёт: по правилам AML деньги возвращаются тем же путём.</li>'),
 ('<li>Enter the amount and confirm.</li>', '<li>Укажите сумму и подтвердите заявку.</li>'),
 ('''Pocket Option sets no minimum or maximum withdrawal amount when you have no active deposit bonus. If a bonus is
    still active, its amount is deducted from your balance when you withdraw.''', '''Если активного бонуса на депозит нет, минимальной и максимальной суммы вывода у Pocket Option нет. Если бонус ещё
    активен, при выводе его сумма списывается с баланса.'''),
 ('<h2 id="times">Fees and timing</h2>', '<h2 id="times">Комиссии и сроки</h2>'),
 ('<th>Method</th>\n        <th>Deposit</th>\n        <th>Withdrawal arrival</th>', '<th>Способ</th>\n        <th>Пополнение</th>\n        <th>Срок вывода</th>'),
 ('<td>Crypto</td>\n        <td>Minutes, after network confirmations</td>\n        <td>Usually within a day</td>', '<td>Криптовалюта</td>\n        <td>Минуты, после подтверждений в сети</td>\n        <td>Обычно в течение суток</td>'),
 ('<td>E-wallets</td>\n        <td>Instant to minutes</td>\n        <td>Usually within a day</td>', '<td>Электронные кошельки</td>\n        <td>Мгновенно или за минуты</td>\n        <td>Обычно в течение суток</td>'),
 ('<td>Mobile money, local transfers</td>\n        <td>Instant to minutes</td>\n        <td>Same day to a few days</td>', '<td>Мобильные платежи, местные переводы</td>\n        <td>Мгновенно или за минуты</td>\n        <td>От нескольких часов до нескольких дней</td>'),
 ('<td>Bank cards</td>\n        <td>Instant</td>\n        <td>Several business days</td>', '<td>Банковские карты</td>\n        <td>Мгновенно</td>\n        <td>Несколько рабочих дней</td>'),
 ('''Pocket Option charges 0% on deposits and withdrawals. Your bank, card issuer or the blockchain network may still
    charge their own fees or apply a currency conversion rate.''', '''Pocket Option берёт 0% за пополнение и вывод. При этом банк, эмитент карты или блокчейн-сеть могут удержать свою
    комиссию или применить курс конвертации.'''),
 ('<h2 id="problems">If a payment is delayed</h2>', '<h2 id="problems">Если платёж задерживается</h2>'),
 ('<li>Check that your account is fully verified.</li>', '<li>Проверьте, что аккаунт полностью верифицирован.</li>'),
 ('<li>Make sure you are withdrawing to a method you used to deposit.</li>', '<li>Убедитесь, что выводите тем же способом, которым пополняли.</li>'),
 ('<li>Check whether an active bonus is affecting your balance.</li>', '<li>Проверьте, не влияет ли на баланс активный бонус.</li>'),
 ('<li>Contact Pocket Option support from your account with the transaction ID.</li>', '<li>Напишите в поддержку Pocket Option из личного кабинета и укажите ID транзакции.</li>'),
]
UA = [
 ('"Payment methods" }', '"Способи оплати" }'), ('"How to deposit" }', '"Як поповнити рахунок" }'),
 ('"Verification" }', '"Верифікація" }'), ('"How to withdraw" }', '"Як вивести гроші" }'),
 ('"Fees and timing" }', '"Комісії та терміни" }'), ('"If a payment is delayed" }', '"Якщо платіж затримується" }'),
 ('title="Pocket Option Deposit & Withdrawal: Methods, Fees, Times"', 'title="Pocket Option: поповнення та виведення коштів, комісії, терміни"'),
 ('description="Deposit from $5 with 170+ payment methods and withdraw with no Pocket Option fees. Cards, e-wallets, crypto, verification and payout times explained."',
  'description="Поповнення від $5 через 170+ способів оплати й виведення без комісії Pocket Option. Картки, е-гаманці, крипта, верифікація та терміни виплат."'),
 ('h1="Pocket Option deposits and withdrawals"', 'h1="Поповнення та виведення коштів у Pocket Option"'),
 ('lead="Deposits start at $5 and Pocket Option charges no commission either way. Here is how to fund your account, get verified and withdraw without delays."',
  'lead="Депозит — від $5, комісії Pocket Option немає ні на введення, ні на виведення. Розбираємо, як поповнити рахунок, пройти верифікацію й виводити гроші без затримок."'),
 ('crumb="Deposits & withdrawals"', 'crumb="Поповнення і виведення"'),
 ('<h2 id="methods">Payment methods</h2>', '<h2 id="methods">Способи оплати</h2>'),
 ('''Pocket Option lists more than 170 payment methods. What you see in your account depends on your country and
    currency.''', '''У Pocket Option понад 170 способів оплати. Які з них доступні саме вам, залежить від країни та валюти рахунку.'''),
 ('<strong>Cards:</strong> Visa, Mastercard and local card schemes.', '<strong>Банківські картки:</strong> Visa, Mastercard і місцеві платіжні системи.'),
 ('<strong>E-wallets:</strong> Jeton, Volet, WebMoney, Apple Pay, Google Pay, Paytm, GrabPay and more.', '<strong>Електронні гаманці:</strong> Jeton, Volet, WebMoney, Apple Pay, Google Pay, Paytm, GrabPay та інші.'),
 ('<strong>Bank transfers and QR:</strong> UPI, QRIS, DuitNow, VietQR, PSE and other local rails.', '<strong>Банківські перекази та QR:</strong> UPI, QRIS, DuitNow, VietQR, PSE та інші місцеві системи.'),
 ('<strong>Mobile money:</strong> M-Pesa, MTN, Airtel, Orange, Vodacom and others across Africa.', '<strong>Мобільні платежі:</strong> M-Pesa, MTN, Airtel, Orange, Vodacom та інші оператори Африки.'),
 ('<strong>Crypto:</strong> Bitcoin, Ethereum, USDT on several networks, Litecoin, Tron, Solana and more.', '<strong>Криптовалюта:</strong> Bitcoin, Ethereum, USDT у кількох мережах, Litecoin, Tron, Solana та інші.'),
 ('<h2 id="deposit">How to deposit</h2>', '<h2 id="deposit">Як поповнити рахунок</h2>'),
 ('Log in and open <strong>Finance → Deposit</strong>.', 'Увійдіть в акаунт і відкрийте <strong>«Фінанси» → «Поповнення»</strong>.'),
 ('<li>Choose a payment method and enter the amount, from $5 for most methods.</li>', '<li>Оберіть спосіб оплати й вкажіть суму — для більшості способів від $5.</li>'),
 ('''Add a promo code if you have one. Read its conditions first, see{" "}
      <a href="/bonus-promo-code/">bonus and promo codes</a>.''', '''Якщо маєте промокод, введіть його, але спершу прочитайте умови — детальніше в розділі{" "}
      <a href="/bonus-promo-code/">бонуси та промокоди</a>.'''),
 ('<li>Confirm the payment with your provider. Most deposits are credited within minutes.</li>', '<li>Підтвердьте платіж у своїй платіжній системі. Зазвичай гроші зараховуються за кілька хвилин.</li>'),
 ('<h2 id="verify">Verification</h2>', '<h2 id="verify">Верифікація</h2>'),
 ('''Verification protects your account and is required before you can withdraw. Pocket Option asks for your personal
    details, a photo ID and, in some cases, proof of address. Verifying right after registration saves time later.''',
  '''Верифікація захищає акаунт і обов’язкова перед першим виведенням. Pocket Option попросить особисті дані, фото
    документа й іноді підтвердження адреси. Краще пройти її одразу після реєстрації — згодом заощадите час.'''),
 ('''Use your real name and details from the start. A mismatch between your profile and your documents or payment method
    is the most common reason for a delayed withdrawal.''', '''Одразу вказуйте справжні ім’я та дані. Найчастіша причина затримки виведення — розбіжність між профілем,
    документами та платіжним методом.'''),
 ('<h2 id="withdraw">How to withdraw</h2>', '<h2 id="withdraw">Як вивести гроші</h2>'),
 ('Open <strong>Finance → Withdrawal</strong>.', 'Відкрийте <strong>«Фінанси» → «Виведення»</strong>.'),
 ('<li>Select a method you used to deposit. Anti-money-laundering rules require funds to return the same way.</li>', '<li>Оберіть спосіб, яким поповнювали рахунок: за правилами AML гроші повертаються тим самим шляхом.</li>'),
 ('<li>Enter the amount and confirm.</li>', '<li>Вкажіть суму й підтвердьте заявку.</li>'),
 ('''Pocket Option sets no minimum or maximum withdrawal amount when you have no active deposit bonus. If a bonus is
    still active, its amount is deducted from your balance when you withdraw.''', '''Якщо активного бонусу на депозит немає, мінімальної та максимальної суми виведення в Pocket Option немає. Якщо
    бонус ще активний, під час виведення його сума списується з балансу.'''),
 ('<h2 id="times">Fees and timing</h2>', '<h2 id="times">Комісії та терміни</h2>'),
 ('<th>Method</th>\n        <th>Deposit</th>\n        <th>Withdrawal arrival</th>', '<th>Спосіб</th>\n        <th>Поповнення</th>\n        <th>Термін виведення</th>'),
 ('<td>Crypto</td>\n        <td>Minutes, after network confirmations</td>\n        <td>Usually within a day</td>', '<td>Криптовалюта</td>\n        <td>Хвилини, після підтверджень у мережі</td>\n        <td>Зазвичай протягом доби</td>'),
 ('<td>E-wallets</td>\n        <td>Instant to minutes</td>\n        <td>Usually within a day</td>', '<td>Електронні гаманці</td>\n        <td>Миттєво або за хвилини</td>\n        <td>Зазвичай протягом доби</td>'),
 ('<td>Mobile money, local transfers</td>\n        <td>Instant to minutes</td>\n        <td>Same day to a few days</td>', '<td>Мобільні платежі, місцеві перекази</td>\n        <td>Миттєво або за хвилини</td>\n        <td>Від кількох годин до кількох днів</td>'),
 ('<td>Bank cards</td>\n        <td>Instant</td>\n        <td>Several business days</td>', '<td>Банківські картки</td>\n        <td>Миттєво</td>\n        <td>Кілька робочих днів</td>'),
 ('''Pocket Option charges 0% on deposits and withdrawals. Your bank, card issuer or the blockchain network may still
    charge their own fees or apply a currency conversion rate.''', '''Pocket Option бере 0% за поповнення й виведення. Водночас банк, емітент картки чи блокчейн-мережа можуть утримати
    свою комісію або застосувати курс конвертації.'''),
 ('<h2 id="problems">If a payment is delayed</h2>', '<h2 id="problems">Якщо платіж затримується</h2>'),
 ('<li>Check that your account is fully verified.</li>', '<li>Перевірте, що акаунт повністю верифіковано.</li>'),
 ('<li>Make sure you are withdrawing to a method you used to deposit.</li>', '<li>Переконайтеся, що виводите тим самим способом, яким поповнювали.</li>'),
 ('<li>Check whether an active bonus is affecting your balance.</li>', '<li>Перевірте, чи не впливає на баланс активний бонус.</li>'),
 ('<li>Contact Pocket Option support from your account with the transaction ID.</li>', '<li>Напишіть у підтримку Pocket Option з особистого кабінету й вкажіть ID транзакції.</li>'),
]
for L, pairs in [("ru", RU), ("ua", UA)]:
    build("src/pages/deposit-withdrawal.astro", L, pairs, f"src/pages/{L}/deposit-withdrawal.astro")
