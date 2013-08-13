# -*- coding: utf-8 -*-
# vim:set et sts=4 sw=4:
#
# libzhuyin - Library to deal with zhuyin.
#
# Copyright (c) 2010 BYVoid <byvoid1@gmail.com>
# Copyright (C) 2011 Peng Wu <alexepico@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


BOPOMOFO_PINYIN_MAP = {
    "ㄅ" : "b",
    "ㄅㄚ" : "ba",
    "ㄅㄛ" : "bo",
    "ㄅㄞ" : "bai",
    "ㄅㄟ" : "bei",
    "ㄅㄠ" : "bao",
    "ㄅㄢ" : "ban",
    "ㄅㄣ" : "ben",
    "ㄅㄤ" : "bang",
    "ㄅㄥ" : "beng",
    "ㄅㄧ" : "bi",
    "ㄅㄧㄝ" : "bie",
    "ㄅㄧㄠ" : "biao",
    "ㄅㄧㄢ" : "bian",
    "ㄅㄧㄣ" : "bin",
    "ㄅㄧㄥ" : "bing",
    "ㄅㄨ" : "bu",
    "ㄆ" : "p",
    "ㄆㄚ" : "pa",
    "ㄆㄛ" : "po",
    "ㄆㄞ" : "pai",
    "ㄆㄟ" : "pei",
    "ㄆㄠ" : "pao",
    "ㄆㄡ" : "pou",
    "ㄆㄢ" : "pan",
    "ㄆㄣ" : "pen",
    "ㄆㄤ" : "pang",
    "ㄆㄥ" : "peng",
    "ㄆㄧ" : "pi",
    "ㄆㄧㄝ" : "pie",
    "ㄆㄧㄠ" : "piao",
    "ㄆㄧㄢ" : "pian",
    "ㄆㄧㄣ" : "pin",
    "ㄆㄧㄥ" : "ping",
    "ㄆㄨ" : "pu",
    "ㄇ" : "m",
    "ㄇㄚ" : "ma",
    "ㄇㄛ" : "mo",
    "ㄇㄜ" : "me",
    "ㄇㄞ" : "mai",
    "ㄇㄟ" : "mei",
    "ㄇㄠ" : "mao",
    "ㄇㄡ" : "mou",
    "ㄇㄢ" : "man",
    "ㄇㄣ" : "men",
    "ㄇㄤ" : "mang",
    "ㄇㄥ" : "meng",
    "ㄇㄧ" : "mi",
    "ㄇㄧㄝ" : "mie",
    "ㄇㄧㄠ" : "miao",
    "ㄇㄧㄡ" : "miu",
    "ㄇㄧㄢ" : "mian",
    "ㄇㄧㄣ" : "min",
    "ㄇㄧㄥ" : "ming",
    "ㄇㄨ" : "mu",
    "ㄈ" : "f",
    "ㄈㄚ" : "fa",
    "ㄈㄛ" : "fo",
    "ㄈㄜ" : "fe",
    "ㄈㄟ" : "fei",
    "ㄈㄡ" : "fou",
    "ㄈㄢ" : "fan",
    "ㄈㄣ" : "fen",
    "ㄈㄤ" : "fang",
    "ㄈㄥ" : "feng",
    "ㄈㄨ" : "fu",
    "ㄉ" : "d",
    "ㄉㄚ" : "da",
    "ㄉㄜ" : "de",
    "ㄉㄞ" : "dai",
    "ㄉㄟ" : "dei",
    "ㄉㄠ" : "dao",
    "ㄉㄡ" : "dou",
    "ㄉㄢ" : "dan",
    "ㄉㄣ" : "den",
    "ㄉㄤ" : "dang",
    "ㄉㄥ" : "deng",
    "ㄉㄧ" : "di",
    "ㄉㄧㄚ" : "dia",
    "ㄉㄧㄝ" : "die",
    "ㄉㄧㄠ" : "diao",
    "ㄉㄧㄡ" : "diu",
    "ㄉㄧㄢ" : "dian",
    "ㄉㄧㄣ" : "din",
    "ㄉㄧㄥ" : "ding",
    "ㄉㄨ" : "du",
    "ㄉㄨㄛ" : "duo",
    "ㄉㄨㄟ" : "dui",
    "ㄉㄨㄢ" : "duan",
    "ㄉㄨㄣ" : "dun",
    "ㄉㄨㄥ" : "dong",
    "ㄊ" : "t",
    "ㄊㄚ" : "ta",
    "ㄊㄜ" : "te",
    "ㄊㄞ" : "tai",
    "ㄊㄠ" : "tao",
    "ㄊㄡ" : "tou",
    "ㄊㄢ" : "tan",
    "ㄊㄤ" : "tang",
    "ㄊㄥ" : "teng",
    "ㄊㄧ" : "ti",
    "ㄊㄧㄝ" : "tie",
    "ㄊㄧㄠ" : "tiao",
    "ㄊㄧㄢ" : "tian",
    "ㄊㄧㄥ" : "ting",
    "ㄊㄨ" : "tu",
    "ㄊㄨㄛ" : "tuo",
    "ㄊㄨㄟ" : "tui",
    "ㄊㄨㄢ" : "tuan",
    "ㄊㄨㄣ" : "tun",
    "ㄊㄨㄥ" : "tong",
    "ㄋ" : "n",
    "ㄋㄚ" : "na",
    "ㄋㄜ" : "ne",
    "ㄋㄞ" : "nai",
    "ㄋㄟ" : "nei",
    "ㄋㄠ" : "nao",
    "ㄋㄡ" : "nou",
    "ㄋㄢ" : "nan",
    "ㄋㄣ" : "nen",
    "ㄋㄤ" : "nang",
    "ㄋㄥ" : "neng",
    "ㄋㄧ" : "ni",
    "ㄋㄧㄚ" : "nia",
    "ㄋㄧㄝ" : "nie",
    "ㄋㄧㄠ" : "niao",
    "ㄋㄧㄡ" : "niu",
    "ㄋㄧㄢ" : "nian",
    "ㄋㄧㄣ" : "nin",
    "ㄋㄧㄤ" : "niang",
    "ㄋㄧㄥ" : "ning",
    "ㄋㄨ" : "nu",
    "ㄋㄨㄛ" : "nuo",
    "ㄋㄨㄢ" : "nuan",
    "ㄋㄨㄣ" : "nun",
    "ㄋㄨㄥ" : "nong",
    "ㄋㄩ" : "nv",
    "ㄋㄩㄝ" : "nve",
    "ㄌ" : "l",
    "ㄌㄚ" : "la",
    "ㄌㄛ" : "lo",
    "ㄌㄜ" : "le",
    "ㄌㄞ" : "lai",
    "ㄌㄟ" : "lei",
    "ㄌㄠ" : "lao",
    "ㄌㄡ" : "lou",
    "ㄌㄢ" : "lan",
    "ㄌㄣ" : "len",
    "ㄌㄤ" : "lang",
    "ㄌㄥ" : "leng",
    "ㄌㄧ" : "li",
    "ㄌㄧㄚ" : "lia",
    "ㄌㄧㄝ" : "lie",
    "ㄌㄧㄠ" : "liao",
    "ㄌㄧㄡ" : "liu",
    "ㄌㄧㄢ" : "lian",
    "ㄌㄧㄣ" : "lin",
    "ㄌㄧㄤ" : "liang",
    "ㄌㄧㄥ" : "ling",
    "ㄌㄨ" : "lu",
    "ㄌㄨㄛ" : "luo",
    "ㄌㄨㄢ" : "luan",
    "ㄌㄨㄣ" : "lun",
    "ㄌㄨㄥ" : "long",
    "ㄌㄩ" : "lv",
    "ㄌㄩㄝ" : "lve",
    "ㄍ" : "g",
    "ㄍㄚ" : "ga",
    "ㄍㄜ" : "ge",
    "ㄍㄞ" : "gai",
    "ㄍㄟ" : "gei",
    "ㄍㄠ" : "gao",
    "ㄍㄡ" : "gou",
    "ㄍㄢ" : "gan",
    "ㄍㄣ" : "gen",
    "ㄍㄤ" : "gang",
    "ㄍㄥ" : "geng",
    "ㄍㄨ" : "gu",
    "ㄍㄨㄚ" : "gua",
    "ㄍㄨㄛ" : "guo",
    "ㄍㄨㄞ" : "guai",
    "ㄍㄨㄟ" : "gui",
    "ㄍㄨㄢ" : "guan",
    "ㄍㄨㄣ" : "gun",
    "ㄍㄨㄤ" : "guang",
    "ㄍㄨㄥ" : "gong",
    "ㄎ" : "k",
    "ㄎㄚ" : "ka",
    "ㄎㄜ" : "ke",
    "ㄎㄞ" : "kai",
    "ㄎㄟ" : "kei",
    "ㄎㄠ" : "kao",
    "ㄎㄡ" : "kou",
    "ㄎㄢ" : "kan",
    "ㄎㄣ" : "ken",
    "ㄎㄤ" : "kang",
    "ㄎㄥ" : "keng",
    "ㄎㄨ" : "ku",
    "ㄎㄨㄚ" : "kua",
    "ㄎㄨㄛ" : "kuo",
    "ㄎㄨㄞ" : "kuai",
    "ㄎㄨㄟ" : "kui",
    "ㄎㄨㄢ" : "kuan",
    "ㄎㄨㄣ" : "kun",
    "ㄎㄨㄤ" : "kuang",
    "ㄎㄨㄥ" : "kong",
    "ㄏ" : "h",
    "ㄏㄚ" : "ha",
    "ㄏㄜ" : "he",
    "ㄏㄞ" : "hai",
    "ㄏㄟ" : "hei",
    "ㄏㄠ" : "hao",
    "ㄏㄡ" : "hou",
    "ㄏㄢ" : "han",
    "ㄏㄣ" : "hen",
    "ㄏㄤ" : "hang",
    "ㄏㄥ" : "heng",
    "ㄏㄨ" : "hu",
    "ㄏㄨㄚ" : "hua",
    "ㄏㄨㄛ" : "huo",
    "ㄏㄨㄞ" : "huai",
    "ㄏㄨㄟ" : "hui",
    "ㄏㄨㄢ" : "huan",
    "ㄏㄨㄣ" : "hun",
    "ㄏㄨㄤ" : "huang",
    "ㄏㄨㄥ" : "hong",
    "ㄐ" : "j",
    "ㄐㄧ" : "ji",
    "ㄐㄧㄚ" : "jia",
    "ㄐㄧㄝ" : "jie",
    "ㄐㄧㄠ" : "jiao",
    "ㄐㄧㄡ" : "jiu",
    "ㄐㄧㄢ" : "jian",
    "ㄐㄧㄣ" : "jin",
    "ㄐㄧㄤ" : "jiang",
    "ㄐㄧㄥ" : "jing",
    "ㄐㄩ" : "ju",
    "ㄐㄩㄝ" : "jue",
    "ㄐㄩㄢ" : "juan",
    "ㄐㄩㄣ" : "jun",
    "ㄐㄩㄥ" : "jiong",
    "ㄑ" : "q",
    "ㄑㄧ" : "qi",
    "ㄑㄧㄚ" : "qia",
    "ㄑㄧㄝ" : "qie",
    "ㄑㄧㄠ" : "qiao",
    "ㄑㄧㄡ" : "qiu",
    "ㄑㄧㄢ" : "qian",
    "ㄑㄧㄣ" : "qin",
    "ㄑㄧㄤ" : "qiang",
    "ㄑㄧㄥ" : "qing",
    "ㄑㄩ" : "qu",
    "ㄑㄩㄝ" : "que",
    "ㄑㄩㄢ" : "quan",
    "ㄑㄩㄣ" : "qun",
    "ㄑㄩㄥ" : "qiong",
    "ㄒ" : "x",
    "ㄒㄧ" : "xi",
    "ㄒㄧㄚ" : "xia",
    "ㄒㄧㄝ" : "xie",
    "ㄒㄧㄠ" : "xiao",
    "ㄒㄧㄡ" : "xiu",
    "ㄒㄧㄢ" : "xian",
    "ㄒㄧㄣ" : "xin",
    "ㄒㄧㄤ" : "xiang",
    "ㄒㄧㄥ" : "xing",
    "ㄒㄩ" : "xu",
    "ㄒㄩㄝ" : "xue",
    "ㄒㄩㄢ" : "xuan",
    "ㄒㄩㄣ" : "xun",
    "ㄒㄩㄥ" : "xiong",
    "ㄓ" : "zhi",
    "ㄓㄚ" : "zha",
    "ㄓㄜ" : "zhe",
    "ㄓㄞ" : "zhai",
    "ㄓㄟ" : "zhei",
    "ㄓㄠ" : "zhao",
    "ㄓㄡ" : "zhou",
    "ㄓㄢ" : "zhan",
    "ㄓㄣ" : "zhen",
    "ㄓㄤ" : "zhang",
    "ㄓㄥ" : "zheng",
    "ㄓㄨ" : "zhu",
    "ㄓㄨㄚ" : "zhua",
    "ㄓㄨㄛ" : "zhuo",
    "ㄓㄨㄞ" : "zhuai",
    "ㄓㄨㄟ" : "zhui",
    "ㄓㄨㄢ" : "zhuan",
    "ㄓㄨㄣ" : "zhun",
    "ㄓㄨㄤ" : "zhuang",
    "ㄓㄨㄥ" : "zhong",
    "ㄔ" : "chi",
    "ㄔㄚ" : "cha",
    "ㄔㄜ" : "che",
    "ㄔㄞ" : "chai",
    "ㄔㄠ" : "chao",
    "ㄔㄡ" : "chou",
    "ㄔㄢ" : "chan",
    "ㄔㄣ" : "chen",
    "ㄔㄤ" : "chang",
    "ㄔㄥ" : "cheng",
    "ㄔㄨ" : "chu",
    "ㄔㄨㄚ" : "chua",
    "ㄔㄨㄛ" : "chuo",
    "ㄔㄨㄞ" : "chuai",
    "ㄔㄨㄟ" : "chui",
    "ㄔㄨㄢ" : "chuan",
    "ㄔㄨㄣ" : "chun",
    "ㄔㄨㄤ" : "chuang",
    "ㄔㄨㄥ" : "chong",
    "ㄕ" : "shi",
    "ㄕㄚ" : "sha",
    "ㄕㄜ" : "she",
    "ㄕㄞ" : "shai",
    "ㄕㄟ" : "shei",
    "ㄕㄠ" : "shao",
    "ㄕㄡ" : "shou",
    "ㄕㄢ" : "shan",
    "ㄕㄣ" : "shen",
    "ㄕㄤ" : "shang",
    "ㄕㄥ" : "sheng",
    "ㄕㄨ" : "shu",
    "ㄕㄨㄚ" : "shua",
    "ㄕㄨㄛ" : "shuo",
    "ㄕㄨㄞ" : "shuai",
    "ㄕㄨㄟ" : "shui",
    "ㄕㄨㄢ" : "shuan",
    "ㄕㄨㄣ" : "shun",
    "ㄕㄨㄤ" : "shuang",
    "ㄖ" : "ri",
    "ㄖㄜ" : "re",
    "ㄖㄠ" : "rao",
    "ㄖㄡ" : "rou",
    "ㄖㄢ" : "ran",
    "ㄖㄣ" : "ren",
    "ㄖㄤ" : "rang",
    "ㄖㄥ" : "reng",
    "ㄖㄨ" : "ru",
    "ㄖㄨㄚ" : "rua",
    "ㄖㄨㄛ" : "ruo",
    "ㄖㄨㄟ" : "rui",
    "ㄖㄨㄢ" : "ruan",
    "ㄖㄨㄣ" : "run",
    "ㄖㄨㄥ" : "rong",
    "ㄗ" : "zi",
    "ㄗㄚ" : "za",
    "ㄗㄜ" : "ze",
    "ㄗㄞ" : "zai",
    "ㄗㄟ" : "zei",
    "ㄗㄠ" : "zao",
    "ㄗㄡ" : "zou",
    "ㄗㄢ" : "zan",
    "ㄗㄣ" : "zen",
    "ㄗㄤ" : "zang",
    "ㄗㄥ" : "zeng",
    "ㄗㄨ" : "zu",
    "ㄗㄨㄛ" : "zuo",
    "ㄗㄨㄟ" : "zui",
    "ㄗㄨㄢ" : "zuan",
    "ㄗㄨㄣ" : "zun",
    "ㄗㄨㄥ" : "zong",
    "ㄘ" : "ci",
    "ㄘㄚ" : "ca",
    "ㄘㄜ" : "ce",
    "ㄘㄞ" : "cai",
    "ㄘㄠ" : "cao",
    "ㄘㄡ" : "cou",
    "ㄘㄢ" : "can",
    "ㄘㄣ" : "cen",
    "ㄘㄤ" : "cang",
    "ㄘㄥ" : "ceng",
    "ㄘㄨ" : "cu",
    "ㄘㄨㄛ" : "cuo",
    "ㄘㄨㄟ" : "cui",
    "ㄘㄨㄢ" : "cuan",
    "ㄘㄨㄣ" : "cun",
    "ㄘㄨㄥ" : "cong",
    "ㄙ" : "si",
    "ㄙㄚ" : "sa",
    "ㄙㄜ" : "se",
    "ㄙㄞ" : "sai",
    "ㄙㄠ" : "sao",
    "ㄙㄡ" : "sou",
    "ㄙㄢ" : "san",
    "ㄙㄣ" : "sen",
    "ㄙㄤ" : "sang",
    "ㄙㄥ" : "seng",
    "ㄙㄨ" : "su",
    "ㄙㄨㄛ" : "suo",
    "ㄙㄨㄟ" : "sui",
    "ㄙㄨㄢ" : "suan",
    "ㄙㄨㄣ" : "sun",
    "ㄙㄨㄥ" : "song",
    "ㄚ" : "a",
    "ㄛ" : "o",
    "ㄜ" : "e",
    "ㄞ" : "ai",
    "ㄟ" : "ei",
    "ㄠ" : "ao",
    "ㄡ" : "ou",
    "ㄢ" : "an",
    "ㄣ" : "en",
    "ㄤ" : "ang",
    "ㄥ" : "eng",
    "ㄦ" : "er",
    "ㄧ" : "yi",
    "ㄧㄚ" : "ya",
    "ㄧㄛ" : "yo",
    "ㄧㄝ" : "ye",
    "ㄧㄞ" : "yai",
    "ㄧㄠ" : "yao",
    "ㄧㄡ" : "you",
    "ㄧㄢ" : "yan",
    "ㄧㄣ" : "yin",
    "ㄧㄤ" : "yang",
    "ㄧㄥ" : "ying",
    "ㄨ" : "wu",
    "ㄨㄚ" : "wa",
    "ㄨㄛ" : "wo",
    "ㄨㄞ" : "wai",
    "ㄨㄟ" : "wei",
    "ㄨㄢ" : "wan",
    "ㄨㄣ" : "wen",
    "ㄨㄤ" : "wang",
    "ㄨㄥ" : "weng",
    "ㄩ" : "yu",
    "ㄩㄝ" : "yue",
    "ㄩㄢ" : "yuan",
    "ㄩㄣ" : "yun",
    "ㄩㄥ" : "yong",
    "ㄫ" : "ng",
}

PINYIN_BOPOMOFO_MAP = dict([(v, k) for k, v in BOPOMOFO_PINYIN_MAP.items()])

SPECIAL_INITIAL_SET = {'ci', 'chi', 'si', 'shi', 'zi', 'zhi', 'ri'}

'''
SHENG_YUN_BOPOMOFO_MAP = {
    "b" : "ㄅ",
    "p" : "ㄆ",
    "m" : "ㄇ",
    "f" : "ㄈ",
    "d" : "ㄉ",
    "t" : "ㄊ",
    "n" : "ㄋ",
    "l" : "ㄌ",
    "g" : "ㄍ",
    "k" : "ㄎ",
    "h" : "ㄏ",
    "j" : "ㄐ",
    "q" : "ㄑ",
    "x" : "ㄒ",
    "zh" : "ㄓ",
    "ch" : "ㄔ",
    "sh" : "ㄕ",
    "r" : "ㄖ",
    "z" : "ㄗ",
    "c" : "ㄘ",
    "s" : "ㄙ",

    # 韻母為u,ue,un,uan,ong時ㄧ省略
    "y" : ("ㄧ", (("u", "ue", "un", "uan", "ong"), "")),
    "w" : "ㄨ",
    "a" : "ㄚ",
    "o" : "ㄛ",
    "e" : ("ㄜ", ("y", "ㄝ")),  # y後面為ㄝ

    # zh ch sh r z c s y後面為空
    "i" : ("ㄧ", (("zh", "ch", "sh", "r", "z", "c", "s", "y"), "")),

    # jqxy後面為ㄩ w後面為空
    "u" : ("ㄨ", ("jqxy", "ㄩ")),
    "v" : "ㄩ",
    "ai" : "ㄞ",
    "ei" : "ㄟ",
    "ao" : "ㄠ",
    "ou" : "ㄡ",
    "an" : "ㄢ",
    "en" : "ㄣ",
    "ang" : "ㄤ",
    "eng" : "ㄥ",
    "er" : "ㄦ",
    "ia" : "ㄧㄚ",
    "ie" : "ㄧㄝ",
    "iai" : "ㄧㄞ",
    "iao" : "ㄧㄠ",
    "iu" : "ㄧㄡ",
    "ian" : "ㄧㄢ",
    "in" : ("ㄧㄣ", ("y", "ㄣ")),      #y後面為ㄣ
    "iang" : "ㄧㄤ",
    "ing" : ("ㄧㄥ", ("y", "ㄥ")),     #y後面為ㄥ
    "ua" : "ㄨㄚ",
    "uo" : "ㄨㄛ",
    "ue" : "ㄩㄝ",
    # TODO: "ve" is OK?
    "ve" : "ㄩㄝ",
    "uai" : "ㄨㄞ",
    "ui" : "ㄨㄟ",
    "uan" :  ("ㄨㄢ", ("jqxy", "ㄩㄢ")),  # jqxy後面是ㄩㄢ
    "un" :   ("ㄨㄣ", ("jqxy", "ㄩㄣ")),  # jqxy後面是ㄩㄣ
    "uang" : ("ㄨㄤ", ("jqxy", "ㄩㄤ")),  # jqxy後面是ㄩㄤ
    "ong" :  ("ㄨㄥ", ("jqxy", "ㄩㄥ")),  # y後面為ㄩㄥ
    "iong" : "ㄩㄥ",
}
'''

BOPOMOFO_LUOMA_PINYIN_MAP = {
	"ㄅㄚ" : "ba",
	"ㄅㄛ" : "bo",
	"ㄅㄞ" : "bai",
	"ㄅㄟ" : "bei",
	"ㄅㄠ" : "bao",
	"ㄅㄢ" : "ban",
	"ㄅㄣ" : "ben",
	"ㄅㄤ" : "bang",
	"ㄅㄥ" : "beng",
	"ㄅㄧ" : "bi",
	"ㄅㄧㄝ" : "bieh",
	"ㄅㄧㄠ" : "biao",
	"ㄅㄧㄢ" : "bian",
	"ㄅㄧㄣ" : "bin",
	"ㄅㄧㄥ" : "bing",
	"ㄅㄨ" : "bu",
	"ㄆㄚ" : "pa",
	"ㄆㄛ" : "po",
	"ㄆㄞ" : "pai",
	"ㄆㄟ" : "pei",
	"ㄆㄠ" : "pao",
	"ㄆㄡ" : "pou",
	"ㄆㄢ" : "pan",
	"ㄆㄣ" : "pen",
	"ㄆㄤ" : "pang",
	"ㄆㄥ" : "peng",
	"ㄆㄧ" : "pi",
	"ㄆㄧㄝ" : "pieh",
	"ㄆㄧㄠ" : "piao",
	"ㄆㄧㄢ" : "pian",
	"ㄆㄧㄣ" : "pin",
	"ㄆㄧㄥ" : "ping",
	"ㄆㄨ" : "pu",
	"ㄇㄚ" : "ma",
	"ㄇㄛ" : "mo",
	"ㄇㄜ" : "me",
	"ㄇㄞ" : "mai",
	"ㄇㄟ" : "mei",
	"ㄇㄠ" : "mao",
	"ㄇㄡ" : "mou",
	"ㄇㄢ" : "man",
	"ㄇㄣ" : "men",
	"ㄇㄤ" : "mang",
	"ㄇㄥ" : "meng",
	"ㄇㄧ" : "mi",
	"ㄇㄧㄝ" : "mieh",
	"ㄇㄧㄠ" : "miao",
	"ㄇㄧㄡ" : "miou",
	"ㄇㄧㄢ" : "mian",
	"ㄇㄧㄣ" : "min",
	"ㄇㄧㄥ" : "ming",
	"ㄇㄨ" : "mu",
	"ㄈㄚ" : "fa",
	"ㄈㄛ" : "fo",
	"ㄈㄟ" : "fei",
	"ㄈㄡ" : "fou",
	"ㄈㄢ" : "fan",
	"ㄈㄣ" : "fen",
	"ㄈㄤ" : "fang",
	"ㄈㄨ" : "fu",
	"ㄉㄚ" : "da",
	"ㄉㄜ" : "de",
	"ㄉㄞ" : "dai",
	"ㄉㄟ" : "dei",
	"ㄉㄠ" : "dao",
	"ㄉㄡ" : "dou",
	"ㄉㄢ" : "dan",
	"ㄉㄤ" : "dang",
	"ㄉㄥ" : "deng",
	"ㄉㄧ" : "di",
	"ㄉㄧㄝ" : "dieh",
	"ㄉㄧㄠ" : "diao",
	"ㄉㄧㄡ" : "diou",
	"ㄉㄧㄢ" : "dian",
	"ㄉㄧㄥ" : "ding",
	"ㄉㄨ" : "du",
	"ㄉㄨㄛ" : "duo",
	"ㄉㄨㄟ" : "duei",
	"ㄉㄨㄢ" : "duan",
	"ㄉㄨㄣ" : "dun",
	"ㄉㄨㄥ" : "dong",
	"ㄊㄚ" : "ta",
	"ㄊㄜ" : "te",
	"ㄊㄞ" : "tai",
	"ㄊㄠ" : "tao",
	"ㄊㄡ" : "tou",
	"ㄊㄢ" : "tan",
	"ㄊㄤ" : "tang",
	"ㄊㄥ" : "teng",
	"ㄊㄧ" : "ti",
	"ㄊㄧㄝ" : "tieh",
	"ㄊㄧㄠ" : "tiao",
	"ㄊㄧㄢ" : "tian",
	"ㄊㄧㄥ" : "ting",
	"ㄊㄨ" : "tu",
	"ㄊㄨㄛ" : "tuo",
	"ㄊㄨㄟ" : "tuei",
	"ㄊㄨㄢ" : "tuan",
	"ㄊㄨㄣ" : "tun",
	"ㄊㄨㄥ" : "tong",
	"ㄋㄚ" : "na",
	"ㄋㄜ" : "ne",
	"ㄋㄞ" : "nai",
	"ㄋㄟ" : "nei",
	"ㄋㄠ" : "nao",
	"ㄋㄡ" : "nou",
	"ㄋㄢ" : "nan",
	"ㄋㄣ" : "nen",
	"ㄋㄤ" : "nang",
	"ㄋㄥ" : "neng",
	"ㄋㄧ" : "ni",
	"ㄋㄧㄝ" : "nieh",
	"ㄋㄧㄠ" : "niao",
	"ㄋㄧㄡ" : "niou",
	"ㄋㄧㄢ" : "nian",
	"ㄋㄧㄣ" : "nin",
	"ㄋㄧㄤ" : "niang",
	"ㄋㄧㄥ" : "ning",
	"ㄋㄨ" : "nu",
	"ㄋㄨㄛ" : "nuo",
	"ㄋㄨㄢ" : "nuan",
	"ㄋㄨㄣ" : "nun",
	"ㄋㄨㄥ" : "nong",
	"ㄋㄩ" : "nyu",
	"ㄋㄩㄝ" : "nyueh",
	"ㄌㄚ" : "la",
	"ㄌㄛ" : "lo",
	"ㄌㄜ" : "le",
	"ㄌㄞ" : "lai",
	"ㄌㄟ" : "lei",
	"ㄌㄠ" : "lao",
	"ㄌㄡ" : "lou",
	"ㄌㄢ" : "lan",
	"ㄌㄤ" : "lang",
	"ㄌㄥ" : "leng",
	"ㄌㄧ" : "li",
	"ㄌㄧㄚ" : "lia",
	"ㄌㄧㄝ" : "lieh",
	"ㄌㄧㄠ" : "liao",
	"ㄌㄧㄡ" : "liou",
	"ㄌㄧㄢ" : "lian",
	"ㄌㄧㄣ" : "lin",
	"ㄌㄧㄤ" : "liang",
	"ㄌㄧㄥ" : "ling",
	"ㄌㄨ" : "lu",
	"ㄌㄨㄛ" : "luo",
	"ㄌㄨㄢ" : "luan",
	"ㄌㄨㄣ" : "lun",
	"ㄌㄨㄥ" : "long",
	"ㄌㄩ" : "lyu",
	"ㄌㄩㄝ" : "lyueh",
	"ㄌㄩㄢ" : "lyuan",
	"ㄍㄚ" : "ga",
	"ㄍㄜ" : "ge",
	"ㄍㄞ" : "gai",
	"ㄍㄟ" : "gei",
	"ㄍㄠ" : "gao",
	"ㄍㄡ" : "gou",
	"ㄍㄢ" : "gan",
	"ㄍㄣ" : "gen",
	"ㄍㄤ" : "gang",
	"ㄍㄥ" : "geng",
	"ㄍㄨ" : "gu",
	"ㄍㄨㄚ" : "gua",
	"ㄍㄨㄛ" : "guo",
	"ㄍㄨㄞ" : "guai",
	"ㄍㄨㄟ" : "guei",
	"ㄍㄨㄢ" : "guan",
	"ㄍㄨㄣ" : "gun",
	"ㄍㄨㄤ" : "guang",
	"ㄍㄨㄥ" : "gong",
	"ㄎㄚ" : "ka",
	"ㄎㄜ" : "ke",
	"ㄎㄞ" : "kai",
	"ㄎㄠ" : "kao",
	"ㄎㄡ" : "kou",
	"ㄎㄢ" : "kan",
	"ㄎㄣ" : "ken",
	"ㄎㄤ" : "kang",
	"ㄎㄥ" : "keng",
	"ㄎㄨ" : "ku",
	"ㄎㄨㄚ" : "kua",
	"ㄎㄨㄛ" : "kuo",
	"ㄎㄨㄞ" : "kuai",
	"ㄎㄨㄟ" : "kuei",
	"ㄎㄨㄢ" : "kuan",
	"ㄎㄨㄣ" : "kun",
	"ㄎㄨㄤ" : "kuang",
	"ㄎㄨㄥ" : "kong",
	"ㄏㄚ" : "ha",
	"ㄏㄜ" : "he",
	"ㄏㄞ" : "hai",
	"ㄏㄟ" : "hei",
	"ㄏㄠ" : "hao",
	"ㄏㄡ" : "hou",
	"ㄏㄢ" : "han",
	"ㄏㄣ" : "hen",
	"ㄏㄤ" : "hang",
	"ㄏㄥ" : "heng",
	"ㄏㄨ" : "hu",
	"ㄏㄨㄚ" : "hua",
	"ㄏㄨㄛ" : "huo",
	"ㄏㄨㄞ" : "huai",
	"ㄏㄨㄟ" : "huei",
	"ㄏㄨㄢ" : "huan",
	"ㄏㄨㄣ" : "hun",
	"ㄏㄨㄤ" : "huang",
	"ㄏㄨㄥ" : "hong",
	"ㄐㄧ" : "ji",
	"ㄐㄧㄚ" : "jia",
	"ㄐㄧㄝ" : "jieh",
	"ㄐㄧㄠ" : "jiao",
	"ㄐㄧㄡ" : "jiou",
	"ㄐㄧㄢ" : "jian",
	"ㄐㄧㄣ" : "jin",
	"ㄐㄧㄤ" : "jiang",
	"ㄐㄧㄥ" : "jing",
	"ㄐㄩ" : "jyu",
	"ㄐㄩㄝ" : "jyueh",
	"ㄐㄩㄢ" : "jyuan",
	"ㄐㄩㄣ" : "jyun",
	"ㄐㄩㄥ" : "jyong",
	"ㄑㄧ" : "chi",
	"ㄑㄧㄚ" : "chia",
	"ㄑㄧㄝ" : "chieh",
	"ㄑㄧㄠ" : "chiao",
	"ㄑㄧㄡ" : "chiou",
	"ㄑㄧㄢ" : "chian",
	"ㄑㄧㄣ" : "chin",
	"ㄑㄧㄤ" : "chiang",
	"ㄑㄧㄥ" : "ching",
	"ㄑㄩ" : "chyu",
	"ㄑㄩㄝ" : "chyueh",
	"ㄑㄩㄢ" : "chyuan",
	"ㄑㄩㄣ" : "chyun",
	"ㄑㄩㄥ" : "chyong",
	"ㄒㄧ" : "si",
	"ㄒㄧㄚ" : "sia",
	"ㄒㄧㄝ" : "sieh",
	"ㄒㄧㄠ" : "siao",
	"ㄒㄧㄡ" : "siou",
	"ㄒㄧㄢ" : "sian",
	"ㄒㄧㄣ" : "sin",
	"ㄒㄧㄤ" : "siang",
	"ㄒㄧㄥ" : "sing",
	"ㄒㄩ" : "syu",
	"ㄒㄩㄝ" : "syueh",
	"ㄒㄩㄢ" : "syuan",
	"ㄒㄩㄣ" : "syun",
	"ㄒㄩㄥ" : "syong",
	"ㄓ" : "jhih",
	"ㄓㄚ" : "jha",
	"ㄓㄜ" : "jhe",
	"ㄓㄞ" : "jhai",
	"ㄓㄟ" : "jhei",
	"ㄓㄠ" : "jhao",
	"ㄓㄡ" : "jhou",
	"ㄓㄢ" : "jhan",
	"ㄓㄣ" : "jhen",
	"ㄓㄤ" : "jhang",
	"ㄓㄥ" : "jheng",
	"ㄓㄨ" : "jhu",
	"ㄓㄨㄚ" : "jhua",
	"ㄓㄨㄛ" : "jhuo",
	"ㄓㄨㄞ" : "jhuai",
	"ㄓㄨㄟ" : "jhuei",
	"ㄓㄨㄢ" : "jhuan",
	"ㄓㄨㄣ" : "jhun",
	"ㄓㄨㄤ" : "jhuang",
	"ㄓㄨㄥ" : "jhong",
	"ㄔ" : "chih",
	"ㄔㄚ" : "cha",
	"ㄔㄜ" : "che",
	"ㄔㄞ" : "chai",
	"ㄔㄠ" : "chao",
	"ㄔㄡ" : "chou",
	"ㄔㄢ" : "chan",
	"ㄔㄣ" : "chen",
	"ㄔㄤ" : "chang",
	"ㄔㄥ" : "cheng",
	"ㄔㄨ" : "chu",
	"ㄔㄨㄛ" : "chuo",
	"ㄔㄨㄞ" : "chuai",
	"ㄔㄨㄟ" : "chuei",
	"ㄔㄨㄢ" : "chuan",
	"ㄔㄨㄣ" : "chun",
	"ㄔㄨㄤ" : "chuang",
	"ㄔㄨㄥ" : "chong",
	"ㄕ" : "shih",
	"ㄕㄚ" : "sha",
	"ㄕㄜ" : "she",
	"ㄕㄞ" : "shai",
	"ㄕㄟ" : "shei",
	"ㄕㄠ" : "shao",
	"ㄕㄡ" : "shou",
	"ㄕㄢ" : "shan",
	"ㄕㄣ" : "shen",
	"ㄕㄤ" : "shang",
	"ㄕㄥ" : "sheng",
	"ㄕㄨ" : "shu",
	"ㄕㄨㄚ" : "shua",
	"ㄕㄨㄛ" : "shuo",
	"ㄕㄨㄞ" : "shuai",
	"ㄕㄨㄟ" : "shuei",
	"ㄕㄨㄢ" : "shuan",
	"ㄕㄨㄣ" : "shun",
	"ㄕㄨㄤ" : "shuang",
	"ㄖ" : "rih",
	"ㄖㄜ" : "re",
	"ㄖㄠ" : "rao",
	"ㄖㄡ" : "rou",
	"ㄖㄢ" : "ran",
	"ㄖㄣ" : "ren",
	"ㄖㄤ" : "rang",
	"ㄖㄥ" : "reng",
	"ㄖㄨ" : "ru",
	"ㄖㄨㄛ" : "ruo",
	"ㄖㄨㄟ" : "ruei",
	"ㄖㄨㄢ" : "ruan",
	"ㄖㄨㄣ" : "run",
	"ㄖㄨㄥ" : "rong",
	"ㄗ" : "zih",
	"ㄗㄚ" : "za",
	"ㄗㄜ" : "ze",
	"ㄗㄞ" : "zai",
	"ㄗㄟ" : "zei",
	"ㄗㄠ" : "zao",
	"ㄗㄡ" : "zou",
	"ㄗㄢ" : "zan",
	"ㄗㄣ" : "zen",
	"ㄗㄤ" : "zang",
	"ㄗㄥ" : "zeng",
	"ㄗㄨ" : "zu",
	"ㄗㄨㄛ" : "zuo",
	"ㄗㄨㄟ" : "zuei",
	"ㄗㄨㄢ" : "zuan",
	"ㄗㄨㄣ" : "zun",
	"ㄗㄨㄥ" : "zong",
	"ㄘ" : "tsih",
	"ㄘㄚ" : "tsa",
	"ㄘㄜ" : "tse",
	"ㄘㄞ" : "tsai",
	"ㄘㄠ" : "tsao",
	"ㄘㄡ" : "tsou",
	"ㄘㄢ" : "tsan",
	"ㄘㄣ" : "tsen",
	"ㄘㄤ" : "tsang",
	"ㄘㄥ" : "tseng",
	"ㄘㄨ" : "tsu",
	"ㄘㄨㄛ" : "tsuo",
	"ㄘㄨㄟ" : "tsuei",
	"ㄘㄨㄢ" : "tsuan",
	"ㄘㄨㄣ" : "tsun",
	"ㄘㄨㄥ" : "tsong",
	"ㄙ" : "sih",
	"ㄙㄚ" : "sa",
	"ㄙㄜ" : "se",
	"ㄙㄞ" : "sai",
	"ㄙㄠ" : "sao",
	"ㄙㄡ" : "sou",
	"ㄙㄢ" : "san",
	"ㄙㄣ" : "sen",
	"ㄙㄤ" : "sang",
	"ㄙㄥ" : "seng",
	"ㄙㄨ" : "su",
	"ㄙㄨㄛ" : "suo",
	"ㄙㄨㄟ" : "suei",
	"ㄙㄨㄢ" : "suan",
	"ㄙㄨㄣ" : "sun",
	"ㄙㄨㄥ" : "song",
	"ㄚ" : "a",
	"ㄛ" : "o",
	"ㄜ" : "e",
	"ㄝ" : "eh",
	"ㄞ" : "ai",
	"ㄟ" : "ei",
	"ㄠ" : "ao",
	"ㄡ" : "ou",
	"ㄢ" : "an",
	"ㄣ" : "en",
	"ㄤ" : "ang",
	"ㄥ" : "eng",
	"ㄦ" : "er",
	"ㄧ" : "yi",
	"ㄧㄚ" : "ya",
	"ㄧㄛ" : "yo",
	"ㄧㄝ" : "yeh",
	"ㄧㄞ" : "yai",
	"ㄧㄠ" : "yao",
	"ㄧㄡ" : "you",
	"ㄧㄢ" : "yan",
	"ㄧㄣ" : "yin",
	"ㄧㄤ" : "yang",
	"ㄧㄥ" : "ying",
	"ㄨ" : "wu",
	"ㄨㄚ" : "wa",
	"ㄨㄛ" : "wo",
	"ㄨㄞ" : "wai",
	"ㄨㄟ" : "wei",
	"ㄨㄢ" : "wan",
	"ㄨㄣ" : "wun",
	"ㄨㄤ" : "wang",
	"ㄨㄥ" : "wong",
	"ㄩ" : "yu",
	"ㄩㄝ" : "yueh",
	"ㄩㄢ" : "yuan",
	"ㄩㄣ" : "yun",
	"ㄩㄥ" : "yong",
}


BOPOMOFO_SECOND_BOPOMOFO_MAP = {
	"ㄅㄚ" : "ba",
	"ㄅㄛ" : "bo",
	"ㄅㄞ" : "bai",
	"ㄅㄟ" : "bei",
	"ㄅㄠ" : "bau",
	"ㄅㄢ" : "ban",
	"ㄅㄣ" : "ben",
	"ㄅㄤ" : "bang",
	"ㄅㄥ" : "beng",
	"ㄅㄧ" : "bi",
	"ㄅㄧㄝ" : "bie",
	"ㄅㄧㄠ" : "biau",
	"ㄅㄧㄢ" : "bian",
	"ㄅㄧㄣ" : "bin",
	"ㄅㄧㄥ" : "bing",
	"ㄅㄨ" : "bu",
	"ㄆㄚ" : "pa",
	"ㄆㄛ" : "po",
	"ㄆㄞ" : "pai",
	"ㄆㄟ" : "pei",
	"ㄆㄠ" : "pau",
	"ㄆㄡ" : "pou",
	"ㄆㄢ" : "pan",
	"ㄆㄣ" : "pen",
	"ㄆㄤ" : "pang",
	"ㄆㄥ" : "peng",
	"ㄆㄧ" : "pi",
	"ㄆㄧㄝ" : "pie",
	"ㄆㄧㄠ" : "piau",
	"ㄆㄧㄢ" : "pian",
	"ㄆㄧㄣ" : "pin",
	"ㄆㄧㄥ" : "ping",
	"ㄆㄨ" : "pu",
	"ㄇㄚ" : "ma",
	"ㄇㄛ" : "mo",
	"ㄇㄜ" : "me",
	"ㄇㄞ" : "mai",
	"ㄇㄟ" : "mei",
	"ㄇㄠ" : "mau",
	"ㄇㄡ" : "mou",
	"ㄇㄢ" : "man",
	"ㄇㄣ" : "men",
	"ㄇㄤ" : "mang",
	"ㄇㄥ" : "meng",
	"ㄇㄧ" : "mi",
	"ㄇㄧㄝ" : "mie",
	"ㄇㄧㄠ" : "miau",
	"ㄇㄧㄡ" : "miou",
	"ㄇㄧㄢ" : "mian",
	"ㄇㄧㄣ" : "min",
	"ㄇㄧㄥ" : "ming",
	"ㄇㄨ" : "mu",
	"ㄈㄚ" : "fa",
	"ㄈㄛ" : "fo",
	"ㄈㄟ" : "fei",
	"ㄈㄡ" : "fou",
	"ㄈㄢ" : "fan",
	"ㄈㄣ" : "fen",
	"ㄈㄤ" : "fang",
	"ㄈㄨ" : "fu",
	"ㄉㄚ" : "da",
	"ㄉㄜ" : "de",
	"ㄉㄞ" : "dai",
	"ㄉㄟ" : "dei",
	"ㄉㄠ" : "dau",
	"ㄉㄡ" : "dou",
	"ㄉㄢ" : "dan",
	"ㄉㄤ" : "dang",
	"ㄉㄥ" : "deng",
	"ㄉㄧ" : "di",
	"ㄉㄧㄝ" : "die",
	"ㄉㄧㄠ" : "diau",
	"ㄉㄧㄡ" : "diou",
	"ㄉㄧㄢ" : "dian",
	"ㄉㄧㄥ" : "ding",
	"ㄉㄨ" : "du",
	"ㄉㄨㄛ" : "duo",
	"ㄉㄨㄟ" : "duei",
	"ㄉㄨㄢ" : "duan",
	"ㄉㄨㄣ" : "duen",
	"ㄉㄨㄥ" : "dung",
	"ㄊㄚ" : "ta",
	"ㄊㄜ" : "te",
	"ㄊㄞ" : "tai",
	"ㄊㄠ" : "tau",
	"ㄊㄡ" : "tou",
	"ㄊㄢ" : "tan",
	"ㄊㄤ" : "tang",
	"ㄊㄥ" : "teng",
	"ㄊㄧ" : "ti",
	"ㄊㄧㄝ" : "tie",
	"ㄊㄧㄠ" : "tiau",
	"ㄊㄧㄢ" : "tian",
	"ㄊㄧㄥ" : "ting",
	"ㄊㄨ" : "tu",
	"ㄊㄨㄛ" : "tuo",
	"ㄊㄨㄟ" : "tuei",
	"ㄊㄨㄢ" : "tuan",
	"ㄊㄨㄣ" : "tuen",
	"ㄊㄨㄥ" : "tung",
	"ㄋㄚ" : "na",
	"ㄋㄜ" : "ne",
	"ㄋㄞ" : "nai",
	"ㄋㄟ" : "nei",
	"ㄋㄠ" : "nau",
	"ㄋㄡ" : "nou",
	"ㄋㄢ" : "nan",
	"ㄋㄣ" : "nen",
	"ㄋㄤ" : "nang",
	"ㄋㄥ" : "neng",
	"ㄋㄧ" : "ni",
	"ㄋㄧㄝ" : "nie",
	"ㄋㄧㄠ" : "niau",
	"ㄋㄧㄡ" : "niou",
	"ㄋㄧㄢ" : "nian",
	"ㄋㄧㄣ" : "nin",
	"ㄋㄧㄤ" : "niang",
	"ㄋㄧㄥ" : "ning",
	"ㄋㄨ" : "nu",
	"ㄋㄨㄛ" : "nuo",
	"ㄋㄨㄢ" : "nuan",
	"ㄋㄨㄣ" : "nuen",
	"ㄋㄨㄥ" : "nung",
	"ㄋㄩ" : "niu",
	"ㄋㄩㄝ" : "niue",
	"ㄌㄚ" : "la",
	"ㄌㄛ" : "lo",
	"ㄌㄜ" : "le",
	"ㄌㄞ" : "lai",
	"ㄌㄟ" : "lei",
	"ㄌㄠ" : "lau",
	"ㄌㄡ" : "lou",
	"ㄌㄢ" : "lan",
	"ㄌㄤ" : "lang",
	"ㄌㄥ" : "leng",
	"ㄌㄧ" : "li",
	"ㄌㄧㄚ" : "lia",
	"ㄌㄧㄝ" : "lie",
	"ㄌㄧㄠ" : "liau",
	"ㄌㄧㄡ" : "liou",
	"ㄌㄧㄢ" : "lian",
	"ㄌㄧㄣ" : "lin",
	"ㄌㄧㄤ" : "liang",
	"ㄌㄧㄥ" : "ling",
	"ㄌㄨ" : "lu",
	"ㄌㄨㄛ" : "luo",
	"ㄌㄨㄢ" : "luan",
	"ㄌㄨㄣ" : "luen",
	"ㄌㄨㄥ" : "lung",
	"ㄌㄩ" : "liu",
	"ㄌㄩㄝ" : "liue",
	"ㄌㄩㄢ" : "liuan",
	"ㄍㄚ" : "ga",
	"ㄍㄜ" : "ge",
	"ㄍㄞ" : "gai",
	"ㄍㄟ" : "gei",
	"ㄍㄠ" : "gau",
	"ㄍㄡ" : "gou",
	"ㄍㄢ" : "gan",
	"ㄍㄣ" : "gen",
	"ㄍㄤ" : "gang",
	"ㄍㄥ" : "geng",
	"ㄍㄨ" : "gu",
	"ㄍㄨㄚ" : "gua",
	"ㄍㄨㄛ" : "guo",
	"ㄍㄨㄞ" : "guai",
	"ㄍㄨㄟ" : "guei",
	"ㄍㄨㄢ" : "guan",
	"ㄍㄨㄣ" : "guen",
	"ㄍㄨㄤ" : "guang",
	"ㄍㄨㄥ" : "gung",
	"ㄎㄚ" : "ka",
	"ㄎㄜ" : "ke",
	"ㄎㄞ" : "kai",
	"ㄎㄠ" : "kau",
	"ㄎㄡ" : "kou",
	"ㄎㄢ" : "kan",
	"ㄎㄣ" : "ken",
	"ㄎㄤ" : "kang",
	"ㄎㄥ" : "keng",
	"ㄎㄨ" : "ku",
	"ㄎㄨㄚ" : "kua",
	"ㄎㄨㄛ" : "kuo",
	"ㄎㄨㄞ" : "kuai",
	"ㄎㄨㄟ" : "kuei",
	"ㄎㄨㄢ" : "kuan",
	"ㄎㄨㄣ" : "kuen",
	"ㄎㄨㄤ" : "kuang",
	"ㄎㄨㄥ" : "kung",
	"ㄏㄚ" : "ha",
	"ㄏㄜ" : "he",
	"ㄏㄞ" : "hai",
	"ㄏㄟ" : "hei",
	"ㄏㄠ" : "hau",
	"ㄏㄡ" : "hou",
	"ㄏㄢ" : "han",
	"ㄏㄣ" : "hen",
	"ㄏㄤ" : "hang",
	"ㄏㄥ" : "heng",
	"ㄏㄨ" : "hu",
	"ㄏㄨㄚ" : "hua",
	"ㄏㄨㄛ" : "huo",
	"ㄏㄨㄞ" : "huai",
	"ㄏㄨㄟ" : "huei",
	"ㄏㄨㄢ" : "huan",
	"ㄏㄨㄣ" : "huen",
	"ㄏㄨㄤ" : "huang",
	"ㄏㄨㄥ" : "hung",
	"ㄐㄧ" : "ji",
	"ㄐㄧㄚ" : "jia",
	"ㄐㄧㄝ" : "jie",
	"ㄐㄧㄠ" : "jiau",
	"ㄐㄧㄡ" : "jiou",
	"ㄐㄧㄢ" : "jian",
	"ㄐㄧㄣ" : "jin",
	"ㄐㄧㄤ" : "jiang",
	"ㄐㄧㄥ" : "jing",
	"ㄐㄩ" : "jiu",
	"ㄐㄩㄝ" : "jiue",
	"ㄐㄩㄢ" : "jiuan",
	"ㄐㄩㄣ" : "jiun",
	"ㄐㄩㄥ" : "jiung",
	"ㄑㄧ" : "chi",
	"ㄑㄧㄚ" : "chia",
	"ㄑㄧㄝ" : "chie",
	"ㄑㄧㄠ" : "chiau",
	"ㄑㄧㄡ" : "chiou",
	"ㄑㄧㄢ" : "chian",
	"ㄑㄧㄣ" : "chin",
	"ㄑㄧㄤ" : "chiang",
	"ㄑㄧㄥ" : "ching",
	"ㄑㄩ" : "chiu",
	"ㄑㄩㄝ" : "chiue",
	"ㄑㄩㄢ" : "chiuan",
	"ㄑㄩㄣ" : "chiun",
	"ㄑㄩㄥ" : "chiung",
	"ㄒㄧ" : "shi",
	"ㄒㄧㄚ" : "shia",
	"ㄒㄧㄝ" : "shie",
	"ㄒㄧㄠ" : "shiau",
	"ㄒㄧㄡ" : "shiou",
	"ㄒㄧㄢ" : "shian",
	"ㄒㄧㄣ" : "shin",
	"ㄒㄧㄤ" : "shiang",
	"ㄒㄧㄥ" : "shing",
	"ㄒㄩ" : "shiu",
	"ㄒㄩㄝ" : "shiue",
	"ㄒㄩㄢ" : "shiuan",
	"ㄒㄩㄣ" : "shiun",
	"ㄒㄩㄥ" : "shiung",
	"ㄓ" : "jr",
	"ㄓㄚ" : "ja",
	"ㄓㄜ" : "je",
	"ㄓㄞ" : "jai",
	"ㄓㄟ" : "jei",
	"ㄓㄠ" : "jau",
	"ㄓㄡ" : "jou",
	"ㄓㄢ" : "jan",
	"ㄓㄣ" : "jen",
	"ㄓㄤ" : "jang",
	"ㄓㄥ" : "jeng",
	"ㄓㄨ" : "ju",
	"ㄓㄨㄚ" : "jua",
	"ㄓㄨㄛ" : "juo",
	"ㄓㄨㄞ" : "juai",
	"ㄓㄨㄟ" : "juei",
	"ㄓㄨㄢ" : "juan",
	"ㄓㄨㄣ" : "juen",
	"ㄓㄨㄤ" : "juang",
	"ㄓㄨㄥ" : "jung",
	"ㄔ" : "chr",
	"ㄔㄚ" : "cha",
	"ㄔㄜ" : "che",
	"ㄔㄞ" : "chai",
	"ㄔㄠ" : "chau",
	"ㄔㄡ" : "chou",
	"ㄔㄢ" : "chan",
	"ㄔㄣ" : "chen",
	"ㄔㄤ" : "chang",
	"ㄔㄥ" : "cheng",
	"ㄔㄨ" : "chu",
	"ㄔㄨㄛ" : "chuo",
	"ㄔㄨㄞ" : "chuai",
	"ㄔㄨㄟ" : "chuei",
	"ㄔㄨㄢ" : "chuan",
	"ㄔㄨㄣ" : "chuen",
	"ㄔㄨㄤ" : "chuang",
	"ㄔㄨㄥ" : "chung",
	"ㄕ" : "shr",
	"ㄕㄚ" : "sha",
	"ㄕㄜ" : "she",
	"ㄕㄞ" : "shai",
	"ㄕㄟ" : "shei",
	"ㄕㄠ" : "shau",
	"ㄕㄡ" : "shou",
	"ㄕㄢ" : "shan",
	"ㄕㄣ" : "shen",
	"ㄕㄤ" : "shang",
	"ㄕㄥ" : "sheng",
	"ㄕㄨ" : "shu",
	"ㄕㄨㄚ" : "shua",
	"ㄕㄨㄛ" : "shuo",
	"ㄕㄨㄞ" : "shuai",
	"ㄕㄨㄟ" : "shuei",
	"ㄕㄨㄢ" : "shuan",
	"ㄕㄨㄣ" : "shuen",
	"ㄕㄨㄤ" : "shuang",
	"ㄖ" : "r",
	"ㄖㄜ" : "re",
	"ㄖㄠ" : "rau",
	"ㄖㄡ" : "rou",
	"ㄖㄢ" : "ran",
	"ㄖㄣ" : "ren",
	"ㄖㄤ" : "rang",
	"ㄖㄥ" : "reng",
	"ㄖㄨ" : "ru",
	"ㄖㄨㄛ" : "ruo",
	"ㄖㄨㄟ" : "ruei",
	"ㄖㄨㄢ" : "ruan",
	"ㄖㄨㄣ" : "ruen",
	"ㄖㄨㄥ" : "rung",
	"ㄗ" : "tz",
	"ㄗㄚ" : "tza",
	"ㄗㄜ" : "tze",
	"ㄗㄞ" : "tzai",
	"ㄗㄟ" : "tzei",
	"ㄗㄠ" : "tzau",
	"ㄗㄡ" : "tzou",
	"ㄗㄢ" : "tzan",
	"ㄗㄣ" : "tzen",
	"ㄗㄤ" : "tzang",
	"ㄗㄥ" : "tzeng",
	"ㄗㄨ" : "tzu",
	"ㄗㄨㄛ" : "tzuo",
	"ㄗㄨㄟ" : "tzuei",
	"ㄗㄨㄢ" : "tzuan",
	"ㄗㄨㄣ" : "tzuen",
	"ㄗㄨㄥ" : "tzung",
	"ㄘ" : "tsz",
	"ㄘㄚ" : "tsa",
	"ㄘㄜ" : "tse",
	"ㄘㄞ" : "tsai",
	"ㄘㄠ" : "tsau",
	"ㄘㄡ" : "tsou",
	"ㄘㄢ" : "tsan",
	"ㄘㄣ" : "tsen",
	"ㄘㄤ" : "tsang",
	"ㄘㄥ" : "tseng",
	"ㄘㄨ" : "tsu",
	"ㄘㄨㄛ" : "tsuo",
	"ㄘㄨㄟ" : "tsuei",
	"ㄘㄨㄢ" : "tsuan",
	"ㄘㄨㄣ" : "tsun",
	"ㄘㄨㄥ" : "tsung",
	"ㄙ" : "sz",
	"ㄙㄚ" : "sa",
	"ㄙㄜ" : "se",
	"ㄙㄞ" : "sai",
	"ㄙㄠ" : "sau",
	"ㄙㄡ" : "sou",
	"ㄙㄢ" : "san",
	"ㄙㄣ" : "sen",
	"ㄙㄤ" : "sang",
	"ㄙㄥ" : "seng",
	"ㄙㄨ" : "su",
	"ㄙㄨㄛ" : "suo",
	"ㄙㄨㄟ" : "suei",
	"ㄙㄨㄢ" : "suan",
	"ㄙㄨㄣ" : "suen",
	"ㄙㄨㄥ" : "sung",
	"ㄚ" : "a",
	"ㄛ" : "o",
	"ㄜ" : "e",
	"ㄝ" : "ê",
	"ㄞ" : "ai",
	"ㄟ" : "ei",
	"ㄠ" : "au",
	"ㄡ" : "ou",
	"ㄢ" : "an",
	"ㄣ" : "en",
	"ㄤ" : "ang",
	"ㄥ" : "eng",
	"ㄦ" : "er",
	"ㄧ" : "yi",
	"ㄧㄚ" : "ya",
	"ㄧㄛ" : "yo",
	"ㄧㄝ" : "ye",
	"ㄧㄞ" : "yai",
	"ㄧㄠ" : "yau",
	"ㄧㄡ" : "you",
	"ㄧㄢ" : "yan",
	"ㄧㄣ" : "yin",
	"ㄧㄤ" : "yang",
	"ㄧㄥ" : "ying",
	"ㄨ" : "wu",
	"ㄨㄚ" : "wa",
	"ㄨㄛ" : "wo",
	"ㄨㄞ" : "wai",
	"ㄨㄟ" : "wei",
	"ㄨㄢ" : "wan",
	"ㄨㄣ" : "wen",
	"ㄨㄤ" : "wang",
	"ㄨㄥ" : "weng",
	"ㄩ" : "yu",
	"ㄩㄝ" : "yue",
	"ㄩㄢ" : "yuan",
	"ㄩㄣ" : "yun",
	"ㄩㄥ" : "yung",
}
