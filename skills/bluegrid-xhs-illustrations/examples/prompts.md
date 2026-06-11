# Prompt Examples

These prompts are based on the real example image set in `examples/images/` and the stricter source anchors in `assets/style-anchors/`. Use them as calibration patterns, not as layouts to copy exactly.

## Shared Visual DNA

Use this block in every prompt unless the user specifies a different direction:

```text
Pure white background. Minimalist black hand-drawn line art with slightly wobbly pen lines. Fresh sky-blue 小蓝格 character with tiny black dot eyes, thin line arms and legs, and visible simple deep-blue thin-line over-ear headphones. Sparse orange movement path, tiny red correction marks only when needed, and a few short blue handwritten Chinese labels. Lots of white space. Low-tech physical metaphor, not formal UI, not PPT, not commercial vector illustration, not cute mascot poster.
```

## Consistency Lock

Use this before every image prompt:

```text
Use `references/style-lock.md`. Pick 1-3 images from `assets/style-anchors/` as style anchors. Keep 小蓝格's body shape, headphone design, line weight, blue fill, and quiet operator mood consistent with those anchors. Do not make 小蓝格 cuter than the anchors.
```

## 01 Cover: From Prompt Collecting To System Building

Target image: `examples/images/01-cover.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
别再只收藏提示词，要搭一套稳定的 Codex 协作系统。

Composition:
On the left, a messy bin overflows with paper notes labeled “提示词”, “收藏”, “复制”. In the center, 小蓝格 wears thin deep-blue headphones and uses both arms to push the paper overflow away. On the right, a clean desk has several small blue system blocks arranged calmly, with a thin orange line moving toward a circle labeled “系统”. Keep the scene spacious and hand-drawn.

Chinese handwritten labels:
别只收藏 / 搭系统 / 少而稳 / 系统
```

## 02 Retrain Loop: Repeating Context From Scratch

Target image: `examples/images/02-retrain-loop.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
每次打开 AI 都像重新培训一个新人。

Composition:
A hand-drawn loop connects a messy document pile, a small training desk, and two simple doorway characters labeled “下一次”. 小蓝格 stands in the middle wearing headphones, holding a stack of repeated instructions, trying to route them into a stable blue note block. Use a thin orange circular arrow to show repetition and a small red mark labeled “反复教”.

Chinese handwritten labels:
反复教 / 重复交代 / 空白新人 / 稳定规则
```

## 03 Five Layers: Personal Codex Architecture

Target image: `examples/images/03-five-layers.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
我的 Codex 五层架构。

Composition:
Draw a low-tech shelving unit with five blue drawers. The drawers are labeled “身份”, “记忆”, “约束”, “技能”, “场景”. 小蓝格 wears headphones and stands beside the shelf, carefully pushing one drawer into place. A small note on top says “稳定协作”. Keep it clean, sparse, and not like a formal diagram.

Chinese handwritten labels:
五层架构 / 身份 / 记忆 / 约束 / 技能 / 场景
```

## 04 Identity Boundary: Startup Protocol

Target image: `examples/images/04-identity-boundary.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
身份层让 Agent 先知道协作边界。

Composition:
Draw a simple open doorway labeled “启动协议”. 小蓝格 wears headphones and holds a small boundary card at the door, preventing a blank speech bubble from rushing in. Inside the doorway is a calm desk with a small blue rule note. Use one orange path from outside chaos to inside workspace.

Chinese handwritten labels:
身份层 / 启动协议 / 协作边界 / 先对齐
```

## 05 Memory Routing: Layered Memory

Target image: `examples/images/05-memory-routing.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
记忆不是聊天记录，而是分层路由。

Composition:
On the left, a cloud of chat bubbles and loose notes floats messily. 小蓝格 wears headphones and pulls a few selected blue notes into a tidy drawer shelf labeled “核心”, “场景”, “归档”. A red X marks the overflowing pile. Keep the action focused on sorting and routing.

Chinese handwritten labels:
聊天记录 / 记忆层 / 核心 / 场景 / 别全塞
```

## 06 Guardrail Checkpoint: Do Not Rush Into Execution

Target image: `examples/images/06-guardrail-checkpoint.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
约束层让 Agent 先检查，再执行。

Composition:
Draw a small checkpoint on a curved orange road. 小蓝格 wears headphones and holds a checklist beside a stop sign. Several small signposts say “先判断”, “再动手”, “要验证”. A task arrow waits at the checkpoint before moving toward a clean output door.

Chinese handwritten labels:
约束层 / 检查点 / 先判断 / 再动手 / 要验证
```

## 07 Skills Drawer: Load Abilities On Demand

Target image: `examples/images/07-skills-drawer.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
Skills 是按需加载的能力抽屉。

Composition:
Draw a blue drawer cabinet with drawers labeled “写作”, “代码”, “记忆”, “研究”. 小蓝格 wears headphones and pulls out one card labeled “怎么做”. A long scroll labeled “万能 prompt” sits nearby with a large red X. Use a small orange arrow from “任务” to the selected drawer.

Chinese handwritten labels:
技能层 / 按需取用 / 任务 / 怎么做 / 别堆满
```

## 08 Work Contexts: Long-Term Scene Knowledge

Target image: `examples/images/08-work-contexts.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
Work contexts 承接长期场景判断。

Composition:
Draw a tall open cabinet labeled “场景库”, with shelves such as “写作”, “工程”, “学习”. 小蓝格 wears headphones and slides a folder into the correct shelf. A small box labeled “临时任务” sits on the floor, connected by a thin orange path to the cabinet.

Chinese handwritten labels:
场景库 / 长期判断 / 写作 / 工程 / 学习
```

## 09 Build System: From Prompts To Operating Environment

Target image: `examples/images/09-build-system.png`

```text
Generate one 4:5 vertical Xiaohongshu illustration.

Theme:
不要只找神级提示词，先搭协作系统。

Composition:
Draw a simple workbench with several blue system blocks: “协作”, “技能”, “约束”, “身份”. 小蓝格 wears headphones and tightens one small connector on the workbench. On the left, a small box labeled “少收藏” holds scattered prompt papers. Use one orange path from the box to the stable workbench.

Chinese handwritten labels:
搭系统 / 协作 / 技能 / 约束 / 少收藏 / 稳定协作
```

## Repair Prompts

### Make The IP Stronger

```text
Regenerate with the same core meaning, but make 小蓝格 more recognizable: sky-blue rounded-square body, tiny black dot eyes, thin line arms and legs, and clearly visible simple deep-blue thin-line over-ear headphones. Keep the headphones small and adult, not a microphone headset or cute accessory. Put 小蓝格 inside the core action.
```

### Reduce PPT Feeling

```text
Regenerate with fewer formal nodes and fewer arrows. Replace the slide-like layout with one physical low-tech metaphor: drawer, shelf, checkpoint, workbench, doorway, or messy note pile. No top title, no numbered grid, no UI panel. Keep short handwritten labels and at least 35% blank white space.
```

### Remove A Bad Title

```text
Edit the provided image. Remove only the handwritten title "{title}" and its nearby underline or mark. Fill that area with the same clean white background. Preserve 小蓝格, headphones, labels, orange paths, red marks, line style, composition, aspect ratio, and image quality. Do not add new text or objects.
```
