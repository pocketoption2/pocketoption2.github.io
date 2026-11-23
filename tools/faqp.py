import sys; sys.path.insert(0, "tools")
from tr import build
def common(L, home, title, desc, h1, lead):
    return [
 ('const crumbs = [{ href: "/", label: "Home" }, { label: "FAQ" }];', f'const crumbs = [{{ href: "/{L}/", label: "{home}" }}, {{ label: "FAQ" }}];'),
 ('name: "Home", item: `${SITE.url}/` }', f'name: "{home}", item: `${{SITE.url}}/{L}/` }}'),
 ('item: `${SITE.url}/faq/` }', f'item: `${{SITE.url}}/{L}/faq/` }}'),
 ('title="Pocket Option FAQ: Account, Deposits, Withdrawals & App"', f'title="{title}"'),
 ('description="Quick answers about Pocket Option: is it legit, countries, demo, verification, minimum deposit, withdrawal times, payouts and the PocketOption app."', f'description="{desc}"'),
 ('title="Pocket Option FAQ"\n', f'title="{h1}"\n'),
 ('lead="Straight answers to the questions people ask most about Pocket Option, from opening an account to getting paid."', f'lead="{lead}"'),
 ('alt="Pocket Option FAQ"', f'alt="{h1}"'),
]
def qa(pairs):
    out = []
    for a, b in pairs: out.append((a, b))
    return out
EN_Q = [
 '"About Pocket Option"', '"Account and demo"', '"Deposits and withdrawals"', '"Trading"',
 '"What is Pocket Option?"', '"Pocket Option is an online trading platform launched in 2017. It lets you trade currencies, crypto, stocks, commodities and indices from $1 per trade on web, Android, iPhone and Telegram."',
 '"Is PocketOption the same as Pocket Option?"', '"Yes. PocketOption is the one-word spelling of the same broker and the same platform at pocketoption.com."',
 '"Is Pocket Option legit?"', '\'It has operated since 2017 and reports more than 10 million registered users. It is an offshore broker without tier-1 regulation, so it offers less protection than regulated brokers. See our <a href="/review/">review</a>.\'',
 '"Which countries can\'t use Pocket Option?"', '"Pocket Option does not serve residents of the EEA, the USA, the UK, Israel, Japan, the Philippines and Brazil."',
 '"How do I open a Pocket Option account?"', '"Sign up with your email or Google account, confirm your email, then complete verification in your profile before your first withdrawal."',
 '"Is the Pocket Option demo free?"', '\'Yes. The demo has $50,000 in virtual funds, opens in one click without registration and has no time limit. See the <a href="/demo-account/">demo account page</a>.\'',
 '"Can I log in with Google?"', '\'Yes. If you registered with Google and later want to log in with email and password, use password recovery first to set a password. See <a href="/blog/pocket-option-login/">Pocket Option login help</a>.\'',
 '"What documents do I need for verification?"', '"A valid photo ID and, in some cases, proof of address. Your profile details must match your documents."',
 '"What is the minimum deposit?"', '"$5 for most payment methods. The minimum trade amount is $1."',
 '"Does Pocket Option charge fees?"', '"Pocket Option charges no commission on deposits or withdrawals. Your bank, card issuer or crypto network may charge their own fees."',
 '"Is there a minimum withdrawal?"', '"No minimum or maximum withdrawal amount applies when you have no active deposit bonus."',
 '"How long do withdrawals take?"', '"After verification, e-wallet and crypto withdrawals often arrive within a day. Cards and bank transfers can take several business days."',
 '"What can I trade on Pocket Option?"', '"More than 100 assets: currency pairs, cryptocurrencies, stocks, commodities and indices, plus OTC versions that stay open on weekends."',
 '"What is the maximum payout?"', '"Single trades typically pay up to 92% depending on the asset and time of day. Express trades, which combine several forecasts, can pay up to 218%."',
 '"Does Pocket Option have copy trading?"', '"Yes. Social trading lets you copy other traders automatically and set your own limits."',
 '"Is there a Pocket Option app?"', '\'Yes, for Android (Google Play or APK), iPhone and iPad as a web app, desktop browsers and Telegram. See the <a href="/app/">app page</a>.\'',
]
RU_Q = [
 '"О Pocket Option"', '"Аккаунт и демо-счёт"', '"Пополнение и вывод"', '"Торговля"',
 '"Что такое Pocket Option?"', '"Pocket Option — онлайн-платформа для трейдинга, работающая с 2017 года. Здесь можно торговать валютами, криптовалютой, акциями, сырьём и индексами со сделками от $1 — в браузере, на Android, iPhone и в Telegram."',
 '"PocketOption и Pocket Option — одно и то же?"', '"Да. PocketOption — слитное написание того же брокера и той же платформы на pocketoption.com. По-русски его часто называют «Покет Опшн»."',
 '"Pocket Option — развод или нет?"', '\'Компания работает с 2017 года и сообщает о более чем 10 млн зарегистрированных пользователей. Это офшорный брокер без регулятора первого уровня, поэтому защита клиентов слабее, чем у регулируемых брокеров. Подробнее в нашем <a href="/review/">обзоре</a>.\'',
 '"В каких странах Pocket Option недоступен?"', '"Pocket Option не обслуживает жителей стран ЕЭЗ, США, Великобритании, Израиля, Японии, Филиппин и Бразилии."',
 '"Как открыть счёт в Pocket Option?"', '"Зарегистрируйтесь через email или Google, подтвердите почту, а перед первым выводом пройдите верификацию в профиле."',
 '"Демо-счёт Pocket Option бесплатный?"', '\'Да. На демо $50 000 виртуальных средств, оно открывается в один клик без регистрации и не ограничено по сроку. Подробнее на странице <a href="/demo-account/">демо-счёта</a>.\'',
 '"Можно ли войти в Pocket Option через Google?"', '"Да. Если вы регистрировались через Google, а потом хотите входить по email и паролю, сначала задайте пароль через восстановление доступа."',
 '"Какие документы нужны для верификации?"', '"Действующий документ с фото и иногда подтверждение адреса. Данные в профиле должны совпадать с документами."',
 '"Какой минимальный депозит?"', '"$5 для большинства способов оплаты. Минимальная сумма сделки — $1."',
 '"Есть ли комиссии у Pocket Option?"', '"Pocket Option не берёт комиссию за пополнение и вывод. Свою комиссию может удержать банк, эмитент карты или криптосеть."',
 '"Есть ли минимальная сумма вывода?"', '"Если нет активного бонуса на депозит, минимальной и максимальной суммы вывода нет."',
 '"Сколько идёт вывод средств?"', '"После верификации вывод на электронные кошельки и в крипте часто приходит в течение суток. На карты и банковским переводом — до нескольких рабочих дней."',
 '"Чем можно торговать на Pocket Option?"', '"Более 100 активов: валютные пары, криптовалюты, акции, сырьё и индексы, плюс OTC-активы, которые торгуются и в выходные."',
 '"Какая максимальная выплата?"', '"По обычной сделке — как правило, до 92% в зависимости от актива и времени суток. Экспресс-сделки, объединяющие несколько прогнозов, дают до 218%."',
 '"Есть ли в Pocket Option копитрейдинг?"', '"Да. Можно автоматически копировать сделки других трейдеров и задавать свои лимиты."',
 '"Есть ли приложение Pocket Option?"', '\'Да: для Android (Google Play или APK), веб-приложение для iPhone и iPad, версия для браузера на ПК и Telegram-бот. Подробнее на <a href="/app/">странице приложения</a>.\'',
]
UA_Q = [
 '"Про Pocket Option"', '"Акаунт і демо-рахунок"', '"Поповнення і виведення"', '"Торгівля"',
 '"Що таке Pocket Option?"', '"Pocket Option — онлайн-платформа для трейдингу, що працює з 2017 року. Тут можна торгувати валютами, криптовалютою, акціями, сировиною та індексами з угодами від $1 — у браузері, на Android, iPhone і в Telegram."',
 '"PocketOption і Pocket Option — одне й те саме?"', '"Так. PocketOption — злите написання того самого брокера й тієї самої платформи на pocketoption.com. Українською його часто називають «Покет Опшн»."',
 '"Pocket Option — шахрайство чи ні?"', '\'Компанія працює з 2017 року й повідомляє про понад 10 млн зареєстрованих користувачів. Це офшорний брокер без регулятора першого рівня, тому захист клієнтів слабший, ніж у регульованих брокерів. Детальніше в нашому <a href="/review/">огляді</a>.\'',
 '"У яких країнах Pocket Option недоступний?"', '"Pocket Option не обслуговує мешканців країн ЄЕЗ, США, Великої Британії, Ізраїлю, Японії, Філіппін і Бразилії."',
 '"Як відкрити рахунок у Pocket Option?"', '"Зареєструйтеся через email або Google, підтвердьте пошту, а перед першим виведенням пройдіть верифікацію в профілі."',
 '"Демо-рахунок Pocket Option безкоштовний?"', '\'Так. На демо $50 000 віртуальних коштів, воно відкривається в один клік без реєстрації й не обмежене за терміном. Детальніше на сторінці <a href="/demo-account/">демо-рахунку</a>.\'',
 '"Чи можна увійти в Pocket Option через Google?"', '"Так. Якщо ви реєструвалися через Google, а згодом хочете входити за email і паролем, спершу задайте пароль через відновлення доступу."',
 '"Які документи потрібні для верифікації?"', '"Чинний документ із фото й іноді підтвердження адреси. Дані в профілі мають збігатися з документами."',
 '"Який мінімальний депозит?"', '"$5 для більшості способів оплати. Мінімальна сума угоди — $1."',
 '"Чи є комісії в Pocket Option?"', '"Pocket Option не бере комісію за поповнення й виведення. Свою комісію може утримати банк, емітент картки чи криптомережа."',
 '"Чи є мінімальна сума виведення?"', '"Якщо немає активного бонусу на депозит, мінімальної та максимальної суми виведення немає."',
 '"Скільки триває виведення коштів?"', '"Після верифікації виведення на електронні гаманці та в крипті часто надходить протягом доби. На картки й банківським переказом — до кількох робочих днів."',
 '"Чим можна торгувати на Pocket Option?"', '"Понад 100 активів: валютні пари, криптовалюти, акції, сировина та індекси, плюс OTC-активи, які торгуються й у вихідні."',
 '"Яка максимальна виплата?"', '"За звичайною угодою — як правило, до 92% залежно від активу й часу доби. Експрес-угоди, що об’єднують кілька прогнозів, дають до 218%."',
 '"Чи є в Pocket Option копітрейдинг?"', '"Так. Можна автоматично копіювати угоди інших трейдерів і задавати власні ліміти."',
 '"Чи є застосунок Pocket Option?"', '\'Так: для Android (Google Play або APK), вебзастосунок для iPhone та iPad, версія для браузера на ПК і Telegram-бот. Детальніше на <a href="/app/">сторінці застосунку</a>.\'',
]
assert len(EN_Q) == len(RU_Q) == len(UA_Q)
RU = common("ru", "Главная", "Pocket Option FAQ: вход, демо-счёт, депозит, вывод и приложение", "Ответы на частые вопросы о Pocket Option: развод или нет, страны, демо-счёт, верификация, минимальный депозит, сроки вывода, выплаты и приложение.", "Частые вопросы о Pocket Option", "Прямые ответы на самые популярные вопросы о Pocket Option — от открытия счёта до вывода денег.") + list(zip(EN_Q, RU_Q))
UA = common("ua", "Головна", "Pocket Option FAQ: вхід, демо, депозит, виведення, застосунок", "Відповіді на часті запитання про Pocket Option: шахрайство чи ні, країни, демо-рахунок, верифікація, мінімальний депозит, терміни виведення, виплати й застосунок.", "Часті запитання про Pocket Option", "Прямі відповіді на найпопулярніші запитання про Pocket Option — від відкриття рахунку до виведення грошей.") + list(zip(EN_Q, UA_Q))
for L, pairs in [("ru", RU), ("ua", UA)]:
    build("src/pages/faq.astro", L, pairs, f"src/pages/{L}/faq.astro")
