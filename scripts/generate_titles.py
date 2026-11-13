#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""根据主题生成短视频标题变体（辅助 SKILL 的"包装"步骤）。
用法: python3 generate_titles.py "螺蛳粉"
"""
import sys

TEMPLATES = {
    "悬念": ["你以为{t}？其实全错了", "90%的人都不知道{t}的真相", "{t}，但我劝你先别急"],
    "利益": ["1个方法，让{t}效果翻3倍", "3步搞定{t}，新手也能会", "靠{t}多赚5000，我做对了什么"],
    "痛点": ["是不是{t}总做不好？不是你不行", "别再为{t}花冤枉钱了", "{t}最坑的3个坑，你踩了几个"],
    "身份": ["想{t}的人，这条一定要看完", "{t}的人注意了，红利期就现在", "普通人怎么靠{t}翻身"],
    "冲突": ["别再{t}了，现在都流行这个", "我劝你别{t}，除非你想…", "{t}？别信那些网红说的"],
}


def gen(topic: str):
    out = []
    for cat, ts in TEMPLATES.items():
        for t in ts:
            out.append((cat, t.format(t=topic)))
    return out


if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "拍短视频"
    print(f"# 标题变体（主题：{topic}）")
    for cat, title in gen(topic):
        print(f"[{cat}] {title}")
