import re

def main():
    filepath = 'js/ai-travel-engine.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    # Update badges & headers
    code = code.replace('📍 Selected Spots Only', '🎯 Selected Spots Only')
    code = code.replace('📍 ROUTE A: SELECTED SPOTS ONLY', '🎯 ROUTE A: SELECTED SPOTS ONLY')

    old_func_start = '  renderSpotItemsHtml(spotsArray, routeType, cityClean) {'
    old_func_end = '\n  moveSpot(routeType, index, direction) {'

    start_idx = code.find(old_func_start)
    if start_idx == -1:
        print('Error: old_func_start not found!')
        return

    end_idx = code.find(old_func_end, start_idx)
    if end_idx == -1:
        print('Error: old_func_end not found!')
        return

    new_func = """  renderSpotItemsHtml(spotsArray, routeType, cityClean) {
    if (!spotsArray || spotsArray.length === 0) {
      return '<div style="font-size:0.85rem; color:#9CA3AF; padding:0.75rem; text-align:center; border:1px dashed #E5E7EB; border-radius:8px;">No spots in this route. Add spots or re-select.</div>';
    }

    const t = (key) => window.I18nEngine ? window.I18nEngine.getText(key) : key;

    return spotsArray.map((spot, idx) => {
      const spotDisplayName = this.getLocalizedSpotName(spot);
      const spotDesc = this.getLocalizedDesc(spot);
      const query = `${spot.name || spotDisplayName} ${cityClean}`;
      const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(query)}`;

      return `
        <div class="route-spot-card" style="background:#F8FAFC; border:1.5px solid #E2E8F0; padding:0.65rem 0.75rem; border-radius:12px; font-size:0.88rem; display:flex; flex-direction:column; gap:0.45rem; width:100%; box-sizing:border-box; margin-bottom:0.4rem;">
          
          <!-- Row 1: Top Bar (Index + Spot Name + Badges + Remove ✕ Button) -->
          <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:0.5rem; width:100%;">
            
            <div style="display:flex; align-items:flex-start; gap:0.45rem; flex:1; min-width:0;">
              <!-- Index Badge -->
              <span style="font-weight:800; background:#E2E8F0; color:#334155; width:24px; height:24px; display:inline-flex; align-items:center; justify-content:center; border-radius:50%; font-size:0.75rem; flex-shrink:0; margin-top:1px;">${idx + 1}</span>
              
              <!-- Spot Title & Badges -->
              <div style="display:flex; flex-direction:column; min-width:0; flex:1;">
                <div style="font-weight:800; color:#0F172A; font-size:0.92rem; line-height:1.3; word-break:break-word; cursor:pointer;" ${spot.id ? `onclick="AITravelEngine.openSpotModal('${spot.id}')"` : ''} title="${escapeHtml(spotDisplayName)} — View Details">
                  ${escapeHtml(spotDisplayName)}
                </div>
                <div style="display:flex; align-items:center; gap:0.25rem; flex-wrap:wrap; margin-top:0.2rem;">
                  ${spot.isHotel || spot.category === 'Hotel & Stay' ? `
                    <span style="font-size:0.62rem; font-weight:800; background:#F3E8FF; color:#7E22CE; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #D8B4FE; white-space:nowrap;">🏨 Return Hotel</span>
                  ` : spot.isMustVisit ? `
                    <span style="font-size:0.62rem; font-weight:800; background:#D1FAE5; color:#047857; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #A7F3D0; white-space:nowrap;">🎯 Selected</span>
                  ` : `
                    <span style="font-size:0.62rem; font-weight:800; background:#FEF3C7; color:#B45309; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">✨ AI Pick</span>
                  `}
                  ${spot.timeSlot === 1 ? `<span style="font-size:0.62rem; font-weight:800; background:#E0F2FE; color:#0369A1; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #BAE6FD; white-space:nowrap;">🌅 Sightseeing</span>` : ''}
                  ${spot.timeSlot === 2 ? `<span style="font-size:0.62rem; font-weight:800; background:#FEF3C7; color:#92400E; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">☕ Café Break</span>` : ''}
                  ${spot.timeSlot === 3 ? `<span style="font-size:0.62rem; font-weight:800; background:#FCE7F3; color:#BE185D; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #FBCFE8; white-space:nowrap;">🍷 Dinner</span>` : ''}
                  ${spot.timeSlot === 4 ? `<span style="font-size:0.62rem; font-weight:800; background:#F1F5F9; color:#334155; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #CBD5E1; white-space:nowrap;">🌙 Night Scenery</span>` : ''}
                </div>
              </div>
            </div>

            <!-- Remove Button (✕) -->
            <button type="button" class="icon-touch-btn danger" onclick="AITravelEngine.removeSpot('${routeType}', ${idx})" title="Remove spot from route" aria-label="Remove spot" style="flex-shrink:0; padding:0.25rem 0.45rem; font-weight:800;">✕</button>
          </div>

          <!-- Row 2: Spot Description (Full Width) -->
          ${spotDesc ? `
            <p style="font-size:0.78rem; color:#475569; line-height:1.4; margin:0; padding-left:1.85rem; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; text-overflow:ellipsis;">
              ${escapeHtml(spotDesc)}
            </p>
          ` : ''}

          <!-- Row 3: Bottom Action Bar (Reorder Up/Down Left | View Details & Maps Right) -->
          <div style="display:flex; align-items:center; justify-content:space-between; gap:0.4rem; padding-top:0.35rem; border-top:1px dashed #E2E8F0; margin-top:0.1rem; flex-wrap:wrap;">
            
            <!-- Reorder Controls -->
            <div style="display:flex; align-items:center; gap:0.25rem; flex-shrink:0;">
              <button type="button" class="icon-touch-btn" onclick="AITravelEngine.moveSpot('${routeType}', ${idx}, -1)" ${idx === 0 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''} aria-label="Move Up" style="padding:0.2rem 0.55rem; font-size:0.75rem; border-radius:6px; font-weight:800;">▲</button>
              <button type="button" class="icon-touch-btn" onclick="AITravelEngine.moveSpot('${routeType}', ${idx}, 1)" ${idx === spotsArray.length - 1 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''} aria-label="Move Down" style="padding:0.2rem 0.55rem; font-size:0.75rem; border-radius:6px; font-weight:800;">▼</button>
            </div>

            <!-- View Details & Google Maps Buttons -->
            <div style="display:flex; align-items:center; gap:0.35rem; flex-shrink:0;">
              ${spot.id ? `
                <button type="button" onclick="AITravelEngine.openSpotModal('${spot.id}')" style="display:inline-flex; align-items:center; justify-content:center; gap:0.2rem; background:#EFF6FF; color:#0369A1; border:1px solid #BAE6FD; padding:0.25rem 0.55rem; border-radius:6px; font-weight:800; font-size:0.75rem; cursor:pointer; white-space:nowrap; -webkit-tap-highlight-color:transparent;" title="${t('btn.viewDetails')}">
                  ${t('btn.viewDetails')}
                </button>
              ` : ''}
              <a href="${mapsUrl}" target="_blank" rel="noopener noreferrer" style="color:#2563EB; font-weight:700; text-decoration:none; font-size:0.75rem; background:#EFF6FF; border:1px solid #BFDBFE; padding:0.25rem 0.55rem; display:inline-flex; align-items:center; border-radius:6px; white-space:nowrap;">📍 Maps ↗</a>
            </div>

          </div>

        </div>
      `;
    }).join('');
  }

"""

    new_code = code[:start_idx] + new_func + code[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_code)
    print('SUCCESS: Updated renderSpotItemsHtml cleanly')

if __name__ == '__main__':
    main()
