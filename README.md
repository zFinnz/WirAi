# Bộ kỹ năng AI cho doanh nghiệp

> **Người dùng không chuyên: mở file `index.html` bằng cách nhấp đúp.** Trang đó có danh mục theo phòng ban, ô tìm kiếm, xem nội dung từng skill, nút sao chép và tải về. File README này và HUONG-DAN-SU-DUNG.md là bản nguồn để người quản lý bộ skill chỉnh sửa; sau khi sửa bất kỳ file .md nào, chạy `python3 _build/build-index.py` để tạo lại `index.html`.

> Thư viện kỹ năng (skill) tiếng Việt cho mọi phòng ban. Mỗi skill là **một file độc lập**: người dùng chọn đúng file, dán vào ChatGPT, Claude hoặc Gemini, điền vài dòng bối cảnh công ty và dùng ngay. Không cần cài đặt, không phụ thuộc file khác.

**Trạng thái:** đợt 2, 119 skill trong 12 nhóm. Mỗi skill qua kiểm tra bố cục 6 phần, độ dài 150 đến 250 dòng, không tham chiếu file ngoài.

**Nguồn chắt lọc:** `ai-business-skills` (OPA, 144 skill VN), `business-skills` (viethahong, 61 skill VN), `marketingskills` (Corey Haines, 50 skill EN), `ces-plugin-business-builder` (CES, 191 mẫu tài liệu vận hành) và `thu-vien-agent-tham-chieu` (CES, 12 agent văn phòng).

---

## Cách dùng trong 3 bước

1. Mở bảng danh mục bên dưới, tìm phòng ban của bạn, chọn skill theo cột **Dùng khi**.
2. Mở file, dán toàn bộ nội dung vào công cụ AI theo [HUONG-DAN-SU-DUNG.md](HUONG-DAN-SU-DUNG.md).
3. Điền phần **Bối cảnh công ty** ở đầu file (chỉ cần làm một lần cho mỗi skill), rồi nêu yêu cầu.

---

## Quy ước chung cho mọi skill

| Hạng mục | Quy ước |
|---|---|
| Ngôn ngữ | Tiếng Việt có dấu. Thuật ngữ dịch sang tiếng Việt, kèm tiếng Anh trong ngoặc ở lần xuất hiện đầu. Ví dụ: chi phí thu hút khách hàng (CAC). |
| Bố cục | 6 phần cố định: 0 Bối cảnh công ty, 1 Vai trò, 2 Thu thập thông tin, 3 Nguyên tắc, 4 Cấu trúc kết quả, 5 Danh sách kiểm tra. |
| Độ dài | 150 đến 250 dòng mỗi file. |
| Hỏi trước khi làm | Tối đa 4 câu hỏi một lượt. Thiếu thông tin thì hỏi, không đoán. Hỏi xong, tóm tắt và đề xuất cách làm trong 3 đến 5 dòng, chờ xác nhận rồi mới làm. |
| Biểu mẫu | Nếu người dùng dán mẫu đang dùng trong công ty, kết quả phải khớp mẫu đó. Chỉ dùng cấu trúc của skill khi không có mẫu. |
| Kết quả | Luôn có cấu trúc rõ, bảng và danh sách, kết thúc bằng 3 đến 5 việc cần làm tiếp. |
| Số liệu | Chuẩn so sánh (benchmark) thị trường Việt Nam. Không bịa số, mọi con số ước tính phải ghi rõ là giả định. Chỗ thiếu dữ liệu ghi `[cần bổ sung]`. |
| Tên file | `[MÃ]-[ten-khong-dau].md`, ví dụ `MKT-01-ke-hoach-marketing.md`. |

---

## Danh mục skill (119 skill, 12 nhóm)

Cột **Nguồn** ghi skill gốc đã chắt lọc: OPA = ai-business-skills, BS = business-skills, CH = marketingskills (Corey Haines), CES = ces-plugin-business-builder, VP = thu-vien-agent-tham-chieu, Mới = viết mới từ kiến thức chung. Tên file nằm trong thư mục phòng ban tương ứng, bắt đầu bằng mã skill.

### 1. Marketing và nội dung (`marketing/`, mã MKT) — 25 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| MKT-01 | Kế hoạch marketing | Cần kế hoạch marketing cho một quý hoặc một năm, cả bản đầy đủ và bản 1 trang cho lãnh đạo | Kế hoạch 7 phần: tình hình, chiến lược, nội dung, kênh và ngân sách, KPI 3 kịch bản, rủi ro, lịch triển khai | OPA 00, CH marketing-plan |
| MKT-02 | Chân dung và insight khách hàng | Chưa hiểu khách đủ sâu để viết nội dung hoặc chọn tệp quảng cáo | Chân dung 3 tầng, bản đồ nỗi đau, danh sách lý do từ chối, kho ngôn ngữ của khách | OPA 09, CH customer-research |
| MKT-03 | Nghiên cứu đối thủ | Cần biết đối thủ đang làm gì và mình đứng ở đâu | Bản đồ định vị, SWOT, bảng so sánh kênh và nội dung, khoảng trống khai thác | OPA 08, BS competitor-analysis |
| MKT-04 | Định vị và thông điệp thương hiệu | Chưa trả lời được vì sao khách chọn mình thay vì đối thủ | Tuyên bố định vị, ma trận khác biệt, 3 thông điệp cốt lõi | OPA 58, BS brand-building |
| MKT-05 | Giọng nói thương hiệu | Nội dung mỗi người viết một kiểu, cần chốt một giọng chung | Bảng giọng điệu, từ nên dùng và cấm dùng, 5 ví dụ mẫu | OPA 35 |
| MKT-06 | Tính KPI ngược và phân bổ ngân sách | Có mục tiêu doanh thu, cần biết phải chi bao nhiêu và cần bao nhiêu khách | Chuỗi phễu tính ngược, ngân sách theo kênh và tháng, ngưỡng cắt lỗ | OPA 10, OPA 61 |
| MKT-07 | Lịch nội dung tháng | Cần lịch đăng bài cả tháng cho nhiều kênh | Trụ cột nội dung và tỉ lệ, lịch theo ngày và khung giờ, ma trận tái sử dụng | OPA 01 |
| MKT-08 | Bài đăng mạng xã hội | Cần viết bài đăng tự nhiên cho Facebook, TikTok, Zalo, Instagram | 2 phương án mở bài khác hướng, nội dung, hashtag, ghi chú chọn bản | OPA 37, BS social-media |
| MKT-09 | Kịch bản video ngắn | Cần kịch bản TikTok, Reels, Shorts | Mở bài 3 giây, cấu trúc theo giây, 2 biến thể thử nghiệm | OPA 04 |
| MKT-10 | Nội dung quảng cáo trả phí | Cần nội dung chạy quảng cáo Facebook, TikTok, Google | 6 biến thể theo 3 tầng phễu, đúng giới hạn ký tự và chính sách | OPA 05, CH ad-creative |
| MKT-11 | Kế hoạch và cấu trúc quảng cáo | Sắp chạy quảng cáo, cần kế hoạch chi tiêu và cấu trúc tài khoản | Phân bổ thử nghiệm, mở rộng, tiếp thị lại; quy tắc đặt tên; ngân sách theo tuần | OPA 52, OPA 54, BS paid-ads |
| MKT-12 | Chẩn đoán hiệu suất quảng cáo | Số liệu đang xấu, cần biết tại sao và sửa gì trong 48 giờ | Chẩn đoán 5 lớp, điểm sức khỏe tài khoản, kế hoạch hành động | OPA 03, OPA 21 |
| MKT-13 | Chuỗi email và Zalo OA | Cần chuỗi tin nhắn chào mừng, nuôi dưỡng, khuyến mãi, kéo lại khách cũ | Luồng tự động, tiêu đề, tần suất, biến thể thử nghiệm | OPA 14, BS zalo-oa-strategy, CH emails |
| MKT-14 | Trang đích và tối ưu chuyển đổi | Cần xây trang bán hàng mới hoặc trang đang có không ra đơn | Cấu trúc từng khối, nội dung, chẩn đoán 7 chiều, danh sách sửa theo ưu tiên | OPA 12, OPA 68, CH cro |
| MKT-15 | SEO và tìm kiếm bằng AI | Muốn tăng lượt truy cập tự nhiên từ Google và các công cụ AI | Kiểm tra kỹ thuật, cụm từ khóa, cấu trúc bài, dữ liệu có cấu trúc | OPA 32, CH seo-audit, CH ai-seo |
| MKT-16 | Hợp tác KOL, KOC và nội dung từ khách hàng | Cần thuê người ảnh hưởng hoặc nhờ khách và nhân viên quay video | Tiêu chí chọn người, bản hướng dẫn quay, điều khoản, cách đo hiệu quả | OPA 06, BS koc-marketing, CH influencer-marketing |
| MKT-17 | Kịch bản phát trực tiếp bán hàng | Sắp phát trực tiếp trên Facebook, TikTok, Shopee | Kịch bản theo phút, ưu đãi theo mốc, phân vai, danh sách chuẩn bị | BS livestream-selling |
| MKT-18 | Vận hành gian hàng sàn thương mại điện tử | Mở mới hoặc tối ưu gian hàng Shopee, TikTok Shop, Lazada | Tối ưu trang sản phẩm, lịch khuyến mãi sàn, chỉ số theo dõi | BS ecommerce-marketplace, BS tiktok-shop-strategy |
| MKT-19 | Thiết kế gói bán và khuyến mãi | Gói bán chưa đủ hấp dẫn, cần đóng gói lại | Chồng giá trị, quà tặng, bảo hành, lý do gấp, bán thêm và bán xuống | OPA 31, CH offers |
| MKT-20 | Chương trình giới thiệu khách hàng | Muốn khách cũ kéo khách mới | Cơ chế thưởng, mức thưởng, cách theo dõi, chống gian lận | OPA 18, CH referrals |
| MKT-21 | Yêu cầu thiết kế hình ảnh | Cần giao việc cho người thiết kế: banner, bộ ảnh, carousel | Mục tiêu hình ảnh, bố cục, chữ trên ảnh, màu, kích thước từng kênh | OPA 41, OPA 42, OPA 43 |
| MKT-22 | Báo cáo và tổng kết marketing | Cần báo cáo tuần cho lãnh đạo, báo cáo tháng, hoặc tổng kết sau chiến dịch | Tóm tắt 1 trang, số so với mục tiêu, nhận định, bài học, đề xuất | OPA 07, OPA 63 |
| MKT-23 | Bản đồ hành trình khách hàng | Cần vẽ các điểm chạm từ biết đến mua lại, tìm chỗ khách rơi rụng | Bảng hành trình theo giai đoạn: điểm chạm, cảm xúc, rào cản, cơ hội, chỉ số đo | CES ban-do-hanh-trinh-khach-hang |
| MKT-24 | Quy chuẩn nhận diện thương hiệu | Cần chốt logo, màu, chữ, phong cách ảnh để mọi thiết kế giống nhau | Bộ quy chuẩn: logo, màu, chữ, hình ảnh, ứng dụng theo kênh, việc cấm | OPA 46, CES huong-dan-nhan-dien-thuong-hieu |
| MKT-25 | Xử lý khủng hoảng truyền thông | Thương hiệu bị tấn công trên mạng, chiến dịch gây phản ứng xấu | Phân cấp mức độ, quy trình 4 giờ đầu, mẫu phản hồi, ai được phát ngôn, hậu kiểm | OPA 66, CES quy-trinh-xu-ly-khung-hoang |

### 2. Bán hàng (`ban-hang/`, mã SAL) — 13 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| SAL-01 | Quy trình bán hàng và quản lý phễu | Khách bị rơi rụng, mỗi nhân viên bán một kiểu, cần quy trình chung | Các giai đoạn phễu, tiêu chí chuyển giai đoạn, kịch bản từng bước, quy tắc theo dõi | BS crm-sales-strategy, CH revops |
| SAL-02 | Chấm điểm khách hàng tiềm năng | Nhiều khách hỏi nhưng không biết ưu tiên ai | Bảng tiêu chí chấm điểm, phân nhóm nóng, ấm, lạnh, hành động cho mỗi nhóm | BS lead-scoring |
| SAL-03 | Tìm kiếm khách hàng doanh nghiệp | Cần danh sách khách doanh nghiệp để tiếp cận | Chân dung khách lý tưởng, nguồn tìm, bảng danh sách, phân loại | OPA 33, CH prospecting |
| SAL-04 | Email và tin nhắn chào hàng lạnh | Cần tiếp cận khách chưa quen qua email, Zalo, LinkedIn | Chuỗi 4 đến 6 bước, tiêu đề, cách cá nhân hóa, lịch gửi | CH cold-email, BS sales-email-templates |
| SAL-05 | Kịch bản tư vấn và chốt đơn | Nhân viên cần kịch bản gọi điện, nhắn tin, tư vấn trực tiếp | Kịch bản mở đầu, hỏi nhu cầu, trình bày, chốt, theo dõi sau | BS crm-sales-strategy, Mới |
| SAL-06 | Xử lý từ chối | Khách nói đắt, để suy nghĩ, đang dùng bên khác | Bảng từ chối và cách đáp, câu hỏi đào sâu, bằng chứng đi kèm | CH sales-enablement, BS crm-sales-strategy |
| SAL-07 | Bộ tài liệu bán hàng | Cần hồ sơ năng lực, tờ giới thiệu 1 trang, bảng so sánh với đối thủ | Từng tài liệu có cấu trúc, điểm mạnh có bằng chứng, chỗ mình thua | OPA 71, CH sales-enablement |
| SAL-08 | Báo giá và đề xuất hợp tác | Cần gửi báo giá hoặc đề xuất cho khách doanh nghiệp | Cấu trúc đề xuất, cách trình bày giá, điều khoản, bước tiếp theo | CH sales-enablement, Mới |
| SAL-09 | Chăm sóc sau bán và bán thêm | Khách mua một lần rồi không quay lại | Lịch chăm sóc theo mốc, tín hiệu sắp rời bỏ, kịch bản bán thêm | OPA 69, BS churn-prevention |
| SAL-10 | Phân nhóm khách hàng theo RFM | Có dữ liệu giao dịch, cần biết ai là khách VIP, ai sắp mất | Bảng phân nhóm theo lần mua gần nhất, tần suất, giá trị; hành động từng nhóm | BS crm-rfm-analysis |
| SAL-11 | Phát triển và chăm sóc đại lý | Bán qua đại lý, nhà phân phối, cần chính sách và quy trình | Chính sách chiết khấu theo bậc, quy trình tuyển đại lý, lịch chăm sóc | Mới |
| SAL-12 | Báo cáo bán hàng | Cần báo cáo tuần hoặc tháng về doanh số, phễu, tỉ lệ chốt | Bảng số so với mục tiêu, phân tích theo nhân viên và sản phẩm, đề xuất | BS periodic-reporting |
| SAL-13 | Sổ tay bán hàng cho người mới | Cần một tài liệu tổng hợp để đào tạo nhân viên bán hàng mới trong tuần đầu | Sổ tay: sản phẩm, khách, quy trình, kịch bản, từ chối, công cụ, quy định, lộ trình học 2 tuần | CES so-tay-ban-hang |

### 3. Chăm sóc khách hàng (`cham-soc-khach-hang/`, mã CS) — 10 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| CS-01 | Quy trình và tiêu chuẩn chăm sóc khách hàng | Cần chuẩn hóa cách tiếp nhận, phản hồi, chuyển tuyến | Quy trình, thời gian phản hồi cam kết, quy tắc ứng xử, giọng điệu | BS customer-support-framework |
| CS-02 | Kịch bản xử lý tình huống | Khiếu nại, đổi trả, hoàn tiền, giao hàng chậm, khách giận | Kịch bản từng tình huống, câu nên nói và không nên nói, khi nào chuyển cấp trên | BS customer-support-framework, OPA 66 |
| CS-03 | Bộ câu hỏi thường gặp và kịch bản chatbot | Cần tự động trả lời câu hỏi lặp lại trên Zalo, Facebook, website | Danh sách câu hỏi theo nhóm, câu trả lời chuẩn, luồng chatbot | BS chatbot-faq-builder |
| CS-04 | Phân tích phản hồi khách hàng | Có nhiều đánh giá, bình luận, tin nhắn cần tổng hợp | Phân loại cảm xúc, chủ đề nổi bật, vấn đề lặp lại, đề xuất cải thiện | BS sentiment-analysis |
| CS-05 | Khảo sát hài lòng và chỉ số NPS | Cần đo mức độ hài lòng và sẵn sàng giới thiệu | Bộ câu hỏi, cách gửi, cách đọc kết quả, hành động theo nhóm | BS customer-research, CH customer-research |
| CS-06 | Giữ chân và kéo lại khách rời bỏ | Khách ngừng mua, hủy gói, không phản hồi | Hệ thống tín hiệu cảnh báo, kịch bản kéo lại, ưu đãi cứu vãn | OPA 69, CH churn-prevention |
| CS-07 | Chính sách đổi trả, hoàn tiền, bảo hành | Cần văn bản chính sách công khai và quy trình xử lý nội bộ | Chính sách công khai, quy trình nội bộ, điều kiện, thời hạn, ai duyệt, mẫu phiếu | CES pol-hoan-tien-bao-hanh |
| CS-08 | Tiếp nhận khách hàng mới B2B và điểm sức khỏe khách hàng | Ký xong hợp đồng, cần bàn giao, đào tạo, theo dõi tín hiệu rủi ro | Quy trình tiếp nhận 30 ngày, bảng điểm sức khỏe, hành động theo mức | CES sop-onboard-khach-hang, frm-customer-health-score |
| CS-09 | Chương trình khách hàng thân thiết | Muốn thiết kế điểm thưởng, hạng thành viên, ưu đãi theo hạng | Cơ chế tích điểm, hạng, quyền lợi, chi phí dự kiến, cách đo | CES man-loyalty-retention |
| CS-10 | Thu thập đánh giá và chứng thực khách hàng | Cần quy trình xin đánh giá trên sàn, Google, Facebook và lời chứng thực cho bán hàng | Thời điểm xin, kịch bản xin, cách xử lý đánh giá xấu, kho chứng thực | CES sop-thu-thap-review |

### 4. Nhân sự (`nhan-su/`, mã HR) — 14 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| HR-01 | Viết mô tả công việc | Cần đăng tuyển, mô tả công việc cũ quá khô khan | Mô tả công việc 6 phần, yêu cầu phân bậc bắt buộc và điểm cộng, quyền lợi cụ thể | BS jd-writing |
| HR-02 | Kế hoạch tuyển dụng | Cần tuyển nhiều vị trí, chọn kênh, tính thời gian và chi phí | Lịch tuyển, kênh theo vị trí, ngân sách, chỉ số theo dõi | BS recruitment-onboarding |
| HR-03 | Sàng lọc hồ sơ ứng viên | Nhiều hồ sơ, cần xếp hạng theo mô tả công việc | Bảng chấm điểm, xếp hạng, lý do loại, câu hỏi cần làm rõ | BS cv-screening |
| HR-04 | Bộ câu hỏi và bảng chấm phỏng vấn | Cần phỏng vấn công bằng và so sánh được giữa các ứng viên | Câu hỏi theo năng lực, câu hỏi tình huống, bảng chấm điểm | BS recruitment-onboarding |
| HR-05 | Kế hoạch hội nhập nhân viên mới | Nhân viên mới hay nghỉ trong 2 tháng đầu | Lịch 30-60-90 ngày, người kèm, mốc kiểm tra, tài liệu cần đọc | BS recruitment-onboarding |
| HR-06 | Đánh giá hiệu quả làm việc | Đến kỳ đánh giá, cần khung công bằng dựa trên dữ liệu | Bảng điểm theo vai trò, ví dụ cụ thể, kế hoạch phát triển | BS performance-review, OPA 65 |
| HR-07 | Xây dựng KPI và OKR cho vị trí | Chưa có chỉ số đo lường rõ cho từng vị trí | Bộ chỉ số theo vị trí, cách đo, tần suất, ngưỡng đạt | Mới, OPA 65 |
| HR-08 | Tài liệu đào tạo nội bộ | Cần giáo trình đào tạo nhân viên mới hoặc kỹ năng mới | Mục tiêu học, cấu trúc bài, bài tập, bài kiểm tra | BS training-content-creator |
| HR-09 | Nội quy, chính sách và truyền thông nội bộ | Cần soạn hoặc cập nhật quy định, thông báo nội bộ | Văn bản chính sách rõ ràng, bản tóm tắt cho nhân viên, câu hỏi thường gặp | Mới |
| HR-10 | Sơ đồ tổ chức và kế hoạch nhân sự | Cần vẽ cơ cấu, định biên, kế hoạch tuyển theo mục tiêu kinh doanh | Sơ đồ tổ chức, bảng định biên theo phòng, kế hoạch tuyển và chi phí nhân sự năm | CES so-do-to-chuc, headcount-plan |
| HR-11 | Quy chế lương, thưởng và phúc lợi | Cần văn bản hóa thang lương, cơ chế thưởng, phúc lợi, lộ trình tăng lương | Thang bậc lương, cơ chế thưởng theo vị trí, phúc lợi, quy trình xét tăng lương | CES quy-che-luong-thuong, chinh-sach-phuc-loi |
| HR-12 | Quy trình nghỉ việc và bàn giao | Nhân viên nghỉ, cần phỏng vấn thôi việc, bàn giao, thu hồi tài sản và tài khoản | Quy trình theo ngày, biên bản bàn giao, danh sách thu hồi, phỏng vấn thôi việc | CES sop-nghi-viec, bien-ban-ban-giao-cong-viec |
| HR-13 | Kế hoạch đào tạo năm và khảo sát nhu cầu | Cần kế hoạch đào tạo theo phòng ban, ngân sách, đo hiệu quả | Khảo sát nhu cầu, kế hoạch năm, ngân sách, cách đo hiệu quả | CES ke-hoach-dao-tao-hang-nam, khao-sat-nhu-cau-dao-tao, bao-cao-roi-dao-tao |
| HR-14 | Kèm cặp và phát triển quản lý kế cận | Muốn xây lớp quản lý kế cận, chương trình kèm cặp, kế hoạch kế nhiệm | Tiêu chí chọn, chương trình kèm cặp 6 tháng, kế hoạch kế nhiệm vị trí chủ chốt | CES chuong-trinh-mentoring-coaching, phat-trien-lanh-dao, ke-hoach-ke-nhiem |

### 5. Tài chính và kế toán (`tai-chinh-ke-toan/`, mã FIN) — 11 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| FIN-01 | Kế hoạch tài chính và dự báo doanh thu | Lập kế hoạch năm, cần dự báo doanh thu và chi phí | Dự báo 3 kịch bản, giả định rõ, điểm hòa vốn | BS financial-planning |
| FIN-02 | Dự báo dòng tiền | Lo thiếu tiền mặt, cần nhìn trước 3 đến 6 tháng | Bảng dòng tiền theo tuần hoặc tháng, cảnh báo thiếu hụt, phương án xử lý | BS cashflow-forecasting |
| FIN-03 | Kinh tế đơn vị khách hàng | Cần biết mỗi khách lãi hay lỗ, kênh nào đáng đầu tư | Chi phí thu hút khách, giá trị vòng đời, thời gian hoàn vốn theo kênh | BS unit-economics |
| FIN-04 | Phân loại và kiểm soát chi phí | Chi phí rối, cần phân loại và tìm chỗ cắt giảm | Bảng phân loại, tỉ trọng, chi phí bất thường, đề xuất tiết kiệm | BS expense-classification |
| FIN-05 | Chiến lược định giá | Cần đặt giá sản phẩm mới hoặc điều chỉnh giá | Mô hình giá, bậc gói, neo giá, so sánh đối thủ, cách trình bày bảng giá | OPA 17, BS pricing-strategy, CH pricing |
| FIN-06 | Báo cáo tài chính quản trị | Cần báo cáo tháng cho ban lãnh đạo dễ hiểu | Tóm tắt 1 trang, bảng chỉ số, biến động và nguyên nhân, đề xuất | BS periodic-reporting |
| FIN-07 | Thẩm định dự án đầu tư | Cân nhắc mua máy, mở chi nhánh, đầu tư lớn | Phân tích chi phí lợi ích, thời gian hoàn vốn, rủi ro, khuyến nghị | BS strategic-decision-making |
| FIN-08 | Quy trình công nợ và thu hồi | Bán chịu cho khách doanh nghiệp, nợ quá hạn tăng | Chính sách tín dụng, phân nhóm nợ, kịch bản nhắc nợ theo mốc | Mới |
| FIN-09 | Ngân sách năm theo phòng ban | Cần lập, duyệt và theo dõi ngân sách từng phòng, so thực tế với kế hoạch | Bảng ngân sách theo phòng và tháng, quy trình duyệt, báo cáo chênh lệch | CES ngan-sach-nam |
| FIN-10 | Quy chế chi tiêu và phê duyệt | Cần hạn mức duyệt theo cấp, chứng từ bắt buộc, quy trình tạm ứng, hoàn ứng | Ma trận hạn mức duyệt, quy trình thu chi, tạm ứng, chứng từ, mẫu phiếu | CES quy-che-chi-tieu-noi-bo, sop-thu-chi, phieu-thu-chi-template |
| FIN-11 | Đóng sổ kế toán tháng và lịch thuế | Cần danh sách việc cuối tháng, đối chiếu, hạn nộp tờ khai thuế | Lịch đóng sổ theo ngày, danh sách đối chiếu, lịch thuế năm, phân công | CES sop-ke-toan-thang, bang-ke-thue-gtgt |

### 6. Vận hành và quản lý (`van-hanh/`, mã OPS) — 11 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| OPS-01 | Thiết kế quy trình chuẩn | Công việc phụ thuộc người, cần văn bản hóa quy trình | Quy trình từng bước, người chịu trách nhiệm, điểm kiểm soát, biểu mẫu | BS sop-designer |
| OPS-02 | Kế hoạch dự án | Cần lập kế hoạch và theo dõi dự án nhiều người | Phân rã công việc, lịch, phân công, rủi ro, mốc nghiệm thu | BS project-management |
| OPS-03 | Biên bản họp và đầu việc | Có ghi chú hoặc bản ghi cuộc họp cần tổng hợp | Biên bản, quyết định, đầu việc có người và hạn, việc tồn đọng | BS meeting-efficiency |
| OPS-04 | Giao việc cho nhân sự | Cần giao việc rõ ràng, tránh hiểu sai | Bản giao việc: mục tiêu, tiêu chuẩn hoàn thành, ràng buộc, điểm kiểm tra | OPA 64 |
| OPS-05 | Báo cáo định kỳ | Cần báo cáo tuần, tháng, quý cho bất kỳ phòng ban nào | Khung báo cáo, so sánh kỳ trước, nhận định, đề xuất | BS periodic-reporting |
| OPS-06 | Tự động hóa quy trình | Việc lặp lại nhiều, muốn nối các công cụ với nhau | Danh sách việc nên tự động, luồng xử lý, công cụ gợi ý, cách kiểm tra | BS workflow-automation |
| OPS-07 | Kho tri thức nội bộ | Kiến thức nằm trong đầu từng người, cần hệ thống hóa | Cấu trúc kho, quy tắc viết, quy trình cập nhật | BS knowledge-base-builder |
| OPS-08 | Yêu cầu thuê ngoài | Thuê agency, freelancer, nhà cung cấp | Phạm vi công việc, tiêu chuẩn bàn giao, số vòng sửa, mốc thanh toán | OPA 67 |
| OPS-09 | Phân tích dữ liệu để ra quyết định | Có dữ liệu thô từ bảng tính, phần mềm, cần rút ra kết luận | Nhận định chính, bảng số minh họa, nhật ký quyết định | OPA 13, BS analytics |
| OPS-10 | Từ điển KPI và bảng điều khiển công ty | Cần định nghĩa thống nhất mọi chỉ số, ai chịu trách nhiệm, bảng theo dõi cấp công ty | Từ điển KPI theo phòng, thiết kế bảng điều khiển, chính sách báo cáo, cảnh báo sớm | CES man-tu-dien-kpi, man-thiet-ke-dashboard, pol-chinh-sach-bao-cao |
| OPS-11 | Kế hoạch duy trì kinh doanh khi có sự cố lớn | Cần phương án khi mất điện, cháy, dịch bệnh, mất dữ liệu, nhân sự chủ chốt nghỉ đột ngột | Danh sách sự cố, mức ưu tiên, phương án thay thế, người phụ trách, diễn tập | CES ke-hoach-duy-tri-kinh-doanh, sop-xu-ly-su-co |

### 7. Lãnh đạo và chiến lược (`lanh-dao/`, mã LD) — 10 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| LD-01 | Ra quyết định chiến lược | Đứng trước lựa chọn lớn, nhiều phương án | Khung so sánh phương án, tiêu chí có trọng số, rủi ro, khuyến nghị | BS strategic-decision-making |
| LD-02 | Giải quyết vấn đề từ gốc | Vấn đề lặp lại, sửa mãi không hết | Phân tích nguyên nhân gốc, giả định cần phá, giải pháp từ nguyên lý | BS first-principles-thinking |
| LD-03 | Hội đồng cố vấn mô phỏng | Cần nhiều góc nhìn phản biện thay vì AI chỉ đồng ý | 5 vai cố vấn tranh luận, điểm mâu thuẫn, kết luận cân bằng | OPA 72, CH marketing-council |
| LD-04 | Lộ trình ứng dụng AI | Muốn đưa AI vào công ty một cách có hệ thống | Đánh giá mức sẵn sàng, việc nên làm trước, lộ trình 3 giai đoạn | BS ai-readiness-assessment, BS ai-implementation-roadmap |
| LD-05 | Giao việc cho AI hiệu quả | Nhân viên dùng AI nhưng kết quả chung chung | Khung 4 yếu tố: bối cảnh, nội dung, ràng buộc, kiểm soát; mẫu câu lệnh | BS prompt-engineering-4c |
| LD-07 | Tầm nhìn, sứ mệnh, giá trị cốt lõi | Cần chốt hoặc làm mới định hướng công ty để truyền thông nội bộ | Tuyên bố tầm nhìn, sứ mệnh, 3 đến 5 giá trị kèm hành vi cụ thể, cách truyền thông | CES tam-nhin-su-menh-gia-tri |
| LD-08 | Kế hoạch kinh doanh năm | Cần kế hoạch tổng cho năm: mô hình kinh doanh, SWOT, mục tiêu, OKR cấp công ty | Mô hình kinh doanh 9 ô, SWOT, mục tiêu năm, OKR công ty, lộ trình quý, ngân sách tổng | CES ke-hoach-kinh-doanh, business-model-canvas, okr-template, ogsm-framework |
| LD-09 | Ma trận phân quyền và quy chế phê duyệt | Không rõ ai quyết việc gì, cần ma trận trách nhiệm và ngưỡng duyệt | Ma trận RACI theo quy trình chính, bảng ngưỡng phê duyệt theo cấp, quy tắc ủy quyền | CES ma-tran-phan-quyen-raci, quy-che-bgd |
| LD-10 | Chẩn đoán sức khỏe doanh nghiệp | Muốn tự đánh giá mức trưởng thành vận hành theo từng mảng để biết làm gì trước | Bảng chấm 10 mảng theo 5 mức, điểm yếu ưu tiên, lộ trình 90 ngày | CES cham-diem-truong-thanh, bo-cau-hoi-intake |
| LD-11 | Mở rộng thị trường và chi nhánh mới | Cân nhắc mở chi nhánh, vào tỉnh mới, thêm kênh phân phối | Tiêu chí chọn thị trường, ước tính đầu tư và hòa vốn, kế hoạch 6 tháng đầu, điều kiện dừng | CES phan-tich-mo-rong-thi-truong |

### 8. Pháp lý và tuân thủ (`phap-ly/`, mã PL) — 6 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| PL-01 | Rà soát hợp đồng mua bán | Nhận hợp đồng từ đối tác, cần chỉ ra điều khoản bất lợi | Bảng điều khoản rủi ro, đề xuất sửa, câu hỏi cho luật sư | Mới |
| PL-02 | Điều khoản dịch vụ và chính sách bảo mật | Website hoặc ứng dụng cần văn bản pháp lý | Bản nháp điều khoản, chính sách bảo mật, danh sách kiểm tra tuân thủ | BS compliance-checklists |
| PL-03 | Tuân thủ quảng cáo và dữ liệu cá nhân | Lo quảng cáo vi phạm hoặc thu thập dữ liệu khách sai quy định | Danh sách kiểm tra theo luật Việt Nam, từ ngữ cấm, cách lấy đồng ý | Mới |
| PL-04 | Soạn hợp đồng mẫu | Cần khung hợp đồng dịch vụ, đại lý, hợp tác, bảo mật thông tin để luật sư hoàn thiện | Khung điều khoản từng loại hợp đồng, điểm cần thương lượng, câu hỏi cho luật sư | CES hop-dong-dich-vu-mau, hop-dong-dai-ly-mau, nda-mau, hop-dong-hop-tac-kinh-doanh |
| PL-05 | Danh mục giấy phép, bảo hiểm và lịch tuân thủ | Cần biết công ty phải có giấy phép gì, hạn gia hạn, bảo hiểm bắt buộc | Danh mục giấy phép theo ngành, lịch gia hạn, bảo hiểm bắt buộc và nên có, lịch tuân thủ năm | CES danh-sach-giay-phep-con, lich-gia-han-giay-phep, danh-muc-bao-hiem-dn, checklist-tuan-thu-phap-ly |
| PL-06 | Quản lý rủi ro doanh nghiệp | Cần sổ đăng ký rủi ro, chấm điểm, người chịu trách nhiệm, rà soát định kỳ | Sổ rủi ro theo nhóm, ma trận khả năng và tác động, kế hoạch giảm thiểu, lịch rà soát | CES so-dang-ky-rui-ro, chinh-sach-quan-ly-rui-ro |

> Mọi skill chỉ hỗ trợ soạn thảo và rà soát sơ bộ. Văn bản pháp lý cần luật sư duyệt trước khi dùng.

### 9. Kho và mua hàng (`kho-mua-hang/`, mã KHO) — 5 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| KHO-01 | Quy trình nhập, xuất và kiểm kê kho | Cần chuẩn hóa nhận hàng, xuất hàng, kiểm kê xoay vòng, xử lý chênh lệch | Quy trình nhập, xuất, kiểm kê; mẫu phiếu; nguyên tắc FIFO, FEFO; KPI kho | CES sop-quan-ly-kho |
| KHO-02 | Mức tồn kho và điểm đặt hàng lại | Hay thiếu hàng hoặc tồn quá nhiều, cần tính tồn an toàn, phân loại ABC | Phân loại ABC, tồn an toàn, điểm đặt hàng, hàng chậm luân chuyển, lịch rà | CES sop-quan-ly-kho, sop-dat-hang |
| KHO-03 | Quy trình mua hàng và đặt hàng | Cần quy trình từ yêu cầu mua, duyệt, đặt hàng, nhận hàng, đối chiếu hóa đơn | Quy trình 6 bước, ngưỡng duyệt, mẫu đơn đặt hàng, đối chiếu 3 chứng từ | CES sop-dat-hang, sop-mua-sam-tai-san |
| KHO-04 | Đánh giá và quản lý nhà cung cấp | Cần chọn, chấm điểm, xếp hạng và rà soát định kỳ nhà cung cấp | Tiêu chí chọn, bảng chấm điểm, danh sách đã duyệt, lịch đánh giá, xử lý vi phạm | CES sop-danh-gia-nha-cung-cap, scorecard-ncc, danh-sach-ncc-da-duyet |
| KHO-05 | Quản lý tài sản và công cụ dụng cụ | Cần sổ theo dõi tài sản, cấp phát, thu hồi, kiểm kê, thanh lý | Sổ tài sản, quy trình cấp phát và thu hồi, kiểm kê, thanh lý, khấu hao cơ bản | CES so-theo-doi-tai-san, sop-mua-sam-tai-san |

### 10. Công nghệ thông tin (`cong-nghe-thong-tin/`, mã IT) — 4 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| IT-01 | Chính sách sử dụng CNTT và bảo mật thông tin | Cần quy định thiết bị, phần mềm, email, dữ liệu, thiết bị cá nhân, AI công cộng | Chính sách theo mục, phân loại dữ liệu 4 mức, quy tắc dùng AI, xử lý vi phạm | CES chinh-sach-cntt, chinh-sach-an-ninh-mang, quy-che-bao-mat-thong-tin |
| IT-02 | Sao lưu dữ liệu và xử lý sự cố | Cần lịch sao lưu, kiểm tra khôi phục, quy trình khi mất dữ liệu, bị mã độc | Lịch sao lưu 3-2-1, kiểm tra khôi phục, quy trình sự cố theo mức, liên hệ khẩn | CES sop-backup-du-lieu, sop-xu-ly-su-co |
| IT-03 | Quản lý tài khoản, phân quyền và bàn giao | Cần danh sách tài khoản hệ thống, ai có quyền gì, thu hồi khi nghỉ việc | Sổ tài khoản, ma trận phân quyền, quy trình cấp và thu hồi, rà soát quý | CES danh-sach-tai-khoan-he-thong, bien-ban-ban-giao-cong-viec |
| IT-04 | Bản đồ phần mềm và lộ trình số hóa | Cần biết đang dùng phần mềm gì, chồng chéo ở đâu, nên thay gì trước | Bản đồ phần mềm theo phòng, chi phí, chồng chéo, lộ trình thay thế 12 tháng | CES tech-stack-map, chinh-sach-cntt |

### 11. Sản phẩm và chất lượng (`san-pham-chat-luong/`, mã SP) — 4 skill

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| SP-01 | Danh mục và tài liệu sản phẩm | Cần bảng danh mục chuẩn, thông số, tài liệu kỹ thuật cho bán hàng và đại lý | Cấu trúc danh mục, thẻ sản phẩm chuẩn, phân tích danh mục, tài liệu cho bán hàng | CES danh-muc-san-pham-dich-vu, product-brief-template, bcg-matrix |
| SP-02 | Quy trình ra mắt sản phẩm mới | Sắp ra sản phẩm mới, cần lộ trình từ ý tưởng đến bán, phối hợp các phòng | Cổng duyệt theo giai đoạn, lịch T-60 đến D+30, việc từng phòng, tiêu chí dừng | CES sop-phat-trien-san-pham-moi, lo-trinh-phat-trien-san-pham, OPA 59, OPA 60, CH launch |
| SP-03 | Kiểm soát chất lượng và xử lý hàng lỗi | Cần tiêu chuẩn kiểm tra đầu vào, đầu ra, cách xử lý hàng không đạt | Tiêu chí kiểm tra, mẫu kiểm, xử lý hàng lỗi, truy nguyên nhân, KPI chất lượng | CES sop-kiem-soat-chat-luong, chinh-sach-chat-luong |
| SP-04 | Đề xuất cải tiến liên tục | Muốn nhân viên đề xuất cải tiến có cấu trúc, đánh giá và theo dõi | Mẫu đề xuất, tiêu chí chấm, bảng theo dõi, cơ chế thưởng, nhịp rà | CES kaizen-board, mau-de-xuat-cai-tien |

### 12. Kỹ năng văn phòng chung (`van-phong-chung/`, mã VP) — 6 skill

Dành cho mọi nhân viên, không theo phòng ban.

| Mã | Tên skill | Dùng khi | Kết quả | Nguồn |
|---|---|---|---|---|
| VP-01 | Viết email công việc | Viết mới, viết lại hoặc trả lời email cho sếp, đồng nghiệp, khách, đối tác | Email hoàn chỉnh đúng giọng, tiêu đề, lời kêu gọi hành động, 2 phương án khi cần | VP 01-viet-thu-dien-tu |
| VP-02 | Tóm tắt tài liệu, hợp đồng, công văn | Có văn bản dài cần nắm nhanh ý chính, số liệu, điểm rủi ro, việc cần làm | Tóm tắt 1 trang, số và mốc quan trọng, điểm cần chú ý, việc cần làm | VP 02-tom-tat-tai-lieu |
| VP-03 | Lập kế hoạch tuần và ưu tiên cá nhân | Ngập việc, cần sắp xếp theo quan trọng và khẩn cấp, cảnh báo quá tải | Kế hoạch tuần theo khung giờ, 1 ưu tiên số 1, việc cắt hoặc ủy quyền | VP 04-lap-ke-hoach |
| VP-04 | Làm sạch và kiểm tra bảng tính | Có bảng Excel, Sheets cần tìm lỗi, ô trống, trùng, gợi ý công thức | Báo cáo chất lượng dữ liệu, đề xuất làm sạch kèm công thức, nhận xét ngắn | VP 06-xu-ly-bang-tinh |
| VP-05 | Theo dõi đầu việc cá nhân và nhóm | Cần danh sách việc có người, hạn, trạng thái, tổng hợp cuối tuần | Bảng việc chuẩn, đánh dấu trễ và bị chặn, tổng hợp tuần | VP 10-theo-doi-cong-viec |
| VP-06 | Đề cương bài trình bày | Chuẩn bị thuyết trình, cần thông điệp chính, mạch kể, phân bổ slide | Thông điệp chính, dàn ý theo slide, mở đầu, kết và kêu gọi, lời dẫn | VP 11-de-cuong-trinh-bay |

---

## Cấu trúc thư mục

```
wir-skill/
├── README.md                      # Danh mục này
├── HUONG-DAN-SU-DUNG.md           # Cách dán skill vào ChatGPT, Claude, Gemini
├── huong-dan-tao-skill-chatgpt.md # Cách tạo, sửa và dùng skill trong ChatGPT
├── index.html                     # Trang danh mục cho người dùng, tạo bằng _build/build-index.py
├── marketing/                     # MKT-01 đến MKT-25
├── ban-hang/                      # SAL-01 đến SAL-13
├── cham-soc-khach-hang/           # CS-01 đến CS-10
├── nhan-su/                       # HR-01 đến HR-14
├── tai-chinh-ke-toan/             # FIN-01 đến FIN-11
├── van-hanh/                      # OPS-01 đến OPS-11
├── lanh-dao/                      # LD-01 đến LD-05, LD-07 đến LD-11
├── phap-ly/                       # PL-01 đến PL-06
├── kho-mua-hang/                  # KHO-01 đến KHO-05
├── cong-nghe-thong-tin/           # IT-01 đến IT-04
├── san-pham-chat-luong/           # SP-01 đến SP-04
└── van-phong-chung/               # VP-01 đến VP-06
```

## Những gì cố ý không đưa vào

- **Thương hiệu cá nhân, avatar AI, podcast**: 7 skill của OPA chỉ phù hợp cá nhân, không phù hợp phòng ban.
- **Xuất khẩu B2B, dropshipping, bán phần mềm tự phục vụ, nhượng quyền, gọi vốn**: ngoài mô hình của công ty.
- **Điều lệ công ty, quy chế hội đồng quản trị, thỏa thuận cổ đông, báo cáo tài chính theo chuẩn kế toán, an toàn lao động và phòng cháy**: cần luật sư, kế toán trưởng hoặc cơ quan chuyên môn làm, AI chỉ nên rà.
- **Các skill phụ thuộc công cụ**: skill chỉ chạy được khi có kết nối MCP, API hoặc file hệ thống đều bị loại vì không hoạt động khi dán vào ChatGPT.
