export const SITE = {
  name: "Pocket Option",
  url: "https://pocketoption2.github.io",
  locale: "en_US",
  updated: "2026-11-23",
};

export const VERIFY = {
  google: "fUL0FjmS-ZiG5MUbaLgeCC8EMfhO1KJXFtTL91vniP4",
  bing: "3CA04D93E5BEE83F0FD74BED3310FC79",
};

const AFFILIATE =
  "https://u3.shortink.io/register?utm_campaign=65155&utm_source=affiliate&utm_medium=sr&a=bsNUQyo6TJ9wXJ&ac=lk";

// Sign-up, login, demo and the iPhone/desktop/Telegram app links share the main affiliate link; Android has its own.
export const LINKS = {
  register: AFFILIATE,
  demo: AFFILIATE,
  app: AFFILIATE,
  android: "https://potrade.onelink.me/oyit/webapp?c=65155&a=bsNUQyo6TJ9wXJ&af_cost_model=revshare&ac=app",
} as const;

export type LinkKey = keyof typeof LINKS;
export const go = (key: LinkKey) => `/go/${key}/`;

export const NAV = [
  { href: "/review/", label: "Review" },
  { href: "/demo-account/", label: "Demo account" },
  { href: "/app/", label: "App" },
  { href: "/deposit-withdrawal/", label: "Deposits" },
  { href: "/bonus-promo-code/", label: "Bonus" },
  { href: "/faq/", label: "FAQ" },
];

export const FOOTER = [
  {
    title: "Pocket Option",
    links: [
      { href: "/review/", label: "Review" },
      { href: "/demo-account/", label: "Demo account" },
      { href: "/app/", label: "App" },
      { href: "/deposit-withdrawal/", label: "Deposits" },
    ],
  },
  {
    title: "Learn",
    links: [
      { href: "/how-to-trade/", label: "How to trade" },
      { href: "/bonus-promo-code/", label: "Bonus and promo codes" },
      { href: "/blog/", label: "Blog" },
      { href: "/faq/", label: "FAQ" },
    ],
  },
  {
    title: "About",
    links: [
      { href: "/about/", label: "About us" },
      { href: "/contact/", label: "Contact" },
      { href: "/disclaimer/", label: "Disclaimer" },
      { href: "/privacy/", label: "Privacy" },
    ],
  },
];
