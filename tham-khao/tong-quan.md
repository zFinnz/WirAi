# Tổng quan

## Lộ trình 4 tầng

Coi ChatGPT là một nhân viên mới rất giỏi: đọc nhanh, viết nhanh, nhưng chưa biết gì về công ty. Dùng ChatGPT cho công việc là đào tạo nhân viên đó, đi đúng 4 bước như khi nhận một người mới vào phòng.

| Tầng | Với nhân viên mới | Với ChatGPT | Tính năng ChatGPT |
|---|---|---|---|
| 1. [Instructions](#instructions) | Ngày đầu đi làm: phát hồ sơ nhập môn và nội quy | Khai báo một lần: tôi là ai, luật chung | Custom Instructions, Project, Memory |
| 2. [Prompt](#prompt) | Mỗi ngày: giao từng việc bằng phiếu giao việc rõ ràng | Giao việc theo công thức 4 phần, kiểm chứng kết quả | Chat, tải file, phân tích dữ liệu |
| 3. [Skill](#skill) | Việc lặp lại: dán tờ quy trình chuẩn lên tường, ai làm cũng ra kết quả giống nhau | Đóng gói quy trình thành skill để gọi lại | Skills |
| 4. [Plugin](#plugin) | Cấp thẻ ra vào và chìa khóa tủ hồ sơ, rồi đóng thùng đồ nghề bàn giao cho người kế nhiệm | Nối Gmail, Drive. Gộp skill, tài liệu và app thành plugin của phòng | Plugins, ChatGPT Work, Scheduled tasks |

Sau 4 tầng là phần nâng cao [AI tự thao tác](#plugin/plugin-nang-cao-ai-tu-thao-tac): Browser extension, Computer use và Dots.

#### Đừng nhảy cóc

- Instructions viết kém thì prompt nào cũng phải dặn lại từ đầu.
- Prompt chưa vững thì không biết nên đóng gói gì vào skill.
- Skill chưa chuẩn thì plugin chỉ nhân bản cái sai nhanh hơn.

## Thông tin nào đặt ở đâu

Trước khi viết gì cho ChatGPT, xác định thông tin đó thuộc loại nào.

| Thông tin | Đặt ở | Vì sao |
|---|---|---|
| "Tôi là nhân viên Sale của Wir Group, phụ trách khách sỉ" | [Instructions](#instructions) | Đúng cho mọi việc |
| "TPCN không dùng từ 'điều trị'; không bịa số" | [Instructions](#instructions) | Luật chung của phòng |
| Số liệu đơn hàng tháng này, yêu cầu của một khách cụ thể | [Prompt](#prompt) | Chỉ dùng 1 lần |
| Các bước viết lịch nội dung 14 ngày | [Skill](#skill) | Quy trình của 1 việc lặp lại |
| Thư trong Gmail, file đơn hàng trên Drive | [Plugin](#plugin) | ChatGPT tự đọc từ nguồn, không phải dán |
| Một việc phòng ban nào cũng làm, đã có bản viết sẵn | [Skill template](#skill-template) | Không cần viết lại từ đầu |

## Ba cách dùng khác nhau thế nào

| | Instructions | Prompt | Skill |
|---|---|---|---|
| Ví như | Nội quy | Phiếu giao việc hôm nay | Tờ quy trình chuẩn cho 1 việc |
| Áp dụng | Mọi việc | 1 lần | Mỗi lần gặp đúng loại việc đó |
| Độ dài | Ngắn, chỉ điều luôn đúng | Vừa đủ cho việc này | Chi tiết, không sợ dài |
| Ai gọi | Tự áp dụng | Mình gõ | ChatGPT tự chọn, hoặc mình gọi bằng `@` |

## Sáu nguyên tắc khi dùng AI

1. **Chống bịa.** Chỉ dùng dữ liệu được cấp. Gắn nhãn `[DATA THẬT]`, `[SUY LUẬN]`, `[CẦN ĐIỀN]`. "Chưa đủ dữ liệu" tốt hơn một con số nghe hợp lý.
2. **Người duyệt cuối.** AI làm nháp, con người ký và bấm gửi. Người gửi chịu trách nhiệm, không đổ cho AI.
3. **Bảo mật.** Không dán giá vốn, hợp đồng có điều khoản bảo mật, thông tin cá nhân nhân viên, mật khẩu, tài liệu đóng dấu MẬT. Thay tên thật bằng tên chung trước khi dán.
4. **Kiểm chứng.** Đối chiếu số liệu, ngày tháng, tên riêng, trích dẫn với nguồn gốc.
5. **Tiêu chuẩn viết bằng số hoặc hành vi,** không bằng tính từ.
6. **Lưu kết quả thành file.** Đầu ra lần trước là đầu vào lần sau.

## Ba điều không đổi

Công cụ sẽ còn thay đổi nhiều. Ba điều sau không đổi, nắm được thì công cụ nào ra sau cũng dùng an toàn được:

1. AI làm nháp, con người duyệt.
2. Quyền cấp từng nấc: đọc → ghi → gửi.
3. "Chưa đủ dữ liệu" tốt hơn một con số bịa.

> **Mẹo:** Việc tiếp theo: chọn một việc lặp lại của phòng bạn và đi lại đủ 4 tầng với chính việc đó.

## Dữ liệu demo để tập

Bộ dữ liệu **DEMO** của Wir Group, dùng với các mẫu trên trang [Prompt](#prompt) và [Plugin](#plugin). Đây không phải số liệu kinh doanh thật. Nhấp vào tên tài liệu để tải về: file Excel mở bằng Excel hoặc Google Sheets, file Word mở bằng Word hoặc Google Docs.

| Tài liệu | Nội dung | Tập với |
|---|---|---|
| [Đơn hàng tháng 7 (Excel)](du-lieu-demo/don-hang-demo.xlsx) | 40 dòng đơn hàng tháng 7, 6 cột | [Phân tích file số liệu](#prompt/prompt-phan-tich-file-so-lieu), [đọc và ghi file trên Drive](#plugin/plugin-doc-va-ghi-file-tren-drive) |
| [Review và tin nhắn khách (Word)](du-lieu-demo/review-va-tin-nhan-khach.docx) | 20 review và 10 tin nhắn hỏi trước khi mua | [Rút insight](#prompt/prompt-rut-insight-tu-review-va-tin-nhan-khach) |
| [Danh sách 12 lead (Excel)](du-lieu-demo/danh-sach-lead.xlsx) | 12 lead ngành làm đẹp và bán sỉ | [Chấm điểm lead](#prompt/prompt-cham-diem-lead-va-soan-tin-tiep-can) |
| [Ghi chú trao đổi lead (Word)](du-lieu-demo/ghi-chu-trao-doi-lead.docx) | Ghi chú trao đổi với 5 lead | [Soạn tin tiếp cận](#prompt/prompt-cham-diem-lead-va-soan-tin-tiep-can), [phép thử plugin](#plugin/plugin-phep-thu-truoc-khi-ban-giao) |
| [Chính sách giá sỉ (Word)](du-lieu-demo/chinh-sach-gia-si-demo.docx) | Chiết khấu sỉ 4 mức, điều chưa có chính sách | [Trả lời khách hỏi giá sỉ](#prompt/prompt-tra-loi-khach-hoi-gia-si) |
| [Bản ghi họp Phòng Kinh doanh (Word)](du-lieu-demo/transcript-hop-demo.docx) | Cuộc họp kế hoạch tháng 8, có chỗ chưa rõ ai làm | [Biên bản họp](#prompt/prompt-bien-ban-hop-va-bang-dau-viec) |
| [Đáp án (Word)](du-lieu-demo/dap-an.docx) | Số đối chiếu và các bẫy cài sẵn | Tự chấm sau khi làm |

> **Lưu ý:** Mỗi file có lỗ hổng cố ý: ô để trống, lead thiếu thông tin, khách đòi điều vượt chính sách, review lệch khen. Đạt là khi ChatGPT ghi `[CẦN ĐIỀN]`, chuyển quản lý, hoặc trả lời "chưa đủ dữ liệu", thay vì tự điền cho đủ. Làm xong mới mở đáp án.
