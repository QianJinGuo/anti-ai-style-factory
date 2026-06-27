#!/usr/bin/env python3
"""
Seed Generator — Produces 10000+ style seeds from design history.
==============================================================
Combines real movements × regions × media × eras to generate
legitimate design style variants. Every seed is grounded in
verifiable design history — no invention.
"""

import random
from pathlib import Path
from itertools import product

# ── Base movements (real, verified) ──
MOVEMENTS = [
    # id, name_zh, era, region, principle, anti_ai_signal
    ("bauhaus", "包豪斯", "1919-1933", "德国", "形式追随功能；原色+黑白；几何构成", "硬阴影, 0圆角, 无渐变, 几何网格"),
    ("swiss-intl", "瑞士国际主义", "1950-1970", "瑞士", "网格系统；无衬线体；数学化排版", "严格网格, 大量留白, 无衬线"),
    ("brutalist-web", "野蛮主义Web", "2016-now", "全球", "原始HTML；裸露结构；反装饰", "系统字体, 单色, 粗边框, 无圆角无阴影"),
    ("art-deco", "装饰艺术", "1925-1940", "法国/美国", "几何装饰；对称；金属质感", "衬线体, 金/黑, 扇形图案"),
    ("de-stijl", "风格派", "1917-1931", "荷兰", "垂直水平线；原色+黑白灰", "仅红黄蓝+黑白, 直角, 无曲线"),
    ("ukiyo-e", "浮世绘", "1600-1900", "日本", "平面色块；线条轮廓；留白", "木版色, 大片留白, 无透视"),
    ("memphis", "孟菲斯", "1981-1988", "意大利", "反功能主义；大胆撞色；几何图案", "圆点/锯齿, 粉+黄+青, 粗边框"),
    ("constructivist", "构成主义", "1913-1940", "俄国", "对角线构图；红黑白", "阶梯式排版, 粗重无衬线, 对角分割"),
    ("terminal", "终端", "1970s-now", "全球", "纯文本；单色CRT；命令行", "等宽字体, 绿底黑字, 无图形"),
    ("editorial", "编辑排版", "1945-1980", "美国/英国", "杂志级排版；衬线标题；栏式布局", "分栏, 嵌入图片, 细线分割"),
    ("art-nouveau", "新艺术运动", "1895-1910", "法国/比利时", "有机曲线；自然形态；手工艺", "卷曲线条, 淡金/橄榄绿, 植物纹样"),
    ("pop-art", "波普艺术", "1958-1970", "美国/英国", "大众文化；放大重复；高饱和", "粗黑线, Ben-Day圆点, 原色+荧光"),
    ("streamline", "流线型现代", "1930-1945", "美国", "速度感；水平线条；金属质感", "铬色/银, 水平流线, 船形轮廓"),
    ("blackletter", "哥特活字", "1450-1600", "德国", "Textura手工质感；密集排版", "羊皮纸底, 红色首字下沉"),
    ("japanese-minimal", "日式极简", "1990-now", "日本", "间(ま)的美学；白是色；触感", "大量负空间, 低对比, 微妙灰度"),
    ("cyberpunk", "赛博朋克", "1982-now", "全球", "高科技低生活；霓虹；故障", "霓虹洋红/青, 扫描线, 故障效果"),
    ("data-ink", "数据墨水比", "1983-now", "美国", "最大化数据墨水；最小化非数据墨水", "极细线条, 无网格线, sparkline"),
    ("dutch-golden", "荷兰黄金时代", "1600-1700", "荷兰", "光影大师；深色背景；静物感", "暗调暖色, 油画质感边框"),
    ("scandinavian", "北欧现代", "1950-now", "北欧", "民主设计；天然材料；功能美感", "白+浅木色, 柔和灰度, 极简线条"),
    ("mid-century", "中世纪现代", "1945-1970", "美国", "有机几何；温暖木色；开放布局", "芥末黄/橙/松绿, 有机曲线"),
    ("vaporwave", "蒸汽波", "2012-now", "全球", "怀旧消费主义；故障美学", "粉/青/紫大理石, 罗马雕像, 棋盘格"),
    ("grunge", "垃圾摇滚", "1990-1996", "美国", "反商业；脏纹理；不完美", "脏噪点纹理, 不对齐, 复印失真"),
    ("skeuomorphic", "拟物化", "2007-2013", "全球", "数字模仿物理；材质感；深度", "皮革/木纹质感, 内阴影, 缝线"),
    ("letterpress", "活版印刷", "1440-now", "全球", "凸印质感；墨迹不均；厚纸", "墨色不匀, 深压痕, 粗纸纹理"),
    ("zine-punk", "朋克志", "1976-now", "英国", "DIY；剪切粘贴；反权威", "剪切拼贴, 高对比复印, 错位"),
    ("chinese-stone", "碑帖", "200-now", "中国", "石刻质感；笔锋；碑文布局", "竖排, 朱砂红印, 宣纸底"),
    ("arabic-geo", "伊斯兰几何", "800-now", "中东/北非", "无限重复；对称；无具象", "几何纹样, 金/青/白, 重复图案"),
    ("african-wax", "非洲蜡染", "1846-now", "西非", "大胆色彩；重复图案；叙事性", "高饱和撞色, 蜡染纹理, 不规则边框"),
    ("neon-sign", "霓虹灯牌", "1920-now", "美国/东亚", "玻璃管光；手弯管；暗夜发光", "霓虹管发光, 暗底, 手写体曲线"),
    ("comic-book", "漫画书", "1938-now", "美国", "面板叙事；动作线；拟声词", "粗黑轮廓, Ben-Day点, 拟声词气泡"),
    ("newspaper", "报纸大报", "1700-now", "全球", "栏式排版；信息密度；铅字", "多栏, 细线分割, 小字号密集"),
    ("film-noir", "黑色电影", "1940-1960", "美国", "高对比明暗；斜射光", "高对比黑白, 斜射光纹理, 暗调"),
    ("wabi-sabi", "侘寂", "1500-now", "日本", "不完美之美；消逝；质朴", "不规则边缘, 暖灰/茶色, 留白"),
    ("persian-mini", "波斯细密画", "1300-1600", "伊朗", "精密细节；平面装饰；边框叙事", "青/金/红, 精密纹样边框, 平面无透视"),
    ("mexican-mural", "墨西哥壁画", "1920-1970", "墨西哥", "公共艺术；社会叙事；大尺幅", "粗笔触, 土地色+红, 壁画纹理"),
    ("ink-wash", "水墨", "600-now", "中国", "留白即画；墨分五色；气韵生动", "宣纸底, 墨色渐层, 大片留白"),
    ("op-art", "光效应艺术", "1960-1970", "英国/匈牙利", "视觉错觉；几何节奏", "严格黑白, 波纹/棋盘, 视觉振动"),
    ("biomorphic", "生物形态", "1930-1960", "全球", "有机曲线；自然形状；流动感", "圆角非均匀, 自然色系, 豆荚形态"),
    ("pixel-art", "像素艺术", "1977-1995", "全球", "像素精确；有限色板；锯齿美学", "8色板, 锯齿边缘, 无抗锯齿"),
    ("terrazzo", "水磨石", "1500-now", "意大利", "碎骨料美学；随机嵌入；抛光面", "碎片纹理嵌入, 柔和底色, 不规则斑点"),
    ("gothic-cath", "哥特教堂", "1140-1500", "欧洲", "尖拱向上；飞扶壁；彩色玫瑰窗", "尖拱轮廓, 深色+金, 玫瑰窗纹样"),
    ("baroque", "巴洛克", "1600-1750", "意大利/法国", "戏剧性；动态曲线；过度装饰", "金+深红, 卷草纹, 雕饰边框"),
    ("dada", "达达", "1916-1924", "瑞士/德国", "反理性；随机；现成品", "混合字体, 不规则拼贴, 倾斜排版"),
    ("art-brut", "原生艺术", "1945-now", "全球", "非专业；直觉创作；原始力量", "粗糙线条, 不均匀色块, 无构图法则"),
    ("space-age", "太空时代", "1957-1972", "全球", "太空竞赛；流线型；未来感", "银/白/橙, 舱体曲线, 星座图案"),
    ("graffiti", "涂鸦", "1970-now", "全球", "街头宣言；标签；荧光喷漆", "荧光色, 喷溅纹理, 重叠层次"),
    ("polaroid", "宝丽来", "1948-now", "全球", "即时显影；白框；褪色质感", "白框照片, 褪色暖调, 显影不匀"),
    ("technicolor", "彩色印片", "1935-1970", "美国", "超饱和三色；技术彩色", "超饱和红/绿/蓝, 胶片颗粒"),
    ("y2k", "千禧虫美学", "1996-2003", "全球", "数字乐观；银色未来；透明塑料", "银色/透明, 泡泡形态, 荧光色"),
    ("retrowave", "复古波", "2010-now", "全球", "80s怀旧；日落渐变；网格地平线", "洋红/青日落, 透视网格, 霓虹线"),
    ("wiener-wk", "维也纳工坊", "1903-1932", "奥地利", "几何装饰；金箔；总体艺术", "方形重复纹样, 金/黑/白"),
    ("vernacular", "招牌字体", "1900-1980", "全球", "手绘感；本地化；功能优先", "手写体, 高对比色, 不规则排版"),
    ("brutalist-arch", "野蛮主义建筑", "1950-1980", "全球", "生混凝土；巨型结构；反装饰", "灰色混凝土纹理, 巨型体块"),
    ("russian-avant", "俄国先锋派", "1910-1930", "俄国", "集体功能；摄影蒙太奇", "粗体俄文, 照片剪贴, 红对角线"),
]

# ── Regional variants ──
REGION_VARIANTS = {
    "bauhaus": [("berlin", "柏林"), ("chicago", "芝加哥"), ("tel-aviv", "特拉维夫"), ("moscow", "莫斯科")],
    "swiss-intl": [("zurich", "苏黎世"), ("basel", "巴塞尔"), ("ulm", "乌尔姆")],
    "art-deco": [("paris", "巴黎"), ("new-york", "纽约"), ("mumbai", "孟买"), ("shanghai", "上海"), ("havana", "哈瓦那")],
    "constructivist": [("moscow", "莫斯科"), ("petrograd", "彼得格勒")],
    "art-nouveau": [("paris", "巴黎"), ("brussels", "布鲁塞尔"), ("vienna", "维也纳"), ("barcelona", "巴塞罗那"), ("glasgow", "格拉斯哥")],
    "pop-art": [("new-york", "纽约"), ("london", "伦敦"), ("los-angeles", "洛杉矶")],
    "japanese-minimal": [("tokyo", "东京"), ("kyoto", "京都"), ("naoshima", "直岛")],
    "scandinavian": [("copenhagen", "哥本哈根"), ("stockholm", "斯德哥尔摩"), ("helsinki", "赫尔辛基"), ("oslo", "奥斯陆")],
    "mid-century": [("palm-springs", "棕榈泉"), ("los-angeles", "洛杉矶"), ("saarinen", "萨里宁")],
    "graffiti": [("nyc", "纽约"), ("london", "伦敦"), ("sao-paulo", "圣保罗"), ("berlin", "柏林"), ("melbourne", "墨尔本")],
    "neon-sign": [("vegas", "拉斯维加斯"), ("hong-kong", "香港"), ("tokyo-shinjuku", "东京新宿"), ("seoul", "首尔")],
    "comic-book": [("marvel", "漫威"), ("dc", "DC"), ("manga", "日漫"), ("bd-francaise", "法漫"), ("manhwa", "韩漫")],
    "baroque": [("rome", "罗马"), ("versailles", "凡尔赛"), ("dresden", "德累斯顿"), ("salzburg", "萨尔茨堡")],
    "arabic-geo": [("andalusia", "安达卢西亚"), ("istanbul", "伊斯坦布尔"), ("fez", "非斯"), ("isfahan", "伊斯法罕"), ("samarkand", "撒马尔罕")],
    "ink-wash": [("landscape", "山水"), ("figure", "人物"), ("bird-flower", "花鸟"), ("calligraphy", "书法"), ("bamboo", "墨竹")],
    "african-wax": [("ghana", "加纳"), ("nigeria", "尼日利亚"), ("ivory-coast", "科特迪瓦"), ("senegal", "塞内加尔")],
    "pixel-art": [("nes", "FC/NES"), ("gameboy", "Game Boy"), ("c64", "Commodore 64"), ("snes", "SFC/SNES"), ("dos", "DOS EGA")],
    "dada": [("zurich", "苏黎世"), ("berlin", "柏林"), ("paris", "巴黎"), ("new-york", "纽约"), ("cologne", "科隆")],
    "vaporwave": [("seapunk", "海朋克"), ("mallsoft", "商场轻音乐"), ("slimecore", "史莱姆核"), ("glitch", "故障风")],
    "ukiyoe": [("edo", "江户"), ("osaka", "大阪"), ("kyoto-u", "京都")],
}

# ── Medium applications ──
MEDIA = [
    ("poster", "海报", "大幅面视觉冲击；远距离可读；焦点单一"),
    ("book-cover", "书籍封面", "封面即广告；类型信号；触感吸引"),
    ("dashboard", "仪表盘", "信息密度；层级分明；数据优先"),
    ("landing", "着陆页", "第一印象；行动召唤；信任建立"),
    ("editorial-spread", "杂志跨页", "叙事流动；图文交织；翻页节奏"),
    ("packaging", "包装", "货架竞争；材料质感；品牌识别"),
    ("signage", "导视系统", "远距可读；方向直觉；环境融合"),
    ("exhibition", "展览设计", "空间叙事；动线引导；沉浸体验"),
    ("infographic", "信息图", "数据叙事；视觉比较；层级递进"),
    ("card-ui", "卡片界面", "模块化；可扫描；交互入口"),
    ("typography-specimen", "字体样张", "字族展示；排版极限；节奏实验"),
    ("wayfinding", "寻路系统", "极简可读；色彩编码；箭头逻辑"),
    ("album-art", "唱片封面", "音乐视觉化；文化信号；收藏价值"),
    ("stamp", "邮票", "微幅面；国族符号；齿孔边框"),
    ("banknote", "纸币", "防伪纹样；权威感；精密线条"),
    ("map", "地图", "空间抽象；图例系统；层级缩放"),
    ("recipe", "食谱", "步骤清晰；食材图示；温度时间"),
    ("ticket", "票券", "信息密度；撕裂线；编号系统"),
    ("catalog", "产品目录", "网格排列；规格表；价格层级"),
    ("annual-report", "年报", "数据叙事；图表系统；品牌一致性"),
]

# ── Color mood variations ──
MOODS = [
    ("warm", "暖调", "赭/琥珀/铜/焦糖"),
    ("cool", "冷调", "冰蓝/钢灰/薄荷/霜白"),
    ("earth", "大地", "陶土/橄榄/赭石/沙色"),
    ("neon", "霓虹", "荧光粉/电青/酸绿/亮橙"),
    ("monochrome", "单色", "纯黑白/灰度/仅一色点缀"),
    ("pastel", "柔和", "淡粉/雾蓝/薄荷/奶油"),
    ("jewel", "宝石", "祖母绿/宝石红/蓝宝石/琥珀"),
    ("muted", "浊色", "灰绿/脏粉/锈色/褪靛"),
]

# ── Texture overlays ──
TEXTURES = [
    ("grain", "颗粒", "胶片颗粒/噪点纹理"),
    ("paper", "纸张", "粗糙纸面/棉纸/水彩纸"),
    ("canvas", "画布", "油画布纹/亚麻质感"),
    ("stone", "石材", "大理石/花岗岩/砂岩纹理"),
    ("metal", "金属", "拉丝/氧化/铸造质感"),
    ("wood", "木材", "木纹/年轮/碳化表面"),
    ("fabric", "织物", "亚麻/丝绸/粗呢纹理"),
    ("concrete", "混凝土", "模板痕/裂缝/水渍"),
    ("wax", "蜡", "蜡染/封蜡/蜂巢纹理"),
    ("glass", "玻璃", "磨砂/水滴/折射纹理"),
]


def generate_seeds(target_count=10000):
    """Generate style seeds from combinatorial expansion of real design history."""
    seeds = []
    seen_ids = set()

    def add_seed(sid, name, era, region, principle, signal, tier):
        if sid in seen_ids:
            return
        seen_ids.add(sid)
        seeds.append({
            "id": sid,
            "name": name,
            "era": era,
            "region": region,
            "principle": principle,
            "anti_ai_signal": signal,
            "tier": tier,
        })

    # Layer 1: Base movements as-is (already have ~55, include for completeness)
    for mid, name, era, region, principle, signal in MOVEMENTS:
        add_seed(mid, name, era, region, principle, signal, 1)

    # Layer 2: Regional variants
    for mid, variants in REGION_VARIANTS.items():
        if isinstance(variants, tuple) and isinstance(variants[0], str):
            variants = [variants]
        base = next((m for m in MOVEMENTS if m[0] == mid), None)
        if not base:
            continue
        for rid, rname in variants:
            sid = f"{mid}-{rid}"
            add_seed(sid, f"{base[1]}·{rname}", base[2], rname,
                     f"{base[3]};{rname}地域变体", f"{base[4]},{rname}特征", 2)

    # Layer 3: Movement × Medium
    for mid, name, era, region, principle, signal in MOVEMENTS:
        for med_id, med_name, med_principle in MEDIA:
            sid = f"{mid}-{med_id}"
            add_seed(sid, f"{name}·{med_name}", era, region,
                     f"{principle};{med_principle}", f"{signal},{med_name}排版", 3)

    # Layer 4: Movement × Mood
    for mid, name, era, region, principle, signal in MOVEMENTS:
        for mood_id, mood_name, mood_colors in MOODS:
            sid = f"{mid}-{mood_id}"
            add_seed(sid, f"{name}·{mood_name}", era, region,
                     f"{principle};{mood_name}色盘", f"{signal},{mood_colors}", 4)

    # Layer 5: Movement × Texture
    for mid, name, era, region, principle, signal in MOVEMENTS:
        for tex_id, tex_name, tex_desc in TEXTURES:
            sid = f"{mid}-{tex_id}"
            add_seed(sid, f"{name}·{tex_name}", era, region,
                     f"{principle};{tex_desc}", f"{signal},{tex_desc}", 5)

    # Layer 6: Movement × Medium × Mood (full combinatorial)
    for mid, name, era, region, principle, signal in MOVEMENTS:
        for med_id, med_name, med_principle in MEDIA:
            for mood_id, mood_name, mood_colors in MOODS:
                sid = f"{mid}-{med_id}-{mood_id}"
                add_seed(sid, f"{name}·{med_name}·{mood_name}", era, region,
                         f"{principle};{med_principle};{mood_name}色盘",
                         f"{signal},{mood_colors},{med_name}排版", 6)

    # Layer 7: Movement × Texture × Mood (full combinatorial)
    for mid, name, era, region, principle, signal in MOVEMENTS:
        for tex_id, tex_name, tex_desc in TEXTURES:
            for mood_id, mood_name, mood_colors in MOODS:
                sid = f"{mid}-{tex_id}-{mood_id}"
                add_seed(sid, f"{name}·{tex_name}·{mood_name}", era, region,
                         f"{principle};{tex_desc};{mood_name}色盘",
                         f"{signal},{mood_colors},{tex_desc}", 7)

    return seeds


def write_seeds_md(seeds, path):
    """Write seeds to SEEDS.md in catalog format."""
    from collections import defaultdict
    by_tier = defaultdict(list)
    for s in seeds:
        by_tier[s["tier"]].append(s)

    tier_names = {
        1: "基础运动", 2: "地域变体", 3: "运动×媒介",
        4: "运动×色盘", 5: "运动×材质", 6: "运动×媒介×色盘",
        7: "运动×媒介×材质",
    }

    lines = [
        "# Style Seed Catalog — 10000+ Expansion",
        "",
        "设计风格种子。每个种子来自真实设计运动的组合扩展。",
        "不凭空发明——全部来自设计史可查的运动、地域、媒介、色盘、材质的合法组合。",
        "",
    ]

    for tier in sorted(by_tier.keys()):
        tier_seeds = by_tier[tier]
        lines.append(f"## Tier {tier}: {tier_names.get(tier, '扩展')}")
        lines.append("")
        lines.append("| ID | 名称 | 时代 | 地区 | 核心原则 | 反 AI 信号 |")
        lines.append("|----|------|------|------|----------|-----------|")
        for s in tier_seeds:
            lines.append(
                f"| `{s['id']}` | {s['name']} | {s['era']} | {s['region']} "
                f"| {s['principle']} | {s['anti_ai_signal']} |"
            )
        lines.append("")

    lines.append(f"## 统计")
    lines.append(f"")
    lines.append(f"Total seeds: {len(seeds)}")

    Path(path).write_text("\n".join(lines), encoding="utf-8")
    return len(seeds)


if __name__ == "__main__":
    seeds = generate_seeds(10000)
    count = write_seeds_md(seeds, "/Users/jinguo/projects/anti-ai-style-factory/catalog/SEEDS.md")
    print(f"Generated {count} seeds")
