"""校验 skills/ 的结构与内部链接。

用法（在仓库根目录执行）：
    python scripts/validate.py

检查项：
  1. 每个技能目录都有 SKILL.md（且没有小写的 skill.md 残留）
  2. YAML frontmatter 里的 name 与目录名一致、description 非空且不超过 1024 字符
  3. SKILL.md 中提到的 *.md 文件确实存在（跨技能引用会标注出来）
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

# 不随仓库分发、由用户自行生成的文件
EXPECTED_ABSENT = {
    "writing_style.md": "用户按模板自行生成的风格档案",
}


def main():
    skill_dirs = sorted(
        d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d))
    )

    shipped = {}
    for d in skill_dirs:
        for dirpath, _, files in os.walk(os.path.join(SKILLS, d)):
            for f in files:
                if f.endswith(".md"):
                    shipped.setdefault(f, []).append(d)

    ok = True
    for name in skill_dirs:
        sd = os.path.join(SKILLS, name)
        if "skill.md" in os.listdir(sd):
            print(f"[FAIL] {name}: 存在小写 skill.md，会和 SKILL.md 冲突")
            ok = False

        skill_md = os.path.join(sd, "SKILL.md")
        if not os.path.isfile(skill_md):
            print(f"[FAIL] {name}: 缺少 SKILL.md")
            ok = False
            continue

        with open(skill_md, encoding="utf-8") as fh:
            text = fh.read()

        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            print(f"[FAIL] {name}: 缺少 YAML frontmatter")
            ok = False
            continue

        fm = m.group(1)
        nm = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
        ds = re.search(r"^description:\s*(.+)$", fm, re.M | re.S)
        if not nm or nm.group(1) != name:
            print(f"[FAIL] {name}: frontmatter name 与目录名不一致 "
                  f"({nm.group(1) if nm else '缺失'})")
            ok = False

        desc_len = len(ds.group(1).strip()) if ds else 0
        if not desc_len:
            print(f"[FAIL] {name}: description 为空")
            ok = False
        elif desc_len > 1024:
            print(f"[WARN] {name}: description {desc_len} 字符，超过 1024")

        refs = set(re.findall(r"([\w\-]+\.md)", text))
        local = os.path.join(sd, "references")
        cross, absent = [], []
        for r in sorted(refs):
            if os.path.isfile(os.path.join(sd, r)) or (
                os.path.isdir(local) and os.path.isfile(os.path.join(local, r))
            ):
                continue
            if r in EXPECTED_ABSENT:
                absent.append((r, "by design"))
            elif r in shipped:
                cross.append((r, ",".join(shipped[r])))
            else:
                absent.append((r, "MISSING"))
                ok = False

        nrefs = len(os.listdir(local)) if os.path.isdir(local) else 0
        print(f"[ok] {name:24s} desc={desc_len:4d}  refs={nrefs:2d}  links={len(refs):2d}")
        for r, where in cross:
            print(f"       跨技能引用: {r} -> {where}")
        for r, why in absent:
            print(f"       {'按设计缺失' if why == 'by design' else '缺失'}: {r}")

    print("\n全部通过" if ok else "\n存在失败项")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
