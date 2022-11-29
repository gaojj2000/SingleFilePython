# _*_ coding:utf-8 _*_
# FileName: get_bilibili_video.py
# IDE: PyCharm

import html
import ctypes
import random
import requests
from urllib import parse

"""
import execjs

link = 'https://www.bilibili.com/video/BV1Xt41157R4/?spm_id_from=autoNext'
r = execjs.eval("Math.random().toString(10).substring(2)")
s = str(execjs.compile(\"""
generateStr = function(t) {
    var a = function() {
        for (var t = 0, e = new Array(256), n = 0; 256 != n; ++n)
            t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = n) ? -306674912 ^ t >>>
                        1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 :
                    t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -
                306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>>
            1,
            e[n] = t;
        return "undefined" != typeof Int32Array ? new Int32Array(e) : e
    }();
    return function(t) {
        for (var e, n, r = -1, i = 0, o = t.length; i < o;)
            r = (e = t.charCodeAt(i++)) < 128 ? r >>> 8 ^ a[255 & (r ^ e)] : e < 2048 ? (r = r >>> 8 ^ a[255 &
                (r ^ (192 | e >> 6 & 31))]) >>> 8 ^ a[255 & (r ^ (128 | 63 & e))] : 55296 <= e && e < 57344 ? (
                e = 64 + (1023 & e),
                n = 1023 & t.charCodeAt(i++),
                (r = (r = (r = r >>> 8 ^ a[255 & (r ^ (240 | e >> 8 & 7))]) >>> 8 ^ a[255 & (r ^ (128 | e >>
                    2 & 63))]) >>> 8 ^ a[255 & (r ^ (128 | n >> 6 & 15 | (3 & e) << 4))]) >>> 8 ^ a[255 & (r ^
                    (128 | 63 & n))]) : (r = (r = r >>> 8 ^ a[255 & (r ^ (224 | e >> 12 & 15))]) >>> 8 ^ a[
                255 & (r ^ (128 | e >> 6 & 63))]) >>> 8 ^ a[255 & (r ^ (128 | 63 & e))];
        return -1 ^ r
    }(t) >>> 0
}
\""").call("generateStr", f"{link}@{r}"))
x_client_data = execjs.compile(\"""
function d(t, e) {
    var n = (65535 & t) + (65535 & e);
    return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
}
function s(t, e, n, r, i, o) {
    console.log(function a(t, e) {
        return t << e | t >>> 32 - e
    }(d(d(e, t), d(r, o)), i))
    return d(function a(t, e) {
        return t << e | t >>> 32 - e
    }(d(d(e, t), d(r, o)), i), n)
}
function h(t, e, n, r, i, o, a) {
    return s(e & n | ~e & r, t, e, i, o, a)
}
function f(t, e, n, r, i, o, a) {
    return s(e & r | n & ~r, t, e, i, o, a)
}
function g(t, e, n, r, i, o, a) {
    return s(e ^ n ^ r, t, e, i, o, a)
}
function p(t, e, n, r, i, o, a) {
    return s(n ^ (e | ~r), t, e, i, o, a)
}
function n(t) {
    return unescape(encodeURIComponent(t))
}
function c(t) {
    var e, n = "", r = 32 * t.length;
    for (e = 0; e < r; e += 8)
        n += String.fromCharCode(t[e >> 5] >>> e % 32 & 255);
    return n
}
function l(t) {
    var e, n = [];
    for (n[(t.length >> 2) - 1] = void 0,
    e = 0; e < n.length; e += 1)
        n[e] = 0;
    var r = 8 * t.length;
    for (e = 0; e < r; e += 8)
        n[e >> 5] |= (255 & t.charCodeAt(e / 8)) << e % 32;
    return n
}
function u(t, e) {
    t[e >> 5] |= 128 << e % 32,
    t[14 + (e + 64 >>> 9 << 4)] = e;
    var n, r, i, o, a, s = 1732584193, u = -271733879, c = -1732584194, l = 271733878;
    // console.log(h(s, u, c, l, t[0], 7, -680876936))
    for (n = 0; n < t.length; n += 16)
        u = p(u = p(u = p(u = p(u = g(u = g(u = g(u = g(u = f(u = f(u = f(u = f(u = h(u = h(u = h(u = h(i = u, c = h(o = c, l = h(a = l, s = h(r = s, u, c, l, t[n], 7, -680876936), u, c, t[n + 1], 12, -389564586), s, u, t[n + 2], 17, 606105819), l, s, t[n + 3], 22, -1044525330), c = h(c, l = h(l, s = h(s, u, c, l, t[n + 4], 7, -176418897), u, c, t[n + 5], 12, 1200080426), s, u, t[n + 6], 17, -1473231341), l, s, t[n + 7], 22, -45705983), c = h(c, l = h(l, s = h(s, u, c, l, t[n + 8], 7, 1770035416), u, c, t[n + 9], 12, -1958414417), s, u, t[n + 10], 17, -42063), l, s, t[n + 11], 22, -1990404162), c = h(c, l = h(l, s = h(s, u, c, l, t[n + 12], 7, 1804603682), u, c, t[n + 13], 12, -40341101), s, u, t[n + 14], 17, -1502002290), l, s, t[n + 15], 22, 1236535329), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 1], 5, -165796510), u, c, t[n + 6], 9, -1069501632), s, u, t[n + 11], 14, 643717713), l, s, t[n], 20, -373897302), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 5], 5, -701558691), u, c, t[n + 10], 9, 38016083), s, u, t[n + 15], 14, -660478335), l, s, t[n + 4], 20, -405537848), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 9], 5, 568446438), u, c, t[n + 14], 9, -1019803690), s, u, t[n + 3], 14, -187363961), l, s, t[n + 8], 20, 1163531501), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 13], 5, -1444681467), u, c, t[n + 2], 9, -51403784), s, u, t[n + 7], 14, 1735328473), l, s, t[n + 12], 20, -1926607734), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 5], 4, -378558), u, c, t[n + 8], 11, -2022574463), s, u, t[n + 11], 16, 1839030562), l, s, t[n + 14], 23, -35309556), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 1], 4, -1530992060), u, c, t[n + 4], 11, 1272893353), s, u, t[n + 7], 16, -155497632), l, s, t[n + 10], 23, -1094730640), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 13], 4, 681279174), u, c, t[n], 11, -358537222), s, u, t[n + 3], 16, -722521979), l, s, t[n + 6], 23, 76029189), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 9], 4, -640364487), u, c, t[n + 12], 11, -421815835), s, u, t[n + 15], 16, 530742520), l, s, t[n + 2], 23, -995338651), c = p(c, l = p(l, s = p(s, u, c, l, t[n], 6, -198630844), u, c, t[n + 7], 10, 1126891415), s, u, t[n + 14], 15, -1416354905), l, s, t[n + 5], 21, -57434055), c = p(c, l = p(l, s = p(s, u, c, l, t[n + 12], 6, 1700485571), u, c, t[n + 3], 10, -1894986606), s, u, t[n + 10], 15, -1051523), l, s, t[n + 1], 21, -2054922799), c = p(c, l = p(l, s = p(s, u, c, l, t[n + 8], 6, 1873313359), u, c, t[n + 15], 10, -30611744), s, u, t[n + 6], 15, -1560198380), l, s, t[n + 13], 21, 1309151649), c = p(c, l = p(l, s = p(s, u, c, l, t[n + 4], 6, -145523070), u, c, t[n + 11], 10, -1120210379), s, u, t[n + 2], 15, 718787259), l, s, t[n + 9], 21, -343485551),
        s = d(s, r),
        u = d(u, i),
        c = d(c, o),
        l = d(l, a);
    return [s, u, c, l]
}
function a(t) {
    return function e(t) {
        return c(u(l(t), 8 * t.length))
    }(n(t))
}
function o(t) {
    var e, n, r = "";
    for (n = 0; n < t.length; n += 1)
        e = t.charCodeAt(n),
        r += "0123456789abcdef".charAt(e >>> 2 & 15) + "0123456789abcdef".charAt(15 & e);
    return r
}
function m(t, e) {
    return function s(t, e) {
        var n, r, i = l(t), o = [], a = [];
        for (o[15] = a[15] = void 0,
        16 < i.length && (i = u(i, 8 * t.length)),
        n = 0; n < 16; n += 1)
            o[n] = 909522486 ^ i[n],
            a[n] = 1549556828 ^ i[n];
        return r = u(o.concat(l(e)), 512 + 8 * e.length),
        c(u(a.concat(r), 640))
    }(n(t), n(e))
}
function md5(t, e, n) {
    return e ? n ? m(e, t) : function r(t, e) {
        return o(m(t, e))
    }(e, t) : n ? a(t) : function i(t) {
        return o(a(t))
    }(t)
}
function uu(t, e) {
    var n = e.charAt(t.charCodeAt(0) % e.length),
        r = e.charAt(t.charCodeAt(t.length - 1) % e.length);
    return md5(n + t + r)
}
\""").call("uu", s, 'bilibili')
print(r)
print(s)
print(x_client_data)
"""

# 32位无符号右移
gt3 = lambda _, __: (_ % (1 << 32)) >> __


def x_client_data(t, e='bilibili'):
    """
    function d(t, e) {
        var n = (65535 & t) + (65535 & e);
        return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
    }
    function s(t, e, n, r, i, o) {
        return d(function a(t, e) {
            return t << e | t >>> 32 - e
        }(d(d(e, t), d(r, o)), i), n)
    }
    function h(t, e, n, r, i, o, a) {
        return s(e & n | ~e & r, t, e, i, o, a)
    }
    function f(t, e, n, r, i, o, a) {
        return s(e & r | n & ~r, t, e, i, o, a)
    }
    function g(t, e, n, r, i, o, a) {
        return s(e ^ n ^ r, t, e, i, o, a)
    }
    function p(t, e, n, r, i, o, a) {
        return s(n ^ (e | ~r), t, e, i, o, a)
    }
    function n(t) {
        return unescape(encodeURIComponent(t))
    }
    function c(t) {
        var e, n = "", r = 32 * t.length;
        for (e = 0; e < r; e += 8)
            n += String.fromCharCode(t[e >> 5] >>> e % 32 & 255);
        return n
    }
    function l(t) {
        var e, n = [];
        for (n[(t.length >> 2) - 1] = void 0,
        e = 0; e < n.length; e += 1)
            n[e] = 0;
        var r = 8 * t.length;
        for (e = 0; e < r; e += 8)
            n[e >> 5] |= (255 & t.charCodeAt(e / 8)) << e % 32;
        return n
    }
    function u(t, e) {
        t[e >> 5] |= 128 << e % 32,
        t[14 + (e + 64 >>> 9 << 4)] = e;
        var n, r, i, o, a, s = 1732584193, u = -271733879, c = -1732584194, l = 271733878;
        for (n = 0; n < t.length; n += 16)
            u = p(u = p(u = p(u = p(u = g(u = g(u = g(u = g(u = f(u = f(u = f(u = f(u = h(u = h(u = h(u = h(i = u, c = h(o = c, l = h(a = l, s = h(r = s, u, c, l, t[n], 7, -680876936), u, c, t[n + 1], 12, -389564586), s, u, t[n + 2], 17, 606105819), l, s, t[n + 3], 22, -1044525330), c = h(c, l = h(l, s = h(s, u, c, l, t[n + 4], 7, -176418897), u, c, t[n + 5], 12, 1200080426), s, u, t[n + 6], 17, -1473231341), l, s, t[n + 7], 22, -45705983), c = h(c, l = h(l, s = h(s, u, c, l, t[n + 8], 7, 1770035416), u, c, t[n + 9], 12, -1958414417), s, u, t[n + 10], 17, -42063), l, s, t[n + 11], 22, -1990404162), c = h(c, l = h(l, s = h(s, u, c, l, t[n + 12], 7, 1804603682), u, c, t[n + 13], 12, -40341101), s, u, t[n + 14], 17, -1502002290), l, s, t[n + 15], 22, 1236535329), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 1], 5, -165796510), u, c, t[n + 6], 9, -1069501632), s, u, t[n + 11], 14, 643717713), l, s, t[n], 20, -373897302), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 5], 5, -701558691), u, c, t[n + 10], 9, 38016083), s, u, t[n + 15], 14, -660478335), l, s, t[n + 4], 20, -405537848), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 9], 5, 568446438), u, c, t[n + 14], 9, -1019803690), s, u, t[n + 3], 14, -187363961), l, s, t[n + 8], 20, 1163531501), c = f(c, l = f(l, s = f(s, u, c, l, t[n + 13], 5, -1444681467), u, c, t[n + 2], 9, -51403784), s, u, t[n + 7], 14, 1735328473), l, s, t[n + 12], 20, -1926607734), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 5], 4, -378558), u, c, t[n + 8], 11, -2022574463), s, u, t[n + 11], 16, 1839030562), l, s, t[n + 14], 23, -35309556), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 1], 4, -1530992060), u, c, t[n + 4], 11, 1272893353), s, u, t[n + 7], 16, -155497632), l, s, t[n + 10], 23, -1094730640), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 13], 4, 681279174), u, c, t[n], 11, -358537222), s, u, t[n + 3], 16, -722521979), l, s, t[n + 6], 23, 76029189), c = g(c, l = g(l, s = g(s, u, c, l, t[n + 9], 4, -640364487), u, c, t[n + 12], 11, -421815835), s, u, t[n + 15], 16, 530742520), l, s, t[n + 2], 23, -995338651), c = p(c, l = p(l, s = p(s, u, c, l, t[n], 6, -198630844), u, c, t[n + 7], 10, 1126891415), s, u, t[n + 14], 15, -1416354905), l, s, t[n + 5], 21, -57434055), c = p(c, l = p(l, s = p(s, u, c, l, t[n + 12], 6, 1700485571), u, c, t[n + 3], 10, -1894986606), s, u, t[n + 10], 15, -1051523), l, s, t[n + 1], 21, -2054922799), c = p(c, l = p(l, s = p(s, u, c, l, t[n + 8], 6, 1873313359), u, c, t[n + 15], 10, -30611744), s, u, t[n + 6], 15, -1560198380), l, s, t[n + 13], 21, 1309151649), c = p(c, l = p(l, s = p(s, u, c, l, t[n + 4], 6, -145523070), u, c, t[n + 11], 10, -1120210379), s, u, t[n + 2], 15, 718787259), l, s, t[n + 9], 21, -343485551),
            s = d(s, r),
            u = d(u, i),
            c = d(c, o),
            l = d(l, a);
        return [s, u, c, l]
    }
    function a(t) {
        return function e(t) {
            return c(u(l(t), 8 * t.length))
        }(n(t))
    }
    function o(t) {
        var e, n, r = "";
        for (n = 0; n < t.length; n += 1)
            e = t.charCodeAt(n),
            r += "0123456789abcdef".charAt(e >>> 2 & 15) + "0123456789abcdef".charAt(15 & e);
        return r
    }
    function m(t, e) {
        return function s(t, e) {
            var n, r, i = l(t), o = [], a = [];
            for (o[15] = a[15] = void 0,
            16 < i.length && (i = u(i, 8 * t.length)),
            n = 0; n < 16; n += 1)
                o[n] = 909522486 ^ i[n],
                a[n] = 1549556828 ^ i[n];
            return r = u(o.concat(l(e)), 512 + 8 * e.length),
            c(u(a.concat(r), 640))
        }(n(t), n(e))
    }
    function md5(t, e, n) {
        return e ? n ? m(e, t) : function r(t, e) {
            return o(m(t, e))
        }(e, t) : n ? a(t) : function i(t) {
            return o(a(t))
        }(t)
    }
    function uu(t, e) {
        if (!0 === window.navigator.webdriver || window.document.documentElement.getAttribute("webdriver") || window
            .callPhantom || window._phantom)
            return md5(o + t + o);
        var n = e.charAt(t.charCodeAt(0) % e.length),
            r = e.charAt(t.charCodeAt(t.length - 1) % e.length);
        return md5(n + t + r)
    }
    """
    def d(t, e):
        n_ = (65535 & t) + (65535 & e)
        return (t >> 16) + (e >> 16) + (n_ >> 16) << 16 | 65535 & n_

    def s(t, e, n_, r, i, o):
        t = d(d(e, t), d(r, o))
        e = i
        return d(ctypes.c_int32(t << i).value | gt3(t, 32 - e), n_)

    def h(t, e, n_, r, i, o, a):
        return s(e & n_ | ~e & r, t, e, i, o, a)

    def f(t, e, n_, r, i, o, a):
        return s(e & r | n_ & ~r, t, e, i, o, a)

    def g(t, e, n_, r, i, o, a):
        return s(e ^ n_ ^ r, t, e, i, o, a)

    def p(t, e, n_, r, i, o, a):
        return s(n_ ^ (e | ~r), t, e, i, o, a)

    def n(t):
        return html.unescape(parse.unquote(t))

    def c(t):
        n = ''
        for e in range(0, 32 * len(t), 8):
            n += chr(gt3(t[e >> 5], e % 32) & 255)
        return n

    def l(t):
        n_ = []
        for e in range(len(t) >> 2):
            n_.append(0)
        for e in range(0, 8 * len(t), 8):
            if (e >> 5) < len(n_):
                n_[e >> 5] |= (255 & ord(t[e // 8])) << e % 32
            else:
                n_.append(0 | (255 & ord(t[e // 8])) << e % 32)
        return n_

    def u(t, e):
        while 14 + (gt3((e + 64), 9) << 4) >= len(t) - 1:
            t.append(0)
        t[e >> 5] |= 128 << e % 32
        t[14 + (gt3((e + 64), 9) << 4)] = e
        s = 1732584193
        u = -271733879
        c = -1732584194
        l = 271733878
        # print(h(s, u, c, l, t[0], 7, -680876936))
        for n_ in range(0, len(t), 16):
            r = s
            s = h(r, u, c, l, t[n_], 7, -680876936)
            a = l
            l = h(a, s, u, c, t[n_ + 1], 12, -389564586)
            o = c
            c = h(o, l, s, u, t[n_ + 2], 17, 606105819)
            i = u
            u = h(i, c, l, s, t[n_ + 3], 22, -1044525330)
            s = h(s, u, c, l, t[n_ + 4], 7, -176418897)
            l = h(l, s, u, c, t[n_ + 5], 12, 1200080426)
            c = h(c, l, s, u, t[n_ + 6], 17, -1473231341)
            u = h(u, c, l, s, t[n_ + 7], 22, -45705983)
            s = h(s, u, c, l, t[n_ + 8], 7, 1770035416)
            l = h(l, s, u, c, t[n_ + 9], 12, -1958414417)
            c = h(c, l, s, u, t[n_ + 10], 17, -42063)
            u = h(u, c, l, s, t[n_ + 11], 22, -1990404162)
            s = h(s, u, c, l, t[n_ + 12], 7, 1804603682)
            l = h(l, s, u, c, t[n_ + 13], 12, -40341101)
            c = h(c, l, s, u, t[n_ + 14], 17, -1502002290)
            u = h(u, c, l, s, t[n_ + 15], 22, 1236535329)
            s = f(s, u, c, l, t[n_ + 1], 5, -165796510)
            l = f(l, s, u, c, t[n_ + 6], 9, -1069501632)
            c = f(c, l, s, u, t[n_ + 11], 14, 643717713)
            u = f(u, c, l, s, t[n_], 20, -373897302)
            s = f(s, u, c, l, t[n_ + 5], 5, -701558691)
            l = f(l, s, u, c, t[n_ + 10], 9, 38016083)
            c = f(c, l, s, u, t[n_ + 15], 14, -660478335)
            u = f(u, c, l, s, t[n_ + 4], 20, -405537848)
            s = f(s, u, c, l, t[n_ + 9], 5, 568446438)
            l = f(l, s, u, c, t[n_ + 14], 9, -1019803690)
            c = f(c, l, s, u, t[n_ + 3], 14, -187363961)
            u = f(u, c, l, s, t[n_ + 8], 20, 1163531501)
            s = f(s, u, c, l, t[n_ + 13], 5, -1444681467)
            l = f(l, s, u, c, t[n_ + 2], 9, -51403784)
            c = f(c, l, s, u, t[n_ + 7], 14, 1735328473)
            u = f(u, c, l, s, t[n_ + 12], 20, -1926607734)
            s = g(s, u, c, l, t[n_ + 5], 4, -378558)
            l = g(l, s, u, c, t[n_ + 8], 11, -2022574463)
            c = g(c, l, s, u, t[n_ + 11], 16, 1839030562)
            u = g(u, c, l, s, t[n_ + 14], 23, -35309556)
            s = g(s, u, c, l, t[n_ + 1], 4, -1530992060)
            l = g(l, s, u, c, t[n_ + 4], 11, 1272893353)
            c = g(c, l, s, u, t[n_ + 7], 16, -155497632)
            u = g(u, c, l, s, t[n_ + 10], 23, -1094730640)
            s = g(s, u, c, l, t[n_ + 13], 4, 681279174)
            l = g(l, s, u, c, t[n_], 11, -358537222)
            c = g(c, l, s, u, t[n_ + 3], 16, -722521979)
            u = g(u, c, l, s, t[n_ + 6], 23, 76029189)
            s = g(s, u, c, l, t[n_ + 9], 4, -640364487)
            l = g(l, s, u, c, t[n_ + 12], 11, -421815835)
            c = g(c, l, s, u, t[n_ + 15], 16, 530742520)
            u = g(u, c, l, s, t[n_ + 2], 23, -995338651)
            s = p(s, u, c, l, t[n_], 6, -198630844)
            l = p(l, s, u, c, t[n_ + 7], 10, 1126891415)
            c = p(c, l, s, u, t[n_ + 14], 15, -1416354905)
            u = p(u, c, l, s, t[n_ + 5], 21, -57434055)
            s = p(s, u, c, l, t[n_ + 12], 6, 1700485571)
            l = p(l, s, u, c, t[n_ + 3], 10, -1894986606)
            c = p(c, l, s, u, t[n_ + 10], 15, -1051523)
            u = p(u, c, l, s, t[n_ + 1], 21, -2054922799)
            s = p(s, u, c, l, t[n_ + 8], 6, 1873313359)
            l = p(l, s, u, c, t[n_ + 15], 10, -30611744)
            c = p(c, l, s, u, t[n_ + 6], 15, -1560198380)
            u = p(u, c, l, s, t[n_ + 13], 21, 1309151649)
            s = p(s, u, c, l, t[n_ + 4], 6, -145523070)
            l = p(l, s, u, c, t[n_ + 11], 10, -1120210379)
            c = p(c, l, s, u, t[n_ + 2], 15, 718787259)
            u = p(u, c, l, s, t[n_ + 9], 21, -343485551)
            s = d(s, r)
            u = d(u, i)
            c = d(c, o)
            l = d(l, a)
        return [s, u, c, l]

    def a(t):
        return c(u(l(n(t)), 8 * len(t)))

    def o(t):
        r = ''
        for n_ in range(len(t)):
            e = ord(t[n_])
            r += "0123456789abcdef"[gt3(e, 2) & 15] + "0123456789abcdef"[15 & e]
        return r

    def m(t, e):
        t = n(t)
        e = n(e)
        i = l(t)
        o = []
        a= []
        if 16 < len(i):
            i = u(i, 8 * len(t))
        for n_ in range(16):
            o.append(909522486 ^ i[n_])
            a.append(1549556828 ^ i[n_])
        r = u(o + e, 512 + 8 * len(e))
        return r, c(u(a + r, 640))

    def md5(t, e=None, n_=None):
        if e:
            if n_:
                m(e, t)
            else:
                return o(m(e, t))
        else:
            if n_:
                a(t)
            else:
                return o(a(t))
    n_ = e[ord(t[0]) % len(e)]
    r = e[ord(t[-1]) % len(e)]
    return md5(n_ + t + r)


def generate_str(t):
    """
    var generateStr = function(t) {
        var a = function() {
            for (var t = 0, e = new Array(256), n = 0; 256 != n; ++n)
                t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = n) ? -306674912 ^ t >>>
                            1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 :
                        t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -
                    306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>>
                1,
                e[n] = t;
            return "undefined" != typeof Int32Array ? new Int32Array(e) : e
        }();
        return function(t) {
            for (var e, n, r = -1, i = 0, o = t.length; i < o;)
                r = (e = t.charCodeAt(i++)) < 128 ? r >>> 8 ^ a[255 & (r ^ e)] : e < 2048 ? (r = r >>> 8 ^ a[255 &
                    (r ^ (192 | e >> 6 & 31))]) >>> 8 ^ a[255 & (r ^ (128 | 63 & e))] : 55296 <= e && e < 57344 ? (
                    e = 64 + (1023 & e),
                    n = 1023 & t.charCodeAt(i++),
                    (r = (r = (r = r >>> 8 ^ a[255 & (r ^ (240 | e >> 8 & 7))]) >>> 8 ^ a[255 & (r ^ (128 | e >>
                        2 & 63))]) >>> 8 ^ a[255 & (r ^ (128 | n >> 6 & 15 | (3 & e) << 4))]) >>> 8 ^ a[255 & (r ^
                        (128 | 63 & n))]) : (r = (r = r >>> 8 ^ a[255 & (r ^ (224 | e >> 12 & 15))]) >>> 8 ^ a[
                    255 & (r ^ (128 | e >> 6 & 63))]) >>> 8 ^ a[255 & (r ^ (128 | 63 & e))];
            return -1 ^ r
        }(t) >>> 0
    }
    """
    a = []
    for n in range(256):
        for _ in range(8):
            if 1 & n:
                n = -306674912 ^ gt3(n, 1)
            else:
                n = gt3(n, 1)
        a.append(n)
    r = -1
    i = 0
    while i < len(t):
        e = ord(t[i])
        i += 1
        if e < 128:
            r = gt3(r, 8) ^ a[255 & (r ^ e)]
        else:
            if e < 2048:
                r = gt3(gt3(r, 8) ^ a[255 & (r ^ (192 | e >> 6 & 31))], 8) ^ a[255 & (r ^ (128 | 63 & e))]
            else:
                if 55296 <= e < 57344:
                    e = 64 + (1023 & e)
                    n = 1023 & ord(t[i])
                    i += 1
                    r = gt3(gt3(gt3(gt3(r, 8) ^ a[255 & (r ^ (240 | e >> 8 & 7))], 8) ^ a[255 & (r ^ (128 | e >> 2 & 63))], 8) ^ a[255 & (r ^ (128 | n >> 6 & 15 | (3 & e) << 4))], 8) ^ a[255 & (r ^ (128 | 63 & n))]
                else:
                    r = gt3(gt3(gt3(r, 8) ^ a[255 & (r ^ (224 | e >> 12 & 15))], 8) ^ a[255 & (r ^ (128 | e >> 6 & 63))], 8) ^ a[255 & (r ^ (128 | 63 & e))]
    return str(gt3(-1 ^ r, 0))


# https://bilibili.iiilab.com

headers = {
    "Origin": "https://bilibili.iiilab.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

session = requests.session()
session.headers = headers
session.get('https://bilibili.iiilab.com/')
session.post('https://service0.iiilab.com/sponsor/getByPage', data=dict(page='bilibili'))
session.headers["Referer"] = "https://bilibili.iiilab.com/"
session.headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
# cookies = requests.utils.dict_from_cookiejar(session.cookies)
# cookies.update(dict(zzz0821='1'))
# session.cookies = requests.utils.cookiejar_from_dict(cookies)
session.cookies = requests.sessions.merge_cookies(session.cookies, dict(zzz0821='1'))
# session.headers.update(dict(Cookie=';'.join([(lambda _: f'{_}={cookies[_]}')(_) for _ in cookies])))
link = 'https://www.bilibili.com/video/BV1Xt41157R4/?spm_id_from=autoNext'
ran = str(random.random())[2:]
s = generate_str(f"{link}@{ran}")
session.headers["X-Client-Data"] = x_client_data(s)
res = session.post('https://service0.iiilab.com/video/web/bilibili', data=dict(link=link, r=ran, s=s))
if res.ok:
    print(res.json())
