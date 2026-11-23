# -*- coding: utf-8 -*-
import glob
import os

block_to_insert = """          <!-- [Columns] Table Column Headers (Brand vs Competitors) -->
          <div class="field-row">
            <div class="field-header">
              <div class="field-title-wrap">
                <span class="field-callout-pill">[Columns] Headers</span>
                <span class="field-title-text">Comparison Table Column Headers (Your Brand vs Competitors)</span>
              </div>
              <span class="field-target-loc">Comparison Table > Column Headers</span>
            </div>
            <div class="old-content-box">
              <div class="old-tag">Live Site Existing Content:</div>
              <div class="old-text">Our product<br>Others</div>
            </div>
            <div class="copy-box">
              <div class="content-preview" id="table-cols-en">Zelmiqo<br>Other Brands</div>
              <div class="copy-btn-bar">
                <button class="copy-btn" onclick="copyFrom('table-cols-en', this)">📋 Copy English</button>
              </div>
            </div>
            <div class="copy-box">
              <div class="content-preview arabic" id="table-cols-ar">زيلميكو<br>العلامات الأخرى</div>
              <div class="copy-btn-bar">
                <button class="copy-btn" onclick="copyFrom('table-cols-ar', this)">📋 Copy Arabic</button>
              </div>
            </div>
          </div>

"""

target_marker = "<!-- [2] 5-Row Comparison Matrix -->"

files = sorted(glob.glob("new-content-html-pages/product-*.html"))
updated_count = 0

for f in files:
    if "dock" in f:
        # Already updated in pilot
        continue
    with open(f, "r", encoding="utf-8") as fo:
        content = fo.read()
    
    if "table-cols-en" in content:
        print(f"Skipping {f} (already contains table-cols-en)")
        continue
    
    if target_marker in content:
        new_content = content.replace(target_marker, block_to_insert + target_marker)
        with open(f, "w", encoding="utf-8") as fo:
            fo.write(new_content)
        updated_count += 1
        print(f"Updated: {f}")
    else:
        print(f"ERROR: marker not found in {f}")

print(f"\nSuccessfully added column headers block to {updated_count} product workstations!")
