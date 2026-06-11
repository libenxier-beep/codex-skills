# Example 04: PPT 感失败图与修复

## Failure Scenario

生成图出现以下问题：

- 顶部有大标题“AI 工作流路线图”。
- 画面是整齐矩形节点和箭头。
- 小蓝格站在角落，没有参与动作。
- 中文标签很多，像课程页。

## Diagnosis

这不是小蓝格正文配图，而是 PPT 信息图。失败层在 prompt 的构图约束和动作主体。

## Repair Prompt

```text
Regenerate with the same core idea, but remove the PPT layout completely.

Use one low-tech physical metaphor instead of formal boxes and arrows: a simple hand-drawn sorting shelf with one loose orange path line. 小蓝格 must be in the center wearing thin deep-blue headphones, actively pulling one clean blue thread out of a messy input tangle. Keep pure white background, sparse black hand-drawn line art, sky-blue 小蓝格, minimal labels, and at least 40% blank space.

Allowed Chinese labels only:
输入不清 / 判断 / 可交付 / 别传混乱

Do not write any top title. Do not use a grid, formal nodes, numbered steps, icons, UI panels, or course-slide style. Do not add extra accessories besides the headphone.
```

## Pass Criteria

- No top title.
- No formal node grid.
- 小蓝格 performs the repair action.
- Labels are reduced to 4 short phrases.
- The main subject occupies no more than 60% of the canvas.

