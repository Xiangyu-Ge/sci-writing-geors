# 发布脚本

发新版时的三步，都在仓库根目录执行。

```bash
# 1. 改完之后先自检结构和链接
python scripts/validate.py

# 2. 重新打包 dist/（版本号取自 VERSION）
python scripts/build_zips.py

# 3. 发布到 GitHub（需要 GH_TOKEN）
python scripts/publish_release.py --dry-run   # 先确认计划
python scripts/publish_release.py             # 正式发布
```

## 发版流程

1. 修改 `skills/` 下的内容
2. 更新 `VERSION`（例如 `2.1.0`）
3. 在 `CHANGELOG.md` 顶部加一节 `## [2.1.0] · YYYY-MM-DD`
4. 按上面三步执行

`publish_release.py` 会读 `VERSION` 得到 tag `v2.1.0`，并从 `CHANGELOG.md` 里自动截取
`[2.1.0]` 那一节作为 Release 正文，无需另写。

## 参数

| 参数 | 说明 |
|---|---|
| `--dry-run` | 只打印计划，不联网、不改动任何东西 |
| `--tag` | 覆盖 tag，默认 `v<VERSION>` |
| `--name` | Release 标题，默认与 tag 相同 |
| `--notes FILE` | 用指定 Markdown 作为正文，不用 CHANGELOG |
| `--no-latest` | 不设置 Latest 徽章（补发历史版本时用） |

## 注意

- 脚本可以重复执行：Release 已存在时会复用，已上传的同名附件会跳过。
- 补发历史版本时务必加 `--no-latest`，否则会把当前版本从 Latest 挤下去。
- `GH_TOKEN` 只从环境变量读，不要写进脚本或提交到仓库。
- `build_zips.py` 每次重新打包都会更新 zip 内的时间戳，因此产物字节会有变化，属正常现象。
