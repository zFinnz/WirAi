# Review bộ slide "Lộ trình đào tạo AI trên ChatGPT" · 09/10/2026

Đối chiếu từng slide với ChatGPT thật (tài khoản Plus, chế độ Instant, đã đăng nhập) và giao diện ChatGPT ngày 09/10/2026. File đã sửa: `Lo-trinh-dao-tao-AI-ChatGPT-Wir-Group-v2.pptx` (bản gốc giữ nguyên).

## Tóm tắt

| Nhóm | Slide | Kết luận |
|---|---|---|
| Đã lỗi thời, đã sửa | 4, 12, 14, 15, 16, 17, 18, 28 | Bẫy "ChatGPT bịa" không còn xảy ra; tên mức quyền plugin đổi |
| Thiếu một nơi lưu, đã bổ sung | 5 | Thêm Library (kho file dùng chung mọi chat) |
| Đúng, có bằng chứng, giữ nguyên | 2, 9, 10, 11, 20, 21, 22, 31 | Tên menu, demo Project, cơ chế Skill, Plugin Creator đều khớp |
| Khái niệm, không phụ thuộc phiên bản | 1, 3, 6, 7, 8, 13, 19, 26, 27, 34, 35 | Giữ nguyên |
| Chưa tự kiểm được | 23, 24, 29, 30, 33 | Cần anh/chị làm thử, xem mục cuối |

## Bằng chứng đã chạy

1. **Chat "Phân tích doanh số nhân viên"** (anh/chị chạy trước): tải file, gõ "Phân tích doanh số theo từng nhân viên bán hàng". ChatGPT đếm 40 giao dịch, nêu 6 cột, báo thiếu cột nhân viên, phân tích theo kênh, tổng 147.300.000 đ đúng, đề xuất thêm cột Nhan_vien. Bẫy cũ của slide 16 không còn tác dụng.
2. **Chat "Tính lợi nhuận sản phẩm"**: dán 40 dòng dạng chữ, hỏi lợi nhuận theo sản phẩm. ChatGPT không bịa giá vốn, tính đúng doanh thu từng sản phẩm, xin giá vốn. Hỏi tiếp "Vì sao Shopee nhiều đơn nhất mà doanh thu thấp?": ChatGPT tính nhẩm sai bảng theo kênh và nói chắc, còn "đính chính" ngược số đúng của lượt trước.

   | Kênh | ChatGPT nói | File thật |
   |---|---|---|
   | Đại lý sỉ | 6 đơn, 96,71 tr | 7 đơn, 106,71 tr |
   | Website | 11 đơn, 16,44 tr | 10 đơn, 15,25 tr |
   | Shopee | 11 đơn, 9,16 tr | 11 đơn, 10,35 tr |
   | Fanpage | 5 đơn, 8,31 tr | 6 đơn, 9,35 tr |
   | Zalo | 7 đơn, 6,54 tr | 6 đơn, 5,64 tr |

   Đây là bẫy mới cho slide 16: tải file thì ChatGPT chạy code nên đúng, dán chữ thì tính nhẩm. Phần nguyên nhân nó tự tách "cần kiểm chứng thêm" khỏi số liệu, đúng quy tắc 4.
3. **Chat "Hỏi giá sỉ Elasten"**: prompt một dòng "Trả lời spa hỏi giá sỉ Elasten." ChatGPT không bịa giá, không hứa vượt bảng, không nhắc bà bầu. Nó viết tin chung chung, thêm "collagen Đức" không có nguồn, emoji ❤️🌷, không dùng bảng giá sỉ, rồi hỏi lại số lượng và giá nhập. Ba dòng "kết quả" cũ của slide 14 sai, đã thay bằng kết quả thật.
4. **Chat "Xác định công ty khách hàng sản phẩm"**: chat mới ngoài Project, hỏi "Tôi làm ở công ty nào, phụ trách khách nào, bán sản phẩm gì?". ChatGPT trả lời đúng Wir Group, khách đại lý miền Bắc, 8 nhãn hàng, trích nguồn file ho-so-sale.md trong Library. Câu "Mỗi chat mới, ChatGPT lại quên bạn là ai" ở slide 4 sai với tài khoản đã khai báo.
5. **Chat "Viết bài Facebook Elasten"** trong Project Marketing: bài có câu bắt buộc, số liệu +28% có nguồn, giá [CẦN ĐIỀN], ChatGPT tự gắn nhãn [DATA THẬT]/[SUY LUẬN], tự thêm mục "Tự rà", và có chip nguồn bấm được tới file. Hỏi "Chỗ nào bạn tự suy đoán mà tài liệu không nói?": nó liệt kê 4 chỗ, phân loại, chỉ tới "ho-so-elasten.md, mục 6, dòng 46–50". Slide 10, 11 đúng; slide 17 cách 1 và cách 4 cập nhật.
6. **Chat "Tìm hiểu Skills ChatGPT"**: ChatGPT (có skill-creator cài sẵn) xác nhận chọn skill theo name và description, chỉ tải SKILL.md khi khớp (progressive disclosure), gọi được bằng @, tạo skill từ chat đang làm dở bằng cách yêu cầu đóng gói, hoặc Plugins → Skills → Create. Slide 20, 21, 22 đúng.
7. **Giao diện**: thanh bên có Scheduled, Library, Plugins; đầu trang có Chat / Work; Settings → Personalization có Custom instructions, Memory, Library search, Connector search; Settings → Data controls có "Improve the model for everyone"; Plugins → Skills có tab riêng; Plugin Creator đã cài; Settings → Plugins → bấm từng plugin → Permission có 4 mức: Always ask, Allow read-only tools, Allow low-risk tools (mặc định), Allow all tools (gắn nhãn Elevated risk). Ô Default permission chung chỉ có 3 mức đầu.
8. **Tài liệu OpenAI** (help.openai.com, bài Projects in ChatGPT): project instructions ghi đè custom instructions. Slide 5 đúng.

## Từng slide

| Slide | Đánh giá | Thay đổi trong v2 |
|---|---|---|
| 1 | Bìa, đúng | Không |
| 2 | Tên tính năng khớp giao diện (Plugins, Work, Scheduled) | Không |
| 3 | Ẩn dụ nhân viên mới, rõ | Không |
| 4 | Câu "mỗi chat mới lại quên" sai với tài khoản đã khai báo | Đổi thành "Chưa khai báo, ChatGPT không biết bạn là ai…"; mục 1 thêm Library; ghi chú kể kết quả chạy thử |
| 5 | Thiếu Library, nơi thứ tư ChatGPT tự tìm file | Cột Memory ghi thêm Library; ghi chú giải thích và cảnh báo file nhạy cảm |
| 6, 7, 8 | Đúng | Không |
| 9 | Đường dẫn Data controls đúng | Không |
| 10 | Kết quả thật 08/10, vẫn đúng hôm nay | Không |
| 11 | Phép thử chống bịa đạt | Không |
| 12 | "Phải hỏi lại 4–5 lượt" quá đà | "ChatGPT phải đoán hoặc hỏi lại, mất thêm lượt"; kỹ thuật 2 đổi tên |
| 13 | Đúng | Không |
| 14 | Ba dòng kết quả prompt tồi không còn xảy ra | Thay bằng kết quả thật 09/10: hỏi lại số lượng, thêm "collagen Đức" và emoji, bỏ qua bảng giá sỉ và câu bà bầu |
| 15 | "Cho AI hỏi lại" nay ChatGPT tự làm | Đổi thành "Chốt số câu hỏi lại", câu mẫu "hỏi tôi tối đa 3 câu, rồi mới làm" |
| 16 | Bẫy cũ không còn; bẫy mới là dán chữ thay vì tải file | Viết lại 4 quy tắc và toàn bộ hộp demo với số thật |
| 17 | Ctrl+F thay bằng chip nguồn; cách 4 đã kiểm | Cập nhật cách 1, 2, 4 |
| 18 | Câu hỏi chốt 1 mất tính bất ngờ | Đổi thành "Dán 40 dòng vào chat hay tải file lên?" |
| 19–22 | Cơ chế Skill khớp lời ChatGPT và tab Skills | Không |
| 23, 24, 25 | Chưa tự kiểm bước "đóng gói thành skill" và "tự kích hoạt ở phiên mới" | Không |
| 26, 27 | Khớp danh mục Plugins | Không |
| 28 | Bốn mức đúng, tên chính xác là Always ask / Allow read-only tools / Allow low-risk tools / Allow all tools; mặc định là low-risk | Sửa tên mức, đường dẫn Permission của từng plugin; ghi chú nhắc đổi Gmail về Always ask |
| 29 | Chưa kiểm màn hình OAuth Gmail (tôi không được phép cấp quyền) | Không |
| 30 | Trang Scheduled có; task theo sự kiện và "tạm dừng chờ duyệt" chưa kiểm | Không |
| 31 | Plugin Creator có trong danh mục và đã cài | Không |
| 32 | Phụ thuộc 28, 29 | Không |
| 33 | Chưa thấy tên Browser extension, Computer use, Dots trong giao diện web | Không |
| 34, 35 | Đúng | Không |

## Việc cần anh/chị làm thử (tôi không tự làm được hoặc không nên làm)

1. **Slide 23–24, tạo skill**: trong Project có tài liệu CH Alpha Plus, chat tay 5 lượt như slide 23 rồi gõ "Hãy đóng gói cách làm vừa rồi thành một skill tên tom-tat-tai-lieu". Sau đó mở chat mới, tải tài liệu Lactobact Intima, chỉ gõ "Tóm tắt tài liệu này". Nhìn: ChatGPT có đề nghị cài skill không, phiên mới có hiện skill được gọi không, gõ @ có gợi ý tom-tat-tai-lieu không. Việc này tạo thêm skill vào tài khoản nên tôi không tự làm.
2. **Slide 29, nối Gmail**: bấm Connect Gmail trong Plugins với tài khoản cá nhân, chụp màn hình danh sách quyền Google hiện ra, rồi gỡ ngay. Nhìn: quyền có gộp đọc, soạn, gửi không; có cảnh báo "ứng dụng chưa xác minh" không.
3. **Slide 30**: trong Scheduled, thử tạo một task "Mỗi thứ Hai 7h đọc file don-hang-demo.csv trên Drive và lập bảng doanh thu theo sản phẩm". Nhìn: có tùy chọn kích hoạt theo sự kiện (thư Gmail mới) không; khi task cần ghi file có dừng hỏi không.
4. **Slide 33**: mở ứng dụng ChatGPT desktop hoặc Work mode, tìm tên thật của ba tính năng Browser extension, Computer use, Dots và nút cho phép.
