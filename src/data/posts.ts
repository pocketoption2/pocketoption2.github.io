export const POSTS = [
  {
    slug: "pocket-option-login",
    title: "Pocket Option login: fix the most common problems",
    excerpt:
      "How to sign in on web and mobile, reset your password, and what to do when Google sign-in or 2FA gets in the way.",
    date: "2026-11-21",
  },
  {
    slug: "pocket-option-otc",
    title: "Pocket Option OTC assets explained",
    excerpt:
      "What OTC means on Pocket Option, why it is open on weekends and how its payouts and prices differ from regular markets.",
    date: "2026-11-19",
  },
  {
    slug: "pocket-option-minimum-deposit",
    title: "Pocket Option minimum deposit: what $5 gets you",
    excerpt:
      "What you can realistically do with a $5, $50 or $100 deposit, and how to size your trades so a small account lasts.",
    date: "2026-11-17",
  },
];
export const fmtDate = (d: string) =>
  new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
