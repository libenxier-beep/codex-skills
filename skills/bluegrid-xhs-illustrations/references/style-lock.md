# Style Lock

## Purpose

Use this file before every direct image generation. The goal is to reduce drift: 小蓝格 should not become a cute blue mascot, robot, app icon, or random square character after several generations.

## Anchor Set

The stable source images live in `assets/style-anchors/`.

| Anchor | Best For |
| --- | --- |
| `01-cover-anchor.png` | Core character proportions, headphones, pushing away prompt clutter |
| `03-five-layers-anchor.png` | Five-drawer system metaphor and 4:5 layout density |
| `05-memory-routing-anchor.png` | Chat-pile sorting, blue thread, drawer routing |
| `07-skills-drawer-anchor.png` | Drawer cabinet, card-in-hand action, anti-prompt-scroll contrast |
| `08-work-contexts-anchor.png` | Tall scene-library shelf and folder insertion |
| `09-build-system-anchor.png` | Workbench, connector action, stable collaboration mood |

## Generation Rule

Before writing the final prompt:

1. Pick one character anchor: usually `01-cover-anchor.png`, `05-memory-routing-anchor.png`, or `09-build-system-anchor.png`.
2. Pick one composition anchor that matches the current metaphor: drawer, shelf, checkpoint, workbench, doorway, or routing pile.
3. If generating a series, keep the same character anchor across the whole series and vary only the composition anchor.
4. If the image tool supports visual references, attach the chosen anchor images as style references. If not, include the Style Lock Block below verbatim in the prompt.

Do not copy the anchor layout directly. Use anchors to lock line weight, character shape, color, spacing, and visual maturity.

## Style Lock Block

```text
Style lock:
Match the Bluegrid anchor set. 小蓝格 is a sky-blue rounded-square content-system operator with subtle light-blue hand-painted fill, tiny black dot eyes, thin black line arms and legs, and simple deep-blue thin-line over-ear headphones. The body is softly square, slightly uneven, and adult, not a cute blob, not a robot, not an app icon, not a mascot sticker. Use black hand-drawn pen lines, light blue fills, deep-blue headphone accents, sparse orange movement paths, tiny red correction marks only when needed, and large clean white space. Keep the composition like a quiet hand-drawn creator-system sketch: low-tech physical objects, gentle line hatching, simple labels, no glossy vector polish, no chibi proportions, no big smile, no oversized eyes, no cartoon poster mood.
```

## Character Consistency Rules

- Body: rounded square, wider than tall or nearly square; never a circle, blob, robot head, or icon tile.
- Face: two tiny black dot eyes; no mouth unless the anchor-like neutral small line is necessary.
- Headphones: deep-blue thin over-ear arc plus two simple ear pads; no microphone, cat ears, helmet, DJ headset, or bulky gear.
- Limbs: thin black line arms and legs; simple hand/foot marks only.
- Fill: light sky-blue watercolor-like fill, with subtle blue edge variation; not flat corporate vector blue.
- Mood: calm and useful, slightly dry-humored; not adorable, childish, excited, or expressive.

## Drift Repair Prompts

### Too Cute

```text
Regenerate with stricter Bluegrid style lock. Make 小蓝格 less cute and more like a quiet content-system operator: tiny black dot eyes, neutral expression, thin limbs, simple deep-blue headphones, softly square sky-blue body, no big smile, no oversized eyes, no chibi body, no mascot sticker mood.
```

### Character Changed Shape

```text
Regenerate while preserving the same core idea, but restore 小蓝格 to the anchor-set shape: a sky-blue rounded square with subtle hand-painted fill, tiny black dot eyes, thin black limbs, and visible simple deep-blue over-ear headphones. Do not make it a robot, app icon, blob, or generic blue character.
```

### Style Became Too Polished

```text
Regenerate in the anchor-set style: hand-drawn black pen lines, light blue fills, sparse orange path marks, lots of white space, low-tech physical metaphor. Remove glossy vector polish, UI panels, gradients, decorative shadows, poster composition, and formal diagram layout.
```

