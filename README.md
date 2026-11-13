# Shopify Store SEO Skill

A Claude skill for store and product SEO on Shopify, built from Asjad's real SEO work on his live store. Claude handles all the work end to end — keyword plan, product titles and descriptions, image alt text, collection descriptions, meta titles and descriptions, internal linking and menu, sitemap and Google Search Console, and a pre-launch SEO checklist — with the owner involved only for the decisions, accounts, sign-ins and approval gates. It is modeled on the live store Fragrance Empire, a complete Shopify store with 155 products, 18 brands and 28 collections.

## What it does

Takes a store's SEO from keyword plan to launch in one repeatable workflow:

1. **Keyword plan** — main keyword for the store, one keyword per product and per collection, tier agreed. No writing before the plan is confirmed.
2. **Product titles and descriptions** — keyword + benefit title structure, and the four-part description template used across the reference catalog: opening line naming the product / brand / size, a notes paragraph (only when the facts exist), a short benefits section, and a closing trust line. A product with no notes gets no notes paragraph — none is invented.
3. **Image alt text** — descriptive, keyword-first, unique per image, under 125 characters, no keyword stuffing.
4. **Collection descriptions** — the four-part pattern used for the store's 21 collection descriptions, with a reusable template and worked examples.
5. **Meta titles and descriptions** — templates for products, collections, the homepage and store pages, with hard character limits (meta title up to 60, meta description 120–160).
6. **Internal linking and menu** — audience collections (For Him / For Her / Unisex), brand collections, bundles, and the main menu structure, with link rules.
7. **Sitemap + Google Search Console** — verify the sitemap loads (the reference store's sitemap had 184 pages), submit it in Search Console, check indexed pages.
8. **Pre-launch SEO checklist + approval gate** — nothing goes live until the owner approves the keyword plan, the description template, the meta templates and the checklist.
9. **First month** — weekly Search Console checks, fixes, and full SEO on every new product before it is published.

## Who does what — Claude handles all the work end to end

Claude runs every step — keyword plan, titles and descriptions, alt text, collection copy, meta templates, internal-link plan, the SEO checker script, checklists. The owner is involved only at three points: (1) decisions only the owner can make (market and language, keywords, product facts, delivery / returns promises, tier); (2) accounts, sign-ins and money (Google account for Search Console, Shopify Admin sign-in, paid SEO apps — all on the owner's own device); and (3) approval gates (keyword plan, description template, meta templates, final checklist). The two device-bound exceptions are Shopify Admin access (browser with the owner's sign-in, or Admin API with an access token the owner creates) and Google Search Console verification (owner's Google account, on their device). Everything else is Claude's work — do not hand it back to the owner as homework.

## The live example store

- **Store:** Fragrance Empire — https://fragranceempire.my
- **Platform:** Shopify, Basic plan, Horizon theme, currency MYR, timezone Asia/Kuala_Lumpur, market Malaysia
- **Catalog:** 155 products = 142 single products + 13 bundles, 18 brands, 28 collections
- **Collections:** For Him, For Her, Unisex, one collection per brand (18), Bundles, Featured / Best Sellers — 21 collection descriptions written
- **Main menu:** Home, Executive range, Bundles, For Him, For Her, Unisex, Categories (18 brand collections), Contact, About Us
- **Sitemap:** 184 pages
- **Payments:** Cash on Delivery (COD) + card payments via Stripe (Visa, Mastercard, Amex, JCB, Discover, Diners, Apple Pay, Google Pay)
- **Shipping:** Standard, FREE, 3–5 business days across Malaysia
- **Built by:** Asjad Farooq, Shopify Store Designer — Fiverr gig https://www.fiverr.com/s/L34yBpA

## Service tiers (the seller's real packages)

| Tier | Products covered | Pages covered | Delivery | Revisions |
|---|---|---|---|---|
| Basic | 10 | 5 | 3 days | Unlimited |
| Standard | 30 | 8 | 5 days | Unlimited |
| Premium | 50 | 10 | 7 days | Unlimited |

Prices: Basic $80, Standard $180, Premium $350. "Products covered" means full SEO for that many products (title, description, alt text, meta title, meta description). Ask the owner which tier the SEO work is before starting, and do not build a bigger scope than the tier covers without agreement.

## Files

```
shopify-store-seo/
├── README.md                                  # this file
└── shopify-store-seo/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── check_seo.py                       # checks a product CSV for SEO problems
    └── templates/
        ├── meta-templates.md                  # meta title / description templates
        ├── collection-description-template.md # collection description template + examples
        ├── pre-launch-seo-checklist.md        # keyword plan + pre-launch SEO checklist
        └── seo-product-sample.csv             # sample product CSV (intentionally has SEO problems — see below)
```

## Setup

### 1. Get the keyword plan first

Fill in `templates/pre-launch-seo-checklist.md` (Step 1 of `SKILL.md`) with the owner: store name, market, currency, language, main store keyword, one keyword per product and per collection, tier. Do not start writing until the owner confirms the plan.

### 2. Choose the store-update route (one of these)

**Route A — Shopify Admin in the browser (recommended to start).** The owner signs in to Shopify Admin on their own device and approves each step, or approves a browser session. Claude prepares everything (titles, descriptions, alt text, meta tags, collection copy) and the owner applies it in Admin. No API key needed.

**Route B — Shopify Admin API with a custom app.** The owner creates a custom app in Shopify Admin, sets the needed access scopes, and creates an access token on their own device. The skill then follows the API steps. This is more setup, and it is the only route that lets an agent change the store without the browser.

Do not use any other route. Do not paste API keys, passwords or credentials into the skill files, into chat, or into a repo — credentials live only in the owner's secure storage.

### 3. Check the SEO before publishing

Run the checker on the product CSV (Shopify export format) until it passes:

```bash
python3 shopify-store-seo/scripts/check_seo.py shopify-store-seo/templates/seo-product-sample.csv
```

The sample CSV intentionally contains SEO problems (missing SEO title, missing alt text, over-long SEO title, too-short description, duplicate SEO title, over-long product title, short description) so you can see what the checker reports. A real product CSV must pass with 0 errors before anything is published.

### 4. Use in Claude

Copy the `shopify-store-seo/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `shopify-store-seo/SKILL.md`. Then ask Claude to run the workflow, for example: "Do the SEO for my Shopify perfume store using the shopify-store-seo skill. Tier: Standard."

## Honest limits — read before using

- **Never invent product facts.** Every brand, size, note, feature and price comes from the owner or the owner's verified supplier list. A product with no notes gets no notes paragraph — none is invented — and the gap is flagged for the owner.
- **No keyword stuffing.** A keyword appears once in a title and once or twice in a description, in natural language.
- **No duplicate meta titles or descriptions.** Every product, collection and page gets its own. The checker flags duplicates.
- **No credentials in the skill.** No API keys, passwords, access tokens, bank details or secrets are stored in these files. Logins and Search Console verification happen on the owner's own device.
- **Approval gate is mandatory.** No title, description or meta tag is published until the owner approves the exact final version. A changed title, description or meta tag needs fresh approval.
- **SEO takes time and is never guaranteed.** Rankings depend on Google, competition and time. Never promise a position, a traffic number, or a date by which the store will rank.
- **No fake reviews or fake claims.** SEO copy never claims a product is original / authentic unless the owner states it and takes responsibility for it.

## How to run one SEO job

1. Fill in the keyword plan in `templates/pre-launch-seo-checklist.md` and get the owner to confirm it.
2. Write the product titles and descriptions, alt text and collection descriptions from the templates (Steps 2–4 of `SKILL.md`).
3. Write the meta titles and descriptions and set up the internal links and menu (Steps 5–6).
4. Verify the sitemap and submit it in Search Console (Step 7).
5. Run `scripts/check_seo.py` on the product CSV until it passes, fill in the checklist, and get the owner's approval at the gate (Step 8).
6. Launch, then do the first-month checks (Step 9).
