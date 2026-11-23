export const LANGS = {
  en: { name: "English", short: "EN", hreflang: "en", html: "en", og: "en_US", date: "en-GB" },
  ru: { name: "Русский", short: "RU", hreflang: "ru", html: "ru", og: "ru_RU", date: "ru-RU" },
  ua: { name: "Українська", short: "UA", hreflang: "uk", html: "uk", og: "uk_UA", date: "uk-UA" },
} as const;
export type Lang = keyof typeof LANGS;

// Pages that exist in every language; everything else is English-only.
export const TRANSLATED = [
  "/",
  "/review/",
  "/demo-account/",
  "/app/",
  "/deposit-withdrawal/",
  "/bonus-promo-code/",
  "/how-to-trade/",
  "/faq/",
];

export const getLang = (url: URL): Lang => {
  const seg = url.pathname.split("/")[1];
  return seg === "ru" || seg === "ua" ? seg : "en";
};

export const basePath = (pathname: string) => pathname.replace(/^\/(ru|ua)(?=\/)/, "") || "/";

export const lp = (lang: Lang, path: string) =>
  lang === "en" || !TRANSLATED.includes(path) ? path : `/${lang}${path}`;

const STR = {
  en: {
    skip: "Skip to content",
    home: "Home",
    nav: ["Review", "Demo account", "App", "Deposits", "Bonus", "FAQ"],
    tryDemo: "Try demo",
    openAccount: "Open account",
    openPo: "Open a Pocket Option account",
    tryFree: "Try the free demo",
    openMenu: "Open menu",
    closeMenu: "Close menu",
    drawerRisk: "Trading involves risk. Only invest what you can afford to lose.",
    language: "Language",
    footAbout:
      "Pocket Option is a web trading platform for currencies, crypto, stocks and commodities, with a $5 minimum deposit, $1 trades and a free $50,000 demo account.",
    footCols: ["Pocket Option", "Learn", "About"],
    footLinks: {
      "/review/": "Review",
      "/demo-account/": "Demo account",
      "/app/": "App",
      "/deposit-withdrawal/": "Deposits",
      "/how-to-trade/": "How to trade",
      "/bonus-promo-code/": "Bonus and promo codes",
      "/blog/": "Blog",
      "/faq/": "FAQ",
      "/about/": "About us",
      "/contact/": "Contact",
      "/disclaimer/": "Disclaimer",
      "/privacy/": "Privacy",
      "/risk-warning/": "Risk warning",
    } as Record<string, string>,
    risk: "Risk warning: trading financial instruments involves significant risk and may result in the loss of your invested capital. Only trade with money you can afford to lose. This website is for information only and is not investment advice. Some links are affiliate links; we may earn a commission at no extra cost to you.",
    rights: "All rights reserved.",
    endTitle: "Try Pocket Option risk-free on the demo",
    endNowrap: "risk-free",
    endText: "Practise with $50,000 in virtual funds and learn the platform before you trade with real money.",
    updated: "Updated",
    toc: "On this page",
    side: {
      title: "Pocket Option at a glance",
      rows: [
        ["Minimum deposit", "$5"],
        ["Minimum trade", "$1"],
        ["Demo balance", "$50,000"],
        ["Assets", "100+"],
        ["Founded", "2017"],
      ],
      open: "Open an account",
    },
    payNote:
      "Plus Jeton, Volet, WebMoney, Tron, Solana, local bank transfers, mobile money and 160+ more, depending on your country.",
  },
  ru: {
    skip: "Перейти к содержимому",
    home: "Главная",
    nav: ["Обзор", "Демо-счёт", "Приложение", "Пополнение", "Бонусы", "FAQ"],
    tryDemo: "Демо-счёт",
    openAccount: "Открыть счёт",
    openPo: "Открыть счёт в Pocket Option",
    tryFree: "Попробовать демо",
    openMenu: "Открыть меню",
    closeMenu: "Закрыть меню",
    drawerRisk: "Торговля связана с риском. Вкладывайте только те деньги, потерю которых можете себе позволить.",
    language: "Язык",
    footAbout:
      "Pocket Option — веб-платформа для торговли валютами, криптовалютой, акциями и сырьём: депозит от $5, сделки от $1 и бесплатный демо-счёт на $50 000.",
    footCols: ["Pocket Option", "Обучение", "О сайте"],
    footLinks: {
      "/review/": "Обзор",
      "/demo-account/": "Демо-счёт",
      "/app/": "Приложение",
      "/deposit-withdrawal/": "Пополнение и вывод",
      "/how-to-trade/": "Как торговать",
      "/bonus-promo-code/": "Бонусы и промокоды",
      "/blog/": "Блог (EN)",
      "/faq/": "FAQ",
      "/about/": "О нас (EN)",
      "/contact/": "Контакты (EN)",
      "/disclaimer/": "Отказ от ответственности",
      "/privacy/": "Конфиденциальность",
      "/risk-warning/": "Предупреждение о рисках",
    } as Record<string, string>,
    risk: "Предупреждение о рисках: торговля финансовыми инструментами связана с высоким риском и может привести к потере вложенных средств. Торгуйте только теми деньгами, которые готовы потерять. Материалы сайта носят информационный характер и не являются инвестиционной рекомендацией. Часть ссылок — партнёрские: мы можем получать комиссию без дополнительных затрат для вас.",
    rights: "Все права защищены.",
    endTitle: "Попробуйте Pocket Option без риска на демо-счёте",
    endNowrap: "без риска",
    endText: "Потренируйтесь на виртуальных $50 000 и освойтесь на платформе, прежде чем торговать реальными деньгами.",
    updated: "Обновлено",
    toc: "Содержание",
    side: {
      title: "Pocket Option в цифрах",
      rows: [
        ["Минимальный депозит", "$5"],
        ["Минимальная сделка", "$1"],
        ["Демо-баланс", "$50 000"],
        ["Активы", "100+"],
        ["Год основания", "2017"],
      ],
      open: "Открыть счёт",
    },
    payNote:
      "А также Jeton, Volet, WebMoney, Tron, Solana, местные банковские переводы, мобильные платежи и ещё 160+ способов — набор зависит от страны.",
  },
  ua: {
    skip: "Перейти до вмісту",
    home: "Головна",
    nav: ["Огляд", "Демо-рахунок", "Застосунок", "Поповнення", "Бонуси", "FAQ"],
    tryDemo: "Демо-рахунок",
    openAccount: "Відкрити рахунок",
    openPo: "Відкрити рахунок у Pocket Option",
    tryFree: "Спробувати демо",
    openMenu: "Відкрити меню",
    closeMenu: "Закрити меню",
    drawerRisk: "Трейдинг пов’язаний із ризиком. Інвестуйте лише ті гроші, втрату яких можете собі дозволити.",
    language: "Мова",
    footAbout:
      "Pocket Option — вебплатформа для торгівлі валютами, криптовалютою, акціями та сировиною: депозит від $5, угоди від $1 і безкоштовний демо-рахунок на $50 000.",
    footCols: ["Pocket Option", "Навчання", "Про сайт"],
    footLinks: {
      "/review/": "Огляд",
      "/demo-account/": "Демо-рахунок",
      "/app/": "Застосунок",
      "/deposit-withdrawal/": "Поповнення і виведення",
      "/how-to-trade/": "Як торгувати",
      "/bonus-promo-code/": "Бонуси та промокоди",
      "/blog/": "Блог (EN)",
      "/faq/": "FAQ",
      "/about/": "Про нас (EN)",
      "/contact/": "Контакти (EN)",
      "/disclaimer/": "Відмова від відповідальності",
      "/privacy/": "Конфіденційність",
      "/risk-warning/": "Попередження про ризики",
    } as Record<string, string>,
    risk: "Попередження про ризики: торгівля фінансовими інструментами пов’язана з високим ризиком і може призвести до втрати вкладених коштів. Торгуйте лише тими грошима, які готові втратити. Матеріали сайту мають інформаційний характер і не є інвестиційною порадою. Частина посилань — партнерські: ми можемо отримувати комісію без додаткових витрат для вас.",
    rights: "Усі права захищено.",
    endTitle: "Спробуйте Pocket Option без ризику на демо-рахунку",
    endNowrap: "без ризику",
    endText: "Потренуйтеся на віртуальних $50 000 і освойтеся на платформі, перш ніж торгувати реальними грошима.",
    updated: "Оновлено",
    toc: "Зміст",
    side: {
      title: "Pocket Option у цифрах",
      rows: [
        ["Мінімальний депозит", "$5"],
        ["Мінімальна угода", "$1"],
        ["Демо-баланс", "$50 000"],
        ["Активи", "100+"],
        ["Рік заснування", "2017"],
      ],
      open: "Відкрити рахунок",
    },
    payNote:
      "А також Jeton, Volet, WebMoney, Tron, Solana, місцеві банківські перекази, мобільні платежі та ще 160+ способів — набір залежить від країни.",
  },
};

export const t = (lang: Lang) => STR[lang];
