# Family Travel Skills｜家庭旅行 Skill 套件

面向「老人 + 低龄宝宝」家庭的旅行规划与穿搭 Agent Skills。  
可直接用于 Claude Code / Cursor / Codex 等支持 Agent Skill 的环境。

## Skills

| Skill | 目录 | 做什么 |
|-------|------|--------|
| **Family Slow Travel Planner**｜家庭松弛旅行策划 | [`family-slow-travel-planner/`](./family-slow-travel-planner/) | 交通骨架、酒店筛选、午睡锚点、每日主题、景点取舍、餐饮、Plan B、A4 攻略、行李清单、微信分享长图 |
| **Travel Capsule Wardrobe**｜旅行胶囊穿搭 | [`travel-capsule-wardrobe/`](./travel-capsule-wardrobe/) | 少量高复用衣物 → 多套 Look；场景/天气适配；打包清单与每日穿搭表 |

两个 Skill 可独立使用，也可联动：家庭行程定稿后，在行李阶段调用穿搭 Skill 生成衣物与每日 Look。

每个 Skill 目录包含：

- `SKILL.md` — 执行规范（怎么规划、怎么输出）
- `BACKGROUND.md` — 长期偏好与项目背景（为什么这样定）

## 快速安装

### Cursor

复制到个人 skills 目录：

```bash
git clone https://github.com/iriswong31/family-travel-skills.git
cp -R family-travel-skills/family-slow-travel-planner ~/.cursor/skills/
cp -R family-travel-skills/travel-capsule-wardrobe ~/.cursor/skills/
```

### Claude Code / skills.sh

```bash
npx skills add iriswong31/family-travel-skills
```

（若 CLI 按子目录识别失败，请手动把上述两个目录拷到 `~/.claude/skills/`。）

## 典型触发语

- 「用家庭松弛旅行 Skill 帮我规划 ____」
- 「帮我做这趟旅行的胶囊衣橱」
- 「这次去 XX，老人宝宝怎么安排、穿什么」

## 设计原则（摘要）

1. **节奏松弛优先**：低龄宝宝午睡是硬约束；不追求景点数量。  
2. **酒店服务行程**：午休回房睡床，而不是推车将就。  
3. **穿搭服务行程**：先理解每天去哪、天气与活动，再决定带什么衣服。  
4. **Skill / Background 分离**：方法可复用；家庭偏好可单独维护。

## 版本

当前内容版本：**v1.1**（2026-09-23）

## License

[MIT](./LICENSE)

欢迎 fork、改写成你自己家庭的偏好，或提交改进 PR。
