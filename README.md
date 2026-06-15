# Anti-AI Style Factory

原创反 AI 味设计风格库的 harness pipeline。从种子目录读取设计运动 DNA，通过 LLM 生成 DESIGN.md + reference HTML，8-dim 评分器验证（必须 ≤4/16），不合格自动迭代重生成。

## 架构

```
catalog/seeds.json       ← 风格种子定义
config/settings.json     ← LLM 配置、评分阈值
src/
  generator/             ← LLM 调用层（生成 DESIGN.md + HTML）
  scorer/                ← 8-dim 评分器 + LLM judge
  pipeline/              ← 主 harness 循环（generate → score → accept/reject → iterate）
styles/{seed-id}/        ← 输出：每个风格的完整产出物
output/                  ← 运行报告、统计
logs/                    ← 运行日志
```

## 快速开始

```bash
pip install -r requirements.txt
python -m src.pipeline.run --seed bauhaus-1919
python -m src.pipeline.run --all          # 处理所有种子
python -m src.pipeline.run --continuous   # 持续模式：处理新种子 + 重试失败的
```

## 评分门控

所有生成的 reference.html 必须：
- 8-dim rubric ≤ 4/16
- 不含 Inter/Roboto/Lato/Open Sans/Poppins 字体
- 不含紫蓝渐变 (#667eea, #764ba2)
- 不含 glassmorphism (backdrop-filter: blur)
- 不含 emoji 作为图标
