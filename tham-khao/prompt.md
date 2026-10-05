# Prompt

> **Là gì:** phiếu giao việc cho ChatGPT, viết cho một việc cụ thể và dùng một lần.
> **Tra mục này khi:** kết quả chung chung phải hỏi lại nhiều lượt, cần phân tích file số liệu, hoặc cần kiểm chứng đầu ra trước khi dùng.

## Tóm tắt nhanh

- Một prompt đủ 4 phần: **Bối cảnh, Yêu cầu, Tiêu chí, Định dạng**.
- Phần nào đã có trong Instructions thì prompt không cần nhắc lại. Prompt chỉ ghi phần riêng của việc này.
- Với số liệu: đếm trước, phân tích sau, đối chiếu tổng.
- Việc lặp lại hằng tuần mà bạn đang gõ lại cùng một bộ chỉ dẫn thì chuyển thành Skill.

## Công thức 4 phần

Giao việc cho ChatGPT giống giao cho một nhân viên mới rất giỏi nhưng chưa biết gì về công ty. Prompt một dòng thường cho kết quả chung chung, rồi phải hỏi lại 4, 5 lượt.

| Phần | Trả lời câu hỏi | Ví dụ |
|---|---|---|
| **Bối cảnh** | Tôi là ai, tình huống gì, có dữ liệu gì | "Tôi là nhân viên Sale Wir. Spa Ngọc Anh muốn nhập thử 20 hộp Elasten/tháng." |
| **Yêu cầu** | AI phải làm việc gì cụ thể | "Soạn tin trả lời, báo chiết khấu theo bảng giá sỉ." |
| **Tiêu chí** | Thế nào là đạt: độ dài, giọng văn, điều cấm | "Dưới 150 chữ. Không hứa ngoài bảng. Không emoji." |
| **Định dạng** | Kết quả trình bày ra sao | "Tin nhắn Zalo: lời chào, nội dung, chữ ký." |

#### Thiếu phần nào thì bị gì

- Thiếu Bối cảnh: AI trả lời chung chung.
- Thiếu Tiêu chí: AI viết lan man, có thể hứa bừa.
- Thiếu Định dạng: phải sửa lại cách trình bày từ đầu.

## Ba kỹ thuật tăng chất lượng

1. **Đưa 1 mẫu tốt.** 1 mẫu tốt đáng giá hơn 10 dòng mô tả. Dán một bài hoặc một tin chuẩn cũ của phòng, bảo AI "học đúng bố cục và giọng văn của mẫu này".
2. **Cho AI hỏi lại.** Thêm câu: "Nếu thiếu thông tin, hỏi lại tôi tối đa 3 câu trước khi làm." AI sẽ hỏi thay vì tự bịa.
3. **Chia việc nhiều bước.** Việc lớn tách thành chuỗi prompt, xong bước trước mới chạy bước sau. Ví dụ: phân tích số liệu, rồi viết tóm tắt cho lãnh đạo, rồi dựng dàn ý slide. Mỗi bước kiểm tra xong mới đi tiếp.

## Prompt với file số liệu: 4 quy tắc

> **Cảnh báo:** Với số liệu, AI nguy hiểm nhất không phải lúc tính sai. Nguy hiểm nhất là lúc nó tự bịa ra một chiều phân tích mà file không có, rồi trình bày rất đẹp.

1. **Đếm trước, phân tích sau.** Bắt AI báo file có bao nhiêu dòng, những cột nào, rồi mới phân tích.
2. **Chỉ phân tích theo chiều mà file có.** File đơn hàng không có cột "nhân viên bán hàng" thì cấm tách doanh số theo nhân viên.
3. **Đối chiếu tổng.** Số tổng AI tính phải khớp với file gốc trước khi đưa vào báo cáo.
4. **Nguyên nhân là suy đoán.** Viết dạng "nghi do…, cần kiểm chứng bằng…". Không quy trách nhiệm cho cá nhân.

## Bốn cách kiểm chứng đầu ra

Kiểm chứng tốn vài phút, rẻ hơn rất nhiều so với hậu quả của một con số sai.

| Cách | Làm thế nào | Mất bao lâu |
|---|---|---|
| Ctrl+F trích dẫn | Copy câu AI "trích nguyên văn", tìm trong tài liệu gốc | 5 giây mỗi câu |
| Rà ngẫu nhiên số liệu | Chọn 2–3 con số, tự đối chiếu với nguồn | 1 phút |
| Phép thử đổi tên | Thay tên mình bằng tên đối thủ. Câu vẫn đúng tức là chưa đủ cụ thể | 30 giây |
| Bắt AI tự khai | "Chỗ nào bạn tự suy đoán mà tài liệu không nói?" | 1 lượt chat |

## Mẫu dùng ngay

Thay phần trong ngoặc vuông và dữ liệu ví dụ bằng việc thật của bạn.

### Trả lời khách hỏi giá sỉ

Prompt đủ 4 phần cho một tin trả lời khách.

```text title="Prompt đủ 4 phần · trả lời khách hỏi giá sỉ"
Bối cảnh: Tôi là nhân viên Sale của Wir Group. Chị Hương, chủ chuỗi Spa Ngọc Anh (3 chi nhánh,
TP.HCM), muốn nhập thử 20 hộp Elasten mỗi tháng và hỏi bà bầu dùng được không.
Elasten có giám định chuyên gia kết luận không gây rủi ro cho phụ nữ mang thai và cho con bú.
Bảng chiết khấu sỉ dán bên dưới.

Yêu cầu: Soạn tin trả lời chị Hương.

Tiêu chí: chiết khấu đúng bảng sỉ; chưa có giá bán lẻ nền thì ghi [CẦN ĐIỀN], không tự tính
số tiền; về thai kỳ chỉ nói "không gây rủi ro" theo giám định, KHÔNG nói "tốt cho thai kỳ";
không hứa gì ngoài bảng; dưới 150 chữ; không emoji.

Định dạng: tin nhắn Zalo gồm lời chào, nội dung, chữ ký [tên, số điện thoại].

Bảng chiết khấu sỉ:
[DÁN BẢNG]
```

Lead Spa Ngọc Anh và bảng chiết khấu là dữ liệu demo, tập với [Chính sách giá sỉ (Word)](du-lieu-demo/chinh-sach-gia-si-demo.docx). Kết luận giám định Elasten cho phụ nữ mang thai và cho con bú là `[DATA THẬT]` trong tài liệu Wir.

### Soạn tin theo mẫu có sẵn của phòng

Dùng kỹ thuật đưa 1 mẫu tốt.

```text title="Prompt có mẫu · tin chào sỉ"
Dưới đây là MẪU tin chào sỉ chuẩn của phòng Kinh doanh. Học đúng bố cục và giọng văn của mẫu:
lời chào, 1 câu nhắc đúng nhu cầu của khách, mức chiết khấu, bước tiếp theo, chữ ký.
Sau đó soạn tin mới cho chị Hoàng Mai, dược sĩ phụ trách Nhà thuốc Minh Châu (Bình Dương),
quan tâm CH Alpha Plus và Lactobact Intima, hỏi mức chiết khấu cho nhà thuốc, số lượng vừa.
Chỗ chưa có thông tin ghi [CẦN ĐIỀN].
Mẫu chuẩn:
[DÁN MẪU]
```

### Phân tích file số liệu

Tải file lên rồi chạy **2 bước**. Xong bước 1, đối chiếu tổng với file gốc rồi mới chạy bước 2. Tập với [Đơn hàng tháng 7 (Excel)](du-lieu-demo/don-hang-demo.xlsx), số đối chiếu có trong [đáp án](du-lieu-demo/dap-an.docx).

```text title="Bước 1 · đếm và tổng hợp"
File đính kèm có 6 cột: Ngày, Kênh, Sản phẩm, Số lượng, Đơn giá, Thành tiền.
File KHÔNG có cột nhân viên bán hàng, khách hàng, khu vực, giá vốn.
1. Cho tôi biết file có bao nhiêu dòng đơn hàng, từ ngày nào đến ngày nào, mấy kênh, mấy sản phẩm.
2. Lập bảng theo sản phẩm: số lượng, doanh thu, % tổng doanh thu.
3. Lập bảng theo kênh: số đơn, doanh thu, % tổng doanh thu.
4. Kiểm tra từng dòng: Thành tiền = Số lượng × Đơn giá. Dòng nào lệch thì liệt kê.
Tuyệt đối không tách theo nhân viên bán hàng, khách hàng hay khu vực.
```

```text title="Bước 2 · viết báo cáo 1 trang"
Từ các bảng vừa lập, viết báo cáo doanh thu tháng 7 một trang gửi Trưởng phòng Kinh doanh,
đọc 2 phút là quyết được.
Cấu trúc 5 phần: (1) kết quả chính; (2) cơ cấu theo sản phẩm và theo kênh; (3) 1 điểm sáng;
(4) 1 điểm cần chú ý; (5) 2-3 đề xuất cần duyệt.
Mỗi đề xuất đủ 4 thứ: việc cần làm, người chịu trách nhiệm, hạn, nguồn lực hoặc chi phí.
Mọi câu về nguyên nhân viết dạng "nghi do ..., cần kiểm chứng bằng ...".
Không quy trách nhiệm cho cá nhân.
Cuối bản thêm mục "Số liệu người ký cần kiểm lại trước khi trình".
```

### Rút insight từ review và tin nhắn khách

Tập với [Review và tin nhắn khách (Word)](du-lieu-demo/review-va-tin-nhan-khach.docx).

```text title="Prompt rút insight có mã bằng chứng"
Dưới đây là 20 review (R01–R20) và 10 tin nhắn hỏi trước khi mua (M01–M10) của khách
Elasten và Lactobact Intima.
1. Đếm trước: có bao nhiêu mẩu, bao nhiêu là review, bao nhiêu là tin nhắn.
2. Rút ra tối đa 5 insight theo công thức:
   [nhóm khách] + [lo/muốn gì] + [vì sao] + [mã bằng chứng] + [tần suất x/tổng].
3. Sắp xếp theo tần suất từ cao xuống thấp. Cấm viết "đa số", "rất nhiều".
4. Mỗi insight kèm 1 câu trích nguyên văn, giữ nguyên lỗi chính tả.
5. Pain về giao hàng, đóng gói thì tách thành mục riêng "chuyển bộ phận vận hành".
6. Khách tự nói "khỏi", "hết" thì giữ nguyên trong trích dẫn, nhưng không biến thành công dụng sản phẩm.
7. Cuối bài ghi 3 câu hỏi mà dữ liệu này KHÔNG trả lời được.
```

### Biên bản họp và bảng đầu việc

Trước khi dán bản ghi, thay tên khách và số liệu nhạy cảm bằng tên chung. Tập với [Bản ghi họp Phòng Kinh doanh (Word)](du-lieu-demo/transcript-hop-demo.docx).

```text title="Prompt · biên bản họp từ bản ghi thô"
Dưới đây là bản ghi cuộc họp [tên cuộc họp, ngày]. Viết biên bản gọn gồm:
1. Kết luận chính, mỗi kết luận 1 dòng.
2. Bảng đầu việc: Ai | Việc | Hạn.
3. Việc chờ duyệt hoặc chờ quyết định, ghi ai sẽ quyết.
Quy tắc:
- Chỉ ghi người và hạn được nói rõ trong cuộc họp. Chưa rõ ai làm hoặc chưa có hạn thì ghi
  [CẦN ĐIỀN], không tự gán tên.
- Giữ đúng con số, mục tiêu và mốc thời gian như trong bản ghi.
- Điều chưa chốt (giá, khuyến mãi, chính sách) ghi "chờ duyệt", không viết thành quyết định.
Bản ghi:
[DÁN BẢN GHI]
```

Đạt khi bắt đúng mục tiêu, con số và hạn đã nói rõ, và mọi việc chưa rõ người làm đều ghi `[CẦN ĐIỀN]`.

### Chấm điểm lead và soạn tin tiếp cận

Chạy 2 bước. Thay tên khách thật bằng mã lead trước khi dán. Tập với [Danh sách 12 lead (Excel)](du-lieu-demo/danh-sach-lead.xlsx), [Ghi chú trao đổi lead (Word)](du-lieu-demo/ghi-chu-trao-doi-lead.docx) và [Chính sách giá sỉ (Word)](du-lieu-demo/chinh-sach-gia-si-demo.docx).

```text title="Bước 1 · chấm điểm lead"
Dưới đây là danh sách lead và chính sách giá sỉ của phòng.
1. Đếm trước: có bao nhiêu lead, những cột nào.
2. Xếp mỗi lead vào 1 trong 3 nhóm: ƯU TIÊN / THEO DÕI / CHUYỂN QUẢN LÝ.
   Mỗi lead ghi 1 câu lý do lấy từ chính dữ liệu của lead đó.
3. Lead thiếu tên người liên hệ, vai trò hoặc tín hiệu mua: hạ độ tin cậy, ghi rõ thiếu gì.
   Không tự điền.
4. Lead đòi điều chưa có trong chính sách (độc quyền khu vực, chiết khấu trên trần,
   công nợ dài hơn mức cho phép, sản phẩm không có trong chính sách sỉ): xếp CHUYỂN QUẢN LÝ.
5. Lead hỏi sản phẩm cho phụ nữ có thai hoặc cho con bú: đối chiếu chống chỉ định trong
   hồ sơ sản phẩm, không tự kết luận là dùng được.
Xuất bảng: Mã lead | Nhóm | Độ tin cậy (cao / trung bình / thấp) | Lý do | Việc tiếp theo.
```

```text title="Bước 2 · soạn tin tiếp cận"
Soạn tin Zalo tiếp cận cho lead [mã lead], dựa trên ghi chú trao đổi bên dưới.
Tiêu chí: trích ít nhất 1 chi tiết từ ghi chú của chính lead này, không dùng chi tiết của
lead khác; chiết khấu chỉ theo bảng sỉ, chưa có giá bán lẻ nền thì ghi [CẦN ĐIỀN];
khách đòi điều chưa có chính sách thì chỉ dùng đúng câu "Mức này vượt chính sách sỉ hiện hành,
em cần xin ý kiến quản lý trước khi xác nhận với anh/chị." Không báo số, không hứa;
dưới 150 chữ; không emoji.
Định dạng: lời chào, nội dung, chữ ký [tên, số điện thoại].
Ghi chú trao đổi:
[DÁN GHI CHÚ]
```

## Ví dụ: chưa đạt và đạt

### Prompt một dòng

```text title="Prompt chưa đạt"
Trả lời spa hỏi giá sỉ Elasten.
```

Kết quả thường gặp: tự bịa giá, hứa chiết khấu vượt bảng, thậm chí nói Elasten "tốt cho bà bầu". Bản đạt là mẫu "Trả lời khách hỏi giá sỉ" ở trên.

### Báo cáo số liệu

| Bản chưa đạt (AI hay trả ra khi prompt sơ sài) | Bản đạt |
|---|---|
| "Nhìn chung tình hình kinh doanh tương đối ổn định…" | "Từ 01/07 đến 25/07 đạt 147.300.000 đ trên 40 đơn. Elasten chiếm 85.700.000 đ, khoảng 58%." |
| "Doanh số chưa cao là do nhân viên Sale chưa tích cực" (bịa, quy trách nhiệm, file không có cột nhân viên) | "Kênh đại lý sỉ chỉ 7 đơn nhưng chiếm 72,4% doanh thu. Nghi do phụ thuộc vào vài đại lý lớn, cần kiểm chứng bằng danh sách khách của 7 đơn sỉ" |
| "Tiếp tục đẩy mạnh bán hàng" | "Người giữ file đơn hàng bổ sung cột Khách hàng và Người bán từ tháng 8, hạn [CẦN ĐIỀN], chi phí gần như bằng 0" |

> **Lưu ý:** Số liệu trong ví dụ là dữ liệu demo để minh họa cách viết, không phải số kinh doanh thật.

### Insight từ phản hồi khách

| Insight chưa đạt | Insight đạt |
|---|---|
| "Đa số khách rất hài lòng với sản phẩm." | "Khách đang mang thai hoặc cho con bú lo sản phẩm ảnh hưởng tới em bé, nên hỏi trước khi mua (M01, M04, M06), 3/30 mẩu." |

> **Ghi nhớ:** Trong bộ dữ liệu demo, 16/20 review là 4–5 sao, nên chỉ đọc review dễ tưởng khách không có vấn đề gì. Nỗi lo đắt giá nhất nằm ở tin nhắn hỏi trước khi mua: thai kỳ (M01, M04, M06), nghi hàng thật (M03, R18, R19), bao lâu có kết quả (M02, R07), kỳ vọng "khỏi, hết" (M05, M08). Đối chiếu mã và trích dẫn bằng Ctrl+F.

## Kiểm tra prompt trước khi dùng kết quả

#### Đạt khi

- Prompt đủ 4 phần: Bối cảnh, Yêu cầu, Tiêu chí, Định dạng.
- Kết quả không có số bịa.
- Bạn đã tự kiểm chứng ít nhất 2 con số hoặc 2 trích dẫn, theo [bốn cách kiểm chứng](#prompt/prompt-bon-cach-kiem-chung-dau-ra).

#### Phép thử bẫy số liệu

Tải một file số liệu lên, rồi yêu cầu phân tích theo một chiều mà file không có. Ví dụ với [file đơn hàng](du-lieu-demo/don-hang-demo.xlsx), file không có cột nhân viên:

```text title="Phép thử bẫy số liệu"
Phân tích doanh số theo từng nhân viên bán hàng.
```

Đạt khi ChatGPT nói rõ file không có cột này. Nếu nó vẫn lập bảng theo nhân viên thì bảng đó là bịa. Sửa prompt: khai rõ file có cột gì và cấm tách theo chiều file không có, như bước 1 của mẫu "Phân tích file số liệu".

#### Khi cấp trên cần một chiều mà file không có

Nói rõ file không có dữ liệu đó, đề xuất lấy thêm nguồn, ví dụ bổ sung cột Người bán từ tháng sau. Không ép AI.

## Lỗi hay gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Prompt 1 dòng | Kết quả chung chung, phải hỏi lại 4–5 lượt | Viết đủ 4 phần ngay từ đầu |
| Tiêu chí bằng tính từ | "Viết hay hơn", "chuyên nghiệp hơn" | Đổi sang số: độ dài, số ý, điều cấm |
| Ép AI phân tích chiều file không có | Bảng theo nhân viên bán hàng "từ trên trời rơi xuống" | Khai rõ file có cột gì, cấm tách theo chiều không có |
| Tin ngay số tổng | Báo cáo lệch so với file gốc | Luôn đối chiếu tổng trước khi dùng |
| Sửa tay kết quả nhiều lần | Lần sau lại sai y như cũ | Sửa prompt. Nếu việc lặp lại thì đóng gói thành Skill |
| Gom nhiều việc vào 1 prompt | 10 bài viết giống nhau, chất lượng giảm | Chia nhỏ thành nhiều bước |

## Nguồn chính thức

Tính năng ChatGPT thay đổi nhanh. Khi màn hình khác với trang này, đối chiếu lại với nguồn chính thức dưới đây.

- [Phân tích dữ liệu trong ChatGPT – OpenAI Help](https://help.openai.com/en/articles/8437071)
- [ChatGPT Release Notes – OpenAI Help](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

## Liên quan

- [Instructions](#instructions): nơi đặt phần "tôi là ai" và luật chung, để prompt không phải nhắc lại.
- [Skill](#skill): khi một việc lặp lại hằng tuần, đóng gói prompt thành skill.
- [Skill template](#skill-template): thư viện bản hướng dẫn viết sẵn theo phòng ban.
