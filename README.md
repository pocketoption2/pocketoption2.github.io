# pocketoption2.github.io

Static Astro site for https://pocketoption2.github.io.

- `npm install` then `npm run dev` (local) or `npm run build` (output in `dist/`).
- Affiliate URLs: edit `LINKS` in `src/data/site.ts`. All CTAs go through `/go/<key>/` redirect pages (noindex, disallowed in robots.txt).
- Deploy: `.github/workflows/deploy.yml` runs manually (Actions → Deploy to GitHub Pages → Run workflow). Set Pages source to "GitHub Actions" first.
