export const SITE = {
  name: "Pocket Option",
  url: "https://pocketoption2.github.io",
  locale: "en_US",
  updated: "2026-11-23",
};

// Replace these with the affiliate URLs before going live.
export const LINKS = {
  register: "https://pocketoption.com",
  demo: "https://pocketoption.com",
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

export const DRAWER_NAV = [
  { href: "/review/", label: "Review" },
  { href: "/demo-account/", label: "Demo account" },
  { href: "/app/", label: "App" },
  { href: "/deposit-withdrawal/", label: "Deposits & withdrawals" },
  { href: "/bonus-promo-code/", label: "Bonus & promo codes" },
  { href: "/how-to-trade/", label: "How to trade" },
  { href: "/blog/", label: "Blog" },
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
