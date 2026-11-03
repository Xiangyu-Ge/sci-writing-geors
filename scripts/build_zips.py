"""从 skills/ 重新打包 dist/ 下的分发 zip。

用法（在仓库根目录执行）：
    python scripts/build_zips.py

产物：
    dist/<skill-name>.zip              每个技能一个，根目录为 <skill-name>/SKILL.md
    dist/geo-writing-suite-v<VERSION>.zip   四个技能合并
"""

import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
DIST = os.path.join(ROOT, "dist")


def add_tree(zf, skill_dir, base):
    for dirpath, dirnames, filenames in os.walk(skill_dir):
        dirnames.sort()
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, skill_dir)
            arc = os.path.join(base, rel).replace(os.sep, "/")
            zf.write(full, arc)


def main():
    with open(os.path.join(ROOT, "VERSION"), encoding="utf-8") as fh:
        version = fh.read().strip()

    os.makedirs(DIST, exist_ok=True)
    skills = sorted(
        d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d))
    )
    if not skills:
        raise SystemExit(f"skills/ 下没有找到技能目录：{SKILLS}")

    built = []
    for name in skills:
        if not os.path.isfile(os.path.join(SKILLS, name, "SKILL.md")):
            raise SystemExit(f"{name}/SKILL.md 不存在，跳过打包前请先补上")
        out = os.path.join(DIST, f"{name}.zip")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            add_tree(zf, os.path.join(SKILLS, name), name)
        built.append(out)

    suite = os.path.join(DIST, f"geo-writing-suite-v{version}.zip")
    with zipfile.ZipFile(suite, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for name in skills:
            add_tree(zf, os.path.join(SKILLS, name), name)
    built.append(suite)

    for path in built:
        with zipfile.ZipFile(path) as zf:
            bad = zf.testzip()
            state = "OK" if bad is None else f"CORRUPT: {bad}"
            print(f"{os.path.basename(path):40s} {os.path.getsize(path):8d} B  "
                  f"{len(zf.namelist()):3d} entries  {state}")


if __name__ == "__main__":
    main()
