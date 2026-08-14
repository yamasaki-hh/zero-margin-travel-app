# Zero-Margin Travel App - Version Changelog

All notable changes and release checkpoints for the Zero-Margin Travel App will be documented in this file.

---

## 🏷️ [v1.2.0] - 2026-08-14 (Area Zone & Kids Filter Release)

### 🌟 Summary
- **Step 1 Form Simplification**: Removed `Traveler Type` and `Transportation Mode` dropdowns. Added clean `エリア選択 (Area Zone)` dropdown (`✨ すべて (市内＋郊外)`, `🏙️ 市内スポット`, `🏞️ 郊外・日帰りスポット`).
- **Step 2 Kids Filter Chips & Multi-Tagting**: Added `🧸 Kids (子供向け)` filter chip to Step 2. Supports multi-category matching (e.g. NEMO Science Museum or Pompidou Center appear under BOTH `🎨 美術館・博物館` and `🧸 Kids`).
- **Cascading Filter Logic**: Selecting "Paris" + "郊外" in Step 1 automatically filters Step 2 to Paris suburban spots (e.g. Versailles, Disneyland Paris). Clicking `🧸 Kids` in Step 2 further narrows down to Paris suburban kid-friendly attractions!
- **Visual Badge System**: Every spot candidate card displays `🏙️ 市内` or `🏞️ 郊外` and `🧸 Kids` badges.

---

## 🏷️ [v1.0.0-stable] - 2026-08-14 (Baseline Checkpoint)

### 🌟 Summary
- **7 European Cities Fully Active**: Paris (45), Berlin (32), Amsterdam (20), Brussels (13), Luxembourg City (20), Cologne (9), Munich (12). Total 151 Candidate Spots.
- **Ultra-Simple Wikipedia REST Summary API Architecture**: 110 spots with verified official Wikipedia summary photos (73% photo match rate across all cities).
- **0% Photo Mismatch Guard**: 41 local cafes/bakeries cleanly fall back to Warm Atelier Category Header Boxes.
- **UI Fallback Protection**: Added `onerror` handler to hide broken image boxes instantly if browser CDN throttling occurs.

### 🔖 Git Tag Rollback Command
To instantly roll back the entire codebase to this exact working version at any point in the future:
```bash
git checkout v1.0.0-stable
```

---

## 🚀 How Version Rollbacks Work

1. **Roll Back Entire Codebase (Local Testing)**:
   ```bash
   git checkout v1.0.0-stable
   ```
2. **Roll Back GitHub Pages Deployment**:
   ```bash
   git checkout main
   git reset --hard v1.0.0-stable
   git push origin main --force
   ```
3. **Return to Latest Development**:
   ```bash
   git checkout main
   ```
