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

export const faqSchema = (items: QA[]) => ({
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: items.map((i) => ({
    "@type": "Question",
    name: i.q,
    acceptedAnswer: { "@type": "Answer", text: i.a.replace(/<[^>]+>/g, "") },
  })),
});
