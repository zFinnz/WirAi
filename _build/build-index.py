#!/usr/bin/env python3
"""Tạo index.html từ các trang tham khảo và các file skill .md.

Chạy lại mỗi khi sửa hoặc thêm skill:
    python3 _build/build-index.py

Script làm các việc sau rồi ghép vào template.html thành file index.html:
1. Đọc thư mục tham-khao/ cho các trang Tổng quan, Instructions, Prompt, Skill, Plugin.
2. Đọc mọi thư mục nhóm skill, trích mã, tên, "Dùng khi", "Kết quả", "Không dùng khi" và nội dung
   cho trang Skill template.
3. Đọc thư mục slides/ (mỗi trang slide một file .svg, kèm file .pptx để tải) cho trang Slide.
   Xóa thư mục slides/ rồi chạy lại script thì tab Slide tự ẩn. File slides/data-demo.md (mỗi mục một tiêu đề
   "## Mục N · Tên (slide a, b–c)") thành mục Data demo dưới danh sách slide: các bước, mẫu prompt, file để tải.
4. Liệt kê các file Word, Excel, Markdown (trừ README.md) trong thư mục du-lieu-demo/ để liên kết dạng [tên](du-lieu-demo/ten-file) trên
   các trang tham khảo thành nút tải file. Giống file .pptx của slide, các file này nằm cạnh index.html, không nhúng vào.
5. Nhúng logo _build/wir_logo.jpg vào góc trái thanh đầu trang và làm biểu tượng tab. Không có file logo thì
   dùng ô chữ "W" như cũ.
File index.html
mở được bằng cách nhấp đúp, không cần máy chủ hay internet.
"""
import base64
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "template.html"
LOGO = Path(__file__).resolve().parent / "wir_logo.jpg"
OUT = ROOT / "index.html"

# Các trang tham khảo, theo đúng thứ tự trên thanh điều hướng. Sửa nội dung trong thư mục tham-khao/.
REF_DIR = ROOT / "tham-khao"
REF_PAGES = [
    ("instructions", "instructions.md"),
    ("prompt", "prompt.md"),
    ("skill", "skill.md"),
    ("plugin", "plugin.md"),
]
HUB_FILE = "tong-quan.md"  # nội dung phần dưới của trang Tổng quan

# Bộ slide: các file NN_ten.svg theo thứ tự tên file, và một file .pptx để tải về.
SLIDE_DIR = ROOT / "slides"
# Data demo cho các slide cần demo: mỗi mục là một tiêu đề "## Slide N · Tên" trong file này.
DEMO_MD = SLIDE_DIR / "data-demo.md"

# Dữ liệu demo để tập (Word, Excel). README.md trong thư mục chỉ để đọc trên repo.
DEMO_DIR = ROOT / "du-lieu-demo"
DEMO_TYPES = (".docx", ".xlsx", ".pdf", ".pptx", ".md")

# Thứ tự và mô tả nhóm cho người dùng không chuyên.
GROUPS = [
    ("marketing", "MKT", "Marketing và nội dung",
     "Kế hoạch, nội dung, quảng cáo, SEO, email, thương hiệu, báo cáo marketing.",
     "Nhân viên và trưởng phòng marketing, người làm nội dung, chạy quảng cáo."),
    ("ban-hang", "SAL", "Bán hàng",
     "Quy trình bán, kịch bản tư vấn, xử lý từ chối, báo giá, đại lý, báo cáo doanh số.",
     "Nhân viên kinh doanh, trưởng nhóm bán hàng, quản lý đại lý."),
    ("cham-soc-khach-hang", "CS", "Chăm sóc khách hàng",
     "Quy trình phục vụ, xử lý khiếu nại, câu hỏi thường gặp, khảo sát hài lòng, giữ chân khách.",
     "Nhân viên chăm sóc khách hàng, trực hotline, trực chat sàn và Zalo."),
    ("nhan-su", "HR", "Nhân sự",
     "Tuyển dụng, hội nhập, đánh giá, KPI, đào tạo, nội quy, lương thưởng, nghỉ việc.",
     "Phòng nhân sự, trưởng phòng cần tuyển và đánh giá người."),
    ("tai-chinh-ke-toan", "FIN", "Tài chính và kế toán",
     "Kế hoạch tài chính, dòng tiền, chi phí, định giá, công nợ, ngân sách, đóng sổ tháng.",
     "Kế toán, kế toán trưởng, chủ doanh nghiệp theo dõi tiền."),
    ("van-hanh", "OPS", "Vận hành và quản lý",
     "Quy trình chuẩn, dự án, họp, giao việc, báo cáo, tự động hóa, dữ liệu, KPI công ty.",
     "Trưởng phòng, trợ lý điều hành, người xây quy trình."),
    ("lanh-dao", "LD", "Lãnh đạo và chiến lược",
     "Ra quyết định, kế hoạch kinh doanh, phân quyền, chẩn đoán doanh nghiệp, ứng dụng AI.",
     "Ban giám đốc, chủ doanh nghiệp, quản lý cấp cao."),
    ("phap-ly", "PL", "Pháp lý và tuân thủ",
     "Rà soát hợp đồng, soạn hợp đồng mẫu, chính sách bảo mật, quảng cáo đúng luật, quản lý rủi ro.",
     "Pháp chế, hành chính, người ký hợp đồng. Văn bản cần luật sư duyệt."),
    ("kho-mua-hang", "KHO", "Kho và mua hàng",
     "Nhập xuất kiểm kê, tồn kho, mua hàng, nhà cung cấp, tài sản.",
     "Thủ kho, nhân viên mua hàng, kế toán kho."),
    ("cong-nghe-thong-tin", "IT", "Công nghệ thông tin",
     "Chính sách CNTT, sao lưu, tài khoản và phân quyền, bản đồ phần mềm.",
     "Phụ trách IT, hành chính, người quản lý tài khoản hệ thống."),
    ("san-pham-chat-luong", "SP", "Sản phẩm và chất lượng",
     "Danh mục sản phẩm, ra mắt sản phẩm mới, kiểm soát chất lượng, cải tiến.",
     "Phụ trách sản phẩm, kiểm hàng, quản lý chất lượng."),
    ("van-phong-chung", "VP", "Kỹ năng văn phòng chung",
     "Chọn skill, viết email, tóm tắt tài liệu, kế hoạch tuần, bảng tính, theo dõi việc, trình bày.",
     "Mọi nhân viên, không phân biệt phòng ban."),
]

META_RE = re.compile(r"^> \*\*(Dùng khi|Kết quả|Không dùng khi):\*\*\s*(.*)$")


def parse_skill(path: Path, group_key: str):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title_line = next((l for l in lines if l.startswith("# ")), "")
    m = re.match(r"^# ([A-Z]+-\d+)\s*[·\-:]\s*(.+)$", title_line)
    if not m:
        print(f"CẢNH BÁO: không đọc được tiêu đề ở {path.name}", file=sys.stderr)
        code, name = path.stem.split("-")[0] + "-" + path.stem.split("-")[1], path.stem
    else:
        code, name = m.group(1), m.group(2).strip()
    meta = {"Dùng khi": "", "Kết quả": "", "Không dùng khi": ""}
    for l in lines:
        mm = META_RE.match(l)
        if mm:
            meta[mm.group(1)] = mm.group(2).strip()
    # Mã skill khác được nhắc đến, để hiện "skill liên quan".
    related = sorted(set(re.findall(r"\b(?:MKT|SAL|CS|HR|FIN|OPS|LD|PL|KHO|IT|SP|VP)-\d{2}\b", text)) - {code})
    return {
        "code": code,
        "name": name,
        "group": group_key,
        "file": path.name,
        "when": meta["Dùng khi"],
        "result": meta["Kết quả"],
        "notWhen": meta["Không dùng khi"],
        "related": related,
        "lines": len(lines),
        "raw": text,
    }


REF_META_RE = re.compile(r"^> \*\*(Là gì|Tra mục này khi):\*\*\s*(.*)$")


def load_ref(key, filename):
    """Đọc một trang tham khảo: tiêu đề, hai dòng định nghĩa ở đầu, và phần thân."""
    path = REF_DIR / filename
    if not path.exists():
        print(f"CẢNH BÁO: thiếu trang tham khảo {path.name}", file=sys.stderr)
        return None
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    name, meta, body_start = key, {"Là gì": "", "Tra mục này khi": ""}, 0
    for i, l in enumerate(lines):
        if l.startswith("# ") and name == key:
            name = l[2:].strip()
            body_start = i + 1
            continue
        m = REF_META_RE.match(l)
        if m:
            meta[m.group(1)] = m.group(2).strip()
            body_start = i + 1
            continue
        if l.startswith("## "):
            break
    body = "\n".join(lines[body_start:]).strip()
    # Đếm số mẫu: tiêu đề cấp 3 nằm trong mục "Mẫu dùng ngay" (bỏ qua dòng trong khối mã).
    templates, in_fence, in_tpl = 0, False, False
    for l in lines:
        if l.strip().startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        if l.startswith("## "):
            in_tpl = l[3:].strip().lower().startswith("mẫu dùng ngay")
        elif in_tpl and l.startswith("### "):
            templates += 1
    return {"key": key, "name": name, "what": meta["Là gì"], "when": meta["Tra mục này khi"],
            "md": body, "raw": raw, "file": filename, "templates": templates}


def load_hub():
    path = REF_DIR / HUB_FILE
    if not path.exists():
        return ""
    lines = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(l for i, l in enumerate(lines) if not (i == 0 and l.startswith("# "))).strip()


SLIDE_TEXT_RE = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.S)


def slide_title(svg, role):
    """Tiêu đề slide là các dòng chữ cỡ lớn nhất. Slide mở tầng có một chữ số rất lớn, nên ghép "Tầng N: tên"."""
    items = []
    for attrs, content in SLIDE_TEXT_RE.findall(svg):
        m = re.search(r'font-size="([\d.]+)"', attrs)
        if m:
            items.append((float(m.group(1)), html.unescape(re.sub(r"<[^>]+>", "", content)).strip()))
    if not items:
        return ""
    sizes = sorted({sz for sz, _ in items}, reverse=True)
    at = lambda sz: " ".join(t for s, t in items if s == sz)
    if role == "section" and len(sizes) > 1 and at(sizes[0]).isdigit():
        return f"Tầng {at(sizes[0])}: {at(sizes[1])}"
    return at(sizes[0])


MONO_TEXT_RE = re.compile(r"<text\b([^>]*\bConsolas\b[^>]*)>(.*?)</text>", re.S)
MONO_ADVANCE = 0.5498  # bề rộng một ký tự Consolas, tính theo cỡ chữ


def fix_mono(svg):
    """Slide dựng theo Consolas. Máy không có Consolas (Mac, điện thoại) sẽ dùng phông đơn cách rộng hơn chừng 9%
    và chữ tràn khung. Ghi sẵn bề rộng đúng của từng dòng để máy nào cũng vẽ vừa khung."""
    def one(m):
        attrs, content = m.group(1), m.group(2)
        size = re.search(r'font-size="([\d.]+)"', attrs)
        text = " ".join(html.unescape(re.sub(r"<[^>]+>", "", content)).split())
        if not size or not text or "textLength" in attrs or "letter-spacing" in attrs:
            return m.group(0)
        attrs = attrs.replace("Consolas, 'Courier New', monospace", "Consolas, Menlo, 'DejaVu Sans Mono', 'Courier New', monospace")
        width = round(len(text) * MONO_ADVANCE * float(size.group(1)), 1)
        return f'<text{attrs} textLength="{width}" lengthAdjust="spacingAndGlyphs">{content}</text>'
    return MONO_TEXT_RE.sub(one, svg)


def load_slides():
    if not SLIDE_DIR.is_dir():
        return [], ""
    slides = []
    for p in sorted(SLIDE_DIR.glob("*.svg")):
        svg = p.read_text(encoding="utf-8")
        role = (re.search(r'data-pptx-page-role="([^"]*)"', svg) or [None, ""])[1]
        title = slide_title(svg, role)
        # Bỏ các thuộc tính chỉ dùng khi xuất PowerPoint để file index.html nhẹ hơn.
        svg = fix_mono(re.sub(r'\s+data-pptx-[\w-]+="[^"]*"', "", svg))
        slides.append({"title": title or p.stem, "role": role, "svg": svg.strip()})
    pptx = next(iter(sorted(SLIDE_DIR.glob("*.pptx"))), None)
    return slides, pptx.name if pptx else ""


DEMO_HEAD_RE = re.compile(r"^## (?:Mục (\d+) · )?(.+?)(?: \(slide ([\d,\s\-–]+)\))?$")


def slide_numbers(spec):
    """'10–11', '23-25', '30, 32' -> [10, 11], [23, 24, 25], [30, 32]."""
    nums = []
    for part in re.split(r"[,\s]+", (spec or "").strip()):
        if not part:
            continue
        a, _, b = part.replace("–", "-").partition("-")
        nums.extend(range(int(a), int(b or a) + 1))
    return nums


def load_demo_steps():
    """Đọc slides/data-demo.md thành mục Data demo: dòng "# ..." đầu là tên mục, đoạn trước tiêu đề "## " đầu tiên
    là lời dẫn, mỗi tiêu đề "## Mục N · Tên (slide a, b–c)" là một thẻ (số mục, tên, slide nào, markdown)."""
    if not DEMO_MD.exists():
        return {"title": "", "intro": "", "items": []}
    title, intro, items, cur = "Data demo", [], [], None
    for l in DEMO_MD.read_text(encoding="utf-8").splitlines():
        if cur is None and not intro and l.startswith("# "):
            title = l[2:].strip()
            continue
        m = DEMO_HEAD_RE.match(l)
        if m:
            cur = {"num": m.group(1) or "", "slides": slide_numbers(m.group(3)), "title": m.group(2).strip(), "md": []}
            items.append(cur)
            continue
        (cur["md"] if cur else intro).append(l)
    for it in items:
        it["md"] = "\n".join(it["md"]).strip()
    return {"title": title, "intro": "\n".join(intro).strip(), "items": items}


def load_demo():
    if not DEMO_DIR.is_dir():
        return []
    return [p.name for p in sorted(DEMO_DIR.iterdir()) if p.suffix in DEMO_TYPES and p.name != "README.md"]


def main():
    groups = []
    skills = []
    for folder, prefix, name, desc, audience in GROUPS:
        d = ROOT / folder
        if not d.is_dir():
            print(f"CẢNH BÁO: thiếu thư mục {folder}", file=sys.stderr)
            continue
        files = sorted(p for p in d.glob("*.md"))
        for p in files:
            skills.append(parse_skill(p, folder))
        groups.append({"key": folder, "prefix": prefix, "name": name, "desc": desc,
                       "audience": audience, "count": len(files)})
    guide_path = ROOT / "HUONG-DAN-SU-DUNG.md"
    guide = guide_path.read_text(encoding="utf-8") if guide_path.exists() else ""
    guide2_path = ROOT / "huong-dan-tao-skill-chatgpt.md"
    guide2 = guide2_path.read_text(encoding="utf-8") if guide2_path.exists() else ""
    refs = [r for r in (load_ref(k, f) for k, f in REF_PAGES) if r]
    slides, slide_pptx = load_slides()
    demo = load_demo()
    demo_steps = load_demo_steps()
    data = {"groups": groups, "skills": skills, "guide": guide, "guideChatgpt": guide2,
            "refs": refs, "hub": load_hub(), "slides": slides, "slidePptx": slide_pptx, "demo": demo, "demoSteps": demo_steps,
            "total": len(skills), "builtAt": __import__("datetime").date.today().isoformat()}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", payload)
    if LOGO.exists():
        src = "data:image/jpeg;base64," + base64.b64encode(LOGO.read_bytes()).decode()
        html = html.replace("<!--__FAVICON__-->", f'<link rel="icon" type="image/jpeg" href="{src}">')
        html = html.replace("<!--__BRAND_MARK__-->", f'<img class="brand-mark logo" src="{src}" alt="Wir Group" height="34">')
    else:
        html = html.replace("<!--__FAVICON__-->", "").replace("<!--__BRAND_MARK__-->", '<div class="brand-mark">W</div>')
    OUT.write_text(html, encoding="utf-8")
    print(f"Đã tạo {OUT.name}: {len(refs)} trang tham khảo ({', '.join(r['name'] for r in refs)}), "
          f"{len(skills)} skill template, {len(groups)} nhóm, {len(slides)} slide, {len(demo)} file demo, "
          f"{len(demo_steps['items'])} mục data demo, "
          f"{OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
