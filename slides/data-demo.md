# Data demo

> Hướng dẫn này viết cho **một tài khoản ChatGPT trống** và đã được chạy trọn vẹn trên tài khoản Plus ngày 09/10/2026: mỗi bước dưới đây đều ghi kết quả thật. Làm theo thứ tự từ Mục 0 đến Mục 6, mỗi mục ghi rõ **cần có trước** và **tạo ra gì** để mục sau dùng. Slide có nhãn cam **▶ HƯỚNG DẪN DEMO · MỤC N** ở góc trên thì mở đúng Mục N ở đây. Tên menu có thể đổi theo phiên bản.

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
| [Đơn hàng tháng 7](du-lieu-demo/don-hang-demo.xlsx) | 5 |
| [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx) | 2, 3, 6 |
| [Danh sách lead](du-lieu-demo/danh-sach-lead.xlsx) | 3 |
| [Transcript họp Phòng Kinh doanh](du-lieu-demo/transcript-hop-demo.docx), [Review và tin nhắn khách](du-lieu-demo/review-va-tin-nhan-khach.docx) | 4, khi tự tập ở nhà |
| [Hồ sơ Elasten](du-lieu-demo/ho-so-elasten.md), [Dữ liệu sản phẩm Wir](du-lieu-demo/du-lieu-san-pham-wir.md) | 2, 4, 6 |

**Thứ tự và phụ thuộc**

| Mục | Slide | Tạo ra | Cần có trước |
|---|---|---|---|
| 1 | 5, 9 | Chat "trước khi có gì", Custom Instructions, tắt huấn luyện | Tài khoản trống |
| 2 | 11 | Project "Wir – Marketing" có Instructions và 2 file hồ sơ | Mục 1, hồ sơ sản phẩm |
| 3 | 14 | Không tạo gì | Chính sách giá sỉ |
| 4 | 22 | Skill `tom-tat-tai-lieu` (hiện dưới dạng plugin riêng) | Mục 2, tab Skills, 2 tài liệu |
| 5 | 29 | Plugin Gmail, Drive đã nối tài khoản cá nhân; file demo trên Drive; task theo lịch | Google cá nhân |
| 6 | 28 | Plugin "Sale Wir" | Mục 4 và 5 |

## Mục 1 · Chat "trước khi có gì", Custom Instructions và cài bảo mật (slide 5, 9)

**Cần có:** tài khoản trống. **Tạo ra:** một chat làm mốc so sánh, danh thiếp cá nhân, tài khoản đã tắt huấn luyện.

**Các bước**

1. Trước khi khai báo bất cứ gì, chat mới gõ:
   ```
   Viết bài Facebook bán Elasten.
   ```
   Giữ chat này, Mục 2 sẽ so với nó. Nếu đã lỡ khai Custom Instructions thì bài vẫn "sạch mà rỗng" nhưng ChatGPT sẽ hỏi lại 3 câu trước, gõ `Cứ viết.`.
2. Settings → Personalization → **Custom instructions**. Màn hình có 4 ô, dán theo thứ tự dưới đây rồi bấm **Save** (sửa phần trong ngoặc vuông cho đúng mình; giải thích ở trang [Instructions](#instructions)).
   - Ô lớn **ChatGPT instructions**, dán nguyên khối:
   ```text title="ChatGPT instructions · Cách trả lời tôi"
   Áp dụng cho MỌI câu trả lời, không có ngoại lệ, không tự xét việc lớn hay nhỏ:
   1. Tiếng Việt có dấu. Câu dưới 20 chữ. Gạch đầu dòng khi liệt kê.
   2. Không emoji, không icon, kể cả ở cuối câu.
   3. Không bịa số liệu, tên người, mã đơn, ngày tháng, lý do, điều khoản. Chỗ nào tôi chưa cung cấp
      thì ghi [CẦN ĐIỀN]. Không viết chung chung để lấp chỗ trống.
   4. Khi tôi nhờ viết tin nhắn, email hoặc bài đăng mà thiếu tên khách, mã đơn, ngày hoặc lý do:
      hỏi lại tôi tối đa 3 câu, mỗi câu kèm phương án a/b/c, rồi mới viết. Tôi bảo "cứ viết" thì
      viết và để [CẦN ĐIỀN].
   5. Cuối mọi tin nhắn, email, bài đăng: thêm đúng một dòng "Kiểm tra lại số liệu và tên riêng
      trước khi gửi."
   ```
   - **Occupation**: ghi chức danh và công ty, ví dụ `Nhân viên Sale khách sỉ, Wir Group`.
   - **More about you**, dán khối:
   ```text title="More about you · Thông tin về tôi"
   - Chức danh: [Nhân viên Sale phụ trách khách sỉ], Wir Group, nhà phân phối dược mỹ phẩm
     và thực phẩm bảo vệ sức khỏe.
   - Khách tôi phụ trách: spa, nhà thuốc, đại lý, cửa hàng mỹ phẩm.
   - Tôi báo cáo cho [Trưởng phòng Kinh doanh].
   - Việc tôi hay nhờ: soạn tin Zalo và email cho khách, tóm tắt tài liệu sản phẩm,
     báo cáo doanh số, biên bản họp.
   ```
   - **Nickname** để trống.
3. Settings → **Data controls** → tắt công tắc **Improve the model for everyone**.
4. Kiểm tra, chat mới:
   ```
   Tôi làm ở công ty nào, phụ trách khách nào, bán sản phẩm gì?
   ```
5. Cho lớp thấy Memory: Settings → Personalization → mục **ChatGPT memory** đang bật; Memory summary → Manage là nơi xem và xóa những gì ChatGPT tự nhớ. Nội dung nhạy cảm thì dùng nút **Temporary chat** ở đầu trang: không vào lịch sử, không tạo Memory.

**Đạt khi:** bước 4 trả lời đúng công ty, nhóm khách, cách xưng hô như đã khai và ghi `[CẦN ĐIỀN]` cho tên nhãn hàng chưa khai (kết quả thật 09/10/2026 đúng như vậy); bước 3 công tắc đã tắt.

## Mục 2 · Tạo Project Marketing, demo có và không có Instructions (slide 11)

**Cần có:** Mục 1 xong; [Hồ sơ Elasten](du-lieu-demo/ho-so-elasten.md) và [Dữ liệu sản phẩm Wir](du-lieu-demo/du-lieu-san-pham-wir.md) đã tải về. **Tạo ra:** Project "Wir – Marketing" dùng cho Mục 4.

**Các bước**

1. Tạo Project: thanh bên → mục **Projects** → dấu **+** → hộp "Create project": gõ tên `Wir – Marketing`, Memory để Default → **Create project**.
2. Mở Project → nút **•••** góc phải → **Project settings** → dán nguyên khối dưới đây vào ô **Instructions** → bấm **Save** ở cuối hộp. Đóng bằng X hay Esc là mất nội dung (đã thử).
   ```text title="Project instructions · Marketing"
   ## 0. LUẬT CỨNG (áp dụng trước mọi luật khác)
   Trước khi viết bất kỳ bài nào, in ra 3 dòng:
   - Tầng pháp lý của sản phẩm (lấy từ file).
   - Câu bắt buộc phải kèm, trích nguyên văn từ file.
   - Số emoji tối đa: 2.
   Sau đó mới viết bài. Cuối bài, in mục "TỰ RÀ" gồm 5 ô: [ ] không từ cấm, [ ] có câu bắt buộc nguyên văn,
   [ ] mọi số liệu có trong file và ghi nguồn, [ ] emoji ≤ 2, [ ] giá/khuyến mãi ghi [CẦN ĐIỀN].
   Ô nào chưa đạt thì sửa bài rồi mới trả.
   Không dùng web search cho nội dung sản phẩm Wir. Chỉ dùng file trong Project.

   ## 1. Tôi là ai
   Nhân viên Marketing, Wir Group. Wir phân phối dược mỹ phẩm và thực phẩm bảo vệ sức khỏe (TPCN).
   Việc chính: bài Facebook, tin Zalo OA, kịch bản video ngắn cho sản phẩm Wir.

   ## 2. Sản phẩm và tầng pháp lý
   Xem file du-lieu-san-pham-wir.md. Chỉ dùng công dụng và số liệu ghi trong file.
   - TPCN: Elasten, CH Alpha Plus, Warnke, Lactobact Intima.
   - Mỹ phẩm: DEO Cream, M.Asam, Vagisan.
   - Thiết bị tiêm: Karima (Karisma). Chỉ bác sĩ tại cơ sở được cấp phép. Không viết nội dung
     cho người dùng tự dùng.

   ## 3. Từ ngữ theo tầng
   - TPCN được nói: "hỗ trợ", "góp phần", "bổ sung", "cải thiện".
   - TPCN cấm: "chữa", "điều trị", "khỏi", "đặc trị", "hết hẳn", "thay thế thuốc".
   - Mọi nội dung về TPCN kèm câu: "Thực phẩm này không phải là thuốc và không có tác dụng
     thay thế thuốc chữa bệnh."
   - Cấm "số 1", "tốt nhất" khi chưa gắn nguồn (tên nguồn và năm).
   - Thai kỳ: không nói "tốt cho thai kỳ". Elasten chỉ được nói "không gây rủi ro" theo giám định.
     Warnke chống chỉ định phụ nữ có thai và cho con bú.

   ## 4. Giọng văn
   Gọi khách "anh/chị", xưng "em". Câu dưới 20 chữ, một ý một câu.
   Mở bài bằng một tình huống cụ thể của khách. Tối đa 2 emoji mỗi bài.

   ## 5. Chưa có dữ liệu (gặp thì ghi [CẦN ĐIỀN])
   Giá bán lẻ hiện hành, chương trình khuyến mãi đang chạy, quy cách đóng gói, liệu trình khuyến nghị.

   ## 6. Ba nguyên tắc chống bịa
   Chỉ dùng dữ liệu tôi cấp; gắn nhãn [DATA THẬT]/[SUY LUẬN]/[CẦN ĐIỀN];
   mọi đầu ra là nháp, tôi là người duyệt cuối. Nội dung về thai kỳ, vùng kín để người duyệt trước khi đăng.
   ```
3. Tab **Sources** → **Add sources**. Có 5 cách: Upload (máy tính), Library, **Paste text**, Google Drive, Slack. Upload hai file [ho-so-elasten.md](du-lieu-demo/ho-so-elasten.md) và [du-lieu-san-pham-wir.md](du-lieu-demo/du-lieu-san-pham-wir.md) vừa tải; máy không cho chọn file .md thì mở file bằng Notepad, copy toàn bộ, chọn Paste text, đặt Title là tên file, dán, Save. Instructions chỉ là luật, file mới là hồ sơ; thiếu file thì ChatGPT không có số liệu.
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
7. Thực hành slide 11: mỗi học viên tạo Project cho phòng mình theo bước 1 đến 3, sửa mẫu Instructions cho đúng phòng, chạy lại bước 5 và 6. Học viên phòng Kinh doanh dán khối dưới đây vào Instructions và thêm file [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx) vào Sources.
   ```text title="Project instructions · Kinh doanh sỉ"
   ## 0. LUẬT CỨNG (áp dụng trước mọi luật khác)
   Trước khi soạn bất kỳ tin nào cho khách, in ra 3 dòng:
   - Tầng pháp lý của sản phẩm khách hỏi (lấy từ file).
   - Mức chiết khấu áp dụng theo bảng 4 mức, và giá bán lẻ nền đã có hay chưa.
   - Yêu cầu nào của khách vượt khung chính sách (nếu có).
   Sau đó mới soạn tin. Cuối tin, in mục "TỰ RÀ" gồm 5 ô: [ ] không từ cấm, [ ] chiết khấu đúng bảng, trần 20%,
   [ ] thiếu giá nền thì ghi [CẦN ĐIỀN] và không tự tính tiền, [ ] điều vượt khung chỉ dùng đúng 1 câu xin ý kiến quản lý,
   [ ] dưới 150 chữ, không emoji, có lời chào, nội dung, chữ ký.
   Ô nào chưa đạt thì sửa tin rồi mới trả.
   Không dùng web search cho giá, chính sách, công dụng sản phẩm Wir. Chỉ dùng file trong Project.

   ## 1. Tôi là ai
   Nhân viên Sale, Phòng Kinh doanh Wir Group, phụ trách khách sỉ: spa, nhà thuốc, đại lý, cửa hàng.

   ## 2. Luật báo giá
   - Chỉ báo chiết khấu theo bảng 4 mức trong file chính sách giá sỉ. Trần chiết khấu 20%.
   - Chưa có giá bán lẻ nền thì ghi [CẦN ĐIỀN], không tự tính ra số tiền cuối.
   - Khách đòi điều chưa có chính sách (độc quyền khu vực, chiết khấu trên 20%, công nợ quá 15 ngày,
     ký gửi, giá riêng từng SKU): chỉ nói đúng 1 câu "Mức này vượt chính sách sỉ hiện hành,
     em cần xin ý kiến quản lý trước khi xác nhận với anh/chị." Không báo số, không hứa.
   - Karima là thiết bị tiêm, không nằm trong chính sách sỉ: chuyển quản lý.

   ## 3. Ranh giới sản phẩm
   Dùng bộ từ cấm theo tầng pháp lý trong file du-lieu-san-pham-wir.md.
   Khách hỏi thai kỳ: Elasten chỉ nói "không gây rủi ro" theo giám định; Warnke chống chỉ định;
   sản phẩm khác chưa có tài liệu thì chuyển người phụ trách.

   ## 4. Giọng văn
   Gọi khách "anh/chị", xưng "em". Tin nhắn dưới 150 chữ, không emoji.
   Tin Zalo gồm lời chào, nội dung, chữ ký.

   ## 5. Ba nguyên tắc chống bịa
   Chỉ dùng dữ liệu tôi cấp; gắn nhãn [DATA THẬT]/[SUY LUẬN]/[CẦN ĐIỀN];
   mọi tin gửi khách là nháp, tôi tự gửi.
   ```

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

## Mục 4 · Năm lượt chat thành một skill (slide 22)

**Cần có:** thanh bên → **Plugins** → tab **Skills** mở được (tài khoản Plus thử ngày 09/10/2026 có sẵn skill `skill-creator`, chính nó sẽ đóng gói giúp); một tài liệu dài để làm tay và một tài liệu khác để thử. Trên lớp dùng [Dữ liệu sản phẩm Wir](du-lieu-demo/du-lieu-san-pham-wir.md) (file `du-lieu-san-pham-wir.md` đã nằm trong Sources của Project) để làm tay, và [Hồ sơ Elasten](du-lieu-demo/ho-so-elasten.md) hoặc một tài liệu bất kỳ để thử. Tự tập ở nhà thì dùng [Transcript họp](du-lieu-demo/transcript-hop-demo.docx) để làm tay và [Review và tin nhắn khách](du-lieu-demo/review-va-tin-nhan-khach.docx) để thử. **Tạo ra:** skill `tom-tat-tai-lieu`, dùng lại ở Mục 6.

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
5. Thực hành slide 22: mỗi người chọn một việc lặp lại hằng tuần của mình, chat tay 3–5 lượt rồi đóng gói như bước 2. Sai thì sửa skill, không sửa tay kết quả.

**Đạt khi (kết quả thật 09/10/2026):** lượt 4 liệt kê 7 cụm "điều trị", "phòng ngừa & điều trị", "chữa khỏi"… vượt ranh giới TPCN; bước 3 skill tự chạy không cần gọi tên, bài ra đúng cấu trúc đã đóng gói (4 mục nội dung, kèm quy tắc chống bịa); bước 4 trong Project trả lời "Tài liệu không đề cập" và `[CẦN ĐIỀN]`.

## Mục 5 · Plugin có sẵn: Gmail, Drive, task tự động (slide 29)

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
   Khi tới bước ghi file, ChatGPT dừng và hiện hộp **"Allow ChatGPT to use Google Drive?"** với ba nút **Always allow / Deny / Allow once**. Bấm **Allow once**. Đây chính là chốt người duyệt của slide 25. Đáp án: 40 dòng, tổng 147.300.000 đ, Elasten 85.700.000 đ, Đại lý sỉ 106.710.000 đ. Mở Drive cho lớp thấy file mới, file gốc còn nguyên. Nếu Drive chưa có file, ChatGPT tìm theo tên, báo không thấy và xin link, không bịa số; có thể bảo nó tạo luôn: dán 40 dòng vào chat và gõ "Tạo trên Google Drive của tôi một Google Sheet tên don-hang-demo có đúng dữ liệu dưới đây" (đã thử, tạo đúng 41 dòng, 6 cột).
4. Task theo lịch: thanh bên → **Scheduled** → gõ vào ô "Schedule a task":
   ```
   Mỗi thứ Hai lúc 7:00, đọc file đơn hàng tuần mới nhất tên don-hang-demo trên Google Drive của tôi.
   Lập bảng doanh thu theo sản phẩm và theo kênh. Đối chiếu tổng với tổng cột Thanh_tien.
   Đánh dấu [CẢNH BÁO] ở dòng nào có Thanh_tien khác So_luong × Don_gia.
   Nếu file thiếu cột hoặc thiếu ngày: KHÔNG phân tích, chỉ báo cho tôi thiếu gì.
   Chỉ tạo thư NHÁP gửi tôi, không gửi cho ai khác.
   ```
   ChatGPT trả lời "Đã thiết lập lịch tự động", task hiện trong Scheduled với dòng "Weekly · Next run in N days". Nó chỉ chạy vào thứ Hai, giảng viên kiểm thư nháp sau lần chạy đầu. Demo xong thì xóa task.
5. Thực hành slide 29, phần 4A: học viên làm lại bước 1 đến 3 trên Gmail và Drive cá nhân của mình. Ai không nối Gmail thì dán 5 thư mẫu bất kỳ vào chat để làm bước 2.

**Đạt khi:** nối đúng tài khoản cá nhân; thư nháp chưa gửi; hộp Allow once xuất hiện trước khi ghi file; file gốc trên Drive còn nguyên; demo xong xóa task demo trong Scheduled.

## Mục 6 · Plugin tự tạo bằng Plugin Creator (slide 28)

**Cần có:** skill `tom-tat-tai-lieu` từ Mục 4, Gmail và Drive từ Mục 5, [Chính sách giá sỉ](du-lieu-demo/chinh-sach-gia-si-demo.docx) và [Dữ liệu sản phẩm Wir](du-lieu-demo/du-lieu-san-pham-wir.md). Thanh bên → Plugins → tìm **Plugin Creator** → Install. **Tạo ra:** plugin "Sale Wir".

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
4. Thực hành slide 29, phần 4B: viết Playbook 7 mục cho plugin (mục đích, ai dùng, quy trình, tiêu chuẩn đầu ra, ranh giới, chỉ số đo, xử lý khi sai) và đưa một đồng nghiệp chạy thử bằng @Sale Wir mà không được hỏi lại.

**Đạt khi (kết quả thật 09/10/2026 với @Sale Wir):** tin có đúng câu "Mức này vượt chính sách sỉ hiện hành, em cần xin ý kiến quản lý trước khi xác nhận với anh", không hứa độc quyền, cuối tin có "Đây là bản nháp", lưu ý nội bộ ghi `[DATA THẬT] Nguồn: Sale Wir, mục Hàng rào giá`; đồng nghiệp chạy được không cần hỏi.
