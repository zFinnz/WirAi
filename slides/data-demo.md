# Data demo

> Mỗi mục ứng với một slide cần demo. Làm theo thứ tự: tải file, dán prompt, đối chiếu với mục "Đạt khi". Đây là dữ liệu DEMO, không trộn dữ liệu khách thật vào. Kết quả ChatGPT mỗi lần một khác, giảng viên chạy thử trước buổi học.

## Slide 10–11 · Tầng 1: cùng một câu lệnh, có và không có Instructions

**Chuẩn bị:** một Project "Wir – Marketing" đã dán [mẫu Project instructions](#instructions) và tải hồ sơ sản phẩm của phòng (tài liệu nội bộ, không kèm ở đây).

**Các bước**

1. Chat mới, ngoài Project:
   ```
   Viết bài Facebook bán Elasten.
   ```
   Hỏi lớp: câu bắt buộc của TPCN đâu? Số liệu lấy nguồn ở đâu? Đếm emoji.
2. Vào Project, gõ lại đúng câu trên.
3. Phép thử chống bịa, trong Project:
   ```
   Giá bán lẻ Elasten hiện nay là bao nhiêu? Tháng này đang có chương trình khuyến mãi gì?
   ```
4. Kiểm tra trí nhớ, mở chat mới trong cùng Project:
   ```
   Elasten thuộc tầng pháp lý nào? Khi viết bài thì những từ nào bị cấm?
   ```

**Đạt khi**

- Bước 2: có câu "Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh", số +28% độ ẩm da sau 12 tuần ghi nguồn, giá bán ghi `[CẦN ĐIỀN]`, không quá 2 emoji.
- Bước 3: trả lời chưa đủ dữ liệu và xin bảng giá, không đưa ra con số.
- Bước 4: nêu đúng TPCN và các từ cấm "chữa", "điều trị", "khỏi", "đặc trị".

## Slide 14 · Prompt một dòng và prompt đủ 4 phần

**Chuẩn bị:** [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx), [Danh sách lead](du-lieu-demo/danh-sach-lead.xlsx) (Spa Ngọc Anh là lead L01).

**Các bước**

1. Prompt một dòng, chat mới:
   ```
   Trả lời spa hỏi giá sỉ Elasten.
   ```
   Hỏi lớp: bản này gửi khách được chưa, thiếu gì? Kết quả thật 09/10/2026: không bịa giá, nhưng hỏi lại số lượng, tự thêm "collagen Đức" và emoji, không dùng bảng giá sỉ.
2. Prompt đủ 4 phần, dán bảng chiết khấu vào cuối:
   ```
   Bối cảnh: Tôi là nhân viên Sale của Wir Group. Chị Hương, chủ chuỗi Spa Ngọc Anh (3 chi nhánh, TP.HCM),
   muốn nhập thử 20 hộp Elasten mỗi tháng và hỏi bà bầu dùng được không.
   Elasten có giám định chuyên gia kết luận không gây rủi ro cho phụ nữ mang thai và cho con bú.
   Bảng chiết khấu sỉ dán bên dưới.

   Yêu cầu: Soạn tin trả lời chị Hương.

   Tiêu chí: chiết khấu đúng bảng sỉ; chưa có giá bán lẻ nền thì ghi [CẦN ĐIỀN], không tự tính số tiền;
   về thai kỳ chỉ nói "không gây rủi ro" theo giám định, KHÔNG nói "tốt cho thai kỳ";
   không hứa gì ngoài bảng; dưới 150 chữ; không emoji.

   Định dạng: tin nhắn Zalo gồm lời chào, nội dung, chữ ký [tên, số điện thoại].

   Bảng chiết khấu sỉ:
   [DÁN BẢNG]
   ```

**Đạt khi:** nêu đúng các mức chiết khấu trong bảng; số tiền cuối ghi `[CẦN ĐIỀN]`; thai kỳ chỉ nói "không gây rủi ro"; dưới 150 chữ, có lời chào, nội dung, chữ ký.

## Slide 16 · Bẫy số liệu: tải file hay dán chữ

**Chuẩn bị:** [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx), [Đáp án](du-lieu-demo/dap-an.docx).

**Các bước**

1. Bẫy cũ, tải file lên rồi gõ:
   ```
   Phân tích doanh số theo từng nhân viên bán hàng.
   ```
   ChatGPT bản hiện nay sẽ báo file không có cột nhân viên và phân tích theo kênh. Khen nó, chỉ cho lớp thấy 6 cột của file.
2. Bẫy mới, chat mới, mở file Excel, copy 40 dòng và dán vào chat dạng chữ (không tải file), rồi gõ:
   ```
   Đây là 40 dòng đơn hàng tháng 7. Vì sao kênh Shopee có nhiều đơn nhất nhưng doanh thu thấp? Nêu nguyên nhân.
   ```
   ChatGPT tính nhẩm bảng theo kênh và sai (chạy 09/10/2026: Đại lý sỉ 6 đơn, 96,71 triệu). Đối chiếu với đáp án bên dưới.
3. Cách đúng, tải file lên, chạy 2 bước. Bước 1, đếm và tổng hợp:
   ```
   File đính kèm có 6 cột: Ngày, Kênh, Sản phẩm, Số lượng, Đơn giá, Thành tiền.
   File KHÔNG có cột nhân viên bán hàng, khách hàng, khu vực, giá vốn.
   1. Cho tôi biết file có bao nhiêu dòng đơn hàng, từ ngày nào đến ngày nào, mấy kênh, mấy sản phẩm.
   2. Lập bảng theo sản phẩm: số lượng, doanh thu, % tổng doanh thu.
   3. Lập bảng theo kênh: số đơn, doanh thu, % tổng doanh thu.
   4. Kiểm tra từng dòng: Thành tiền = Số lượng × Đơn giá. Dòng nào lệch thì liệt kê.
   Tuyệt đối không tách theo nhân viên bán hàng, khách hàng hay khu vực.
   ```
   Bước 2, viết báo cáo một trang:
   ```
   Từ các bảng vừa lập, viết báo cáo doanh thu tháng 7 một trang gửi Trưởng phòng Kinh doanh, đọc 2 phút là quyết được.
   Cấu trúc 5 phần: (1) kết quả chính; (2) cơ cấu theo sản phẩm và theo kênh; (3) 1 điểm sáng;
   (4) 1 điểm cần chú ý; (5) 2-3 đề xuất cần duyệt.
   Mỗi đề xuất đủ 4 thứ: việc cần làm, người chịu trách nhiệm, hạn, nguồn lực hoặc chi phí.
   Mọi câu về nguyên nhân viết dạng "nghi do ..., cần kiểm chứng bằng ...".
   Không quy trách nhiệm cho cá nhân.
   Cuối bản thêm mục "Số liệu người ký cần kiểm lại trước khi trình".
   ```

**Đáp án**

| Chỉ tiêu | Số đúng |
|---|---|
| Số dòng, thời gian | 40 đơn, 01/07 đến 25/07/2026, 5 kênh, 7 sản phẩm |
| Tổng doanh thu | 147.300.000 đ, mọi dòng khớp Số lượng × Đơn giá |
| Theo sản phẩm | Elasten 85.700.000 đ (58,2%), Lactobact Intima 36.150.000 đ, CH Alpha Plus 14.200.000 đ |
| Theo kênh | Đại lý sỉ 7 đơn, 106.710.000 đ (72,4%); Website 10 đơn, 15.250.000 đ; Shopee 11 đơn, 10.350.000 đ; Fanpage 6 đơn, 9.350.000 đ; Zalo 6 đơn, 5.640.000 đ |

## Slide 17 · Kiểm chứng đầu ra trong vài phút

**Chuẩn bị:** dùng lại chat bài Facebook ở slide 10, trong Project có file.

**Các bước**

1. Bấm chip tên file ngay sau câu ChatGPT trích, xem có mở đúng đoạn không. Câu nào không có chip thì Ctrl+F trong file gốc.
2. Chọn 2–3 con số trong bài, tự đối chiếu với file gốc. Đây là cách bắt được lỗi tính nhẩm ở slide 16.
3. Thay "Elasten" bằng tên một collagen khác, bài còn đúng thì chưa đủ cụ thể.
4. Bắt AI tự khai:
   ```
   Chỗ nào bạn tự suy đoán mà tài liệu không nói?
   ```

**Đạt khi:** bước 4 ChatGPT liệt kê từng chỗ, gắn nhãn `[DATA THẬT]` / `[SUY LUẬN]` và chỉ tới mục, dòng trong file.

## Slide 18 · Thực hành tầng 2: bốn việc trên dữ liệu demo

Mỗi người chọn ít nhất 3 việc. Làm xong mới mở [Đáp án](du-lieu-demo/dap-an.docx), không dán đáp án vào ChatGPT.

**1. Biên bản họp và bảng đầu việc.** File: [Transcript họp Phòng Kinh doanh](du-lieu-demo/transcript-hop-demo.docx).
```
Bối cảnh: tôi là thư ký cuộc họp kế hoạch tháng 8 của Phòng Kinh doanh Wir. Bản ghi thô đính kèm.
Yêu cầu: viết biên bản họp và bảng đầu việc.
Tiêu chí: mỗi việc đủ ai làm, việc gì, hạn; việc chưa rõ người thì ghi [CẦN ĐIỀN], không tự gán tên;
chỉ dùng thông tin có trong bản ghi.
Định dạng: biên bản 5 mục (mục tiêu, quyết định, đầu việc, chưa thống nhất, lần họp sau) và một bảng đầu việc.
```
Đạt khi: bắt đúng mục tiêu tháng 8 tăng 20%, hạn nội dung 05/08; 3 việc chưa rõ người ghi `[CẦN ĐIỀN]`.

**2. Báo cáo doanh thu.** File: [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx). Dùng 2 bước ở slide 16, đối chiếu đáp án ở đó.

**3. Năm insight có mã bằng chứng.** File: [Review và tin nhắn khách](du-lieu-demo/review-va-tin-nhan-khach.docx).
```
Dưới đây là 20 review (R01–R20) và 10 tin nhắn hỏi trước khi mua (M01–M10) của khách Elasten và Lactobact Intima.
1. Đếm trước: có bao nhiêu mẩu, bao nhiêu là review, bao nhiêu là tin nhắn.
2. Rút ra tối đa 5 insight theo công thức: [nhóm khách] + [lo/muốn gì] + [vì sao] + [mã bằng chứng] + [tần suất x/tổng].
3. Sắp xếp theo tần suất từ cao xuống thấp. Cấm viết "đa số", "rất nhiều".
4. Mỗi insight kèm 1 câu trích nguyên văn, giữ nguyên lỗi chính tả.
5. Pain về giao hàng, đóng gói thì tách thành mục riêng "chuyển bộ phận vận hành".
6. Khách tự nói "khỏi", "hết" thì giữ nguyên trong trích dẫn, nhưng không biến thành công dụng sản phẩm.
7. Cuối bài ghi 3 câu hỏi mà dữ liệu này KHÔNG trả lời được.
```
Đạt khi: nỗi lo lớn lấy từ tin nhắn M01–M10 (thai kỳ M01, M04, M06), mã và trích dẫn Ctrl+F thấy trong file.

**4. Chấm điểm 12 lead và soạn tin tiếp cận.** File: [Danh sách lead](du-lieu-demo/danh-sach-lead.xlsx), [Ghi chú trao đổi lead](du-lieu-demo/ghi-chu-trao-doi-lead.docx), [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx).
```
Bối cảnh: tôi là Sale khách sỉ của Wir. Đính kèm danh sách 12 lead, ghi chú trao đổi và chính sách giá sỉ.
Yêu cầu: chấm điểm từng lead theo 3 mức nóng, ấm, lạnh và soạn tin tiếp cận cho 3 lead nóng nhất.
Tiêu chí: lead thiếu thông tin thì hạ độ tin cậy và ghi thiếu gì; lead đòi điều chưa có trong chính sách
thì chỉ dùng đúng một câu xin ý kiến quản lý, không báo số; sản phẩm Karima không báo giá;
tin tiếp cận phải trích được chi tiết từ ghi chú của chính lead đó, dưới 150 chữ.
Định dạng: bảng 12 dòng (mã lead, mức, lý do 1 câu, việc tiếp theo) và 3 tin nhắn Zalo.
```
Đạt khi: L02 (hỏi Karima), L05 (đòi độc quyền khu vực), L09 (đòi công nợ 45 ngày) chuyển quản lý; L03, L07, L10 hạ độ tin cậy; L04 hỏi Warnke cho mẹ bầu phải nêu chống chỉ định.

## Slide 23–25 · Tầng 3: năm lượt chat thành một skill

**Chuẩn bị:** một tài liệu sản phẩm dài của phòng bạn để làm tay (ví dụ CH Alpha Plus, tài liệu nội bộ, không kèm) và một tài liệu thứ hai để thử skill.

**Các bước**

1. Tải tài liệu lên, chạy lần lượt 5 lượt, sau mỗi lượt ghi lên bảng "Lượt N → mục X":
   - `Tóm tắt giúp tôi tài liệu này.`
   - `Liệt kê theo từng phần của tài liệu.`
   - `Bóc mọi con số, mốc thời gian, cam kết.`
   - `Có câu nào vượt ranh giới pháp lý của TPCN, hay mâu thuẫn trong tài liệu không?`
   - `Chỗ nào bạn tự đoán? Rút 3–5 ý gửi sếp.`
2. Đóng gói ngay trong chat đó:
   ```
   Kết quả ổn rồi. Hãy đóng gói cách làm vừa rồi thành một skill tên tom-tat-tai-lieu, để lần sau
   tôi chỉ cần nói "Tóm tắt tài liệu này" là bạn tự dùng skill.
   Khi tôi đưa tài liệu, làm theo các bước:
   1. Đọc toàn bộ tài liệu.
   2. Xuất đúng cấu trúc:
      - TÓM TẮT NHANH: 3-5 gạch đầu dòng ý chính nhất.
      - Ý CHÍNH CHI TIẾT: theo từng mục/phần của tài liệu.
      - SỐ LIỆU, NGÀY THÁNG, HẠN CHÓT: mọi con số, mốc thời gian, cam kết.
      - ĐIỂM CẦN LƯU Ý / RỦI RO: câu vượt ranh giới pháp lý theo tầng sản phẩm, chỗ mâu thuẫn, chỗ mập mờ.
      - QUY TẮC: chỉ dùng thông tin trong tài liệu; không có thì ghi "Tài liệu không đề cập", không suy đoán;
        trích nguyên văn trong ngoặc kép khi cần bằng chứng.
   ```
   ChatGPT hỏi thêm vài câu rồi đề nghị cài skill. Mở skill ra, chỉ từng mục khớp với 5 lượt trên bảng.
3. Phép thử phiên mới: mở chat mới, tải tài liệu thứ hai, gõ đúng một câu:
   ```
   Tóm tắt tài liệu này.
   ```
4. Bẫy chống bịa, hỏi một con số tài liệu không có:
   ```
   Một hộp Elasten có bao nhiêu ống, giá bán lẻ bao nhiêu?
   ```

**Đạt khi:** lượt 4 bắt được cụm "điều trị" trong tài liệu TPCN; bước 3 skill tự chạy, ra đủ 5 mục; bước 4 trả lời "Tài liệu không đề cập", không bịa số.

## Slide 30–32 · Tầng 4: plugin có sẵn, task tự động

**Chuẩn bị:** Gmail và Google Drive **cá nhân**, không dùng tài khoản công ty. Tải [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx) lên Drive cá nhân. Sau khi nối Gmail, vào Settings → Plugins → Gmail và đặt mức Always ask.

**Các bước**

1. Kiểm tra đã nối đúng:
   ```
   Đọc tiêu đề 3 thư gần nhất trong hộp thư đến. Chỉ đọc, không trả lời, không xóa.
   ```
   Đạt khi ra đúng 3 tiêu đề đang thấy trong Gmail.
2. Phân loại và soạn nháp:
   ```
   Đọc 20 thư gần nhất trong hộp thư. Xếp vào 4 nhóm: KHẨN / QUAN TRỌNG / CHỜ / BỎ QUA.
   Xuất bảng: Người gửi | Nhóm | Lý do (1 câu) | Việc cần làm | Hạn.
   Sau đó soạn NHÁP trả lời cho thư khẩn nhất. Không gửi.
   Thư nào hỏi về thai kỳ, công dụng chữa bệnh hoặc giá ngoài chính sách thì ghi [CẦN NGƯỜI DUYỆT].
   ```
3. Đọc và ghi file trên Drive:
   ```
   Trên Drive của tôi có file don-hang-demo.xlsx. Đọc tên các cột và đếm số dòng trước.
   Tổng hợp doanh thu theo sản phẩm và theo kênh.
   Lưu kết quả thành file mới tên tom-tat-don-hang-thang-7 trong cùng thư mục. Không sửa file gốc.
   ```
   Đáp án: 40 dòng, tổng 147.300.000 đ, Elasten 85.700.000 đ, Đại lý sỉ 106.710.000 đ.
4. Task theo lịch, tạo trong mục Scheduled:
   ```
   Mỗi thứ Hai lúc 7:00, đọc file đơn hàng tuần mới nhất trong thư mục Báo cáo trên Drive.
   Lập bảng doanh thu theo sản phẩm và theo kênh. Đối chiếu tổng với tổng cột Thành tiền.
   Đánh dấu [CẢNH BÁO] ở dòng nào có Thành tiền khác Số lượng × Đơn giá.
   Nếu file thiếu cột hoặc thiếu ngày: KHÔNG phân tích, chỉ báo cho tôi thiếu gì.
   Chỉ tạo thư NHÁP gửi tôi, không gửi cho ai khác.
   ```
5. Gỡ quyền ngay sau buổi học: myaccount.google.com/linkedapps → ChatGPT → Remove access; trong ChatGPT: Settings → Plugins → ngắt kết nối.

**Đạt khi:** nối đúng tài khoản cá nhân; thư nháp chưa gửi; file gốc trên Drive còn nguyên; đã gỡ quyền.

## Slide 31 · Plugin tự tạo bằng Plugin Creator

**Chuẩn bị:** cài Plugin Creator từ danh mục Plugins; có sẵn skill `tom-tat-tai-lieu` ở tầng 3, [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx) làm file tham chiếu.

**Các bước**

1. Gõ trong chat mới:
   ```
   @plugin-creator Tôi muốn tạo plugin "Sale Wir" cho đội Sale khách sỉ. Tôi không biết code.
   Hãy phỏng vấn tôi trước, mỗi lần một nhóm câu, đừng tạo ngay:
   1. Việc lặp lại nào plugin sẽ làm, ai dùng, đầu ra gửi cho ai.
   2. Các bước và bước nào bắt buộc có người duyệt.
   3. Tiêu chuẩn đầu ra: hỏi tôi bằng số. Nếu tôi trả lời bằng tính từ, hỏi ngược "một bản KHÔNG đạt trông thế nào?".
   4. Ranh giới: từ cấm theo tầng pháp lý sản phẩm, điều chưa có chính sách giá sỉ, sản phẩm không được báo giá (Karima).
   5. File tôi có sẵn và app cần nối.
   Sau khi phỏng vấn: gộp các skill tôi đã có, thêm file tham chiếu và app Drive, Gmail.
   Bắt buộc có 3 nguyên tắc chống bịa: chỉ dùng dữ liệu tôi cấp; gắn nhãn [DATA THẬT]/[SUY LUẬN];
   mọi thứ gửi khách là nháp, không tự gửi.
   Cuối cùng đề xuất 2 yêu cầu thử nằm ngoài những gì tôi đã kể.
   ```
2. Phép thử, chat mới, không gọi tên plugin hay skill:
   ```
   Anh Bảo, Công ty phân phối Bảo Phát (Hải Phòng), muốn làm đại lý Elasten nhưng đòi độc quyền
   khu vực Hải Phòng. Soạn giúp tôi tin trả lời.
   ```

**Đạt khi:** báo chiết khấu đúng bảng 4 mức, giá nền `[CẦN ĐIỀN]`; phần độc quyền chỉ dùng câu xin ý kiến quản lý, không hứa; cuối bản có dòng "Đây là bản nháp".
