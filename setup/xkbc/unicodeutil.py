# vim:set et sts=4 sw=4:
#
# ibus-xkbc - The Input Bus Keyboard Layout emulaton engine.
#
# Copyright (c) 2009, 2010 Oracle and/or its affiliates. All rights reserved.
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
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

keysym_to_unicode = {
    "space" : 0x20,
    "exclam" : 0x21,
    "quotedbl" : 0x22,
    "doublequote" : 0x22,
    "numbersign" : 0x23,
    "dollar" : 0x24,
    "percent" : 0x25,
    "ampersand" : 0x26,
    "apostrophe" : 0x27,
    "quoteright" : 0x27,
    "parenleft" : 0x28,
    "parenright" : 0x29,
    "asterisk" : 0x2a,
    "plus" : 0x2b,
    "comma" : 0x2c,
    "minus" : 0x2d,
    "period" : 0x2e,
    "slash" : 0x2f,
    "0" : 0x30,
    "1" : 0x31,
    "2" : 0x32,
    "3" : 0x33,
    "4" : 0x34,
    "5" : 0x35,
    "6" : 0x36,
    "7" : 0x37,
    "8" : 0x38,
    "9" : 0x39,
    "colon" : 0x3a,
    "semicolon" : 0x3b,
    "less" : 0x3c,
    "equal" : 0x3d,
    "greater" : 0x3e,
    "question" : 0x3f,
    "at" : 0x40,
    "A" : 0x41,
    "B" : 0x42,
    "C" : 0x43,
    "D" : 0x44,
    "E" : 0x45,
    "F" : 0x46,
    "G" : 0x47,
    "H" : 0x48,
    "I" : 0x49,
    "J" : 0x4a,
    "K" : 0x4b,
    "L" : 0x4c,
    "M" : 0x4d,
    "N" : 0x4e,
    "O" : 0x4f,
    "P" : 0x50,
    "Q" : 0x51,
    "R" : 0x52,
    "S" : 0x53,
    "T" : 0x54,
    "U" : 0x55,
    "V" : 0x56,
    "W" : 0x57,
    "X" : 0x58,
    "Y" : 0x59,
    "Z" : 0x5a,
    "bracketleft" : 0x5b,
    "backslash" : 0x5c,
    "bracketright" : 0x5d,
    "asciicircum" : 0x5e,
    "asciicirum" : 0x5e,
    "underscore" : 0x5f,
    "grave" : 0x60,
    "quoteleft" : 0x60,
    "a" : 0x61,
    "b" : 0x62,
    "c" : 0x63,
    "d" : 0x64,
    "e" : 0x65,
    "f" : 0x66,
    "g" : 0x67,
    "h" : 0x68,
    "i" : 0x69,
    "j" : 0x6a,
    "k" : 0x6b,
    "l" : 0x6c,
    "m" : 0x6d,
    "n" : 0x6e,
    "o" : 0x6f,
    "p" : 0x70,
    "q" : 0x71,
    "r" : 0x72,
    "s" : 0x73,
    "t" : 0x74,
    "u" : 0x75,
    "v" : 0x76,
    "w" : 0x77,
    "x" : 0x78,
    "y" : 0x79,
    "z" : 0x7a,
    "braceleft" : 0x7b,
    "bar" : 0x7c,
    "braceright" : 0x7d,
    "asciitilde" : 0x7e,
    "nobreakspace" : 0xa0,
    "exclamdown" : 0xa1,
    "cent" : 0xa2,
    "sterling" : 0xa3,
    "currency" : 0xa4,
    "yen" : 0xa5,
    "brokenbar" : 0xa6,
    "section" : 0xa7,
    "diaeresis" : 0xa8,
    "copyright" : 0xa9,
    "ordfeminine" : 0xaa,
    "guillemotleft" : 0xab,
    "notsign" : 0xac,
    "hyphen" : 0xad,
    "soft_hyphen" : 0xad,
    "registered" : 0xae,
    "macron" : 0xaf,
    "degree" : 0xb0,
    "plusminus" : 0xb1,
    "twosuperior" : 0xb2,
    "threesuperior" : 0xb3,
    "acute" : 0xb4,
    "mu" : 0xb5,
    "paragraph" : 0xb6,
    "periodcentered" : 0xb7,
    "cedilla" : 0xb8,
    "onesuperior" : 0xb9,
    "masculine" : 0xba,
    "guillemotright" : 0xbb,
    "onequarter" : 0xbc,
    "onehalf" : 0xbd,
    "threequarters" : 0xbe,
    "questiondown" : 0xbf,
    "Agrave" : 0xc0,
    "Aacute" : 0xc1,
    "Acircumflex" : 0xc2,
    "Atilde" : 0xc3,
    "Adiaeresis" : 0xc4,
    "Aring" : 0xc5,
    "AE" : 0xc6,
    "Ccedilla" : 0xc7,
    "Egrave" : 0xc8,
    "Eacute" : 0xc9,
    "Ecircumflex" : 0xca,
    "Ediaeresis" : 0xcb,
    "Igrave" : 0xcc,
    "Iacute" : 0xcd,
    "Icircumflex" : 0xce,
    "Idiaeresis" : 0xcf,
    "ETH" : 0xd0,
    "Eth" : 0xd0,
    "Ntilde" : 0xd1,
    "Ograve" : 0xd2,
    "Oacute" : 0xd3,
    "Ocircumflex" : 0xd4,
    "Otilde" : 0xd5,
    "Odiaeresis" : 0xd6,
    "multiply" : 0xd7,
    "Ooblique" : 0xd8,
    "Oslash" : 0xd8,
    "Ugrave" : 0xd9,
    "Uacute" : 0xda,
    "Ucircumflex" : 0xdb,
    "Udiaeresis" : 0xdc,
    "Yacute" : 0xdd,
    "THORN" : 0xde,
    "Thorn" : 0xde,
    "ssharp" : 0xdf,
    "agrave" : 0xe0,
    "aacute" : 0xe1,
    "acircumflex" : 0xe2,
    "atilde" : 0xe3,
    "adiaeresis" : 0xe4,
    "aring" : 0xe5,
    "ae" : 0xe6,
    "ccedilla" : 0xe7,
    "egrave" : 0xe8,
    "eacute" : 0xe9,
    "ecircumflex" : 0xea,
    "ediaeresis" : 0xeb,
    "igrave" : 0xec,
    "iacute" : 0xed,
    "icircumflex" : 0xee,
    "idiaeresis" : 0xef,
    "eth" : 0xf0,
    "ntilde" : 0xf1,
    "ograve" : 0xf2,
    "oacute" : 0xf3,
    "ocircumflex" : 0xf4,
    "otilde" : 0xf5,
    "odiaeresis" : 0xf6,
    "division" : 0xf7,
    "oslash" : 0xf8,
    "ugrave" : 0xf9,
    "uacute" : 0xfa,
    "ucircumflex" : 0xfb,
    "udiaeresis" : 0xfc,
    "yacute" : 0xfd,
    "thorn" : 0xfe,
    "ydiaeresis" : 0xff,
    "Aogonek" : 0x104,
    "breve" : 0x2d8,
    "Lstroke" : 0x141,
    "Lcaron" : 0x13d,
    "Sacute" : 0x15a,
    "Scaron" : 0x160,
    "Scedilla" : 0x15e,
    "Tcaron" : 0x164,
    "Zacute" : 0x179,
    "Zcaron" : 0x17d,
    "Zabovedot" : 0x17b,
    "aogonek" : 0x105,
    "ogonek" : 0x2db,
    "lstroke" : 0x142,
    "lcaron" : 0x13e,
    "sacute" : 0x15b,
    "caron" : 0x2c7,
    "scaron" : 0x161,
    "scedilla" : 0x15f,
    "tcaron" : 0x165,
    "zacute" : 0x17a,
    "doubleacute" : 0x2dd,
    "zcaron" : 0x17e,
    "zabovedot" : 0x17c,
    "Racute" : 0x154,
    "Abreve" : 0x102,
    "Lacute" : 0x139,
    "Cacute" : 0x106,
    "Ccaron" : 0x10c,
    "Eogonek" : 0x118,
    "Ecaron" : 0x11a,
    "Dcaron" : 0x10e,
    "Dstroke" : 0x110,
    "Nacute" : 0x143,
    "Ncaron" : 0x147,
    "Odoubleacute" : 0x150,
    "Rcaron" : 0x158,
    "Uring" : 0x16e,
    "Udoubleacute" : 0x170,
    "Tcedilla" : 0x162,
    "racute" : 0x155,
    "abreve" : 0x103,
    "lacute" : 0x13a,
    "cacute" : 0x107,
    "ccaron" : 0x10d,
    "eogonek" : 0x119,
    "ecaron" : 0x11b,
    "dcaron" : 0x10f,
    "dstroke" : 0x111,
    "nacute" : 0x144,
    "ncaron" : 0x148,
    "odoubleacute" : 0x151,
    "rcaron" : 0x159,
    "uring" : 0x16f,
    "udoubleacute" : 0x171,
    "tcedilla" : 0x163,
    "abovedot" : 0x2d9,
    "Hstroke" : 0x126,
    "Hcircumflex" : 0x124,
    "Iabovedot" : 0x130,
    "Gbreve" : 0x11e,
    "Jcircumflex" : 0x134,
    "hstroke" : 0x127,
    "hcircumflex" : 0x125,
    "idotless" : 0x131,
    "gbreve" : 0x11f,
    "jcircumflex" : 0x135,
    "Cabovedot" : 0x10a,
    "Ccircumflex" : 0x108,
    "Gabovedot" : 0x120,
    "Gcircumflex" : 0x11c,
    "Ubreve" : 0x16c,
    "Scircumflex" : 0x15c,
    "cabovedot" : 0x10b,
    "ccircumflex" : 0x109,
    "gabovedot" : 0x121,
    "gcircumflex" : 0x11d,
    "ubreve" : 0x16d,
    "scircumflex" : 0x15d,
    "kappa" : 0x138,
    "kra" : 0x138,
    "Rcedilla" : 0x156,
    "Itilde" : 0x128,
    "Lcedilla" : 0x13b,
    "Emacron" : 0x112,
    "Gcedilla" : 0x122,
    "Tslash" : 0x166,
    "rcedilla" : 0x157,
    "itilde" : 0x129,
    "lcedilla" : 0x13c,
    "emacron" : 0x113,
    "gcedilla" : 0x123,
    "tslash" : 0x167,
    "ENG" : 0x14a,
    "eng" : 0x14b,
    "Amacron" : 0x100,
    "Iogonek" : 0x12e,
    "Eabovedot" : 0x116,
    "Imacron" : 0x12a,
    "Ncedilla" : 0x145,
    "Omacron" : 0x14c,
    "Kcedilla" : 0x136,
    "Uogonek" : 0x172,
    "Utilde" : 0x168,
    "Umacron" : 0x16a,
    "amacron" : 0x101,
    "iogonek" : 0x12f,
    "eabovedot" : 0x117,
    "imacron" : 0x12b,
    "ncedilla" : 0x146,
    "omacron" : 0x14d,
    "kcedilla" : 0x137,
    "uogonek" : 0x173,
    "utilde" : 0x169,
    "umacron" : 0x16b,
    "overline" : 0x203e,
    "kana_fullstop" : 0x3002,
    "kana_openingbracket" : 0x300c,
    "kana_closingbracket" : 0x300d,
    "kana_comma" : 0x3001,
    "kana_conjunctive" : 0x30fb,
    "kana_middledot" : 0x30fb,
    "kana_WO" : 0x30f2,
    "kana_a" : 0x30a1,
    "kana_i" : 0x30a3,
    "kana_u" : 0x30a5,
    "kana_e" : 0x30a7,
    "kana_o" : 0x30a9,
    "kana_ya" : 0x30e3,
    "kana_yu" : 0x30e5,
    "kana_yo" : 0x30e7,
    "kana_tsu" : 0x30c3,
    "kana_tu" : 0x30c3,
    "prolongedsound" : 0x30fc,
    "kana_A" : 0x30a2,
    "kana_I" : 0x30a4,
    "kana_U" : 0x30a6,
    "kana_E" : 0x30a8,
    "kana_O" : 0x30aa,
    "kana_KA" : 0x30ab,
    "kana_KI" : 0x30ad,
    "kana_KU" : 0x30af,
    "kana_KE" : 0x30b1,
    "kana_KO" : 0x30b3,
    "kana_SA" : 0x30b5,
    "kana_SHI" : 0x30b7,
    "kana_SU" : 0x30b9,
    "kana_SE" : 0x30bb,
    "kana_SO" : 0x30bd,
    "kana_TA" : 0x30bf,
    "kana_CHI" : 0x30c1,
    "kana_TI" : 0x30c1,
    "kana_TSU" : 0x30c4,
    "kana_TU" : 0x30c4,
    "kana_TE" : 0x30c6,
    "kana_TO" : 0x30c8,
    "kana_NA" : 0x30ca,
    "kana_NI" : 0x30cb,
    "kana_NU" : 0x30cc,
    "kana_NE" : 0x30cd,
    "kana_NO" : 0x30ce,
    "kana_HA" : 0x30cf,
    "kana_HI" : 0x30d2,
    "kana_FU" : 0x30d5,
    "kana_HU" : 0x30d5,
    "kana_HE" : 0x30d8,
    "kana_HO" : 0x30db,
    "kana_MA" : 0x30de,
    "kana_MI" : 0x30df,
    "kana_MU" : 0x30e0,
    "kana_ME" : 0x30e1,
    "kana_MO" : 0x30e2,
    "kana_YA" : 0x30e4,
    "kana_YU" : 0x30e6,
    "kana_YO" : 0x30e8,
    "kana_RA" : 0x30e9,
    "kana_RI" : 0x30ea,
    "kana_RU" : 0x30eb,
    "kana_RE" : 0x30ec,
    "kana_RO" : 0x30ed,
    "kana_WA" : 0x30ef,
    "kana_N" : 0x30f3,
    "voicedsound" : 0x309b,
    "semivoicedsound" : 0x309c,
    "Arabic_comma" : 0x60c,
    "Arabic_semicolon" : 0x61b,
    "Arabic_question_mark" : 0x61f,
    "Arabic_hamza" : 0x621,
    "Arabic_maddaonalef" : 0x622,
    "Arabic_hamzaonalef" : 0x623,
    "Arabic_hamzaonwaw" : 0x624,
    "Arabic_hamzaunderalef" : 0x625,
    "Arabic_hamzaonyeh" : 0x626,
    "Arabic_alef" : 0x627,
    "Arabic_beh" : 0x628,
    "Arabic_tehmarbuta" : 0x629,
    "Arabic_teh" : 0x62a,
    "Arabic_theh" : 0x62b,
    "Arabic_jeem" : 0x62c,
    "Arabic_hah" : 0x62d,
    "Arabic_khah" : 0x62e,
    "Arabic_dal" : 0x62f,
    "Arabic_thal" : 0x630,
    "Arabic_ra" : 0x631,
    "Arabic_zain" : 0x632,
    "Arabic_seen" : 0x633,
    "Arabic_sheen" : 0x634,
    "Arabic_sad" : 0x635,
    "Arabic_dad" : 0x636,
    "Arabic_tah" : 0x637,
    "Arabic_zah" : 0x638,
    "Arabic_ain" : 0x639,
    "Arabic_ghain" : 0x63a,
    "Arabic_tatweel" : 0x640,
    "Arabic_feh" : 0x641,
    "Arabic_qaf" : 0x642,
    "Arabic_kaf" : 0x643,
    "Arabic_lam" : 0x644,
    "Arabic_meem" : 0x645,
    "Arabic_noon" : 0x646,
    "Arabic_ha" : 0x647,
    "Arabic_heh" : 0x647,
    "Arabic_waw" : 0x648,
    "Arabic_alefmaksura" : 0x649,
    "Arabic_yeh" : 0x64a,
    "Arabic_fathatan" : 0x64b,
    "Arabic_dammatan" : 0x64c,
    "Arabic_kasratan" : 0x64d,
    "Arabic_fatha" : 0x64e,
    "Arabic_damma" : 0x64f,
    "Arabic_kasra" : 0x650,
    "Arabic_shadda" : 0x651,
    "Arabic_sukun" : 0x652,
    "Serbian_dje" : 0x452,
    "Macedonia_gje" : 0x453,
    "Cyrillic_io" : 0x451,
    "Ukrainian_ie" : 0x454,
    "Ukranian_je" : 0x454,
    "Macedonia_dse" : 0x455,
    "Ukrainian_i" : 0x456,
    "Ukranian_i" : 0x456,
    "Ukrainian_yi" : 0x457,
    "Ukranian_yi" : 0x457,
    "Cyrillic_je" : 0x458,
    "Serbian_je" : 0x458,
    "Cyrillic_lje" : 0x459,
    "Serbian_lje" : 0x459,
    "Cyrillic_nje" : 0x45a,
    "Serbian_nje" : 0x45a,
    "Serbian_tshe" : 0x45b,
    "Macedonia_kje" : 0x45c,
    "Byelorussian_shortu" : 0x45e,
    "Cyrillic_dzhe" : 0x45f,
    "Serbian_dze" : 0x45f,
    "numerosign" : 0x2116,
    "Serbian_DJE" : 0x402,
    "Macedonia_GJE" : 0x403,
    "Cyrillic_IO" : 0x401,
    "Ukrainian_IE" : 0x404,
    "Ukranian_JE" : 0x404,
    "Macedonia_DSE" : 0x405,
    "Ukrainian_I" : 0x406,
    "Ukranian_I" : 0x406,
    "Ukrainian_YI" : 0x407,
    "Ukranian_YI" : 0x407,
    "Ukrainian_ghe_with_upturn" : 0x491,
    "Ukrainian_GHE_WITH_UPTURN" : 0x490,
    "Cyrillic_JE" : 0x408,
    "Serbian_JE" : 0x408,
    "Cyrillic_LJE" : 0x409,
    "Serbian_LJE" : 0x409,
    "Cyrillic_NJE" : 0x40a,
    "Serbian_NJE" : 0x40a,
    "Serbian_TSHE" : 0x40b,
    "Macedonia_KJE" : 0x40c,
    "Byelorussian_SHORTU" : 0x40e,
    "Cyrillic_DZHE" : 0x40f,
    "Serbian_DZE" : 0x40f,
    "Cyrillic_yu" : 0x44e,
    "Cyrillic_a" : 0x430,
    "Cyrillic_be" : 0x431,
    "Cyrillic_tse" : 0x446,
    "Cyrillic_de" : 0x434,
    "Cyrillic_ie" : 0x435,
    "Cyrillic_ef" : 0x444,
    "Cyrillic_ghe" : 0x433,
    "Cyrillic_ha" : 0x445,
    "Cyrillic_i" : 0x438,
    "Cyrillic_shorti" : 0x439,
    "Cyrillic_ka" : 0x43a,
    "Cyrillic_el" : 0x43b,
    "Cyrillic_em" : 0x43c,
    "Cyrillic_en" : 0x43d,
    "Cyrillic_o" : 0x43e,
    "Cyrillic_pe" : 0x43f,
    "Cyrillic_ya" : 0x44f,
    "Cyrillic_er" : 0x440,
    "Cyrillic_es" : 0x441,
    "Cyrillic_te" : 0x442,
    "Cyrillic_u" : 0x443,
    "Cyrillic_zhe" : 0x436,
    "Cyrillic_ve" : 0x432,
    "Cyrillic_softsign" : 0x44c,
    "Cyrillic_yeru" : 0x44b,
    "Cyrillic_ze" : 0x437,
    "Cyrillic_sha" : 0x448,
    "Cyrillic_e" : 0x44d,
    "Cyrillic_shcha" : 0x449,
    "Cyrillic_che" : 0x447,
    "Cyrillic_hardsign" : 0x44a,
    "Cyrillic_YU" : 0x42e,
    "Cyrillic_A" : 0x410,
    "Cyrillic_BE" : 0x411,
    "Cyrillic_TSE" : 0x426,
    "Cyrillic_DE" : 0x414,
    "Cyrillic_IE" : 0x415,
    "Cyrillic_EF" : 0x424,
    "Cyrillic_GHE" : 0x413,
    "Cyrillic_HA" : 0x425,
    "Cyrillic_I" : 0x418,
    "Cyrillic_SHORTI" : 0x419,
    "Cyrillic_KA" : 0x41a,
    "Cyrillic_EL" : 0x41b,
    "Cyrillic_EM" : 0x41c,
    "Cyrillic_EN" : 0x41d,
    "Cyrillic_O" : 0x41e,
    "Cyrillic_PE" : 0x41f,
    "Cyrillic_YA" : 0x42f,
    "Cyrillic_ER" : 0x420,
    "Cyrillic_ES" : 0x421,
    "Cyrillic_TE" : 0x422,
    "Cyrillic_U" : 0x423,
    "Cyrillic_ZHE" : 0x416,
    "Cyrillic_VE" : 0x412,
    "Cyrillic_SOFTSIGN" : 0x42c,
    "Cyrillic_YERU" : 0x42b,
    "Cyrillic_ZE" : 0x417,
    "Cyrillic_SHA" : 0x428,
    "Cyrillic_E" : 0x42d,
    "Cyrillic_SHCHA" : 0x429,
    "Cyrillic_CHE" : 0x427,
    "Cyrillic_HARDSIGN" : 0x42a,
    "Cyrillic_schwa" : 0x4d9,
    "Cyrillic_SCHWA" : 0x4d8,
    "Cyrillic_en_descender" : 0x4a3,
    "Cyrillic_EN_descender" : 0x4a2,
    "Cyrillic_ghe_bar" : 0x493,
    "Cyrillic_GHE_bar" : 0x492,
    "Cyrillic_u_straight" : 0x4af,
    "Cyrillic_U_straight" : 0x4ae,
    "Cyrillic_u_straight_bar" : 0x4b1,
    "Cyrillic_U_straight_bar" : 0x4b0,
    "Cyrillic_ka_descender" : 0x49b,
    "Cyrillic_KA_descender" : 0x49a,
    "Cyrillic_o_bar" : 0x4e9,
    "Cyrillic_O_bar" : 0x4e8,
    "Cyrillic_shha" : 0x4bb,
    "Cyrillic_SHHA" : 0x4ba,
    "Greek_ALPHAaccent" : 0x386,
    "Greek_EPSILONaccent" : 0x388,
    "Greek_ETAaccent" : 0x389,
    "Greek_IOTAaccent" : 0x38a,
    "Greek_IOTAdieresis" : 0x3aa,
    "Greek_IOTAdiaeresis" : 0x3aa,
    "Greek_OMICRONaccent" : 0x38c,
    "Greek_UPSILONaccent" : 0x38e,
    "Greek_UPSILONdieresis" : 0x3ab,
    "Greek_OMEGAaccent" : 0x38f,
    "Greek_accentdieresis" : 0x385,
    "Greek_horizbar" : 0x2015,
    "Greek_alphaaccent" : 0x3ac,
    "Greek_epsilonaccent" : 0x3ad,
    "Greek_etaaccent" : 0x3ae,
    "Greek_iotaaccent" : 0x3af,
    "Greek_iotadieresis" : 0x3ca,
    "Greek_iotaaccentdieresis" : 0x390,
    "Greek_omicronaccent" : 0x3cc,
    "Greek_upsilonaccent" : 0x3cd,
    "Greek_upsilondieresis" : 0x3cb,
    "Greek_upsilonaccentdieresis" : 0x3b0,
    "Greek_omegaaccent" : 0x3ce,
    "Greek_ALPHA" : 0x391,
    "Greek_BETA" : 0x392,
    "Greek_GAMMA" : 0x393,
    "Greek_DELTA" : 0x394,
    "Greek_EPSILON" : 0x395,
    "Greek_ZETA" : 0x396,
    "Greek_ETA" : 0x397,
    "Greek_THETA" : 0x398,
    "Greek_IOTA" : 0x399,
    "Greek_KAPPA" : 0x39a,
    "Greek_LAMBDA" : 0x39b,
    "Greek_LAMDA" : 0x39b,
    "Greek_MU" : 0x39c,
    "Greek_NU" : 0x39d,
    "Greek_XI" : 0x39e,
    "Greek_OMICRON" : 0x39f,
    "Greek_PI" : 0x3a0,
    "Greek_RHO" : 0x3a1,
    "Greek_SIGMA" : 0x3a3,
    "Greek_TAU" : 0x3a4,
    "Greek_UPSILON" : 0x3a5,
    "Greek_PHI" : 0x3a6,
    "Greek_CHI" : 0x3a7,
    "Greek_PSI" : 0x3a8,
    "Greek_OMEGA" : 0x3a9,
    "Greek_alpha" : 0x3b1,
    "Greek_beta" : 0x3b2,
    "Greek_gamma" : 0x3b3,
    "Greek_delta" : 0x3b4,
    "Greek_epsilon" : 0x3b5,
    "Greek_zeta" : 0x3b6,
    "Greek_eta" : 0x3b7,
    "Greek_theta" : 0x3b8,
    "Greek_iota" : 0x3b9,
    "Greek_kappa" : 0x3ba,
    "Greek_lambda" : 0x3bb,
    "Greek_lamda" : 0x3bb,
    "Greek_mu" : 0x3bc,
    "Greek_nu" : 0x3bd,
    "Greek_xi" : 0x3be,
    "Greek_omicron" : 0x3bf,
    "Greek_pi" : 0x3c0,
    "Greek_rho" : 0x3c1,
    "Greek_sigma" : 0x3c3,
    "Greek_finalsmallsigma" : 0x3c2,
    "Greek_tau" : 0x3c4,
    "Greek_upsilon" : 0x3c5,
    "Greek_phi" : 0x3c6,
    "Greek_chi" : 0x3c7,
    "Greek_psi" : 0x3c8,
    "Greek_omega" : 0x3c9,
    "leftradical" : 0x23b7,
    "topleftradical" : 0x250c,
    "horizconnector" : 0x2500,
    "topintegral" : 0x2320,
    "botintegral" : 0x2321,
    "vertconnector" : 0x2502,
    "topleftsqbracket" : 0x23a1,
    "botleftsqbracket" : 0x23a3,
    "toprightsqbracket" : 0x23a4,
    "botrightsqbracket" : 0x23a6,
    "topleftparens" : 0x239b,
    "botleftparens" : 0x239d,
    "toprightparens" : 0x239e,
    "botrightparens" : 0x23a0,
    "leftmiddlecurlybrace" : 0x23a8,
    "rightmiddlecurlybrace" : 0x23ac,
    "lessthanequal" : 0x2264,
    "notequal" : 0x2260,
    "greaterthanequal" : 0x2265,
    "integral" : 0x222b,
    "therefore" : 0x2234,
    "variation" : 0x221d,
    "infinity" : 0x221e,
    "nabla" : 0x2207,
    "approximate" : 0x223c,
    "similarequal" : 0x2243,
    "ifonlyif" : 0x21d4,
    "implies" : 0x21d2,
    "identical" : 0x2261,
    "radical" : 0x221a,
    "includedin" : 0x2282,
    "includes" : 0x2283,
    "intersection" : 0x2229,
    "union" : 0x222a,
    "logicaland" : 0x2227,
    "logicalor" : 0x2228,
    "partialderivative" : 0x2202,
    "function" : 0x192,
    "leftarrow" : 0x2190,
    "uparrow" : 0x2191,
    "rightarrow" : 0x2192,
    "downarrow" : 0x2193,
    "soliddiamond" : 0x25c6,
    "checkerboard" : 0x2592,
    "ht" : 0x2409,
    "ff" : 0x240c,
    "cr" : 0x240d,
    "lf" : 0x240a,
    "nl" : 0x2424,
    "vt" : 0x240b,
    "lowrightcorner" : 0x2518,
    "uprightcorner" : 0x2510,
    "upleftcorner" : 0x250c,
    "lowleftcorner" : 0x2514,
    "crossinglines" : 0x253c,
    "horizlinescan1" : 0x23ba,
    "horizlinescan3" : 0x23bb,
    "horizlinescan5" : 0x2500,
    "horizlinescan7" : 0x23bc,
    "horizlinescan9" : 0x23bd,
    "leftt" : 0x251c,
    "rightt" : 0x2524,
    "bott" : 0x2534,
    "topt" : 0x252c,
    "vertbar" : 0x2502,
    "emspace" : 0x2003,
    "enspace" : 0x2002,
    "em3space" : 0x2004,
    "em4space" : 0x2005,
    "digitspace" : 0x2007,
    "punctspace" : 0x2008,
    "thinspace" : 0x2009,
    "hairspace" : 0x200a,
    "emdash" : 0x2014,
    "endash" : 0x2013,
    "ellipsis" : 0x2026,
    "doubbaselinedot" : 0x2025,
    "onethird" : 0x2153,
    "twothirds" : 0x2154,
    "onefifth" : 0x2155,
    "twofifths" : 0x2156,
    "threefifths" : 0x2157,
    "fourfifths" : 0x2158,
    "onesixth" : 0x2159,
    "fivesixths" : 0x215a,
    "careof" : 0x2105,
    "figdash" : 0x2012,
    "leftanglebracket" : 0x2329,
    "rightanglebracket" : 0x232a,
    "oneeighth" : 0x215b,
    "threeeighths" : 0x215c,
    "fiveeighths" : 0x215d,
    "seveneighths" : 0x215e,
    "trademark" : 0x2122,
    "signaturemark" : 0x2613,
    "leftopentriangle" : 0x25c1,
    "rightopentriangle" : 0x25b7,
    "emopencircle" : 0x25cb,
    "emopenrectangle" : 0x25af,
    "leftsinglequotemark" : 0x2018,
    "rightsinglequotemark" : 0x2019,
    "leftdoublequotemark" : 0x201c,
    "rightdoublequotemark" : 0x201d,
    "prescription" : 0x211e,
    "minutes" : 0x2032,
    "seconds" : 0x2033,
    "latincross" : 0x271d,
    "filledrectbullet" : 0x25ac,
    "filledlefttribullet" : 0x25c0,
    "filledrighttribullet" : 0x25b6,
    "emfilledcircle" : 0x25cf,
    "emfilledrect" : 0x25ae,
    "enopencircbullet" : 0x25e6,
    "enopensquarebullet" : 0x25ab,
    "openrectbullet" : 0x25ad,
    "opentribulletup" : 0x25b3,
    "opentribulletdown" : 0x25bd,
    "openstar" : 0x2606,
    "enfilledcircbullet" : 0x2022,
    "enfilledsqbullet" : 0x25aa,
    "filledtribulletup" : 0x25b2,
    "filledtribulletdown" : 0x25bc,
    "leftpointer" : 0x261c,
    "rightpointer" : 0x261e,
    "club" : 0x2663,
    "diamond" : 0x2666,
    "heart" : 0x2665,
    "maltesecross" : 0x2720,
    "dagger" : 0x2020,
    "doubledagger" : 0x2021,
    "checkmark" : 0x2713,
    "ballotcross" : 0x2717,
    "musicalsharp" : 0x266f,
    "musicalflat" : 0x266d,
    "malesymbol" : 0x2642,
    "femalesymbol" : 0x2640,
    "telephone" : 0x260e,
    "telephonerecorder" : 0x2315,
    "phonographcopyright" : 0x2117,
    "caret" : 0x2038,
    "singlelowquotemark" : 0x201a,
    "doublelowquotemark" : 0x201e,
    "leftcaret" : 0x3c,
    "rightcaret" : 0x3e,
    "downcaret" : 0x2228,
    "upcaret" : 0x2227,
    "overbar" : 0xaf,
    "downtack" : 0x22a5,
    "upshoe" : 0x2229,
    "downstile" : 0x230a,
    "underbar" : 0x5f,
    "jot" : 0x2218,
    "quad" : 0x2395,
    "uptack" : 0x22a4,
    "circle" : 0x25cb,
    "upstile" : 0x2308,
    "downshoe" : 0x222a,
    "rightshoe" : 0x2283,
    "leftshoe" : 0x2282,
    "lefttack" : 0x22a2,
    "righttack" : 0x22a3,
    "hebrew_doublelowline" : 0x2017,
    "hebrew_aleph" : 0x5d0,
    "hebrew_bet" : 0x5d1,
    "hebrew_beth" : 0x5d1,
    "hebrew_gimel" : 0x5d2,
    "hebrew_gimmel" : 0x5d2,
    "hebrew_dalet" : 0x5d3,
    "hebrew_daleth" : 0x5d3,
    "hebrew_he" : 0x5d4,
    "hebrew_waw" : 0x5d5,
    "hebrew_zain" : 0x5d6,
    "hebrew_zayin" : 0x5d6,
    "hebrew_chet" : 0x5d7,
    "hebrew_het" : 0x5d7,
    "hebrew_tet" : 0x5d8,
    "hebrew_teth" : 0x5d8,
    "hebrew_yod" : 0x5d9,
    "hebrew_finalkaph" : 0x5da,
    "hebrew_kaph" : 0x5db,
    "hebrew_lamed" : 0x5dc,
    "hebrew_finalmem" : 0x5dd,
    "hebrew_mem" : 0x5de,
    "hebrew_finalnun" : 0x5df,
    "hebrew_nun" : 0x5e0,
    "hebrew_samech" : 0x5e1,
    "hebrew_samekh" : 0x5e1,
    "hebrew_ayin" : 0x5e2,
    "hebrew_finalpe" : 0x5e3,
    "hebrew_pe" : 0x5e4,
    "hebrew_finalzade" : 0x5e5,
    "hebrew_finalzadi" : 0x5e5,
    "hebrew_zade" : 0x5e6,
    "hebrew_zadi" : 0x5e6,
    "hebrew_kuf" : 0x5e7,
    "hebrew_qoph" : 0x5e7,
    "hebrew_resh" : 0x5e8,
    "hebrew_shin" : 0x5e9,
    "hebrew_taf" : 0x5ea,
    "hebrew_taw" : 0x5ea,
    "Thai_kokai" : 0xe01,
    "Thai_khokhai" : 0xe02,
    "Thai_khokhuat" : 0xe03,
    "Thai_khokhwai" : 0xe04,
    "Thai_khokhon" : 0xe05,
    "Thai_khorakhang" : 0xe06,
    "Thai_ngongu" : 0xe07,
    "Thai_chochan" : 0xe08,
    "Thai_choching" : 0xe09,
    "Thai_chochang" : 0xe0a,
    "Thai_soso" : 0xe0b,
    "Thai_chochoe" : 0xe0c,
    "Thai_yoying" : 0xe0d,
    "Thai_dochada" : 0xe0e,
    "Thai_topatak" : 0xe0f,
    "Thai_thothan" : 0xe10,
    "Thai_thonangmontho" : 0xe11,
    "Thai_thophuthao" : 0xe12,
    "Thai_nonen" : 0xe13,
    "Thai_dodek" : 0xe14,
    "Thai_totao" : 0xe15,
    "Thai_thothung" : 0xe16,
    "Thai_thothahan" : 0xe17,
    "Thai_thothong" : 0xe18,
    "Thai_nonu" : 0xe19,
    "Thai_bobaimai" : 0xe1a,
    "Thai_popla" : 0xe1b,
    "Thai_phophung" : 0xe1c,
    "Thai_fofa" : 0xe1d,
    "Thai_phophan" : 0xe1e,
    "Thai_fofan" : 0xe1f,
    "Thai_phosamphao" : 0xe20,
    "Thai_moma" : 0xe21,
    "Thai_yoyak" : 0xe22,
    "Thai_rorua" : 0xe23,
    "Thai_ru" : 0xe24,
    "Thai_loling" : 0xe25,
    "Thai_lu" : 0xe26,
    "Thai_wowaen" : 0xe27,
    "Thai_sosala" : 0xe28,
    "Thai_sorusi" : 0xe29,
    "Thai_sosua" : 0xe2a,
    "Thai_hohip" : 0xe2b,
    "Thai_lochula" : 0xe2c,
    "Thai_oang" : 0xe2d,
    "Thai_honokhuk" : 0xe2e,
    "Thai_paiyannoi" : 0xe2f,
    "Thai_saraa" : 0xe30,
    "Thai_maihanakat" : 0xe31,
    "Thai_saraaa" : 0xe32,
    "Thai_saraam" : 0xe33,
    "Thai_sarai" : 0xe34,
    "Thai_saraii" : 0xe35,
    "Thai_saraue" : 0xe36,
    "Thai_sarauee" : 0xe37,
    "Thai_sarau" : 0xe38,
    "Thai_sarauu" : 0xe39,
    "Thai_phinthu" : 0xe3a,
    "Thai_maihanakat_maitho" : 0xdde,
    "Thai_baht" : 0xe3f,
    "Thai_sarae" : 0xe40,
    "Thai_saraae" : 0xe41,
    "Thai_sarao" : 0xe42,
    "Thai_saraaimaimuan" : 0xe43,
    "Thai_saraaimaimalai" : 0xe44,
    "Thai_lakkhangyao" : 0xe45,
    "Thai_maiyamok" : 0xe46,
    "Thai_maitaikhu" : 0xe47,
    "Thai_maiek" : 0xe48,
    "Thai_maitho" : 0xe49,
    "Thai_maitri" : 0xe4a,
    "Thai_maichattawa" : 0xe4b,
    "Thai_thanthakhat" : 0xe4c,
    "Thai_nikhahit" : 0xe4d,
    "Thai_leksun" : 0xe50,
    "Thai_leknung" : 0xe51,
    "Thai_leksong" : 0xe52,
    "Thai_leksam" : 0xe53,
    "Thai_leksi" : 0xe54,
    "Thai_lekha" : 0xe55,
    "Thai_lekhok" : 0xe56,
    "Thai_lekchet" : 0xe57,
    "Thai_lekpaet" : 0xe58,
    "Thai_lekkao" : 0xe59,
    "Hangul_Kiyeog" : 0x3131,
    "Hangul_SsangKiyeog" : 0x3132,
    "Hangul_KiyeogSios" : 0x3133,
    "Hangul_Nieun" : 0x3134,
    "Hangul_NieunJieuj" : 0x3135,
    "Hangul_NieunHieuh" : 0x3136,
    "Hangul_Dikeud" : 0x3137,
    "Hangul_SsangDikeud" : 0x3138,
    "Hangul_Rieul" : 0x3139,
    "Hangul_RieulKiyeog" : 0x313a,
    "Hangul_RieulMieum" : 0x313b,
    "Hangul_RieulPieub" : 0x313c,
    "Hangul_RieulSios" : 0x313d,
    "Hangul_RieulTieut" : 0x313e,
    "Hangul_RieulPhieuf" : 0x313f,
    "Hangul_RieulHieuh" : 0x3140,
    "Hangul_Mieum" : 0x3141,
    "Hangul_Pieub" : 0x3142,
    "Hangul_SsangPieub" : 0x3143,
    "Hangul_PieubSios" : 0x3144,
    "Hangul_Sios" : 0x3145,
    "Hangul_SsangSios" : 0x3146,
    "Hangul_Ieung" : 0x3147,
    "Hangul_Jieuj" : 0x3148,
    "Hangul_SsangJieuj" : 0x3149,
    "Hangul_Cieuc" : 0x314a,
    "Hangul_Khieuq" : 0x314b,
    "Hangul_Tieut" : 0x314c,
    "Hangul_Phieuf" : 0x314d,
    "Hangul_Hieuh" : 0x314e,
    "Hangul_A" : 0x314f,
    "Hangul_AE" : 0x3150,
    "Hangul_YA" : 0x3151,
    "Hangul_YAE" : 0x3152,
    "Hangul_EO" : 0x3153,
    "Hangul_E" : 0x3154,
    "Hangul_YEO" : 0x3155,
    "Hangul_YE" : 0x3156,
    "Hangul_O" : 0x3157,
    "Hangul_WA" : 0x3158,
    "Hangul_WAE" : 0x3159,
    "Hangul_OE" : 0x315a,
    "Hangul_YO" : 0x315b,
    "Hangul_U" : 0x315c,
    "Hangul_WEO" : 0x315d,
    "Hangul_WE" : 0x315e,
    "Hangul_WI" : 0x315f,
    "Hangul_YU" : 0x3160,
    "Hangul_EU" : 0x3161,
    "Hangul_YI" : 0x3162,
    "Hangul_I" : 0x3163,
    "Hangul_J_Kiyeog" : 0x11a8,
    "Hangul_J_SsangKiyeog" : 0x11a9,
    "Hangul_J_KiyeogSios" : 0x11aa,
    "Hangul_J_Nieun" : 0x11ab,
    "Hangul_J_NieunJieuj" : 0x11ac,
    "Hangul_J_NieunHieuh" : 0x11ad,
    "Hangul_J_Dikeud" : 0x11ae,
    "Hangul_J_Rieul" : 0x11af,
    "Hangul_J_RieulKiyeog" : 0x11b0,
    "Hangul_J_RieulMieum" : 0x11b1,
    "Hangul_J_RieulPieub" : 0x11b2,
    "Hangul_J_RieulSios" : 0x11b3,
    "Hangul_J_RieulTieut" : 0x11b4,
    "Hangul_J_RieulPhieuf" : 0x11b5,
    "Hangul_J_RieulHieuh" : 0x11b6,
    "Hangul_J_Mieum" : 0x11b7,
    "Hangul_J_Pieub" : 0x11b8,
    "Hangul_J_PieubSios" : 0x11b9,
    "Hangul_J_Sios" : 0x11ba,
    "Hangul_J_SsangSios" : 0x11bb,
    "Hangul_J_Ieung" : 0x11bc,
    "Hangul_J_Jieuj" : 0x11bd,
    "Hangul_J_Cieuc" : 0x11be,
    "Hangul_J_Khieuq" : 0x11bf,
    "Hangul_J_Tieut" : 0x11c0,
    "Hangul_J_Phieuf" : 0x11c1,
    "Hangul_J_Hieuh" : 0x11c2,
    "Hangul_RieulYeorinHieuh" : 0x316d,
    "Hangul_SunkyeongeumMieum" : 0x3171,
    "Hangul_SunkyeongeumPieub" : 0x3178,
    "Hangul_PanSios" : 0x317f,
    "Hangul_KkogjiDalrinIeung" : 0x3181,
    "Hangul_SunkyeongeumPhieuf" : 0x3184,
    "Hangul_YeorinHieuh" : 0x3186,
    "Hangul_AraeA" : 0x318d,
    "Hangul_AraeAE" : 0x318e,
    "Hangul_J_PanSios" : 0x11eb,
    "Hangul_J_KkogjiDalrinIeung" : 0x11f0,
    "Hangul_J_YeorinHieuh" : 0x11f9,
    "Korean_Won" : 0x20a9,
    "OE" : 0x152,
    "oe" : 0x153,
    "Ydiaeresis" : 0x178,
    "EcuSign" : 0x20a0,
    "ColonSign" : 0x20a1,
    "CruzeiroSign" : 0x20a2,
    "FFrancSign" : 0x20a3,
    "LiraSign" : 0x20a4,
    "MillSign" : 0x20a5,
    "NairaSign" : 0x20a6,
    "PesetaSign" : 0x20a7,
    "RupeeSign" : 0x20a8,
    "WonSign" : 0x20a9,
    "NewSheqelSign" : 0x20aa,
    "DongSign" : 0x20ab,
    "EuroSign" : 0x20ac,
    "dead_grave" : 0x300,
    "dead_acute" : 0x301,
    "dead_acutee" : 0x301,
    "dead_circumflex" : 0x302,
    "dead_tilde" : 0x303,
    "dead_macron" : 0x304,
    "dead_breve" : 0x306,
    "dead_abovedot" : 0x307,
    "dead_diaeresis" : 0x308,
    "dead_abovering" : 0x30a,
    "dead_doubleacute" : 0x30b,
    "dead_caron" : 0x30c,
    "dead_cedilla" : 0x327,
    "dead_ogonek" : 0x328,
    "dead_iota" : 0x345,
    "dead_voiced_sound" : 0x30f,
    "dead_semivoiced_sound" : 0x30a,
    "dead_belowdot" : 0x323,
    "BackSpace" : 0x8,
    "Tab" : 0x9,
    "Linefeed" : 0xa,
    "Clear" : 0xb,
    "Return" : 0xd,
    "VoidSymbol" : 0x20
}

non_trans_list = [
     0xfe02, #  ISO_Level2_Latch
     0xfe03, #  ISO_Level3_Shift
     0xfe0a, #  ISO_Prev_Group
     0xfe0b, #  ISO_Prev_Group_Lock
     0xfd18, #  3270_Record
     0xfd19, #  3270_ChangeScreen
     0xfd1a, #  3270_DeleteWord
     0xfd1b, #  3270_ExSelect
     0xfd1c, #  3270_CursorSelect
     0xfd1d, #  3270_PrintScreen
     0xfd1e, #  3270_Enter
     0xfe01, #  ISO_Lock
     0xfe04, #  ISO_Level3_Latch
     0xfe05, #  ISO_Level3_Lock
     0xfe06, #  ISO_Group_Latch
     0xfe07, #  ISO_Group_Lock
     0xfe08, #  ISO_Next_Group
     0xfe09, #  ISO_Next_Group_Lock
     0xfe0c, #  ISO_First_Group
     0xfe0d, #  ISO_First_Group_Lock
     0xfe0e, #  ISO_Last_Group
     0xfe0f, #  ISO_Last_Group_Lock
     0xfe11, #  ISO_Level5_Shift
     0xfe12, #  ISO_Level5_Latch
     0xfe13, #  ISO_Level5_Lock
     0xfe20, #  ISO_Left_Tab
     0xfe21, #  ISO_Move_Line_Up
     0xfe22, #  ISO_Move_Line_Down
     0xfe23, #  ISO_Partial_Line_Up
     0xfe24, #  ISO_Partial_Line_Down
     0xfe25, #  ISO_Partial_Space_Left
     0xfe26, #  ISO_Partial_Space_Right
     0xfe27, #  ISO_Set_Margin_Left
     0xfe28, #  ISO_Set_Margin_Right
     0xfe29, #  ISO_Release_Margin_Left
     0xfe2a, #  ISO_Release_Margin_Right
     0xfe2b, #  ISO_Release_Both_Margins
     0xfe2c, #  ISO_Fast_Cursor_Left
     0xfe2d, #  ISO_Fast_Cursor_Right
     0xfe2e, #  ISO_Fast_Cursor_Up
     0xfe2f, #  ISO_Fast_Cursor_Down
     0xfe30, #  ISO_Continuous_Underline
     0xfe31, #  ISO_Discontinuous_Underline
     0xfe32, #  ISO_Emphasize
     0xfe33, #  ISO_Center_Object
     0xfe34, #  ISO_Enter
     0xfe70, #  AccessX_Enable
     0xfe71, #  AccessX_Feedback_Enable
     0xfe72, #  RepeatKeys_Enable
     0xfe73, #  SlowKeys_Enable
     0xfe74, #  BounceKeys_Enable
     0xfe75, #  StickyKeys_Enable
     0xfe76, #  MouseKeys_Enable
     0xfe77, #  MouseKeys_Accel_Enable
     0xfe78, #  Overlay1_Enable
     0xfe79, #  Overlay2_Enable
     0xfe7a, #  AudibleBell_Enable
     0xfed0, #  First_Virtual_Screen
     0xfed1, #  Prev_Virtual_Screen
     0xfed2, #  Next_Virtual_Screen
     0xfed4, #  Last_Virtual_Screen
     0xfed5, #  Terminate_Server
     0xfee0, #  Pointer_Left
     0xfee1, #  Pointer_Right
     0xfee2, #  Pointer_Up
     0xfee3, #  Pointer_Down
     0xfee4, #  Pointer_UpLeft
     0xfee5, #  Pointer_UpRight
     0xfee6, #  Pointer_DownLeft
     0xfee7, #  Pointer_DownRight
     0xfee8, #  Pointer_Button_Dflt
     0xfee9, #  Pointer_Button1
     0xfeea, #  Pointer_Button2
     0xfeeb, #  Pointer_Button3
     0xfeec, #  Pointer_Button4
     0xfeed, #  Pointer_Button5
     0xfeee, #  Pointer_DblClick_Dflt
     0xfeef, #  Pointer_DblClick1
     0xfef0, #  Pointer_DblClick2
     0xfef1, #  Pointer_DblClick3
     0xfef4, #  Pointer_Drag_Dflt
     0xfef5, #  Pointer_Drag1
     0xfef6, #  Pointer_Drag2
     0xfef7, #  Pointer_Drag3
     0xfef8, #  Pointer_Drag4
     0xfef9, #  Pointer_EnableKeys
     0xfefa, #  Pointer_Accelerate
     0xfefb, #  Pointer_DfltBtnNext
     0xfefc, #  Pointer_DfltBtnPrev
     0xfefd, #  Pointer_Drag5
     0xff08, #  BackSpace
     0xff09, #  Tab
     0xff0a, #  Linefeed
     0xff0b, #  Clear
     0xff0d, #  Return
     0xff13, #  Pause
     0xff14, #  Scroll_Lock
     0xff15, #  Sys_Req
     0xff1b, #  Escape
     0xff20, #  Multi_key
     0xff21, #  Kanji
     0xff22, #  Muhenkan
     0xff23, #  Henkan
     0xff24, #  Romaji
     0xff25, #  Hiragana
     0xff26, #  Katakana
     0xff27, #  Hiragana_Katakana
     0xff28, #  Zenkaku
     0xff29, #  Hankaku
     0xff2a, #  Zenkaku_Hankaku
     0xff2b, #  Touroku
     0xff2c, #  Massyo
     0xff2d, #  Kana_Lock
     0xff2e, #  Kana_Shift
     0xff2f, #  Eisu_Shift
     0xff30, #  Eisu_toggle
     0xff31, #  Hangul
     0xff32, #  Hangul_Start
     0xff33, #  Hangul_End
     0xff34, #  Hangul_Hanja
     0xff35, #  Hangul_Jamo
     0xff36, #  Hangul_Romaja
     0xff37, #  Hangul_Codeinput
     0xff38, #  Hangul_Jeonja
     0xff39, #  Hangul_Banja
     0xff3a, #  Hangul_PreHanja
     0xff3b, #  Hangul_PostHanja
     0xff3c, #  Hangul_SingleCandidate
     0xff3d, #  Hangul_MultipleCandidate
     0xff3e, #  Hangul_PreviousCandidate
     0xff3f, #  Hangul_Special
     0xff50, #  Home
     0xff51, #  Left
     0xff52, #  Up
     0xff53, #  Right
     0xff54, #  Down
     0xff55, #  Page_Up
     0xff56, #  Page_Down
     0xff57, #  End
     0xff58, #  Begin
     0xff60, #  Select
     0xff61, #  Print
     0xff62, #  Execute
     0xff63, #  Insert
     0xff65, #  Undo
     0xff66, #  Redo
     0xff67, #  Menu
     0xff68, #  Find
     0xff69, #  Cancel
     0xff6a, #  Help
     0xff6b, #  Break
     0xff7e, #  Hangul_switch
     0xff7f, #  Num_Lock
     0xff80, #  KP_Space
     0xff89, #  KP_Tab
     0xff8d, #  KP_Enter
     0xff91, #  KP_F1
     0xff92, #  KP_F2
     0xff93, #  KP_F3
     0xff94, #  KP_F4
     0xff95, #  KP_Home
     0xff96, #  KP_Left
     0xff97, #  KP_Up
     0xff98, #  KP_Right
     0xff99, #  KP_Down
     0xff9a, #  KP_Page_Up
     0xff9b, #  KP_Page_Down
     0xff9c, #  KP_End
     0xff9d, #  KP_Begin
     0xff9e, #  KP_Insert
     0xff9f, #  KP_Delete
     0xffaa, #  KP_Multiply
     0xffab, #  KP_Add
     0xffac, #  KP_Separator
     0xffad, #  KP_Subtract
     0xffae, #  KP_Decimal
     0xffaf, #  KP_Divide
     0xffb0, #  KP_0
     0xffb1, #  KP_1
     0xffb2, #  KP_2
     0xffb3, #  KP_3
     0xffb4, #  KP_4
     0xffb5, #  KP_5
     0xffb6, #  KP_6
     0xffb7, #  KP_7
     0xffb8, #  KP_8
     0xffb9, #  KP_9
     0xffbd, #  KP_Equal
     0xffbe, #  F1
     0xffbf, #  F2
     0xffc0, #  F3
     0xffc1, #  F4
     0xffc2, #  F5
     0xffc3, #  F6
     0xffc4, #  F7
     0xffc5, #  F8
     0xffc6, #  F9
     0xffc7, #  F10
     0xffc8, #  L1
     0xffc9, #  L2
     0xffca, #  L3
     0xffcb, #  L4
     0xffcc, #  L5
     0xffcd, #  L6
     0xffce, #  L7
     0xffcf, #  L8
     0xffd0, #  L9
     0xffd1, #  L10
     0xffd2, #  R1
     0xffd3, #  R2
     0xffd4, #  R3
     0xffd5, #  R4
     0xffd6, #  R5
     0xffd7, #  R6
     0xffd8, #  R7
     0xffd9, #  R8
     0xffda, #  R9
     0xffdb, #  R10
     0xffdc, #  R11
     0xffdd, #  R12
     0xffde, #  R13
     0xffdf, #  R14
     0xffe0, #  R15
     0xffe1, #  Shift_L
     0xffe2, #  Shift_R
     0xffe3, #  Control_L
     0xffe4, #  Control_R
     0xffe5, #  Caps_Lock
     0xffe6, #  Shift_Lock
     0xffe7, #  Meta_L
     0xffe8, #  Meta_R
     0xffe9, #  Alt_L
     0xffea, #  Alt_R
     0xffeb, #  Super_L
     0xffec, #  Super_R
     0xffed, #  Hyper_L
     0xffee, #  Hyper_R
     0xffffff, #  VoidSymbol
     0xffff, #  Delete
]

def non_trans_key(keyval):
    if keyval in non_trans_list:
        return True
    return False

# have this so that narrow build python can be used
def ucs4_to_utf8(ucs4):
    if ucs4 < 0x80:
        # 1 byte string
        return chr(ucs4 & 0x7f)
    elif ucs4 < 0x800:
        # 2 byte string        
        return chr(0xc0 | ((ucs4 >> 6) & 0x1f)) + \
               chr(0x80 | (ucs4 & 0x3f))
    elif ucs4 < 0x10000:
        # 3 byte string
        return chr(0xe0 | ((ucs4 >> 12) & 0xf)) + \
               chr(0x80 | ((ucs4 >> 6) & 0x3f)) + \
               chr(0x80 + (ucs4 & 0x3f))
    elif ucs4 < 0x200000:
        # 4 byte string
        return chr(0xf0 | ((ucs4 >> 18) & 0x7)) + \
               chr(0x80 | ((ucs4 >> 12) & 0x3f)) + \
               chr(0x80 | ((ucs4 >> 6) & 0x3f)) + \
               chr(0x80 | (ucs4 & 0x3f))
    elif ucs4 < 0x4000000:
        # 5 byte string
        return chr(0xf8 | ((ucs4 >> 24) & 0x3)) + \
               chr(0x80 | ((ucs4 >> 18) & 0x3f)) + \
               chr(0x80 | ((ucs4 >> 12) & 0x3f)) + \
               chr(0x80 | ((ucs4 >> 6) & 0x3f)) + \
               chr(0x80 | (ucs4 & 0x3f))
    else:
        # 6 byte string
        return chr(0xfc | ((ucs4 >> 30) & 0x1)) + \
               chr(0x80 | ((ucs4 >> 24) & 0x3f)) + \
               chr(0x80 | ((ucs4 >> 18) & 0x3f)) + \
               chr(0x80 | ((ucs4 >> 12) & 0x3f)) + \
               chr(0x80 | ((ucs4 >> 6) & 0x3f)) + \
               chr(0x80 | (ucs4 & 0x3f))

def unicode_upper(letter):
    upper_case = letter

    if letter >= 0x61 and letter <= 0x7a:
        # Basic Latin
        upper_case -= 0x20
    elif letter >= 0xe0 and letter <= 0xfe:
        # Latin-1 Supplement
        upper_case -= 0x20
    elif ((letter >= 0x101 and letter <= 0x137) or
          (letter >= 0x14b and letter <= 0x177)): 
        # Latin Extended-A part-1
        if letter % 2 == 1:
            upper_case -= 1
    elif ((letter >= 0x13a and letter <= 0x148) or
          (letter >= 0x17a and letter <= 0x17e)):
        # Latin Extended-A part-2
        if letter % 2 == 0:
            upper_case -= 1
    elif letter >= 0x3ac and letter <= 0x3fb:
        # Greek and Coptic
        if ((letter >= 0x3b1 and letter <= 0x3c1) or
            (letter >= 0x3c3 and letter <= 0x3ce)):
            upper_case -= 0x20
        else:
            if letter == 0x3c2:
                upper_case = 0x3a3
            elif letter == 0x3ac:
                upper_case = 0x386
            elif letter == 0x3ad:
                upper_case = 0x388
            elif letter == 0x3ae:
                upper_case = 0x389
            elif letter == 0x3af:
                upper_case = 0x38a
            elif letter == 0x3d1:
                upper_case = 0x3f4
            elif letter ==  0x3d9:
                upper_case = 0x3d8
            elif letter ==  0x3db:
                upper_case = 0x3da
            elif letter ==  0x3dd:
                upper_case = 0x3dc
            elif letter ==  0x3df:
                upper_case = 0x3df
            elif letter ==  0x3e3:
                upper_case = 0x3e2
            elif letter ==  0x3e5:
                upper_case = 0x3e4
            elif letter ==  0x3e7:
                upper_case = 0x3e6
            elif letter ==  0x3e9:
                upper_case = 0x3e8
            elif letter ==  0x3eb:
                upper_case = 0x3ea
            elif letter ==  0x3ed:
                upper_case = 0x3ec
            elif letter ==  0x3ef:
                upper_case = 0x3ee
            elif letter ==  0x3f2:
                upper_case = 0x3f9
            elif letter ==  0x3f8:
                upper_case = 0x3f7
            elif letter ==  0x3fb:
                upper_case = 0x3fa
    elif letter >= 0x430 and letter <= 0x44f:
        # Basic Russian alphabet
        upper_case -= 0x20
    elif letter >= 0x450 and letter <= 0x45f:
        # Cyrillic extensions
        upper_case -= 0x50
    elif letter >= 0x461 and letter <= 0x47f:
        # Historic cyrillic letters
        if letter % 2 == 1:
            upper_case -= 1

    return upper_case

def unicode_lower(letter):
    lower_case = letter

    if letter >= 0x41 and letter <= 0x5a:
        # Basic Latin
        lower_case += 0x20
    elif letter >= 0xc0 and letter <= 0xde:
        # Latin-1 Supplement
        lower_case += 0x20
    elif ((letter >= 0x100 and letter <= 0x136) or
          (letter >= 0x14a and letter <= 0x176)): 
        # Latin Extended-A part-1
        if letter % 2 == 0:
            lower_case += 1
    elif ((letter >= 0x139 and letter <= 0x147) or
          (letter >= 0x179 and letter <= 0x17d)):
        # Latin Extended-A part-2
        if letter % 2 == 1:
            lower_case += 1
    elif letter >= 0x3ac and letter <= 0x3fb:
        # Greek and Coptic
        if ((letter >= 0x391 and letter <= 0x3a1) or
            (letter >= 0x3a3 and letter <= 0x3ae)):
            lower_case += 0x20
        else:
            if letter == 0x3a3:
                lower_case = 0x3c2
            elif letter == 0x386:
                lower_case = 0x3ac
            elif letter == 0x388:
                lower_case = 0x3ad
            elif letter == 0x389:
                lower_case = 0x3ae
            elif letter == 0x38a:
                lower_case = 0x3af
            elif letter == 0x3f4:
                lower_case = 0x3d1
            elif letter ==  0x3d8:
                lower_case = 0x3d9
            elif letter ==  0x3da:
                lower_case = 0x3db
            elif letter ==  0x3dc:
                lower_case = 0x3dd
            elif letter ==  0x3df:
                lower_case = 0x3df
            elif letter ==  0x3e2:
                lower_case = 0x3e3
            elif letter ==  0x3e4:
                lower_case = 0x3e5
            elif letter ==  0x3e6:
                lower_case = 0x3e7
            elif letter ==  0x3e8:
                lower_case = 0x3e9
            elif letter ==  0x3ea:
                lower_case = 0x3eb
            elif letter ==  0x3ec:
                lower_case = 0x3ed
            elif letter ==  0x3ee:
                lower_case = 0x3ef
            elif letter ==  0x3f9:
                lower_case = 0x3f2
            elif letter ==  0x3f7:
                lower_case = 0x3f8
            elif letter ==  0x3fa:
                lower_case = 0x3fb
    elif letter >= 0x410 and letter <= 0x42f:
        # Basic Russian alphabet
        lower_case += 0x20
    elif letter >= 0x400 and letter <= 0x40f:
        # Cyrillic extensions
        lower_case += 0x50
    elif letter >= 0x460 and letter <= 0x480:
        # Historic cyrillic letters
        if letter % 2 == 0:
            lower_case += 1

    return lower_case

keysym_alias_tbl = {
    "quotedbl" : "doublequote",
    "doublequote" : "quotedbl",
    "quoteleft" : "grave",
    "grave" : "quoteleft",
    "quoteright" : "apostrophe",
    "apostrophe" : "quoteright"
}

def keysym_alias(keysym):
    if keysym in keysym_alias_tbl.keys():
        return keysym_alias_tbl[keysym]
    return None

def check_unicode_representation(keysym):
    if len(keysym) != 5:
        return None
    try:
        code = int(keysym[1:], 16)
        return code
    except:
        return None

key_name_alias_tbl = {
    "<LatQ>" : "<AD01>",
    "<LatW>" : "<AD02>",
    "<LatE>" : "<AD03>",
    "<LatR>" : "<AD04>",
    "<LatT>" : "<AD05>",
    "<LatY>" : "<AD06>",
    "<LatU>" : "<AD07>",
    "<LatI>" : "<AD08>",
    "<LatO>" : "<AD09>",
    "<LatP>" : "<AD10>",
    "<LatA>" : "<AC01>",
    "<LatS>" : "<AC02>",
    "<LatD>" : "<AC03>",
    "<LatF>" : "<AC04>",
    "<LatG>" : "<AC05>",
    "<LatH>" : "<AC06>",
    "<LatJ>" : "<AC07>",
    "<LatK>" : "<AC08>",
    "<LatL>" : "<AC09>",
    "<LatZ>" : "<AB01>",
    "<LatX>" : "<AB02>",
    "<LatC>" : "<AB03>",
    "<LatV>" : "<AB04>",
    "<LatB>" : "<AB05>",
    "<LatN>" : "<AB06>",
    "<LatM>" : "<AB07>"
}

key_name_alias_tbl_r = {
    "<AD01>" : "<LatQ>",
    "<AD02>" : "<LatW>",
    "<AD03>" : "<LatE>",
    "<AD04>" : "<LatR>",
    "<AD05>" : "<LatT>",
    "<AD06>" : "<LatY>",
    "<AD07>" : "<LatU>",
    "<AD08>" : "<LatI>",
    "<AD09>" : "<LatO>",
    "<AD10>" : "<LatP>",
    "<AC01>" : "<LatA>",
    "<AC02>" : "<LatS>",
    "<AC03>" : "<LatD>",
    "<AC04>" : "<LatF>",
    "<AC05>" : "<LatG>",
    "<AC06>" : "<LatH>",
    "<AC07>" : "<LatJ>",
    "<AC08>" : "<LatK>",
    "<AC09>" : "<LatL>",
    "<AB01>" : "<LatZ>",
    "<AB02>" : "<LatX>",
    "<AB03>" : "<LatC>",
    "<AB04>" : "<LatV>",
    "<AB05>" : "<LatB>",
    "<AB06>" : "<LatN>",
    "<AB07>" : "<LatM>"
}

keypad_keysym_to_label = {
    "KP_Space" : "",
    "KP_Tab" : "Tab",
    "KP_Enter" : "Enter",
    "KP_F1" : "F1",
    "KP_F2" : "F2",
    "KP_F3" : "F3",
    "KP_F4" : "F4",
    "KP_Home" : "Home",
    "KP_Left" : "Left",
    "KP_Up" : "Up",
    "KP_Right" : "Right",
    "KP_Down" : "Down",
    "KP_Page_Up" : "Pg Up",
    "KP_Page_Down" : "Pg Dn",
    "KP_End" : "End",
    "KP_Begin" : "Begin",
    "KP_Insert" : "Ins",
    "KP_Delete" : "Del",
    "KP_Multiply" : "*",
    "KP_Add" : "+",
    "KP_Separator" : "Sep",
    "KP_Subtract" : "-",
    "KP_Decimal" : ".",
    "KP_Divide" : "/",
    "KP_0" : "0",
    "KP_1" : "1",
    "KP_2" : "2",
    "KP_3" : "3",
    "KP_4" : "4",
    "KP_5" : "5",
    "KP_6" : "6",
    "KP_7" : "7",
    "KP_8" : "8",
    "KP_9" : "9",
    "KP_Equal" : "=",
    }

def get_key_pad_label(key_sym):
    if keypad_keysym_to_label.has_key(key_sym):
        return keypad_keysym_to_label[key_sym]
    return None

def key_name_alias(key_name):
    if key_name in key_name_alias_tbl.keys():
        return key_name_alias_tbl[key_name]
    return None

def key_name_alias_r(key_name):
    if key_name in key_name_alias_tbl_r.keys():
        return key_name_alias_tbl_r[key_name]
    return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        num = 0x1D400
    else:
        num = int(sys.argv[1], 16)

    print ucs4_to_utf8(num)
