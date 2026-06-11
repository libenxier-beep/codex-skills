# Example 02: 小红书选题到单张生图 Prompt

## User Input

```text
用小蓝格耳机风格生成一张小红书首图：为什么你收藏了很多素材，还是写不出东西。
```

## Expected Read Path

- `SKILL.md`
- `references/style-dna.md`
- `references/bluegrid-ip.md`
- `references/prompt-template.md`
- `references/qa-checklist.md`

## Final Prompt

```text
Generate one standalone 4:5 vertical Xiaohongshu Chinese note illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Fresh sky-blue accent blocks. Sparse orange path marks, red correction marks, and deep-blue handwritten notes only when needed. Clean creator-tool sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
小蓝格, a small sky-blue rounded-square character with tiny black dot eyes, thin line arms and legs, blank serious expression, slightly uneven hand-drawn body shape. 小蓝格 wears a simple thin-line deep-blue over-ear headphone as its fixed signature accessory. The headphone must be visible but minimal, with no microphone boom and no bulky details. 小蓝格 must perform the core conceptual action, not decorate the scene. Make 小蓝格 calm, useful, and slightly dry-humored, not cute.

Theme:
收藏了很多素材，还是写不出东西。

Structure type:
卡点纠偏

Core idea:
素材堆积本身不会变成表达，必须先找到一个真实判断或感受。

Composition:
Pure white vertical canvas. On the left, many small loose paper scraps labeled “素材”, “截图”, “金句” are piled too high in a simple hand-drawn tray. In the center, 小蓝格 wears thin deep-blue headphones and listens to the pile like it is noisy. 小蓝格 uses one thin blue line to pull out a small note labeled “真判断”. On the right, a clean blank note page is waiting, with only a few short black lines beginning to appear. Add a tiny red tag on the overflowing pile: “别堆满”. Use one subtle orange movement line from the pile to the blank note.

Suggested elements:
paper scraps / overflowing tray / thin headphones / blue thread / blank note page

Chinese handwritten labels:
素材 / 截图 / 金句 / 真判断 / 别堆满

Color use:
Black for main line art and text. Sky blue for 小蓝格 and key content blocks. Deep blue for the headphone and secondary notes. Orange only for the main path or movement. Red only for warnings, corrections, or key results.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5 short handwritten Chinese labels. Do not write a big title at the top. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not make 小蓝格 a cute mascot or a commercial logo. Do not add any extra accessories besides the headphone. It should be clear, fresh, adult, minimal, and publishable on Xiaohongshu.
```

## Visual Rubric Focus

- 4:5 vertical.
- 小蓝格 is visible and wears thin blue headphones.
- 小蓝格 performs the action: listening to noisy material and pulling out the judgment.
- No big headline or PPT layout.
- Labels remain short and readable.

