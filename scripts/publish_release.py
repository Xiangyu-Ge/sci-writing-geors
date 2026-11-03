"""为当前 VERSION 创建 GitHub Release，并上传 dist/ 下的全部 zip。

用法（在仓库根目录执行）：
    export GH_TOKEN=<你的 GitHub token>
    python scripts/publish_release.py --dry-run      # 先看要做什么，不联网
    python scripts/publish_release.py                # 正式发布
    python scripts/publish_release.py --no-latest    # 补发历史版本，不抢 Latest 徽章

行为：
  * 版本号取自 VERSION，tag 为 v<version>
  * Release 正文自动从 CHANGELOG.md 中截取对应小节的正文
  * Release 已存在时复用，已上传的同名附件会跳过（可重复执行）
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def repo_slug():
    """从 git remote 推断 owner/repo。"""
    import subprocess
    url = subprocess.check_output(
        ["git", "-C", ROOT, "remote", "get-url", "origin"], text=True
    ).strip()
    m = re.search(r"github\.com[:/]+([^/]+)/([^/]+?)(?:\.git)?$", url)
    if not m:
        raise SystemExit(f"无法从 remote 推断仓库：{url}")
    return m.group(1), m.group(2)


def changelog_section(version):
    with open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8") as fh:
        text = fh.read()
    m = re.search(
        rf"^## \[{re.escape(version)}\].*?$(.*?)(?=^## \[|\Z)", text, re.S | re.M
    )
    if not m:
        raise SystemExit(f"CHANGELOG.md 里找不到 [{version}] 小节")
    return m.group(1).strip()


def api(token, method, url, payload=None, content_type="application/json"):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "sci-writing-geors-release")
    if data is not None:
        req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode() or "{}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只打印计划，不联网")
    ap.add_argument("--tag", help="覆盖 tag，默认 v<VERSION>")
    ap.add_argument("--name", help="Release 标题，默认 v<VERSION>")
    ap.add_argument("--notes", help="用指定 Markdown 文件作为正文，默认取 CHANGELOG")
    ap.add_argument("--no-latest", action="store_true", help="不设置 Latest 徽章")
    args = ap.parse_args()

    with open(os.path.join(ROOT, "VERSION"), encoding="utf-8") as fh:
        version = fh.read().strip()
    tag = args.tag or f"v{version}"
    name = args.name or tag

    dist = os.path.join(ROOT, "dist")
    assets = sorted(
        os.path.join(dist, f) for f in os.listdir(dist) if f.endswith(".zip")
    )
    if not assets:
        raise SystemExit(f"dist/ 下没有 zip，先跑 scripts/build_zips.py")

    if args.notes:
        with open(args.notes, encoding="utf-8") as fh:
            body = fh.read()
    else:
        body = changelog_section(version)

    owner, repo = repo_slug()
    print(f"仓库   : {owner}/{repo}")
    print(f"tag    : {tag}")
    print(f"标题   : {name}")
    print(f"Latest : {'否' if args.no_latest else '是'}")
    print(f"正文   : {len(body)} 字符")
    print("附件:")
    for a in assets:
        print(f"  - {os.path.basename(a):40s} {os.path.getsize(a):8d} B")

    if args.dry_run:
        print("\n[dry-run] 未联网，未做任何修改")
        return 0

    token = os.environ.get("GH_TOKEN")
    if not token:
        raise SystemExit("缺少环境变量 GH_TOKEN")

    base = f"https://api.github.com/repos/{owner}/{repo}"
    status, out = api(token, "POST", f"{base}/releases", {
        "tag_name": tag,
        "name": name,
        "body": body,
        "draft": False,
        "prerelease": False,
        "make_latest": "false" if args.no_latest else "true",
    })
    if status not in (200, 201):
        if status == 422:
            status, out = api(token, "GET", f"{base}/releases/tags/{tag}")
        if status not in (200, 201):
            print(f"创建 Release 失败：{status}\n{json.dumps(out, ensure_ascii=False)[:600]}")
            return 1

    rel_id = out["id"]
    print(f"\nRelease: {out['html_url']}")

    existing = {a["name"] for a in out.get("assets", [])}
    for path in assets:
        fname = os.path.basename(path)
        if fname in existing:
            print(f"  跳过（已存在）: {fname}")
            continue
        with open(path, "rb") as fh:
            data = fh.read()
        status, res = api(
            token, "POST",
            f"https://uploads.github.com/repos/{owner}/{repo}/releases/{rel_id}"
            f"/assets?name={fname}",
            data, content_type="application/zip",
        )
        if status in (200, 201):
            print(f"  已上传: {fname} ({res.get('size')} B)")
        else:
            print(f"  上传失败 {fname}: {status} {json.dumps(res, ensure_ascii=False)[:300]}")
            return 1

    print("完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
