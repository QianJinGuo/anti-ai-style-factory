# Anti-AI Style Factory

原创反 AI 味设计风格库的 harness pipeline。从种子目录读取设计运动 DNA，通过 LLM 生成 DESIGN.md + reference HTML，8-dim 评分器验证（必须 ≤4/16），不合格自动迭代重生成。

## 架构

```
catalog/SEEDS.md         ← 风格种子定义（55+ 设计运动）
config/pipeline.yaml     ← LLM 配置、评分阈值
src/
  generator/             ← LLM 调用层（生成 DESIGN.md + HTML）
  scorer/                ← 8-dim 评分器
  pipeline/              ← 主 harness 循环（generate → score → accept/reject → iterate）
styles/{seed-id}/        ← 输出：每个风格的完整产出物
state/                   ← 批量运行状态
demos/                   ← 演示 HTML
logs/                    ← 运行日志
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
  provider: xfyun         # xfyun | openai
  model: "xopqwen36v35b"
  providers:
    xfyun:
      base_url: "https://maas-api.cn-huabei-1.xf-yun.com/v2"
      api_key_env: "CHATXUNFEI"
    openai:
      base_url: "https://api.openai.com/v1"
      api_key_env: "OPENAI_API_KEY"
```

API key 解析顺序：环境变量 → `~/.zshenv` → `~/.hermes/config.yaml`。

### 生成风格

```bash
anti-ai-factory --seed bauhaus       # 生成单个种子
anti-ai-factory --tier 1             # 生成整个 Tier
anti-ai-factory --batch 5            # 处理下 5 个 pending 种子
anti-ai-factory --workers 5          # 5 路并发
anti-ai-factory --status             # 查看生成状态
anti-ai-factory --dry-run            # 只看不生成
# 等价于：python -m src.pipeline.run ...
```

### 独立使用评分器

评分器是纯 Python、零依赖，可脱离 pipeline 单独使用：

```bash
anti-ai-score styles/bauhaus/reference.html       # 输出 JSON 评分
anti-ai-score a.html b.html --threshold 6         # 自定义通过阈值
cat page.html | anti-ai-score -                   # 从 stdin 读
# 等价于：python -m src.scorer.eight_dim styles/bauhaus/reference.html
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
