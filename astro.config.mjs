import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import { copyFile } from "node:fs/promises";

const plainSitemap = {
  name: "plain-sitemap",
  hooks: {
    "astro:build:done": async ({ dir }) => {
      await copyFile(new URL("sitemap-0.xml", dir), new URL("sitemap.xml", dir));
    },
  },
};

export default defineConfig({
  site: "https://pocketoption2.github.io",
  trailingSlash: "always",
  build: { format: "directory" },
  integrations: [sitemap({
      filter: (page) => !page.includes("/go/"),
      lastmod: new Date(),
      i18n: { defaultLocale: "en", locales: { en: "en", ru: "ru", ua: "uk" } },
    }), plainSitemap],
});
