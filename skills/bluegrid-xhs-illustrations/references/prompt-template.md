# 生图提示词模板

每张图单独生成。根据用户内容替换变量，不要把多张图拼在一起。

## 小红书 4:5 配图模板

```text
Generate one standalone 4:5 vertical Xiaohongshu Chinese note illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Fresh sky-blue accent blocks. Sparse orange path marks, red correction marks, and deep-blue handwritten notes only when needed. Clean creator-tool sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
小蓝格, a small sky-blue rounded-square character with tiny black dot eyes, thin line arms and legs, blank serious expression, slightly uneven hand-drawn body shape. 小蓝格 wears a simple thin-line deep-blue over-ear headphone as its fixed signature accessory. The headphone must be visible but minimal, with no microphone boom and no bulky details. 小蓝格 must perform the core conceptual action, not decorate the scene. Make 小蓝格 calm, useful, and slightly dry-humored, not cute.

Theme:
{配图主题}

Structure type:
{小红书首图 / 碎片收拢 / 前后对比 / 系统局部 / 方法分层 / 卡点纠偏 / 路径地图 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：小蓝格在哪里、戴着耳机正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for main line art and text. Sky blue for 小蓝格 and key content blocks. Deep blue for the headphone and secondary notes. Orange only for the main path or movement. Red only for warnings, corrections, or key results.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a big title at the top. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not make 小蓝格 a cute mascot or a commercial logo. Do not add any extra accessories besides the headphone unless explicitly requested. It should be clear, fresh, adult, minimal, and publishable on Xiaohongshu.
```

## 文章 16:9 正文图模板

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Use the same 小蓝格 IP and visual DNA as above, but compose for a wide article body image with more horizontal breathing room. Keep pure white background, minimalist hand-drawn black line art, sky-blue 小蓝格 with visible thin-line deep-blue headphones, sparse orange/red/deep-blue handwritten annotations, and lots of empty white space.

Theme:
{正文配图主题}

Core idea:
{核心意思}

Composition:
{具体画面}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4}

Constraints:
No top-left title, no formal workflow chart, no PPT style, no dense architecture, no realistic UI, no shadows, no texture, no gradients. 小蓝格 must perform the core action.
```

## 图像编辑提示

去掉标题或错字：

```text
Edit the provided image. Remove only the handwritten text "{要删除的文字}" and its nearby underline or mark. Fill that area with the same clean white background, matching the surrounding blank space. Preserve everything else exactly: 小蓝格, headphones, labels, paths, line style, composition, aspect ratio, and image quality. Do not add new text or objects.
```

增强 IP 识别度：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 小蓝格 more recognizable: a sky-blue rounded-square body, tiny black dot eyes, thin arms and legs, and a clearly visible simple deep-blue thin-line over-ear headphone. Keep the accessory minimal and adult. Do not make it cute or mascot-like.
```

降低 PPT 感：

```text
Regenerate with fewer nodes and fewer arrows. Replace the formal diagram with one low-tech object or physical action. Keep 小蓝格 doing the action, preserve lots of white space, and use only short handwritten Chinese labels.
```

