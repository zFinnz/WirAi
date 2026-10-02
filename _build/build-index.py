#!/usr/bin/env python3
"""Tạo index.html từ các file skill .md.

Chạy lại mỗi khi sửa hoặc thêm skill:
    python3 _build/build-index.py

Script đọc mọi thư mục nhóm, trích mã, tên, "Dùng khi", "Kết quả", "Không dùng khi"
và toàn bộ nội dung, rồi nhúng vào template.html thành một file index.html tự chứa,
mở được bằng cách nhấp đúp, không cần máy chủ hay internet.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "template.html"
OUT = ROOT / "index.html"

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
    data = {"groups": groups, "skills": skills, "guide": guide, "guideChatgpt": guide2,
            "total": len(skills), "builtAt": __import__("datetime").date.today().isoformat()}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", payload)
    OUT.write_text(html, encoding="utf-8")
    print(f"Đã tạo {OUT.name}: {len(skills)} skill, {len(groups)} nhóm, {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
