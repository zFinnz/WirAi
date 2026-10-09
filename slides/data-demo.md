# Data demo

> Hướng dẫn này viết cho **một tài khoản ChatGPT trống** và đã được chạy trọn vẹn trên tài khoản Plus ngày 09/10/2026: mỗi bước dưới đây đều ghi kết quả thật. Làm theo thứ tự từ Mục 0 đến Mục 9, mỗi mục ghi rõ **cần có trước** và **tạo ra gì** để mục sau dùng. Slide có nhãn cam **▶ HƯỚNG DẪN DEMO · MỤC N** ở góc trên thì mở đúng Mục N ở đây. Tên menu có thể đổi theo phiên bản.

## Mục 0 · Chuẩn bị tài khoản trống và file

**Cần có:** tài khoản ChatGPT gói Plus trở lên (gói Free có thể thiếu Projects, Skills, Scheduled), đăng nhập chatgpt.com trên máy tính, và một tài khoản Google **cá nhân** cho tầng 4. Đầu trang có hai nút **Chat / Work**: cả khóa chạy ở **Chat**.

**Nếu tài khoản đã dùng, dọn về trống (10 phút)**

1. Settings → Personalization → Custom instructions: xóa hết nội dung.
2. Settings → Personalization → Memory summary → Manage: xóa các mục đã nhớ.
3. Thanh bên → Projects → mở từng Project → ••• → Project settings → Delete project.
4. Thanh bên → Library: xóa các file đã tải lên, hoặc để lại nếu không liên quan tới Wir.
5. Settings → Plugins → bấm từng plugin → Uninstall. Gmail và Drive thì gỡ cả ở myaccount.google.com/linkedapps.
6. Thanh bên → Plugins → tab Skills → ••• trên từng skill → xóa.
7. Settings → Data controls → Archive all chats, để lịch sử chat không lẫn vào demo.

**5 thao tác dùng suốt buổi**

1. **Tải file:** bấm dấu **+** bên trái ô chat → **Add photos & files** (từ máy tính) hoặc **Add from library** (file đã tải lên trước đó, gõ tên để tìm, bấm **Add to chat**). Excel, Word, CSV tải thẳng được.
2. **Dùng prompt:** bấm **Sao chép** ở góc khối lệnh, dán vào ô chat, sửa phần trong ngoặc vuông như `[DÁN BẢNG]`, rồi Enter.
3. **Chat mới ngoài Project:** New chat ở thanh bên. **Chat trong Project:** bấm tên Project ở thanh bên rồi gõ vào ô "New chat in …". Tên Project phải hiện ở đầu khung chat.
4. **Khi ChatGPT hỏi lại 3 câu a/b/c thay vì làm:** đó là luật số 4 trong Custom Instructions. Trả lời ngắn (ví dụ `1b, 2c`) hoặc gõ `Cứ viết.` để nó làm và để trống `[CẦN ĐIỀN]`.
5. **Model và dữ liệu:** để model mặc định (Instant). Toàn bộ file ở đây là dữ liệu DEMO; không dán dữ liệu khách thật, giá vốn, lương, hợp đồng vào ChatGPT.

**File cần có, tải về trước**

| File | Dùng ở mục |
|---|---|
| [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx) | 4, 6, 8 |
| [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx) | 3, 6, 9 |
| [Danh sách lead](du-lieu-demo/danh-sach-lead.xlsx), [Ghi chú trao đổi lead](du-lieu-demo/ghi-chu-trao-doi-lead.docx) | 3, 6 |
| [Transcript họp Phòng Kinh doanh](du-lieu-demo/transcript-hop-demo.docx) | 6, 7 |
| [Review và tin nhắn khách](du-lieu-demo/review-va-tin-nhan-khach.docx) | 6, 7 |
| [Đáp án](du-lieu-demo/dap-an.docx) | 4, 6, mở sau khi làm |
| [Hồ sơ Elasten](du-lieu-demo/ho-so-elasten.md), [Dữ liệu sản phẩm Wir](du-lieu-demo/du-lieu-san-pham-wir.md) | 2, 5, 7, 9 |

**Thứ tự và phụ thuộc**

| Mục | Slide | Tạo ra | Cần có trước |
|---|---|---|---|
| 1 | 5, 9 | Chat "trước khi có gì", Custom Instructions, tắt huấn luyện | Tài khoản trống |
| 2 | 11 | Project "Wir – Marketing" có Instructions và 2 file hồ sơ | Mục 1, hồ sơ sản phẩm |
| 3 | 14 | Không tạo gì | Chính sách giá sỉ |
| 4 | 16 | Không tạo gì | Đơn hàng tháng 7 |
| 5 | 17 | Không tạo gì | Chat bài Facebook ở Mục 2 |
| 6 | 18 | Không tạo gì | File demo |
| 7 | 25 | Skill `tom-tat-tai-lieu` (hiện dưới dạng plugin riêng) | Tab Skills, 2 tài liệu |
| 8 | 32 | Plugin Gmail, Drive đã nối tài khoản cá nhân; file demo trên Drive; task theo lịch | Google cá nhân |
| 9 | 31 | Plugin "Sale Wir" | Mục 7 và 8 |

## Mục 1 · Chat "trước khi có gì", Custom Instructions và cài bảo mật (slide 5, 9)

**Cần có:** tài khoản trống. **Tạo ra:** một chat làm mốc so sánh, danh thiếp cá nhân, tài khoản đã tắt huấn luyện.

**Các bước**

1. Trước khi khai báo bất cứ gì, chat mới gõ:
   ```
   Viết bài Facebook bán Elasten.
   ```
   Giữ chat này, Mục 2 sẽ so với nó. Nếu đã lỡ khai Custom Instructions thì bài vẫn "sạch mà rỗng" nhưng ChatGPT sẽ hỏi lại 3 câu trước, gõ `Cứ viết.`.
2. Settings → Personalization → **Custom instructions**. Màn hình có 4 ô: ô lớn **ChatGPT instructions** dán khối "Cách trả lời tôi" của [mẫu Custom Instructions cá nhân](#instructions); **Occupation** ghi chức danh và công ty; **More about you** dán khối "Thông tin về tôi" (khách phụ trách, báo cáo cho ai, việc hay nhờ); **Nickname** để trống. Bấm **Save**.
3. Settings → **Data controls** → tắt công tắc **Improve the model for everyone**.
4. Kiểm tra, chat mới:
   ```
   Tôi làm ở công ty nào, phụ trách khách nào, bán sản phẩm gì?
   ```
5. Cho lớp thấy Memory: Settings → Personalization → mục **ChatGPT memory** đang bật; Memory summary → Manage là nơi xem và xóa những gì ChatGPT tự nhớ. Nội dung nhạy cảm thì dùng nút **Temporary chat** ở đầu trang: không vào lịch sử, không tạo Memory.

**Đạt khi:** bước 4 trả lời đúng công ty, nhóm khách, cách xưng hô như đã khai và ghi `[CẦN ĐIỀN]` cho tên nhãn hàng chưa khai (kết quả thật 09/10/2026 đúng như vậy); bước 3 công tắc đã tắt.

## Mục 2 · Tạo Project Marketing, demo có và không có Instructions (slide 11)

**Cần có:** Mục 1 xong; [Hồ sơ Elasten](du-lieu-demo/ho-so-elasten.md) và [Dữ liệu sản phẩm Wir](du-lieu-demo/du-lieu-san-pham-wir.md) đã tải về. **Tạo ra:** Project "Wir – Marketing" dùng cho Mục 5 và Mục 7.

**Các bước**

1. Tạo Project: thanh bên → mục **Projects** → dấu **+** → hộp "Create project": gõ tên `Wir – Marketing`, Memory để Default → **Create project**.
2. Mở Project → nút **•••** góc phải → **Project settings** → dán [mẫu Project instructions cho phòng Marketing](#instructions) vào ô **Instructions** → bấm **Save** ở cuối hộp. Đóng bằng X hay Esc là mất nội dung (đã thử).
3. Tab **Sources** → **Add sources**. Có 5 cách: Upload (máy tính), Library, **Paste text**, Google Drive, Slack. Upload hai file `ho-so-elasten.md` và `du-lieu-san-pham-wir.md` vừa tải; máy không cho chọn file .md thì mở file bằng Notepad, copy toàn bộ, chọn Paste text, đặt Title là tên file, dán, Save. Instructions chỉ là luật, file mới là hồ sơ; thiếu file thì ChatGPT không có số liệu.
4. Gõ vào ô "New chat in Wir – Marketing" đúng câu ở Mục 1 bước 1:
   ```
   Viết bài Facebook bán Elasten.
   ```
   ChatGPT in 3 dòng luật cứng (tầng pháp lý, câu bắt buộc, số emoji), có thể hỏi lại 3 câu, gõ `Cứ viết.`. Chiếu bài này cạnh bài ở Mục 1.
5. Phép thử chống bịa, cùng chat:
   ```
   Giá bán lẻ Elasten hiện nay là bao nhiêu? Tháng này đang có chương trình khuyến mãi gì?
   ```
6. Kiểm tra trí nhớ, chat mới trong cùng Project:
   ```
   Elasten thuộc tầng pháp lý nào? Khi viết bài thì những từ nào bị cấm?
   ```
7. Thực hành slide 11: mỗi học viên tạo Project cho phòng mình theo bước 1 đến 3, sửa mẫu Instructions cho đúng phòng, chạy lại bước 5 và 6. Học viên phòng Kinh doanh dùng [mẫu Project instructions cho khách sỉ](#instructions) và thêm file Chính sách giá sỉ vào Sources.

**Đạt khi (kết quả thật 09/10/2026)**

- Bước 4: bài có `[DATA THẬT]` trước số liệu +28%, +20%, −24% kèm nguồn, câu "Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh", giá `[CẦN ĐIỀN]`, 0 emoji, mục TỰ RÀ 5 ô và chip nguồn tới file. Bài ở Mục 1 không có số liệu, không có nguồn.
- Bước 5: bảng 4 dòng đều `[CẦN ĐIỀN]`, ChatGPT nói "chưa thể xác nhận giá hoặc ưu đãi khi thiếu dữ liệu được duyệt".
- Bước 6: nêu đúng TPCN, liệt kê từ cấm "chữa, điều trị, khỏi, đặc trị, hết hẳn, thay thế thuốc", chỉ nguồn "Hồ sơ Elasten, mục 3".

## Mục 3 · Prompt một dòng và prompt đủ 4 phần (slide 14)

**Cần có:** [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx) mở sẵn bằng Word để copy bảng chiết khấu; [Danh sách lead](du-lieu-demo/danh-sach-lead.xlsx) để chỉ cho lớp Spa Ngọc Anh là lead L01. Cả hai prompt chạy trong chat mới **ngoài Project**. **Tạo ra:** không.

**Các bước**

1. Prompt một dòng:
   ```
   Trả lời spa hỏi giá sỉ Elasten.
   ```
   Kết quả thật 09/10/2026: ChatGPT hỏi lại 3 câu (giá, số lượng, nhóm khách). Gõ `Cứ viết.` thì ra tin chung chung: giá, số lượng tối thiểu, ưu đãi đều `[CẦN ĐIỀN]`, không có bảng chiết khấu, không nhắc câu hỏi bà bầu. Hỏi lớp: tin này gửi khách được chưa?
2. Prompt đủ 4 phần. Thay `[DÁN BẢNG]` bằng bảng chiết khấu copy từ file:
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
3. Chiếu hai kết quả cạnh nhau. Chốt: "Không phải ChatGPT giỏi lên, là mình giao việc rõ hơn."

**Đạt khi:** bản 2 chào đúng chị Hương, nêu 4 mức chiết khấu 5/10/15/20%, cọc 30% từ 40 triệu, giá bán lẻ `[CẦN ĐIỀN]`, thai kỳ chỉ nói "không gây rủi ro", có chữ ký, không emoji (kết quả thật 09/10/2026 đạt đủ).

## Mục 4 · Bẫy số liệu: tải file hay dán chữ (slide 16)

**Cần có:** [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx) mở sẵn bằng Excel; [Đáp án](du-lieu-demo/dap-an.docx). Chạy ở model mặc định. **Tạo ra:** không.

**Các bước**

1. Bẫy cũ. Chat mới, bấm **+** → Add photos & files → tải file đơn hàng, gõ:
   ```
   Phân tích doanh số theo từng nhân viên bán hàng.
   ```
   Kết quả thật: ChatGPT chạy code, báo "Số dòng 40, số cột 6, cột nhân viên bán hàng: không có", từ chối gán mỗi kênh là một nhân viên, xin thêm cột Nhan_vien. Khen nó, chỉ cho lớp thấy 6 cột của file.
2. Bẫy mới. Chat mới khác, **không tải file**: trong Excel bôi đen 40 dòng dữ liệu kể cả dòng tiêu đề, Ctrl+C, dán vào ô chat, rồi gõ thêm bên dưới:
   ```
   Đây là 40 dòng đơn hàng tháng 7. Vì sao kênh Shopee có nhiều đơn nhất nhưng doanh thu thấp? Nêu nguyên nhân.
   ```
   ChatGPT tính nhẩm bảng theo kênh và sai, mỗi lần sai một chỗ khác nhau: lần 1 Đại lý sỉ 6 đơn, 96,71 triệu (thật 7 đơn, 106,71 triệu); lần 2 Website 11 đơn, 17,32 triệu (thật 10 đơn, 15,25 triệu) và Zalo 5 đơn (thật 6). Bảng vẫn trình bày rất chắc. Mở Đáp án đối chiếu từng kênh trước lớp.
3. Cách đúng. Quay lại chat ở bước 1 (file đã có), chạy 2 bước. Bước 1, đếm và tổng hợp:
   ```
   File đính kèm có 6 cột: Ngày, Kênh, Sản phẩm, Số lượng, Đơn giá, Thành tiền.
   File KHÔNG có cột nhân viên bán hàng, khách hàng, khu vực, giá vốn.
   1. Cho tôi biết file có bao nhiêu dòng đơn hàng, từ ngày nào đến ngày nào, mấy kênh, mấy sản phẩm.
   2. Lập bảng theo sản phẩm: số lượng, doanh thu, % tổng doanh thu.
   3. Lập bảng theo kênh: số đơn, doanh thu, % tổng doanh thu.
   4. Kiểm tra từng dòng: Thành tiền = Số lượng × Đơn giá. Dòng nào lệch thì liệt kê.
   Tuyệt đối không tách theo nhân viên bán hàng, khách hàng hay khu vực.
   ```
   Bước 2, cùng chat đó, viết báo cáo một trang:
   ```
   Từ các bảng vừa lập, viết báo cáo doanh thu tháng 7 một trang gửi Trưởng phòng Kinh doanh, đọc 2 phút là quyết được.
   Cấu trúc 5 phần: (1) kết quả chính; (2) cơ cấu theo sản phẩm và theo kênh; (3) 1 điểm sáng;
   (4) 1 điểm cần chú ý; (5) 2-3 đề xuất cần duyệt.
   Mỗi đề xuất đủ 4 thứ: việc cần làm, người chịu trách nhiệm, hạn, nguồn lực hoặc chi phí.
   Mọi câu về nguyên nhân viết dạng "nghi do ..., cần kiểm chứng bằng ...".
   Không quy trách nhiệm cho cá nhân.
   Cuối bản thêm mục "Số liệu người ký cần kiểm lại trước khi trình".
   ```

**Đáp án để đối chiếu**

| Chỉ tiêu | Số đúng |
|---|---|
| Số dòng, thời gian | 40 đơn, 01/07 đến 25/07/2026, 5 kênh, 7 sản phẩm |
| Tổng doanh thu | 147.300.000 đ, mọi dòng khớp Số lượng × Đơn giá |
| Theo sản phẩm | Elasten 85.700.000 đ (58,2%), Lactobact Intima 36.150.000 đ, CH Alpha Plus 14.200.000 đ |
| Theo kênh | Đại lý sỉ 7 đơn, 106.710.000 đ (72,4%); Website 10 đơn, 15.250.000 đ; Shopee 11 đơn, 10.350.000 đ; Fanpage 6 đơn, 9.350.000 đ; Zalo 6 đơn, 5.640.000 đ |

**Đạt khi:** bước 3 ra đúng bảng trên, 40/40 dòng khớp (kết quả thật 09/10/2026 khớp từng số); báo cáo có đủ 5 phần, mỗi đề xuất đủ 4 thứ với `[CẦN ĐIỀN]` ở người phụ trách, hạn, chi phí, và mọi nguyên nhân viết "nghi do…, cần kiểm chứng bằng…".

## Mục 5 · Kiểm chứng đầu ra trong vài phút (slide 17)

**Cần có:** chat bài Facebook trong Project ở Mục 2. **Tạo ra:** không.

**Các bước**

1. Bấm chip tên file (ví dụ `ho-so-elasten.md.txt`) ngay sau câu ChatGPT trích, xem có mở đúng đoạn không. Câu nào không có chip thì copy câu đó, mở file gốc, Ctrl+F.
2. Chọn 2–3 con số trong bài, tự đối chiếu với file gốc. Đây là cách bắt được lỗi tính nhẩm ở Mục 4.
3. Thay "Elasten" bằng tên một collagen khác, bài còn đúng thì chưa đủ cụ thể.
4. Bắt AI tự khai:
   ```
   Chỗ nào bạn tự suy đoán mà tài liệu không nói?
   ```

**Đạt khi:** bước 4 ChatGPT lập bảng từng chỗ, gắn nhãn `[DATA THẬT]` / `[SUY LUẬN]` / `[CẦN ĐIỀN]`, chỉ ra cả phần "tình huống khách" và "lời kêu gọi" là sáng tạo không phải dữ liệu (kết quả thật 09/10/2026 liệt kê 4 điểm). Tự khai chỉ bắt được chỗ nó biết là suy đoán, không bắt được lỗi tính nhẩm, nên bước 2 vẫn bắt buộc.

## Mục 6 · Thực hành tầng 2: bốn việc trên dữ liệu demo (slide 18)

**Cần có:** các file demo. Mỗi người chọn ít nhất 3 việc, mỗi việc một chat mới ngoài Project, tải file bằng nút **+**. Làm xong mới mở [Đáp án](du-lieu-demo/dap-an.docx), không dán đáp án vào ChatGPT. **Tạo ra:** không.

**1. Biên bản họp và bảng đầu việc.** File: [Transcript họp Phòng Kinh doanh](du-lieu-demo/transcript-hop-demo.docx).
```
Bối cảnh: tôi là thư ký cuộc họp kế hoạch tháng 8 của Phòng Kinh doanh Wir. Bản ghi thô đính kèm.
Yêu cầu: viết biên bản họp và bảng đầu việc.
Tiêu chí: mỗi việc đủ ai làm, việc gì, hạn; việc chưa rõ người thì ghi [CẦN ĐIỀN], không tự gán tên;
chỉ dùng thông tin có trong bản ghi.
Định dạng: biên bản 5 mục (mục tiêu, quyết định, đầu việc, chưa thống nhất, lần họp sau) và một bảng đầu việc.
```
Đạt khi: bắt đúng mục tiêu tháng 8 tăng 20%, hạn nội dung 05/08; 3 việc chưa rõ người ghi `[CẦN ĐIỀN]`.

**2. Báo cáo doanh thu.** File: [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx). Dùng 2 bước ở Mục 4, đối chiếu đáp án ở đó.

**3. Năm insight có mã bằng chứng.** File: [Review và tin nhắn khách](du-lieu-demo/review-va-tin-nhan-khach.docx).
```
File đính kèm có 20 review (R01–R20) và 10 tin nhắn hỏi trước khi mua (M01–M10) của khách Elasten và Lactobact Intima.
1. Đếm trước: có bao nhiêu mẩu, bao nhiêu là review, bao nhiêu là tin nhắn.
2. Rút ra tối đa 5 insight theo công thức: [nhóm khách] + [lo/muốn gì] + [vì sao] + [mã bằng chứng] + [tần suất x/tổng].
3. Sắp xếp theo tần suất từ cao xuống thấp. Cấm viết "đa số", "rất nhiều".
4. Mỗi insight kèm 1 câu trích nguyên văn, giữ nguyên lỗi chính tả.
5. Pain về giao hàng, đóng gói thì tách thành mục riêng "chuyển bộ phận vận hành".
6. Khách tự nói "khỏi", "hết" thì giữ nguyên trong trích dẫn, nhưng không biến thành công dụng sản phẩm.
7. Cuối bài ghi 3 câu hỏi mà dữ liệu này KHÔNG trả lời được.
```
Đạt khi: nỗi lo lớn lấy từ tin nhắn M01–M10 (thai kỳ M01, M04, M06); mã và trích dẫn Ctrl+F thấy trong file.

**4. Chấm điểm 12 lead và soạn tin tiếp cận.** File: [Danh sách lead](du-lieu-demo/danh-sach-lead.xlsx), [Ghi chú trao đổi lead](du-lieu-demo/ghi-chu-trao-doi-lead.docx), [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx). Tải cả 3 file vào cùng một chat.
```
Bối cảnh: tôi là Sale khách sỉ của Wir. Đính kèm danh sách 12 lead, ghi chú trao đổi và chính sách giá sỉ.
Yêu cầu: chấm điểm từng lead theo 3 mức nóng, ấm, lạnh và soạn tin tiếp cận cho 3 lead nóng nhất.
Tiêu chí: lead thiếu thông tin thì hạ độ tin cậy và ghi thiếu gì; lead đòi điều chưa có trong chính sách
thì chỉ dùng đúng một câu xin ý kiến quản lý, không báo số; sản phẩm Karima không báo giá;
tin tiếp cận phải trích được chi tiết từ ghi chú của chính lead đó, dưới 150 chữ.
Định dạng: bảng 12 dòng (mã lead, mức, lý do 1 câu, việc tiếp theo) và 3 tin nhắn Zalo.
```
Đạt khi: L02 (hỏi Karima), L05 (đòi độc quyền khu vực), L09 (đòi công nợ 45 ngày) chuyển quản lý; L03, L07, L10 hạ độ tin cậy; L04 hỏi Warnke cho mẹ bầu phải nêu chống chỉ định.

**Đạt chung:** prompt đủ 4 phần, kết quả không có số sai, tự kiểm chứng được ít nhất 2 con số hoặc 2 trích dẫn.

## Mục 7 · Năm lượt chat thành một skill (slide 25)

**Cần có:** thanh bên → **Plugins** → tab **Skills** mở được (tài khoản Plus thử ngày 09/10/2026 có sẵn skill `skill-creator`, chính nó sẽ đóng gói giúp); một tài liệu dài để làm tay và một tài liệu khác để thử. Trên lớp dùng `du-lieu-san-pham-wir.md` đã nằm trong Sources của Project để làm tay, và [Hồ sơ Elasten](du-lieu-demo/ho-so-elasten.md) hoặc một tài liệu bất kỳ để thử. Tự tập ở nhà thì dùng [Transcript họp](du-lieu-demo/transcript-hop-demo.docx) để làm tay và [Review và tin nhắn khách](du-lieu-demo/review-va-tin-nhan-khach.docx) để thử. **Tạo ra:** skill `tom-tat-tai-lieu`, dùng lại ở Mục 9.

**Các bước**

1. Chat mới trong Project Wir – Marketing, chạy lần lượt 5 lượt, sau mỗi lượt ghi lên bảng "Lượt N → mục X":
   - `Tóm tắt giúp tôi tài liệu du-lieu-san-pham-wir.md trong Sources.`
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
   ChatGPT làm khoảng một phút rồi báo "Đã tạo Skill tom-tat-tai-lieu, phiên bản 1.0.0, đã được tạo thành plugin riêng tư trên tài khoản của bạn", kèm link mở và nút tải file ZIP. Skill nằm ở Settings → **Plugins** (danh sách đã cài), không nằm ở tab Skills. Mở link, chỉ cho lớp mô tả skill khớp với 5 lượt trên bảng.
3. Phép thử phiên mới: chat mới **ngoài Project**, bấm + → Add from library hoặc tải tài liệu thứ hai, gõ đúng một câu:
   ```
   Tóm tắt tài liệu này.
   ```
4. Bẫy chống bịa, hỏi một con số tài liệu không có. Chạy **trong Project** (Instructions đã cấm tìm web):
   ```
   Một hộp Elasten có bao nhiêu ống, giá bán lẻ bao nhiêu?
   ```
   Chạy ngoài Project, ChatGPT trả lời "theo tài liệu: chưa có" rồi tự tìm web và đưa giá của Watsons, các sàn bán lẻ. Đó là giá thị trường, không phải giá Wir. Muốn demo ngoài Project thì tắt trước Settings → Personalization → **Web search**.
5. Thực hành slide 25: mỗi người chọn một việc lặp lại hằng tuần của mình, chat tay 3–5 lượt rồi đóng gói như bước 2. Sai thì sửa skill, không sửa tay kết quả.

**Đạt khi (kết quả thật 09/10/2026):** lượt 4 liệt kê 7 cụm "điều trị", "phòng ngừa & điều trị", "chữa khỏi"… vượt ranh giới TPCN; bước 3 skill tự chạy không cần gọi tên, bài ra đúng 5 mục; bước 4 trong Project trả lời "Tài liệu không đề cập" và `[CẦN ĐIỀN]`.

## Mục 8 · Plugin có sẵn: Gmail, Drive, task tự động (slide 32)

**Cần có:** tài khoản Google **cá nhân**; [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx). **Tạo ra:** plugin Gmail và Google Drive đã nối, file `don-hang-demo` và `tom-tat-don-hang-thang-7` trên Drive, một task theo lịch.

**Cài đặt trước (10 phút)**

1. Đăng xuất tài khoản Google công ty trên trình duyệt. Tải file Đơn hàng tháng 7 lên Drive cá nhân, để ở thư mục gốc. Không tải được thì ở bước 3 bên dưới có cách để ChatGPT tự tạo file.
2. Thanh bên → **Plugins** → tìm **Gmail** → Install → Connect → chọn tài khoản cá nhân → đọc hết danh sách quyền Google rồi mới Allow. Làm tương tự với **Google Drive**.
3. Settings → **Plugins** → bấm dòng Gmail → Connected accounts phải là địa chỉ cá nhân. Thấy địa chỉ công ty thì ••• → gỡ ngay, vì ChatGPT đọc được cả thư lương, hợp đồng trong hộp thư đó.
4. Cùng trang → mục **Permission** → chọn **Always ask**. Mặc định là Allow low-risk tools, phải tự đổi. Làm tương tự cho Google Drive.

**Các bước**

1. Kiểm tra đã nối đúng, chat mới:
   ```
   Đọc tiêu đề 3 thư gần nhất trong hộp thư đến. Chỉ đọc, không trả lời, không xóa.
   ```
   Đạt khi ra đúng 3 tiêu đề đang thấy trong Gmail. Tiêu đề lạ tức là chưa nối được, ChatGPT đang bịa.
2. Phân loại và soạn nháp:
   ```
   Đọc 20 thư gần nhất trong hộp thư. Xếp vào 4 nhóm: KHẨN / QUAN TRỌNG / CHỜ / BỎ QUA.
   Xuất bảng: Người gửi | Nhóm | Lý do (1 câu) | Việc cần làm | Hạn.
   Sau đó soạn NHÁP trả lời cho thư khẩn nhất. Không gửi.
   Thư nào hỏi về thai kỳ, công dụng chữa bệnh hoặc giá ngoài chính sách thì ghi [CẦN NGƯỜI DUYỆT].
   ```
   Mở Gmail, tìm thư nháp, cho lớp thấy thư chưa gửi.
3. Đọc và ghi file trên Drive:
   ```
   Trên Drive của tôi có file don-hang-demo. Đọc tên các cột và đếm số dòng trước.
   Tổng hợp doanh thu theo sản phẩm và theo kênh.
   Lưu kết quả thành file mới tên tom-tat-don-hang-thang-7 trong cùng thư mục. Không sửa file gốc.
   ```
   Khi tới bước ghi file, ChatGPT dừng và hiện hộp **"Allow ChatGPT to use Google Drive?"** với ba nút **Always allow / Deny / Allow once**. Bấm **Allow once**. Đây chính là chốt người duyệt của slide 28. Đáp án: 40 dòng, tổng 147.300.000 đ, Elasten 85.700.000 đ, Đại lý sỉ 106.710.000 đ. Mở Drive cho lớp thấy file mới, file gốc còn nguyên. Nếu Drive chưa có file, ChatGPT tìm theo tên, báo không thấy và xin link, không bịa số; có thể bảo nó tạo luôn: dán 40 dòng vào chat và gõ "Tạo trên Google Drive của tôi một Google Sheet tên don-hang-demo có đúng dữ liệu dưới đây" (đã thử, tạo đúng 41 dòng, 6 cột).
4. Task theo lịch: thanh bên → **Scheduled** → gõ vào ô "Schedule a task":
   ```
   Mỗi thứ Hai lúc 7:00, đọc file đơn hàng tuần mới nhất tên don-hang-demo trên Google Drive của tôi.
   Lập bảng doanh thu theo sản phẩm và theo kênh. Đối chiếu tổng với tổng cột Thanh_tien.
   Đánh dấu [CẢNH BÁO] ở dòng nào có Thanh_tien khác So_luong × Don_gia.
   Nếu file thiếu cột hoặc thiếu ngày: KHÔNG phân tích, chỉ báo cho tôi thiếu gì.
   Chỉ tạo thư NHÁP gửi tôi, không gửi cho ai khác.
   ```
   ChatGPT trả lời "Đã thiết lập lịch tự động", task hiện trong Scheduled với dòng "Weekly · Next run in N days". Nó chỉ chạy vào thứ Hai, giảng viên kiểm thư nháp sau lần chạy đầu. Demo xong thì xóa task.
5. Thực hành slide 32, phần 4A: học viên làm lại bước 1 đến 3 trên Gmail và Drive cá nhân của mình. Ai không nối Gmail thì dán 5 thư mẫu bất kỳ vào chat để làm bước 2.

**Đạt khi:** nối đúng tài khoản cá nhân; thư nháp chưa gửi; hộp Allow once xuất hiện trước khi ghi file; file gốc trên Drive còn nguyên; cuối buổi gỡ quyền Google như slide 29 (myaccount.google.com/linkedapps → Remove access, rồi Settings → Plugins → ngắt kết nối) và xóa task demo trong Scheduled.

## Mục 9 · Plugin tự tạo bằng Plugin Creator (slide 31)

**Cần có:** skill `tom-tat-tai-lieu` từ Mục 7, Gmail và Drive từ Mục 8, [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx) và [Dữ liệu sản phẩm Wir](du-lieu-demo/du-lieu-san-pham-wir.md). Thanh bên → Plugins → tìm **Plugin Creator** → Install. **Tạo ra:** plugin "Sale Wir".

**Các bước**

1. Chat mới, dán nguyên câu dưới đây (gõ `@plugin-creator` ở đầu là đủ để gọi, không cần chọn trong menu gợi ý):
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
   Plugin Creator hỏi đúng 5 nhóm, mỗi nhóm 4–5 câu có lựa chọn sẵn. Trả lời ngắn kiểu `Câu 1: …; Câu 2: …`. Gợi ý trả lời: nhóm 2 "Ưu tiên Drive, thiếu thì hỏi Sale; duyệt nội dung gửi khách và mọi báo giá; Sale duyệt nội dung, Trưởng phòng duyệt giá ngoại lệ; thiếu dữ liệu thì tạo nháp ghi [CẦN ĐIỀN]"; nhóm 3 "Zalo 150 từ, email 250 từ, tóm tắt 1 trang, hỏi lại tối đa 3 câu, không emoji, cuối tin có dòng Đây là bản nháp"; nhóm 4 dán bộ từ cấm và câu hàng rào "Mức này vượt chính sách sỉ hiện hành, em cần xin ý kiến quản lý trước khi xác nhận với anh/chị."; nhóm 5 "Drive và Gmail; kiểm kê và gộp skill tom-tat-tai-lieu; chỉ thư mục chia sẻ cho đội".
2. Sau nhóm 5 nó xin 2 file tham chiếu: tải lên bằng nút + hoặc dán nội dung hai file vào chat. Khoảng một phút sau: "Đã tạo thành công Sale Wir, phiên bản 0.1.0, plugin riêng tư", kèm hai tình huống thử nó tự đề xuất (tài liệu mâu thuẫn chiết khấu; nhân viên đòi gửi email ngay không qua duyệt).
3. Phép thử. Plugin tự tạo **không tự kích hoạt** khi chat thường (đã thử: chat mới gõ tình huống anh Bảo thì ChatGPT trả lời chung, không dùng câu hàng rào). Phải gọi tên: gõ `@` rồi chọn **Sale Wir**, hoặc vào trang plugin → **Try in chat**, rồi gõ:
   ```
   Anh Bảo, Công ty phân phối Bảo Phát (Hải Phòng), muốn làm đại lý Elasten nhưng đòi độc quyền
   khu vực Hải Phòng. Soạn giúp tôi tin trả lời.
   ```
4. Thực hành slide 32, phần 4B: viết Playbook 7 mục cho plugin (mục đích, ai dùng, quy trình, tiêu chuẩn đầu ra, ranh giới, chỉ số đo, xử lý khi sai) và đưa một đồng nghiệp chạy thử bằng @Sale Wir mà không được hỏi lại.

**Đạt khi (kết quả thật 09/10/2026 với @Sale Wir):** tin có đúng câu "Mức này vượt chính sách sỉ hiện hành, em cần xin ý kiến quản lý trước khi xác nhận với anh", không hứa độc quyền, cuối tin có "Đây là bản nháp", lưu ý nội bộ ghi `[DATA THẬT] Nguồn: Sale Wir, mục Hàng rào giá`; đồng nghiệp chạy được không cần hỏi.
