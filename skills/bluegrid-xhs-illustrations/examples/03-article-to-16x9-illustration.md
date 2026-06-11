# Example 03: 中文文章到 16:9 正文图

## User Input

```text
这段文章需要一张横版正文配图：
很多 AI 工作流失败，不是因为工具不够多，而是每一步都没有明确输入输出。最后看似自动化，其实只是把混乱传递给下一个工具。
```

## Expected Strategy

使用 16:9 横版，不做小红书首图。图只表达“混乱被传递，而不是被处理”。

## Final Prompt

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Fresh sky-blue accent blocks. Sparse orange path marks and red correction marks only when needed. No gradients, no shadows, no paper texture, no commercial vector style, no PPT infographic look, no realistic UI.

Recurring IP character required:
小蓝格, a small sky-blue rounded-square character with tiny black dot eyes, thin line arms and legs, blank serious expression, wearing a simple thin-line deep-blue over-ear headphone. The headphone must be visible but minimal. 小蓝格 must perform the core conceptual action.

Theme:
AI 工作流失败，是因为输入输出不清楚。

Core idea:
自动化不能只是把混乱传给下一个工具，每一步都需要明确接收、处理和交付。

Composition:
Wide white canvas with three simple low-tech boxes connected by a thin orange line. The first box receives a messy tangle labeled “输入不清”. The second box is open, and 小蓝格 wearing thin blue headphones is standing inside, holding a small blue measuring ruler and trying to straighten the tangle into a clean strip. The third box receives a cleaner strip labeled “可交付”. A red tag sits on a bypass line that sends the tangle directly forward: “别传混乱”. Keep the boxes loose and hand-drawn, not a formal architecture diagram.

Chinese handwritten labels:
输入不清 / 判断 / 可交付 / 别传混乱

Constraints:
16:9 horizontal. No top-left title, no formal workflow chart, no PPT style, no dense architecture, no realistic UI, no shadows, no texture, no gradients. Keep at least 40% blank white space. 小蓝格 must be central to the repair action.
```

## Acceptance Notes

- The image should read as a hand-drawn metaphor, not a system architecture slide.
- If 小蓝格 only stands beside the boxes, regenerate with 小蓝格 inside the middle box doing the repair.

