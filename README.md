# Zelmiqo

E-commerce store assets, page components, categories, codes, and media.

## Project Structure

- `categories/` – Category listing pages and category visual badges
- `codes/` – Active CSS and JS stylesheets/scripts (including RTL/Arabic variants)
- `codes-old/` – Previous version styles and scripts
- `icons/` – SVG and PNG icon assets
- `images/` – High-resolution product and banner imagery
- `images-old/` – Archival images
- `new-content/` – Markdown product documentation and product descriptions
- `pages/` – Full page design mockups and sections (header, footer, product details, cart, home, etc.)
- `payment-method/` – Payment gateway brand badges
- `url-list.html` & `zelmiqo-pages-urls.txt` – Page URLs and directory references

## Automated Git Sync

This repository includes a background auto-push service that automatically monitors file edits, commits changes, and pushes directly to GitHub:

- **Start auto-push service**: `./start-autopush.sh`
- **Stop auto-push service**: `./stop-autopush.sh`
- **View sync logs**: `cat .autopush.log`
