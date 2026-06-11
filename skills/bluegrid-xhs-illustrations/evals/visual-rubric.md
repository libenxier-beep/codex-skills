# Visual Rubric

Use this rubric after image generation or when comparing variants. Score each item as 0 or 1.

## Eleven-Point Rubric

- [ ] Correct aspect ratio: 4:5 for Xiaohongshu, 16:9 for article body, unless user specified otherwise.
- [ ] Pure white background with no paper texture, gradient, shadow, gray wash, or decorative pattern.
- [ ] 小蓝格 appears as the recurring IP character.
- [ ] 小蓝格 is a sky-blue rounded square with tiny black dot eyes and thin limbs.
- [ ] The thin-line deep-blue over-ear headphone is visible and not a microphone headset, helmet, cat-ear, or DJ accessory.
- [ ] 小蓝格 matches the anchor-set maturity: quiet operator, not cute mascot, chibi, robot, app icon, or sticker.
- [ ] 小蓝格 performs the core conceptual action rather than standing aside as decoration.
- [ ] The image keeps at least about 35% blank space and the main subject stays around 40%-60% of the canvas.
- [ ] The image does not look like a PPT slide, course page, formal flowchart, commercial vector illustration, cute mascot poster, or realistic UI.
- [ ] Chinese handwritten labels are sparse, short, readable, and not a big title or paragraph.
- [ ] The core metaphor is understandable within one second at phone-feed size.

## Score Interpretation

- 11: Strong final candidate.
- 9-10: Usable, with optional minor edit.
- 7-8: Direction is recoverable; rewrite the prompt around the failed items.
- 0-5: Regenerate from a simpler concept and read `references/composition-patterns.md` again.

## Required Reviewer Notes

When scoring below 10, write the failed item numbers and one repair instruction. Example:

```text
Score: 7/10
Failed: 5, 6, 8
Repair: Make the headphones thin and visible, put 小蓝格 inside the sorting action, remove formal node boxes.
```

## Variant Selection Rule

When multiple variants pass 8/10, prefer the one where:

- 小蓝格's action is clearest.
- The image has more white space.
- The labels are fewer.
- The metaphor is less template-like.
