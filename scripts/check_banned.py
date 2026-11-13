#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描文本是否含违禁词（与 references/banned-words.md 对应，可扩展）。
用法: python3 check_banned.py "这是全网最低价"
      或: echo "文案..." | python3 check_banned.py
退出码 1 表示命中违禁词，0 表示通过。
"""
import sys

BANNED = [
    "最", "第一", "唯一", "顶级", "国家级", "世界级", "极致", "绝无仅有", "万能", "100%", "绝对",
    "独家", "首发", "全网最低", "销量第一", "领导者", "包治", "根治", "保证赚钱", "稳赚",
    "躺赚", "一夜暴富", "治疗", "治愈", "消炎", "抗癌", "排毒", "减肥特效", "丰胸", "增高",
    "加微信", "私聊", "代购", "刷单", "刷量", "算命", "改运", "招财", "风水",
]


def check(text: str):
    return [w for w in BANNED if w in text]


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read()
    hits = check(text)
    if hits:
        print("未通过，命中违禁词：", "、".join(hits))
        sys.exit(1)
    print("通过：未发现已知违禁词")
