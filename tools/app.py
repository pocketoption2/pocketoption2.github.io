import sys; sys.path.insert(0, "tools")
from tr import build
RU = [
 ('"iPhone and iPad" }', '"iPhone и iPad" }'), ('"Windows and macOS" }', '"Windows и macOS" }'),
 ('"Telegram bot" }', '"Telegram-бот" }'), ('"Which one to use" }', '"Что выбрать" }'),
 ('title="Pocket Option App Download: Android, iOS, PC & Telegram"', 'title="Скачать приложение Pocket Option: Android, iOS, ПК и Telegram"'),
 ('description="Download the Pocket Option app for Android, iPhone, Windows and macOS, or use the PocketOption Telegram bot. Install steps, APK and features explained."',
  'description="Скачайте приложение Pocket Option для Android, iPhone, Windows и macOS или торгуйте через Telegram-бот. Установка, APK и возможности приложения."'),
 ('h1="Pocket Option app for every device"', 'h1="Приложение Pocket Option для любого устройства"'),
 ('lead="One account, one balance, every screen. How to install Pocket Option on Android, iPhone, desktop and Telegram, and which version to choose."',
  'lead="Один аккаунт, один баланс, любой экран. Как установить Pocket Option на Android, iPhone, компьютер и в Telegram и какую версию выбрать."'),
 ('crumb="App"', 'crumb="Приложение"'),
 ('alt="Pocket Option app on a phone showing a EUR/USD chart"', 'alt="Приложение Pocket Option на телефоне с графиком EUR/USD"'),
 ('<figcaption>The Pocket Option mobile platform with an EUR/USD chart and trade panel.</figcaption>', '<figcaption>Мобильная платформа Pocket Option: график EUR/USD и панель сделок.</figcaption>'),
 ('''The Android app is available on <strong>Google Play</strong>. Where Google Play is not available, Pocket Option
    offers an <strong>APK</strong> download from its website. The app supports every trade type, indicators, social
    trading, deposits and withdrawals.''', '''Приложение для Android есть в <strong>Google Play</strong>. Если Google Play недоступен, Pocket Option предлагает
    скачать <strong>APK</strong> со своего сайта. В приложении доступны все типы сделок, индикаторы, копитрейдинг,
    пополнение и вывод средств.'''),
 ('        Get the Pocket Option app\n', '        Скачайте приложение Pocket Option\n'),
 ('from Google Play, or download the APK from the official site.', 'в Google Play или загрузите APK с официального сайта.'),
 ('<li>For the APK, allow installs from your browser when Android asks.</li>', '<li>Для APK разрешите установку из браузера, когда Android попросит.</li>'),
 ('<li>Log in with your existing account or open the demo.</li>', '<li>Войдите в свой аккаунт или откройте демо-счёт.</li>'),
 ('<h2 id="iphone">iPhone and iPad</h2>', '<h2 id="iphone">iPhone и iPad</h2>'),
 ('''On iOS, Pocket Option runs as a <strong>web app</strong>. It installs to the home screen and opens full screen like
    a native app.''', '''На iOS Pocket Option работает как <strong>веб-приложение</strong>: оно ставится на главный экран и открывается
    на весь экран, как обычное приложение.'''),
 ('      Open{" "}\n', '      Откройте{" "}\n'), ('      in Safari.\n', '      в Safari.\n'),
 ('Tap the Share button, then <strong>Add to Home Screen</strong>.', 'Нажмите «Поделиться», затем <strong>«На экран „Домой“»</strong>.'),
 ('<li>Launch Pocket Option from the new icon.</li>', '<li>Запускайте Pocket Option с новой иконки.</li>'),
 ('<h2 id="desktop">Windows and macOS</h2>', '<h2 id="desktop">Windows и macOS</h2>'),
 ('''There is no separate download for desktop. The full platform runs in Chrome, Edge, Safari or Firefox, which keeps it
    up to date automatically and makes it work on any operating system. In Chrome or Edge you can also install it as an
    app from the address bar.''', '''Отдельной программы для компьютера нет — и она не нужна. Полная версия платформы работает в Chrome, Edge, Safari
    или Firefox, всегда обновлена и запускается на любой ОС. В Chrome или Edge её можно установить как приложение прямо
    из адресной строки.'''),
 ('<h2 id="telegram">Telegram bot</h2>', '<h2 id="telegram">Telegram-бот</h2>'),
 ('''Pocket Option also runs a Telegram bot linked to your account. It is useful for quick checks and notifications on
    the go, while full charting is better on the app or web platform.''', '''У Pocket Option есть и Telegram-бот, привязанный к вашему аккаунту. Он удобен, чтобы быстро что-то проверить
    и получать уведомления на ходу, а полноценный анализ графиков лучше делать в приложении или веб-версии.'''),
 ('<h2 id="compare">Which one to use</h2>', '<h2 id="compare">Что выбрать</h2>'),
 ('<th>Version</th>\n        <th>Best for</th>\n        <th>Install</th>', '<th>Версия</th>\n        <th>Для чего лучше</th>\n        <th>Установка</th>'),
 ('<td>Web platform</td>\n        <td>Analysis on a large screen</td>\n        <td>None</td>', '<td>Веб-платформа</td>\n        <td>Анализ на большом экране</td>\n        <td>Не нужна</td>'),
 ('<td>Android app</td>\n        <td>Trading on the go</td>\n        <td>Google Play or APK</td>', '<td>Приложение для Android</td>\n        <td>Торговля на ходу</td>\n        <td>Google Play или APK</td>'),
 ('<td>iOS web app</td>\n        <td>iPhone and iPad users</td>\n        <td>Add to Home Screen</td>', '<td>Веб-приложение iOS</td>\n        <td>Для iPhone и iPad</td>\n        <td>«На экран „Домой“»</td>'),
 ('<td>Telegram bot</td>\n        <td>Quick checks, alerts</td>\n        <td>Open in Telegram</td>', '<td>Telegram-бот</td>\n        <td>Быстрые проверки, уведомления</td>\n        <td>Открыть в Telegram</td>'),
 ('    Not sure yet?{" "}\n', '    Ещё не решили?{" "}\n'), ('      Open the demo\n', '      Откройте демо\n'),
 ('on your phone and desktop and see which you prefer.', 'на телефоне и компьютере и посмотрите, что удобнее.'),
]
UA = [
 ('"iPhone and iPad" }', '"iPhone та iPad" }'), ('"Windows and macOS" }', '"Windows і macOS" }'),
 ('"Telegram bot" }', '"Telegram-бот" }'), ('"Which one to use" }', '"Що обрати" }'),
 ('title="Pocket Option App Download: Android, iOS, PC & Telegram"', 'title="Завантажити застосунок Pocket Option: Android, iOS, ПК, Telegram"'),
 ('description="Download the Pocket Option app for Android, iPhone, Windows and macOS, or use the PocketOption Telegram bot. Install steps, APK and features explained."',
  'description="Завантажте застосунок Pocket Option для Android, iPhone, Windows і macOS або торгуйте через Telegram-бот. Встановлення, APK і можливості."'),
 ('h1="Pocket Option app for every device"', 'h1="Застосунок Pocket Option для будь-якого пристрою"'),
 ('lead="One account, one balance, every screen. How to install Pocket Option on Android, iPhone, desktop and Telegram, and which version to choose."',
  'lead="Один акаунт, один баланс, будь-який екран. Як встановити Pocket Option на Android, iPhone, комп’ютер і в Telegram та яку версію обрати."'),
 ('crumb="App"', 'crumb="Застосунок"'),
 ('alt="Pocket Option app on a phone showing a EUR/USD chart"', 'alt="Застосунок Pocket Option на телефоні з графіком EUR/USD"'),
 ('<figcaption>The Pocket Option mobile platform with an EUR/USD chart and trade panel.</figcaption>', '<figcaption>Мобільна платформа Pocket Option: графік EUR/USD і панель угод.</figcaption>'),
 ('''The Android app is available on <strong>Google Play</strong>. Where Google Play is not available, Pocket Option
    offers an <strong>APK</strong> download from its website. The app supports every trade type, indicators, social
    trading, deposits and withdrawals.''', '''Застосунок для Android є в <strong>Google Play</strong>. Якщо Google Play недоступний, Pocket Option пропонує
    завантажити <strong>APK</strong> зі свого сайту. У застосунку доступні всі типи угод, індикатори, копітрейдинг,
    поповнення й виведення коштів.'''),
 ('        Get the Pocket Option app\n', '        Завантажте застосунок Pocket Option\n'),
 ('from Google Play, or download the APK from the official site.', 'у Google Play або завантажте APK з офіційного сайту.'),
 ('<li>For the APK, allow installs from your browser when Android asks.</li>', '<li>Для APK дозвольте встановлення з браузера, коли Android попросить.</li>'),
 ('<li>Log in with your existing account or open the demo.</li>', '<li>Увійдіть у свій акаунт або відкрийте демо-рахунок.</li>'),
 ('<h2 id="iphone">iPhone and iPad</h2>', '<h2 id="iphone">iPhone та iPad</h2>'),
 ('''On iOS, Pocket Option runs as a <strong>web app</strong>. It installs to the home screen and opens full screen like
    a native app.''', '''На iOS Pocket Option працює як <strong>вебзастосунок</strong>: він встановлюється на головний екран і відкривається
    на весь екран, як звичайний застосунок.'''),
 ('      Open{" "}\n', '      Відкрийте{" "}\n'), ('      in Safari.\n', '      у Safari.\n'),
 ('Tap the Share button, then <strong>Add to Home Screen</strong>.', 'Натисніть «Поділитися», потім <strong>«На початковий екран»</strong>.'),
 ('<li>Launch Pocket Option from the new icon.</li>', '<li>Запускайте Pocket Option з нової іконки.</li>'),
 ('<h2 id="desktop">Windows and macOS</h2>', '<h2 id="desktop">Windows і macOS</h2>'),
 ('''There is no separate download for desktop. The full platform runs in Chrome, Edge, Safari or Firefox, which keeps it
    up to date automatically and makes it work on any operating system. In Chrome or Edge you can also install it as an
    app from the address bar.''', '''Окремої програми для комп’ютера немає — і вона не потрібна. Повна версія платформи працює в Chrome, Edge, Safari
    або Firefox, завжди оновлена й запускається на будь-якій ОС. У Chrome чи Edge її можна встановити як застосунок просто
    з адресного рядка.'''),
 ('<h2 id="telegram">Telegram bot</h2>', '<h2 id="telegram">Telegram-бот</h2>'),
 ('''Pocket Option also runs a Telegram bot linked to your account. It is useful for quick checks and notifications on
    the go, while full charting is better on the app or web platform.''', '''У Pocket Option є й Telegram-бот, прив’язаний до вашого акаунта. Він зручний, щоб швидко щось перевірити
    й отримувати сповіщення в дорозі, а повноцінний аналіз графіків краще робити в застосунку чи вебверсії.'''),
 ('<h2 id="compare">Which one to use</h2>', '<h2 id="compare">Що обрати</h2>'),
 ('<th>Version</th>\n        <th>Best for</th>\n        <th>Install</th>', '<th>Версія</th>\n        <th>Для чого краще</th>\n        <th>Встановлення</th>'),
 ('<td>Web platform</td>\n        <td>Analysis on a large screen</td>\n        <td>None</td>', '<td>Вебплатформа</td>\n        <td>Аналіз на великому екрані</td>\n        <td>Не потрібне</td>'),
 ('<td>Android app</td>\n        <td>Trading on the go</td>\n        <td>Google Play or APK</td>', '<td>Застосунок для Android</td>\n        <td>Торгівля в дорозі</td>\n        <td>Google Play або APK</td>'),
 ('<td>iOS web app</td>\n        <td>iPhone and iPad users</td>\n        <td>Add to Home Screen</td>', '<td>Вебзастосунок iOS</td>\n        <td>Для iPhone та iPad</td>\n        <td>«На початковий екран»</td>'),
 ('<td>Telegram bot</td>\n        <td>Quick checks, alerts</td>\n        <td>Open in Telegram</td>', '<td>Telegram-бот</td>\n        <td>Швидкі перевірки, сповіщення</td>\n        <td>Відкрити в Telegram</td>'),
 ('    Not sure yet?{" "}\n', '    Ще не вирішили?{" "}\n'), ('      Open the demo\n', '      Відкрийте демо\n'),
 ('on your phone and desktop and see which you prefer.', 'на телефоні та комп’ютері й подивіться, що зручніше.'),
]
for L, pairs in [("ru", RU), ("ua", UA)]:
    build("src/pages/app.astro", L, pairs, f"src/pages/{L}/app.astro")
