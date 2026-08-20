import os

def main():
    filepath = 'js/ai-travel-engine.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    old_init = """window.AITravelEngine = AITravelEngine;

function initAITravelEngine() {
  if (typeof AITravelEngine !== 'undefined') {
    AITravelEngine.renderCandidateSpots();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAITravelEngine);
} else {
  initAITravelEngine();
}

window.addEventListener('load', initAITravelEngine);"""

    new_init = """window.AITravelEngine = AITravelEngine;

function initAITravelEngine() {
  if (typeof AITravelEngine !== 'undefined' && typeof AITravelEngine.renderCandidateSpots === 'function') {
    try {
      AITravelEngine.renderCandidateSpots();
    } catch (err) {
      console.error('Failed in initAITravelEngine:', err);
    }
  }
}

// 1. Immediate Execution as soon as script is parsed
initAITravelEngine();

// 2. DOM Ready and Load Event Listeners
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAITravelEngine);
}
window.addEventListener('load', initAITravelEngine);

// 3. Robust Multi-Stage Retries (Handles slow mobile 4G downloads of 4.2MB JS file)
[100, 300, 600, 1200, 2500].forEach(delay => {
  setTimeout(() => {
    const container = document.getElementById('candidateSpotsGrid');
    if (container && (!container.children || container.children.length === 0)) {
      console.log(`🔄 [0MT ENGINE] Retrying candidate spots render at ${delay}ms...`);
      initAITravelEngine();
    }
  }, delay);
});"""

    if old_init in code:
        code = code.replace(old_init, new_init)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print("SUCCESS: Updated js/ai-travel-engine.js initialization safety block!")
    else:
        print("Error: old_init string not found in ai-travel-engine.js")

if __name__ == '__main__':
    main()
