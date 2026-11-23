export type QA = { q: string; a: string };

export const HOME_FAQ: QA[] = [
  {
    q: "Is Pocket Option legit?",
    a: 'Pocket Option has operated since 2017 and reports more than 10 million registered users. It is an offshore broker, so check that it is legal to use in your country and start with the demo account. Read the full <a href="/review/">Pocket Option review</a>.',
  },
  {
    q: "Are PocketOption and Pocket Option the same?",
    a: "Yes. PocketOption is simply the one-word spelling of Pocket Option, the same broker and the same platform at pocketoption.com.",
  },
  {
    q: "What is the minimum deposit on Pocket Option?",
    a: 'The minimum deposit is $5 for most payment methods, and the minimum trade is $1. See <a href="/deposit-withdrawal/">deposits and withdrawals</a>.',
  },
  {
    q: "Does Pocket Option have a demo account?",
    a: 'Yes. The <a href="/demo-account/">demo account</a> comes with $50,000 in virtual funds and opens in one click without registration.',
  },
  {
    q: "Is there a Pocket Option app?",
    a: 'Yes. Android on Google Play or as an APK, a web app for iPhone and iPad, a Telegram bot and the full platform in any desktop browser. See the <a href="/app/">app page</a>.',
  },
  {
    q: "How long do withdrawals take?",
    a: "Once your account is verified, e-wallet and crypto withdrawals often arrive within a day. Cards and bank transfers can take a few business days, depending on the provider.",
  },
];

export const HOME_FAQ_RU: QA[] = [
  {
    q: "Pocket Option — это развод или нет?",
    a: 'Pocket Option работает с 2017 года и сообщает о более чем 10 млн зарегистрированных пользователей. Это офшорный брокер, поэтому проверьте, разрешён ли он в вашей стране, и начните с демо-счёта. Подробнее — в <a href="/ru/review/">обзоре Pocket Option</a>.',
  },
  {
    q: "PocketOption и Pocket Option — это одно и то же?",
    a: "Да. PocketOption — просто слитное написание Pocket Option (по-русски часто пишут «Покет Опшн»). Это один и тот же брокер и одна платформа на pocketoption.com.",
  },
  {
    q: "Какой минимальный депозит в Pocket Option?",
    a: 'Минимальный депозит — $5 для большинства способов оплаты, минимальная сделка — $1. Подробнее в разделе <a href="/ru/deposit-withdrawal/">пополнение и вывод</a>.',
  },
  {
    q: "Есть ли у Pocket Option демо-счёт?",
    a: 'Да. <a href="/ru/demo-account/">Демо-счёт</a> с виртуальными $50 000 открывается в один клик, без регистрации.',
  },
  {
    q: "Есть ли приложение Pocket Option?",
    a: 'Да. Приложение для Android в Google Play или в виде APK, веб-приложение для iPhone и iPad, Telegram-бот и полная версия платформы в любом браузере на компьютере. Подробнее на <a href="/ru/app/">странице приложения</a>.',
  },
  {
    q: "Сколько идёт вывод средств?",
    a: "После верификации вывод на электронные кошельки и в криптовалюте часто приходит в течение суток. На карты и банковским переводом — до нескольких рабочих дней, в зависимости от платёжной системы.",
  },
];

export const HOME_FAQ_UA: QA[] = [
  {
    q: "Pocket Option — це шахрайство чи ні?",
    a: 'Pocket Option працює з 2017 року й повідомляє про понад 10 млн зареєстрованих користувачів. Це офшорний брокер, тож перевірте, чи дозволений він у вашій країні, і почніть із демо-рахунку. Детальніше — в <a href="/ua/review/">огляді Pocket Option</a>.',
  },
  {
    q: "PocketOption і Pocket Option — це одне й те саме?",
    a: "Так. PocketOption — просто злите написання Pocket Option (українською часто пишуть «Покет Опшн»). Це той самий брокер і та сама платформа на pocketoption.com.",
  },
  {
    q: "Який мінімальний депозит у Pocket Option?",
    a: 'Мінімальний депозит — $5 для більшості способів оплати, мінімальна угода — $1. Детальніше в розділі <a href="/ua/deposit-withdrawal/">поповнення і виведення</a>.',
  },
  {
    q: "Чи є в Pocket Option демо-рахунок?",
    a: 'Так. <a href="/ua/demo-account/">Демо-рахунок</a> із віртуальними $50 000 відкривається в один клік, без реєстрації.',
  },
  {
    q: "Чи є застосунок Pocket Option?",
    a: 'Так. Застосунок для Android у Google Play або у вигляді APK, вебзастосунок для iPhone та iPad, Telegram-бот і повна версія платформи в будь-якому браузері на комп’ютері. Детальніше на <a href="/ua/app/">сторінці застосунку</a>.',
  },
  {
    q: "Скільки триває виведення коштів?",
    a: "Після верифікації виведення на електронні гаманці та в криптовалюті часто надходить протягом доби. На картки й банківським переказом — до кількох робочих днів, залежно від платіжної системи.",
  },
];

export const faqSchema = (items: QA[]) => ({
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: items.map((i) => ({
    "@type": "Question",
    name: i.q,
    acceptedAnswer: { "@type": "Answer", text: i.a.replace(/<[^>]+>/g, "") },
  })),
});
