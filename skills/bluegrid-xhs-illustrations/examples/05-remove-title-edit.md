# Example 05: 去标题修图

## User Input

```text
这张图左上角多了“内容工作流图”几个字，帮我去掉，其它别动。
```

## Expected Behavior

这是图像编辑任务。保留画面、比例、小蓝格、耳机、标注和线条，只去掉指定标题。

## Edit Prompt

```text
Edit the provided image. Remove only the handwritten text “内容工作流图” and its nearby underline or mark from the top-left corner. Fill that area with the same clean pure white background, matching the surrounding blank space.

Preserve everything else exactly: 小蓝格, the thin-line deep-blue headphones, all other handwritten labels, orange path lines, red correction marks, black line-art style, composition, aspect ratio, and image quality.

Do not add new text, objects, shadows, texture, or background elements.
```

## Pass Criteria

- The specified title is gone.
- No new title or replacement text appears.
- No visible patch, smudge, texture, or background mismatch.
- 小蓝格 and all non-target labels are unchanged.

