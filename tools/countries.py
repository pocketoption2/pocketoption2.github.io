# Generates English country pages src/pages/<slug>.astro. Payment methods verified on
# https://pocketoption.com/en/payment-methods/ (2026-11-23).
C = {
"india": dict(
 name="India", cur="INR (Indian rupee)",
 title="Pocket Option India: Login, UPI Deposits & App Guide",
 desc="Pocket Option in India: how to sign up and log in, deposit from $5 with UPI, IMPS, Paytm, PhonePe or GPay, withdraw, and use the app. Risks explained.",
 h1="Pocket Option in India",
 lead="How Indian traders sign up, log in, deposit with UPI and withdraw on Pocket Option, plus the legal and tax points to check before you trade.",
 pay=[("UPI","Bank","Pay from any UPI app linked to your bank account."),("IMPS","Bank","Instant bank transfer, useful for larger amounts."),("Paytm","Bank","Pay through the Paytm app or wallet."),("PhonePe","Bank","UPI payment from the PhonePe app."),("GPay","Bank","UPI payment from Google Pay.")],
 avail="Pocket Option accepts registrations from India and shows Indian payment methods such as UPI when you deposit from an Indian account. India is not on the broker's list of restricted countries.",
 legal="India's rules on online forex and binary-style trading are strict. The Reserve Bank of India publishes an Alert List of unauthorised forex platforms, and Indian residents are generally allowed to trade forex only in permitted INR pairs through authorised brokers on Indian exchanges. Check the current RBI Alert List and consider getting local advice before you deposit. Profits may also be taxable.",
 tips=["Use the UPI ID or bank account in your own name. Third-party payments are a common reason for rejected withdrawals.","Keep the UPI transaction reference until the deposit appears in your balance.","Your bank may show the payment under a payment processor's name rather than Pocket Option."],
 login="Most traders in India use the Android app or a mobile browser. If your network is slow, the web platform at pocketoption.com loads a lighter mobile version automatically.",
 faq=[("Can I deposit with UPI on Pocket Option?","Yes. UPI appears in the deposit list for Indian accounts, along with IMPS, Paytm, PhonePe and GPay. The minimum deposit is $5 for most methods."),("What is the minimum deposit in rupees?","The minimum is set in US dollars: $5 for most methods. The rupee amount shown at checkout depends on the exchange rate of the day."),("Is Pocket Option legal in India?","Pocket Option is an offshore broker and is not authorised by the RBI or SEBI. Check the RBI Alert List and your own legal position before trading."),("How do I withdraw to my bank in India?","Open Finance → Withdrawal after verifying your account and choose the same method you used to deposit, such as UPI or IMPS.")]),
"pakistan": dict(
 name="Pakistan", cur="PKR (Pakistani rupee)",
 title="Pocket Option Pakistan: Deposit with JazzCash & Easypaisa",
 desc="Pocket Option in Pakistan: sign up and log in, deposit from $5 with JazzCash, Easypaisa, Raast QR or bank transfer in PKR, withdraw and use the app.",
 h1="Pocket Option in Pakistan",
 lead="Sign-up, login, JazzCash and Easypaisa deposits, and withdrawals for traders in Pakistan, with the risks to understand first.",
 pay=[("JazzCash","E-wallet","Pay from your JazzCash mobile account."),("Easypaisa","E-wallet","Pay from your Easypaisa mobile account."),("Raast QR","Bank","Scan the QR code with your banking app via Raast, the State Bank instant payment system."),("Bank Transfer (PKR)","Bank","Local transfer in rupees from a Pakistani bank account.")],
 avail="Pakistan is not on Pocket Option's list of restricted countries, and Pakistani accounts see local PKR payment methods at checkout.",
 legal="Pocket Option is not licensed by the Securities and Exchange Commission of Pakistan (SECP). The SECP has warned the public about unlicensed online trading platforms, so you trade without local regulatory protection. Check the SECP's current guidance before depositing.",
 tips=["Your JazzCash or Easypaisa account must be registered in the same name as your Pocket Option profile.","Complete the OTP or in-app approval quickly; payment sessions time out after a few minutes.","Keep the transaction ID from the SMS or app receipt in case support asks for it."],
 login="Mobile is the main way to trade in Pakistan. Install the Android app from Google Play or the official APK, and keep 2-factor confirmation on in your profile.",
 faq=[("Can I deposit with JazzCash or Easypaisa?","Yes. Both are listed as e-payment methods with 0% Pocket Option commission. The minimum deposit is $5 for most methods."),("Can I use Raast?","Yes. Raast QR is available: scan the code shown at checkout with your banking app."),("Is Pocket Option regulated in Pakistan?","No. It is an offshore broker and is not licensed by the SECP, so local investor protection does not apply."),("How do I withdraw in Pakistan?","Verify your account, then request a withdrawal to the same JazzCash, Easypaisa or bank account you used to deposit.")]),
"nigeria": dict(
 name="Nigeria", cur="NGN (Nigerian naira)",
 title="Pocket Option Nigeria: Naira Deposits, OPay & PalmPay",
 desc="Pocket Option in Nigeria: sign up and log in, deposit from $5 in naira by bank transfer, Verve card, OPay or PalmPay, withdraw and use the app safely.",
 h1="Pocket Option in Nigeria",
 lead="How Nigerian traders fund Pocket Option in naira, get verified and withdraw, with the regulatory points to know before you start.",
 pay=[("Bank Transfer (NGN)","Bank","Transfer naira from your Nigerian bank account to the account shown at checkout."),("Visa, Mastercard, Verve (NGN)","Card","Pay with a naira card, including Verve."),("OPay (NGN)","Bank","Pay from your OPay account."),("PalmPay (NGN)","Bank","Pay from your PalmPay account.")],
 avail="Nigeria is not on Pocket Option's restricted list, and Nigerian accounts can deposit in naira through local banks, cards and fintech wallets.",
 legal="Pocket Option is not registered with Nigeria's Securities and Exchange Commission (SEC Nigeria), which regularly warns about unregistered online investment platforms. Treat it as an offshore broker without local protection.",
 tips=["When paying by bank transfer, send the exact amount shown and use the account details generated for that payment only.","Card payments may need online authorisation from your bank; enable international or online payments if a card is declined.","Withdraw to a bank account or wallet in your own name that you used to deposit."],
 login="Most Nigerian traders use the Android app. If the site is slow on mobile data, switch to the web platform's lighter mobile view or use Wi-Fi for deposits.",
 faq=[("Can I deposit in naira?","Yes. Bank transfer, naira cards (Visa, Mastercard, Verve), OPay and PalmPay are listed for NGN. The minimum deposit is $5 for most methods."),("Is Pocket Option legit in Nigeria?","It has operated since 2017, but it is not registered with SEC Nigeria, so there is no local investor protection."),("How long do naira withdrawals take?","After verification, local transfers usually arrive the same day to a few days, depending on the bank."),("Does Pocket Option work on mobile in Nigeria?","Yes. Use the Android app, the iPhone web app or any mobile browser.")]),
"bangladesh": dict(
 name="Bangladesh", cur="BDT (Bangladeshi taka)",
 title="Pocket Option Bangladesh: Deposit with bKash & Nagad",
 desc="Pocket Option in Bangladesh: sign up and log in, deposit from $5 with bKash or Nagad, withdraw, use the app, and the legal risks to check first.",
 h1="Pocket Option in Bangladesh",
 lead="bKash and Nagad deposits, account verification and withdrawals on Pocket Option for traders in Bangladesh, and why to read the legal section first.",
 pay=[("bKash","E-wallet","Pay from your bKash mobile wallet."),("Nagad","E-wallet","Pay from your Nagad mobile wallet."),("Crypto","Crypto","USDT (TRC-20, BEP20), Bitcoin and other coins are available worldwide.")],
 avail="Bangladesh is not on Pocket Option's list of restricted countries, and bKash and Nagad appear as deposit options.",
 legal="Bangladesh has strict foreign exchange controls. Bangladesh Bank has warned that sending money abroad for online forex or crypto trading without permission may break the Foreign Exchange Regulation Act. Understand these rules, and the risk to your bKash or Nagad account, before you deposit.",
 tips=["Use a bKash or Nagad account registered with your own NID and name, matching your Pocket Option profile.","Do not share your PIN or OTP with anyone, including people offering \"agent\" deposits.","Save the transaction ID from the bKash or Nagad receipt."],
 login="Pocket Option works on the Android app and in any mobile browser. Use the official website or Google Play only; fake APKs and Telegram \"signal\" groups are common scams.",
 faq=[("Can I deposit with bKash on Pocket Option?","Yes. bKash and Nagad are listed as e-payment methods with 0% Pocket Option commission. The minimum deposit is $5 for most methods."),("Is Pocket Option legal in Bangladesh?","Pocket Option is an offshore broker. Bangladesh Bank restricts sending funds abroad for online trading, so check the rules before you deposit."),("How do I withdraw to bKash or Nagad?","Verify your account, then request a withdrawal to the same wallet you used to deposit."),("Is there a Bangla version?","The Pocket Option platform supports more than 40 languages. You can change the language in your profile settings.")]),
}
ORDER = ["india", "pakistan", "nigeria", "bangladesh"]

def esc(s): return s.replace("{", "&#123;").replace("}", "&#125;")

def page(slug, d):
    others = " · ".join(f'<a href="/{o}/">Pocket Option {C[o]["name"]}</a>' for o in ORDER if o != slug)
    rows = "\n".join(f"      <tr>\n        <td>{n}</td>\n        <td>{t}</td>\n        <td>{x}</td>\n      </tr>" for n, t, x in d["pay"])
    tips = "\n".join(f"    <li>{esc(x)}</li>" for x in d["tips"])
    faq = "\n".join(f"  <h3>{q}</h3>\n  <p>{a}</p>" for q, a in d["faq"])
    schema = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]
    import json
    return f'''---
import Article from "../layouts/Article.astro";
import {{ go }} from "../data/site";
const toc = [
  {{ id: "available", label: "Availability" }},
  {{ id: "signup", label: "Sign up and log in" }},
  {{ id: "payments", label: "Payment methods" }},
  {{ id: "withdraw", label: "Withdrawals" }},
  {{ id: "legal", label: "Rules and risks" }},
  {{ id: "faq", label: "FAQ" }},
];
const schema = [{{ "@context": "https://schema.org", "@type": "FAQPage", mainEntity: {json.dumps(schema, ensure_ascii=False)} }}];
---

<Article
  cover="deposit-withdrawal"
  title="{d["title"]}"
  description="{d["desc"]}"
  h1="{d["h1"]}"
  lead="{d["lead"]}"
  crumb="{d["name"]}"
  toc={{toc}}
  schema={{schema}}
>
  <h2 id="available">Is Pocket Option available in {d["name"]}?</h2>
  <p>{d["avail"]} Account currency can be US dollars; local payments are converted from {d["cur"]} at checkout.</p>

  <h2 id="signup">Sign up and log in</h2>
  <ol>
    <li>Open Pocket Option and register with your email or Google account.</li>
    <li>Confirm your email, then try the <a href="/demo-account/">free $50,000 demo</a> before depositing.</li>
    <li>Complete verification in your profile with an ID that matches your name. It is required before your first withdrawal.</li>
  </ol>
  <p>{d["login"]} See the <a href="/app/">app guide</a> for install steps.</p>
  <p>
    <a href={{go("register")}} rel="sponsored nofollow">Open a Pocket Option account →</a>
  </p>

  <h2 id="payments">Payment methods in {d["name"]}</h2>
  <p>These local methods are listed on Pocket Option's official payment page, all with 0% Pocket Option commission. The minimum deposit is $5 for most methods. What you see at checkout can vary by account.</p>
  <table>
    <thead>
      <tr>
        <th>Method</th>
        <th>Type</th>
        <th>How it works</th>
      </tr>
    </thead>
    <tbody>
{rows}
    </tbody>
  </table>
  <p>Cards, crypto such as USDT and Bitcoin, and e-wallets like Jeton and Volet are also available worldwide.</p>
  <h3>Deposit tips</h3>
  <ul>
{tips}
  </ul>

  <h2 id="withdraw">Withdrawals</h2>
  <p>Open <strong>Finance → Withdrawal</strong> after your account is verified. Anti-money-laundering rules require funds to go back to a method you used to deposit. Pocket Option sets no minimum withdrawal when no deposit bonus is active. Full details are on the <a href="/deposit-withdrawal/">deposits and withdrawals page</a>.</p>

  <h2 id="legal">Rules and risks in {d["name"]}</h2>
  <p>{d["legal"]}</p>
  <p>Short-term trading carries a high risk of loss. Only trade money you can afford to lose, and read our <a href="/review/">Pocket Option review</a> before opening a real account.</p>

  <h2 id="faq">Pocket Option {d["name"]} FAQ</h2>
{faq}

  <p>Other countries: {others}</p>
</Article>
'''
for s in ORDER:
    open(f"src/pages/{s}.astro", "w").write(page(s, C[s]))
