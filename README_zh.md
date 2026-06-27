# Anti-AI Style Factory

原创反 AI 味设计风格库的 harness pipeline。从种子目录读取设计运动 DNA，通过 LLM 生成 DESIGN.md + reference HTML，8-dim 评分器验证（必须 ≤4/16），不合格自动迭代重生成。

[English](README.md) | 中文

## 架构

```
catalog/SEEDS.md         ← 风格种子定义（55+ 设计运动，15000+ 组合）
config/pipeline.yaml     ← LLM 配置、评分阈值
src/
  generator/             ← LLM 调用层（生成 DESIGN.md + HTML）
  scorer/                ← 8-dim 评分器（纯 Python，零依赖）
  pipeline/              ← 主 harness 循环（generate → score → accept/reject → iterate）
sample_styles/           ← 10 个精选示例输出
scripts/                 ← Gallery 构建器、种子生成器、修复工具
gallery/                 ← Web 预览 Gallery + 评分器 UI
demos/                   ← 独立演示 HTML 文件
```

## 快速开始

### 安装

```bash
pip install -e .          # 安装为可编辑包，暴露 anti-ai-score / anti-ai-factory CLI
# 或仅装依赖：pip install -r requirements.txt
```

### 配置 LLM Provider

`config/pipeline.yaml` 支持多 provider，切换只需改 `llm.provider` 一行：

```yaml
llm:
  provider: openai         # openai | xfyun | 任何 OpenAI 兼容 API
  model: "gpt-4o"
  providers:
    openai:
      base_url: "https://api.openai.com/v1"
      api_key_env: "OPENAI_API_KEY"
    xfyun:
      base_url: "https://maas-api.cn-huabei-1.xf-yun.com/v2"
      api_key_env: "XFYUN_API_KEY"
```

API key 解析顺序：环境变量 → `.env` 文件。

### 生成风格

```bash
anti-ai-factory --seed bauhaus       # 生成单个种子
anti-ai-factory --tier 1             # 生成整个 Tier
anti-ai-factory --batch 5            # 处理下 5 个 pending 种子
anti-ai-factory --workers 5          # 5 路并发
anti-ai-factory --status             # 查看生成状态
anti-ai-factory --dry-run            # 只看不生成
```

### 独立使用评分器

评分器是纯 Python、零依赖，可脱离 pipeline 单独使用：

```bash
anti-ai-score styles/bauhaus/reference.html       # 输出 JSON 评分
anti-ai-score a.html b.html --threshold 6         # 自定义通过阈值
cat page.html | anti-ai-score -                   # 从 stdin 读
```

也可作为库导入：

```python
from src.scorer import score_html
scores = score_html(html_string)
print(scores["total"])  # 0-16，越低越「反 AI 味」
```

## 评分门控

所有生成的 reference.html 必须：
- 8-dim rubric ≤ 4/16
- 不含 Inter/Roboto/Lato/Open Sans/Poppins 字体
- 不含紫蓝渐变 (#667eea, #764ba2)
- 不含 glassmorphism (backdrop-filter: blur)
- 不含 emoji 作为图标

## 设计运动种子

`catalog/SEEDS.md` 包含 15,000+ 种子定义，按层级组织：

| 层级 | 描述 | 示例 |
|------|------|------|
| Tier 1 | 核心运动 | Bauhaus, Swiss International, Brutalist Web, Art Deco |
| Tier 2 | 地域变体 | 包豪斯·柏林, 装饰艺术·上海, 浮世绘·江户 |
| Tier 3 | 媒介适配 | 海报, 书籍封面, 仪表盘, 落地页 |
| Tier 4 | 色盘变体 | 暖色, 冷色, 大地色, 霓虹, 单色 |
| Tier 5 | 材质纹理 | 颗粒, 纸张, 画布, 石材, 金属 |

## 许可证

[MIT](LICENSE) — 在 CI 中使用评分器，fork 生成器，自由构建。
