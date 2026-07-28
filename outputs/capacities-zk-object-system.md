# Capacities Zettelkasten 对象体系设计方案

> 基于 Bob Doto《A System for Writing》方法论，为 Capacities Pro 用户定制的完整对象体系

---

## 一、你的现状

你已创建 3 个对象类型，覆盖了 Doto 方法论的 Phase 1（捕捉）：

| 对象类型 | Doto 概念 | 状态 |
|----------|-----------|------|
| Zettels | 主笔记 (Main Notes) | 已创建 |
| Fleeting Notes | 临时笔记 (Fleeting Notes) | 已创建 |
| Reference Notes | 参考笔记 (Reference Notes) | 已创建 |

还需补充 Phase 2（连接）和 Phase 3（写作）的对象类型。

---

## 二、建议新建的对象类型

### 4. Hub Notes（枢纽笔记）

**为什么需要**：当某个主题的 Zettels 积累到一定数量时，你需要一个"入口点"来定位不同思维链的起点。Hub Note 不等于目录——它是指向不同思考方向的"高速公路交汇处"。

**自定义属性**：

| 属性名 | 类型 | 说明 |
|--------|------|------|
| area | Text | 主题领域（如"认知偏差"、"写作方法论"） |
| created_date | Date | 创建日期 |

**正文结构**：
```
## {主题领域} 的思维链入口

### 方向一：{关键词}
→ @{第一条 Zettel 的标题}

### 方向二：{关键词}
→ @{第一条 Zettel 的标题}

### 方向三：{关键词}
→ @{第一条 Zettel 的标题}
```

**创建时机**：当你发现某个主题已经有 8-10 条以上 Zettels，且你在找笔记时开始觉得"有点散"的时候。

---

### 5. Structure Notes（结构笔记）

**为什么需要**：当你准备围绕某个主题写作时，需要把相关的 Zettels 按论点逻辑排列，加上过渡段落。Structure Note 就是文章/书籍大纲的雏形。

**自定义属性**：

| 属性名 | 类型 | 说明 |
|--------|------|------|
| status | Select | draft / outline / ready / published |
| project_link | Link to Object | 链接到 Writing Project（可选） |
| target_format | Select | tweet / blog / article / book |

**正文结构**：
```
## 导论
@{Zettel} — 过渡说明为什么这个论点重要

## 论点一：{关键词}
@{Zettel} — 这条笔记提供了核心论据
@{Zettel} — 这条笔记是对立的视角，需要回应

## 论点二：{关键词}
@{Zettel} — 承上启下
@{Zettel} — 核心论证

## 结论
@{Zettel} — 总结性想法

## 需要补充的笔记
- [ ] 还缺一条关于 XX 的 Zettel
```

**创建时机**：当你决定围绕某主题写一篇内容（推文/博客/文章），或者你发现多条 Zettels 自然形成了一个论证链。

---

### 6. CLOG（创意日志）

**为什么需要**：Doto 方法论的独特之处是把写作管理整合进了 ZK 系统。CLOG 记录每次写作会话的进展，核心价值是"下次从哪里继续"——让你不用每次都花时间回忆上次写到哪了。

**自定义属性**：

| 属性名 | 类型 | 说明 |
|--------|------|------|
| project_link | Link to Object | 链接到 Writing Project |
| session_date | Date | 本次写作日期 |

**正文结构**：
```
## 本次完成
- {完成了什么}

## 待处理
- {下一步需要做什么}

## 下次开始建议
- {从哪里继续}
```

**使用频率**：每次写作会话结束时写一条。

---

### 7. Writing Projects（写作项目）— 可选

**为什么需要**：如果你有明确的写作目标（如"写一系列关于 ZK 的博客"），一个项目对象可以把结构笔记、CLOG、发布草稿统一管理。

**自定义属性**：

| 属性名 | 类型 | 说明 |
|--------|------|------|
| status | Select | idea / planning / drafting / editing / published |
| deadline | Date | 截止日期（可选） |
| type | Select | blog-series / article / book / twitter-thread |

**正文结构**：
```
## 项目概述
{目标描述}

## 关联结构笔记
@{Structure Note}

## CLOG 时间线
@{CLOG 1}
@{CLOG 2}

## 发布草稿
@{Publish Draft 1}
```

**建议**：如果你暂时不需要正式项目管理，可以先不建。用 CLOG + 标签就够了。

---

## 三、你现有 3 个对象的属性优化建议

### Zettels（主笔记）— 需要补充属性

这是整个系统的核心。目前需要添加以下自定义属性来映射 Doto 的"主笔记六要素"：

| 属性名 | 属性类型 | 对应六要素 | 说明 | 示例值 |
|--------|----------|-----------|------|--------|
| id | Text | 6. 唯一ID | Folgezettel 字母数字标识 | `3.2a` |
| source_type | Select | 4. 来源 | 想法来源类型 | original / book / article / conversation |
| source_ref | Text | 4. 引用 | 具体引用信息 | `Doto, B. (2024). p.45` |
| used_in | Link to Object | 5. 使用记录 | 链接到使用了这条笔记的发布草稿 | `@发布草稿` |

其余两个要素的映射：
- **1. 标题** → 对象标题本身就是
- **2. 单一想法** → 正文 body 本身就是
- **3. 链接** → 用 `@` 在正文中链接到其他 Zettels（Capacities 原生双向链接）

**Zettel 正文建议结构**：
```markdown
{用自己的话完整表述的单一想法。一条笔记只包含一个想法。}

## 连接
- @{Zettel} — {连接原因：为什么这条和那条相关}
- @{Zettel} — {连接原因}

## 开放问题
- {待探索的方向}
```

> **关键提醒**：每个链接必须带上下文说明，禁止"链接堆砌"。这是 Doto 方法论的核心要求。

---

### Fleeting Notes（临时笔记）— 属性建议

| 属性名 | 属性类型 | 说明 |
|--------|----------|------|
| source | Select | 灵感 / 阅读 / 对话 / 观察 / 其他 |
| created_date | Date | 创建日期 |

**标签使用**：每条 Fleeting Note 都加 `#inbox` 标签，处理完后改为 `#processed` 或删除。

**正文**：不需要结构，越简单越好。一两句话捕捉想法即可。

---

### Reference Notes（参考笔记）— 属性建议

| 属性名 | 属性类型 | 说明 |
|--------|----------|------|
| source_type | Select | book / article / podcast / video / lecture |
| author | Text | 作者 |
| url_isbn | Text | URL 或 ISBN |
| reading_date | Date | 阅读日期 |
| status | Select | reading / completed |

**正文建议结构**：
```markdown
## 关键段落

### p.{页码} — {关键词}
> {原文引用}

**批注**: {为什么这段重要，和什么想法相关}

### p.{页码} — {关键词}
> {原文引用}

**批注**: {个人思考}

## 转化为主笔记
- [ ] @{Zettel} — 从 p.45 的想法转化
- [ ] 待转化：p.67 关于 XX 的段落
```

---

## 四、Daily Note 的角色

Capacities 内置的 Daily Note 在这个体系中有双重角色：

1. **收件箱（Inbox）**：快速捕捉 Fleeting Note 和想法，直接写在 Daily Note 里
2. **每日日记**：Doto 方法论中的 Daily Journal，记录当天做了什么

**Daily Note 模板建议**：
```markdown
## 收件箱
- {快速想法，后续处理为 Fleeting Note 或 Zettel}

## 今日活动
- {做了什么}

## 明日建议
- {下次从哪里继续}
```

---

## 五、MCP 集成能力（AI 教练能做什么）

Capacities 的 MCP 服务器提供以下工具，AI 教练可以利用它们：

| MCP 工具 | 能力 | ZK 场景 |
|----------|------|---------|
| `createObjectViaMd` | 创建任意类型对象 | 创建 Zettel/Fleeting/Reference/Structure Note |
| `appendMdToObject` | 向已有对象追加内容 | 给 Zettel 添加新连接 |
| `getObjectContent` | 读取对象完整内容 | 读取已有笔记，建议连接 |
| `search` | 语义搜索 | 搜索相关主题的笔记 |
| `updateObjectViaMD` | 更新对象属性 | 更新 Zettel 的 used_in 字段 |
| `saveToDailyNote` | 写入今日 Daily Note | 快速捕捉临时想法 |
| `createPage` | 创建简单页面 | 创建草稿 |
| `createTask` | 创建任务 | 创建写作待办 |
| `getObjectTypeShape` | 查看对象类型属性结构 | 了解当前 Zettel 有哪些属性 |
| `createObjectLink` | 生成对象 URL | 生成笔记链接 |

**已知限制**：
- 不支持批量获取某类型的所有对象（如"列出所有 Zettels"）
- 最佳使用场景是单对象操作
- AI 需要用 `search` 来发现相关笔记，而非遍历

---

## 六、完整工作流示例

```
场景：你在读《思考，快与慢》，有个关于锚定效应的想法

Step 1 → Daily Note 收件箱
  AI: saveToDailyNote("锚定效应：人类判断会被最先看到的信息锚定")
  
Step 2 → 创建 Reference Note
  AI: createObjectViaMd("Reference Notes", {
    source_type: "book",
    author: "Daniel Kahneman",
    url_isbn: "9780374275631"
  })
  正文: 页码引用 + 批注

Step 3 → 转化为 Zettel
  AI: createObjectViaMd("Zettels", {
    id: "3.2a",  ← 如果与"认知偏差"主题(假设是3)相关
    source_type: "book",
    source_ref: "Kahneman (2011). p.119"
  })
  正文: 用自己的话重写 + @链接到相关 Zettel

Step 4 → 发现连接
  AI: search("决策偏差") → 找到已有的 Zettel
  AI: appendMdToObject → 添加带上下文的连接

Step 5 → 积累后创建 Structure Note
  AI: createObjectViaMd("Structure Notes", {
    status: "outline",
    target_format: "blog"
  })
  正文: @Zettels 按论点排列

Step 6 → 写作 + 记录使用
  AI: updateObjectViaMD → 更新每条 Zettel 的 used_in
  AI: createObjectViaMd("CLOG") → 记录本次写作进度
```

---

## 七、建议的执行顺序

| 步骤 | 操作 | 优先级 |
|------|------|--------|
| 1 | 给 Zettels 添加 4 个自定义属性 | **立即** |
| 2 | 给 Reference Notes 添加属性 | **立即** |
| 3 | 给 Fleeting Notes 添加属性 | **立即** |
| 4 | 设置 Daily Note 模板（收件箱+日记） | **立即** |
| 5 | 新建 Hub Notes 对象类型 | 笔记积累后 |
| 6 | 新建 Structure Notes 对象类型 | 准备写作时 |
| 7 | 新建 CLOG 对象类型 | 开始写作项目时 |
| 8 | 新建 Writing Projects 对象类型 | 有明确写作目标时 |

步骤 1-4 是基础设置，几分钟就能完成。步骤 5-8 按需添加，不需要一开始就全建。

---

## 八、关于 Folgezettel ID 系统

Doto 的字母数字 ID（如 `1.2a`, `3.4b1`）是一个**可选但强大**的导航系统。在 Capacities 中：

- **ID 存储在 Zettel 的 `id` 属性中**
- **ID 不是必须的**——如果你觉得编号繁琐，可以仅用 `@` 双向链接 + Structure Notes
- **ID 的核心价值**：当你在 Structure Note 中排列论点时，可以用 ID 而非标题来引用，更精确

如果你决定使用 ID 系统，skill 套件中的 `zk-folgezettel` 模块会帮你自动分配。

---

*本方案基于 Bob Doto《A System for Writing》(2024) 方法论 + Capacities MCP 官方文档 + Capacities PKM 指南综合设计。*
