---
name: shopify-store-seo
description: Store and product SEO for Shopify — Claude writes product titles and descriptions (keyword + benefit structure, never inventing product facts), image alt text, collection descriptions, meta titles and descriptions for products / collections / homepage, internal linking and the main menu, sitemap + Google Search Console verification, and a pre-launch SEO checklist. Modeled on the live store Fragrance Empire (fragranceempire.my — 155 products, 18 brands, 28 collections, Malaysia market, Horizon theme, sitemap 184 pages). Use when the user asks for store SEO, product SEO, meta titles or descriptions, alt text, collection descriptions, Search Console setup, or an SEO check / audit of a Shopify store.
---

# Shopify Store SEO

## When to use

Use this skill when the user asks for SEO on a Shopify store: writing or fixing product titles and descriptions, image alt text, collection descriptions, meta titles and descriptions, internal linking and menu structure, sitemap and Google Search Console setup, or running a pre-launch SEO check / SEO audit. The end result is a store where every product, collection and page has unique, accurate search metadata — not a demo.

Do not use it for paid ads (Google Ads, Meta ads), for marketplaces (Amazon, Etsy, eBay), or for a platform other than Shopify, unless the user explicitly asks to adapt it. Do not use it to write fake reviews or fake product claims — SEO never invents facts.

## Who does what — Claude handles all the work end to end

Claude runs every step of the workflow below — keyword plan, product titles and descriptions, alt text, collection descriptions, meta titles and descriptions, internal links and menu, sitemap and Search Console steps, and the pre-launch checklist. The owner is involved only at these points:

1. **Decisions only the owner can make** — the store's target market and language, the keywords that matter to the business, the product facts (brand, size, notes, price), the delivery / returns promises, and which tier the SEO work is (see Scope tiers). Claude drafts everything; the owner supplies the facts and approves them.
2. **Accounts, sign-ins and money** — the Google account used for Google Search Console, the Shopify Admin sign-in, and paying for any paid SEO app. These happen on the owner's own device, with the owner's own details. Claude never handles the owner's password or payment credentials.
3. **Approval gates** — the owner approves the keyword plan, the description template, the meta title / description templates, and the final pre-launch SEO checklist before anything goes live (see Step 8). Nothing is published without that approval.

Two device-bound exceptions, stated honestly so the "end to end" claim is not overstated:

- **Shopify Admin access:** Claude works through the owner's Shopify Admin (browser, with the owner's sign-in) or through the Shopify Admin API with an access token the owner creates in a custom app. Claude never invents store credentials and never logs in as the owner.
- **Google Search Console:** verification and sitemap submission happen in the owner's Google account, on their own device. Claude prepares the exact steps and the sitemap URL; the owner clicks through them.

Everything else — research, keyword plan, title and description writing, alt text, collection copy, meta templates, internal-link plan, the SEO checker script, checklists — is Claude's work. Do not hand any of it back to the owner as homework.

## Store facts — the live reference store (do not invent others)

Fragrance Empire (https://fragranceempire.my) is the live store this skill is modeled on. Use its real, verified facts as the reference example. Do not invent a different reference store.

- **Store:** Fragrance Empire, fragranceempire.my, Shopify Basic plan, Horizon theme, currency MYR, timezone Asia/Kuala_Lumpur, market Malaysia.
- **Catalog:** 155 products = 142 single products + 13 bundles, 18 brands, 28 collections.
- **Collections:** audience collections For Him, For Her and Unisex; one collection per brand (18); a Bundles collection; and a Featured / Best Sellers collection. Products that fit two groups are in both (for example unisex products appear in For Him, For Her and Unisex). 21 collection descriptions were written for the store.
- **Main menu:** Home, Executive range, Bundles, For Him, For Her, Unisex, Categories (the 18 brand collections), Contact, About Us.
- **Description template:** used across all 141 descriptions written for the catalog — opening line naming the product / brand / size, a notes paragraph (fragrance notes / key features), a short benefits section, and a closing trust line (see Step 2).
- **Sitemap:** the store's sitemap had 184 pages (products, collections, pages, blog) at the time it was checked. Shopify generates the sitemap automatically at `<store-domain>/sitemap.xml`.
- **Payments:** Cash on Delivery (COD) active; card payments live through a Stripe card-payments provider. Shopify Payments is not available in Malaysia — do not promise it for a Malaysia store.
- **Shipping:** exactly one rate — Standard, FREE, 3–5 business days, across Malaysia.
- **Trust block on product pages:** Ordered = today, Packed = +1 day, Delivered = +2 days; subtext "Dispatched in 24 hours."
- **Seller services (Fiverr gig https://www.fiverr.com/s/L34yBpA):** Basic $80 — 10 products, 5 pages, 3 days; Standard $180 — 30 products, 8 pages, 5 days; Premium $350 — 50 products, 10 pages, 7 days. Unlimited revisions on all three packages.

## Hard limits — state them honestly, do not work around them

- **Never invent product facts.** Every product name, brand, size, fragrance note, feature and price comes from the owner or the owner's verified supplier list. If a fact is missing, ask — do not fill it in. A few products in the reference catalog have no notes paragraph, and none was invented for them: a product with no notes gets a description with no notes paragraph, and the gap is flagged for the owner. Never write a note, ingredient or benefit the supplier did not state.
- **Never write fake reviews or fake claims.** SEO copy never claims a product is original / authentic unless the owner states it and takes responsibility for it. If the products are impressions / inspired-by, say so in the store's own terms or say nothing — do not write "100% original" into a title, description or meta description on Claude's own initiative.
- **No keyword stuffing.** A keyword appears once in a title and once or twice in a description, in natural language. Repeating a keyword to game rankings is not SEO and damages the listing.
- **No duplicate meta titles or descriptions.** Every product, collection and page gets its own. Duplicates are flagged by `scripts/check_seo.py` and fixed before launch.
- **No credentials in the skill.** Never put an API key, password, access token, bank detail or secret in a skill file, in chat, or in a repo. Logins and Search Console verification happen on the owner's own device.
- **Approval gates are mandatory.** Nothing is published until the owner approves the exact version: keyword plan, description template, meta templates, and the pre-launch checklist. A changed title, description or meta tag needs fresh approval.
- **SEO takes time and is never guaranteed.** Rankings depend on Google, competition and time. Never promise a position, a traffic number, or a date by which the store will rank. Say what was done and what to check, not what Google will do.
- **Paid SEO apps need the owner's approval.** Never install a paid app or accept a paid plan / trial that converts to a charge without the owner approving the exact price first. Free plans only unless approved.
- **Do not guess-attach product photos or alt text.** Alt text describes the image that is actually on the product. If a photo shows a different size or variant than the listing, flag it — do not write alt text that describes the wrong product.

## Scope tiers — ask which one before starting

Mirror the seller's real packages. Ask the owner which tier the SEO work is, and do not build a bigger scope than the tier covers without agreement.

| Tier | Products covered | Pages covered | Delivery | Revisions |
|---|---|---|---|---|
| Basic | 10 | 5 | 3 days | Unlimited |
| Standard | 30 | 8 | 5 days | Unlimited |
| Premium | 50 | 10 | 7 days | Unlimited |

"Products covered" means full SEO for that many products: title, description, alt text, meta title and meta description. "Pages covered" means collections and store pages (Home, About, Contact, policies). If the owner's catalog is bigger than the tier, agree the split (for example: the 50 best-selling products now, the rest as a follow-up) before starting.

## Workflow

### Step 1 — Keyword plan (decisions first, no writing before this)

Collect and write down, in `templates/pre-launch-seo-checklist.md`:

1. Store name, market / country, currency, language, and the store domain.
2. What the store sells (niche, brands, product types) and who buys it.
3. The main keyword for the store — what a customer types to find this kind of store (for example "buy perfume online Malaysia").
4. One main keyword per product — what a customer types to find that exact product (for example "Dior Sauvage EDP 100ml price Malaysia"). The keyword comes from the product's real brand, name and size; never invent a brand or size to make a keyword.
5. One main keyword per collection — audience collections ("perfume for men Malaysia"), brand collections ("[Brand] perfume Malaysia"), bundles ("perfume gift set Malaysia").
6. The tier (Basic / Standard / Premium) and which products and pages it covers.
7. Anything the owner explicitly does NOT want (for example: no "100% original" claims, no fake reviews, no keyword stuffing).

Do not start Step 2 until the keyword plan is filled in and the owner has confirmed it. A missing product fact is a blocker, not something to guess.

### Step 2 — Product titles and descriptions

Every product gets the same four-part structure. Fill in the blanks from the owner's product facts only.

**1. Product title — keyword + benefit structure**

- Pattern: `[Brand] [Product Name] [Type] [Size] — [main benefit or use]`
- Example: `Dior Sauvage Eau de Parfum 100 ML — Fresh Woody Fragrance for Men`
- The brand, product name, type and size come from the supplier list — never invent one. The benefit is one short phrase from the product's real character (for example "fresh woody", "long-lasting", "for daily wear") — never a claim the supplier did not make.
- Keep the title under 70 characters. The brand and product name come first; the benefit is dropped first if the title runs long.
- Every title is unique. Two sizes of the same product are different titles because the size is in the title.

**2. Description — the four-part template (used across the reference catalog)**

- **Opening line (1 sentence):** name the product, brand and size, and what it is. Example: "Dior Sauvage Eau de Parfum 100 ML is a fresh woody fragrance for men from Dior."
- **Notes paragraph (only when the facts exist):** the product's notes / key features, in the supplier's own terms. Example: "Top notes of bergamot and pepper, a heart of lavender and geranium, and a base of ambroxan and cedar." If the supplier gave no notes, there is no notes paragraph — write nothing, invent nothing, and flag the product in the checklist as "no notes supplied".
- **Benefits section (2–4 short lines):** what the product is good for, in plain language, from the real facts only. Example: "Long-lasting wear for day and evening. A versatile everyday fragrance. Presented in the 100 ML bottle."
- **Closing trust line (same on every product):** the store's real delivery and returns promise, matching the shipping policy. Example: "Free delivery across Malaysia in 3–5 business days. Cash on Delivery available."
- Write the description in the store's language (English for Fragrance Empire). One keyword in the opening line, one in the notes or benefits — never more. No keyword stuffing, no repeated phrases copied across products.
- Bundles: the description lists every product in the bundle by name and size, states the saving in the same currency as the prices, and the saving must match the actual prices.

### Step 3 — Image alt text

1. Every product image gets alt text. No image is left with empty alt text, and no two images on the same product share the same alt text.
2. Pattern: `[Brand] [Product Name] [Type] [Size] — [what the image shows]`. Example: `Dior Sauvage Eau de Parfum 100 ML — front view of bottle and box`. The first image is the main image; its alt text names the product, brand and size with no extra words.
3. Keyword-first: the product keyword comes first, then the description of the image. One keyword per alt text, never repeated.
4. Describe what is actually in the image. If the photo shows a different size than the listing (for example a photo showing "200ml" on a 100 ML listing), do not write alt text for it — flag the photo for the owner instead.
5. Keep alt text under 125 characters. No "image of" / "picture of" — start with the product name.

### Step 4 — Collection descriptions

Use the template in `templates/collection-description-template.md`. Every collection gets the same four-part structure:

1. **Opening line:** what the collection is and who it is for. Example: "Shop men's perfumes at Fragrance Empire — designer fragrances for him, delivered free across Malaysia."
2. **What is inside:** the brands or product types in the collection, named exactly as they appear in the store. Never name a brand that is not in the collection.
3. **Why buy here:** one or two lines from the store's real offer — free delivery, COD, the delivery time. Only promises the store actually keeps.
4. **Internal links:** link to the two or three most relevant collections (see Step 6). A brand collection links to the audience collection it belongs to and to Bundles; an audience collection links to its top brand collections.
5. Keep the description to 100–150 words. One main keyword in the opening line, once more in the body — never more.

### Step 5 — Meta titles and descriptions

Use the templates in `templates/meta-templates.md`. Character limits are hard limits — count before publishing.

| Page type | Meta title | Meta description |
|---|---|---|
| Product | Up to 60 characters | 120–160 characters |
| Collection | Up to 60 characters | 120–160 characters |
| Homepage | Up to 60 characters | 120–160 characters |

- **Product meta title:** `[Brand] [Product Name] [Size] | [Store Name]`. Example: `Dior Sauvage EDP 100 ML | Fragrance Empire` (44 characters). Drop the store name first if the title runs long.
- **Product meta description:** keyword + benefit + offer, in one or two sentences. Example: "Buy Dior Sauvage EDP 100 ML online in Malaysia. Fresh woody fragrance for men. Free delivery, Cash on Delivery available at Fragrance Empire."
- **Collection meta title:** `[Collection Name] | [Store Name]`. Example: `Perfume for Men | Fragrance Empire`.
- **Collection meta description:** what the collection is + the store offer. Example: "Shop men's perfumes online in Malaysia — designer fragrances for him. Free delivery in 3–5 days, Cash on Delivery available."
- **Homepage meta title:** `[Store Name] — [main keyword phrase]`. Example: `Fragrance Empire — Buy Perfume Online in Malaysia`.
- **Homepage meta description:** what the store sells + the offer + the market. Example: "Fragrance Empire — designer perfumes online in Malaysia. 18 brands, free delivery in 3–5 days, Cash on Delivery available."
- Every meta title and meta description is unique across the store. Duplicates are flagged by `scripts/check_seo.py`.
- Write the meta description as a sentence a customer would want to click, not a keyword list. Never repeat the keyword more than twice, and never write a claim the store cannot keep.

### Step 6 — Internal linking and the main menu

1. **Main menu (in order):** Home, Executive range, Bundles, For Him, For Her, Unisex, Categories (the 18 brand collections), Contact, About Us. Check every menu link on desktop and mobile — a link to a collection that does not exist is a launch blocker.
2. **Audience collections link to brand collections:** For Him links to the top men's brands in the store; For Her links to the top women's brands; Unisex links to the unisex brands. Link from the collection description text, not only from the menu.
3. **Brand collections link back:** each brand collection links to the audience collection it belongs to and to Bundles.
4. **Bundles link to singles:** each bundle description links to the single products in the bundle, so a customer can compare.
5. **Product pages link up:** each product description links to its brand collection and its audience collection.
6. **Homepage links down:** the homepage links to For Him, For Her, Unisex, Bundles and the top brand collections — never to a collection with no products.
7. **Footer links:** policy pages (Privacy, Refund / Return, Shipping, Terms), About, Contact, and the social links. Every link is checked live before launch.
8. **Link text is descriptive:** use the collection or product name as the link text ("Shop Dior perfumes", not "click here"). No more than 3–4 internal links in any one description — the copy stays readable.

### Step 7 — Sitemap + Google Search Console

1. **Verify the sitemap loads:** open `https://<store-domain>/sitemap.xml` in a browser. Shopify generates it automatically — do not build or upload a sitemap by hand. The reference store's sitemap had 184 pages (products, collections, pages, blog). Note the count in the checklist; a much lower count than the product + collection + page total means pages are missing or unpublished.
2. **Google Search Console (owner's Google account, on their device):**
   - Go to Google Search Console and add the store as a property (Domain or URL-prefix — Domain is preferred if the owner controls DNS).
   - Verify ownership by the method Google offers (DNS record or HTML tag). The owner does this on their own device; Claude prepares the exact steps.
   - Submit the sitemap: Sitemaps > Add a new sitemap > `sitemap.xml`. Record the submission date in the checklist.
3. **Check indexed pages:** after a few days, check Pages > Indexed in Search Console. The indexed count should be close to the sitemap count. Pages listed as "not indexed" are checked one by one: unpublished products, duplicate pages, and pages blocked by mistake are the usual causes. Never submit a sitemap for a store that is still password-protected — remove password protection first.
4. **Check the store as a customer would:** search Google for the store name and for the main product names. The store name and the main products must appear. If a product does not appear after two weeks, check that it is active, has a unique meta title and description, and is linked from a collection.
5. **Bing Webmaster Tools (optional):** same steps, same sitemap URL, if the owner wants it. Do not submit to any other "SEO submission" service — they are not needed and some charge for nothing.

### Step 8 — Pre-launch SEO checklist + approval gate

Complete `templates/pre-launch-seo-checklist.md` for the store. Then stop and get the owner's approval for: the keyword plan, the description template, the meta title / description templates, and the checklist itself. Launch only after approval.

Before asking for approval, run the checker and fix every problem it reports:

```bash
python3 scripts/check_seo.py templates/seo-product-sample.csv
```

The checker reads a product CSV (Shopify export format — see `templates/seo-product-sample.csv` for the columns it reads) and flags, one line per problem:

- Missing SEO title or SEO description
- SEO title over 60 characters, or under 30 characters
- SEO description over 160 characters, or under 120 characters
- Missing image alt text
- Duplicate SEO titles across products
- Product title over 70 characters
- Missing or very short product description (Body under 50 characters)
- Duplicate product Handles

It prints PASS when there are no problems and FAIL with the problem list otherwise, and exits 0 on PASS, 1 on FAIL. Do not publish SEO that fails the check — fix every problem, then run the checker again.

The checklist also covers, by hand (the checker cannot see these): every collection has a description, the homepage title and description are set, the main menu links all work, internal links are in place, the sitemap loads, the sitemap is submitted in Search Console, and the store was checked on mobile and desktop for the exact search terms a customer would use.

### Step 9 — After launch (first month)

1. Check Search Console weekly for the first month: indexed pages going up, no new errors, and the sitemap still submitted.
2. Fix any page Search Console reports as an error, and re-verify live after each fix.
3. When a new product is added, give it the full treatment before publishing: title, four-part description, alt text, meta title and meta description. A product published without SEO is a product customers cannot find.
4. Do not change titles, descriptions or meta tags without the owner's approval, and record every change in the checklist so the next SEO pass starts from a known state.
5. Never promise a ranking position or a date. Report what was done, what Search Console shows, and what is still pending.

## How to run one SEO job

1. Fill in the keyword plan (Step 1) and get the owner to confirm it.
2. Write the product titles and descriptions (Step 2), alt text (Step 3) and collection descriptions (Step 4) from the templates.
3. Write the meta titles and descriptions (Step 5) and set up the internal links and menu (Step 6).
4. Verify the sitemap and submit it in Search Console (Step 7).
5. Run `scripts/check_seo.py` on the product CSV until it passes, fill in `templates/pre-launch-seo-checklist.md`, and get the owner's approval at the gate (Step 8).
6. Launch, then do the first-month checks (Step 9).
