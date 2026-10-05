# Plugin

> **Là gì:** kết nối để ChatGPT với tới ứng dụng và dữ liệu thật như Gmail, Google Drive, lịch; đồng thời là cách đóng gói skill, tài liệu và app thành bộ công cụ của phòng.
> **Tra mục này khi:** cần nối ChatGPT với Gmail hoặc Drive, cần đặt hay gỡ quyền, muốn tự động một việc lặp lại, muốn đóng gói bộ công cụ để bàn giao cho đồng nghiệp, hoặc muốn biết AI tự thao tác trên trình duyệt và máy tính an toàn đến đâu.

## Tóm tắt nhanh

- Skill dạy ChatGPT làm **đúng**. Plugin cho ChatGPT **với tới dữ liệu thật**: hộp thư, file trên Drive, lịch.
- Mở quyền từng nấc: **đọc → ghi → gửi ra ngoài**. Gửi ra ngoài thì không rút lại được, nên luôn có người bấm duyệt.
- Gmail để mức **Always ask**. Khi ChatGPT hỏi duyệt, không bấm **Always allow**.
- Chỉ tự động việc lặp lại đều, quy tắc rõ, sai thì sửa được. Luồng nào cũng có người duyệt và có ghi log.
- Plugin tự tạo gồm **Skill + file tham chiếu + App**, kèm một bản Playbook cho người đọc.
- AI tự thao tác (Browser extension, Computer use, Dots) càng tự chủ thì phanh càng phải chắc. Xem mục [Nâng cao](#plugin/plugin-nang-cao-ai-tu-thao-tac).

## Hai loại plugin

| Loại | Là gì | Ví dụ |
|---|---|---|
| **Plugin có sẵn** | Kết nối do nhà cung cấp làm sẵn, bấm Connect là dùng | Gmail, Google Drive, Calendar, Notion, Slack, SharePoint |
| **Plugin tự tạo** | Gói Skill + file tham chiếu + App cho một quy trình trọn vẹn | "Plugin Marketing Wir", "Plugin Sale Wir" |

Plugin giống thẻ ra vào và chìa khóa tủ hồ sơ cấp cho nhân viên. Cấp chìa nào thì mở được tủ đó, nên cấp đúng và cấp vừa đủ.

## Skill và Plugin khác nhau thế nào

| | Skill | Plugin |
|---|---|---|
| Ví như | Tờ quy trình chuẩn cho 1 việc | Chìa khóa tủ hồ sơ, và thùng đồ nghề bàn giao |
| Cho ChatGPT | Cách làm đúng một loại việc | Đường vào ứng dụng và dữ liệu thật |
| Làm việc trên | Thứ bạn dán hoặc tải vào chat | Hộp thư, file trên Drive, lịch của tài khoản đã nối |
| Rủi ro chính | Làm sai quy trình | Đọc nhầm tài khoản, ghi đè file, gửi nhầm ra ngoài |

> **Ghi nhớ:** Skill chưa chuẩn thì plugin chỉ nhân bản cái sai nhanh hơn. Chuẩn hóa việc thành skill trước, nối app và tự động sau.

## Ba mức quyền: đọc, ghi, gửi ra ngoài

| Mức | ChatGPT làm được | Ví dụ | Rủi ro |
|---|---|---|---|
| **Đọc** | Xem thư, xem file | Phân loại 20 thư, đọc file đơn hàng trên Drive | Lộ thông tin nếu nối nhầm tài khoản |
| **Ghi** | Tạo thư nháp, tạo hoặc sửa file | Lưu bản tóm tắt lên Drive | Ghi đè file gốc |
| **Gửi ra ngoài** | Gửi email, đăng bài | Gửi tin trả lời khách | **Không rút lại được** |

Mở quyền dần từng nấc: đọc, rồi ghi, rồi mới tới gửi. Gửi ra ngoài là nấc cuối và luôn có người bấm duyệt. ChatGPT có hỏi trước khi gửi hay không là do bạn cài đặt, ở bảng dưới đây.

## Bốn mức quyền của mỗi app

Đặt tại Settings → Plugins → chọn app → Permissions.

| Mức quyền | ChatGPT làm gì | Dùng khi nào |
|---|---|---|
| **Always ask** | Hỏi duyệt trước mọi hành động | Mặc định cho Gmail, nhất là khi mới dùng |
| **Allow read** | Tự đọc; muốn ghi hoặc gửi thì hỏi | App chỉ cần để tra cứu, ví dụ Drive để đọc báo cáo |
| **Allow low-risk** (mặc định của ChatGPT) | Tự làm việc rủi ro thấp; việc rủi ro cao như gửi email thì hỏi duyệt hoặc từ chối | Sau khi đã quen và tin quy trình |
| **Allow all** | Làm hết, không hỏi | Không dùng cho Gmail và các kênh gửi ra ngoài |

> **Cảnh báo:** Khi ChatGPT hỏi duyệt, không bấm "Always allow". Bấm nút này là bỏ luôn chốt người duyệt cho những lần sau.

## Nối Gmail và Google Drive

Vào Plugins trong ChatGPT (thanh bên hoặc Settings → Plugins), chọn app → Install → Connect, rồi chọn đúng tài khoản Google.

### Trước khi nối

- Khi tập thử, chỉ nối tài khoản cá nhân. Không nối hộp thư hoặc tài khoản công ty.
- Đăng xuất tài khoản Google công ty trên trình duyệt trước, để không chọn nhầm.
- ChatGPT nối được **nhiều tài khoản Google cùng lúc** và có thể tìm trong cả hộp thư cá nhân lẫn hộp thư công ty. Đã nối nhiều tài khoản thì càng phải kiểm tra kỹ.
- Không muốn nối Gmail thì dán nội dung thư vào chat để làm việc như bình thường.

### Khi cấp quyền

- Đọc hết danh sách quyền trước khi bấm đồng ý.
- Google có thể hiện ô chọn từng quyền khi app xin nhiều nhóm quyền, ví dụ khi nối Drive.
- Riêng Gmail, ChatGPT xin **một quyền gộp "đọc, soạn và gửi email"**. Vì vậy không thể chỉ cho đọc mà chặn gửi ở màn hình của Google. Cách chặn gửi là đặt mức quyền **Always ask** trong ChatGPT.
- Thấy cảnh báo "ứng dụng chưa được xác minh" thì dừng lại, không bấm tiếp.

### Kiểm tra đã nối được chưa

Chạy câu kiểm tra ở mục [Mẫu dùng ngay](#plugin/plugin-kiem-tra-ket-noi). Kết quả đạt khi ChatGPT trả về đúng 3 tiêu đề thư bạn đang thấy trong Gmail. Thấy tiêu đề lạ tức là chưa nối được và ChatGPT đang bịa.

## Gỡ quyền

Gỡ ngay khi không còn dùng tới kết nối. Tập thử xong thì gỡ trong ngày.

1. Vào `myaccount.google.com/linkedapps` (trang Linked apps).
2. Chọn *Access to your Google Account*, rồi chọn dòng ChatGPT / OpenAI.
3. Bấm See details → Remove access → Confirm.
4. Vào ChatGPT: Settings → Plugins → chọn app → ngắt kết nối.

## Tự động hóa có kiểm soát

Tự động hóa là nhân bản quy trình. Quy trình đang tốt thì nhân ra nhiều cái tốt. Quy trình đang loạn thì nhân ra nhiều cái loạn, và nhanh hơn.

### Việc nào được tự động

| Tự động khi đủ cả 3 điều kiện | Không tự động |
|---|---|
| Việc lặp lại đều đặn | Việc dính tới tiền, ví dụ gửi báo giá sỉ |
| Quy tắc rõ ràng | Việc cam kết với khách, ví dụ trả lời về thai kỳ, công dụng sản phẩm |
| Làm sai thì sửa được | Quy trình đang còn loạn |

Nội dung về Karima (thiết bị tiêm) chỉ dành cho nhân viên y tế, tuyệt đối không tự động đăng.

### Ba lớp của một luồng và hai lớp phanh

Mỗi luồng tự động có 3 lớp: **kích hoạt → xử lý → đưa ra**. Chốt người duyệt đặt ở đầu lớp đưa ra.

- **Phanh 1, người duyệt:** ChatGPT chỉ tạo bản nháp, con người bấm gửi.
- **Phanh 2, hẹn giờ:** để một khoảng thời gian còn kịp hủy trước khi kết quả đi tiếp.
- **Ghi log:** luồng nào cũng ghi lại đã chạy lúc nào, ra kết quả gì, ai duyệt. Không có log thì không đo được, cũng không truy được lỗi.

### Công cụ tự động trên ChatGPT

| Công cụ | Kích hoạt | Ghi chú |
|---|---|---|
| **Scheduled task** | Theo lịch, ví dụ 7:00 thứ Hai hằng tuần | Hợp với báo cáo định kỳ |
| **Task theo sự kiện** (chạy trong ChatGPT Work) | Khi có thư Gmail mới (lọc theo người gửi hoặc tiêu đề), tin nhắn kênh Slack | Tối đa 30 lần/giờ, 720 lần/ngày |
| **ChatGPT Work** | Giao trọn một mục tiêu nhiều bước | ChatGPT tự lên kế hoạch và tự làm ra file docx/xlsx/pptx hoặc Google Docs/Sheets/Slides |

- Gặp hành động cần duyệt, task **tạm dừng chờ người duyệt**. Đây chính là phanh thứ nhất.
- Task tạo trong một Project **không đọc được file của Project đó**. File nguồn nên để trên Drive.
- Càng tự động thì phanh càng phải chắc: chỉ cho soạn nháp, Gmail để mức Always ask, và ghi log.

> **Lưu ý:** Tài liệu chính thức ghi task dùng được Gmail và Slack. Task có đọc được Google Drive hay không thì chưa xác minh được, hãy chạy thử trước khi dựa vào. Nếu không đọc được, đổi đầu vào thành "thư báo cáo đơn hàng gửi vào Gmail".

## Plugin tự tạo: bộ công cụ của phòng

Nếu toàn bộ cách làm nằm trong đầu một người thì người đó nghỉ phép là việc dừng. Plugin tự tạo là đóng thùng đồ nghề: quy trình, tài liệu và chìa khóa đi cùng nhau, người khác mở ra là làm được.

| Thành phần | Trong plugin là | Ví dụ "Plugin Marketing Wir" | Ví dụ "Plugin Sale Wir" |
|---|---|---|---|
| **Skill** | Quy trình | `viet-bai-tpcn`, `customer-insight`, `content-engine` | `cham-diem-lead`, `soan-tiep-can-sale`, `xu-ly-tu-choi-sale`, `tom-tat-tai-lieu` |
| **File tham chiếu** | Tài liệu nguồn sự thật | Dữ liệu sản phẩm Wir (bộ từ cấm 3 tầng), hồ sơ Elasten, hồ sơ Lactobact Intima | Dữ liệu sản phẩm Wir, chính sách giá sỉ, playbook |
| **App** | Chìa khóa | Google Drive | Google Drive, Gmail |

```text
Plugin: Sale Wir
├── Skills
│   ├── cham-diem-lead
│   ├── soan-tiep-can-sale
│   ├── xu-ly-tu-choi-sale
│   └── tom-tat-tai-lieu
├── File tham chiếu
│   ├── du-lieu-san-pham-wir.md
│   ├── chinh-sach-gia-si.md
│   └── playbook.md
└── Apps
    ├── Google Drive
    └── Gmail
```

### Cách tạo, không cần code

1. Cài **Plugin Creator** từ danh mục plugin (Plugins → Add).
2. Mở chat, gõ `@plugin-creator` và mô tả plugin muốn tạo. Câu lệnh mẫu có ở mục [Mẫu dùng ngay](#plugin/plugin-cau-lenh-cho-plugin-creator).
3. Gộp các skill đã có, thêm file tham chiếu và app cần nối.

Về mặt kỹ thuật, file tham chiếu nằm trong thư mục `references/` của từng skill.

### Chia sẻ plugin

- Plugin mới tạo ở chế độ **riêng tư**.
- Chia sẻ trong workspace công ty: ••• → Share plugin. Người chia sẻ cần có quyền chia sẻ plugin.
- Người nhận phải tự cài plugin và tự nối app của mình.

### Phép thử trước khi bàn giao

1. Mở chat mới.
2. **Không gọi tên plugin hay skill.**
3. Giao 2 yêu cầu nằm ngoài những gì đã dùng khi xây plugin.

Plugin đạt khi người khác cầm lên chạy được mà không phải hỏi lại, và khi hỏi một con số không có trong tài liệu thì ChatGPT trả lời "chưa đủ dữ liệu".

Ví dụ phép thử cho plugin Sale có chính sách giá sỉ. Khách đòi một điều chưa có trong chính sách:

```text title="Phép thử · khách đòi độc quyền khu vực"
Anh Bảo, Công ty phân phối Bảo Phát (Hải Phòng), muốn làm đại lý Elasten nhưng đòi độc quyền
khu vực Hải Phòng. Soạn giúp tôi tin trả lời.
```

Đạt khi:

- Báo chiết khấu đúng bảng. Chưa có giá bán lẻ nền thì ghi `[CẦN ĐIỀN]`.
- Phần độc quyền khu vực chỉ dùng đúng câu "Mức này vượt chính sách sỉ hiện hành, em cần xin ý kiến quản lý trước khi xác nhận với anh/chị." Không hứa.
- Cuối bản có dòng "Đây là bản nháp".

### Mẫu tài liệu (Templates) trong ChatGPT Work

Dùng cho những việc làm file theo mẫu của phòng.

- **Tạo mẫu:** gọi `@Template-Creator` để tạo mẫu báo cáo, mẫu bảng tính, mẫu slide theo nhận diện của phòng.
- **Dùng mẫu:** gọi `@Documents`, `@Spreadsheets` hoặc `@Presentations` để làm file theo mẫu.
- **Chia sẻ mẫu cho cả đội:** đóng gói mẫu vào plugin của phòng.

## Playbook: phần dành cho người đọc

Skill là thứ ChatGPT đọc. Playbook là thứ con người đọc. Thiếu Playbook thì đồng nghiệp có plugin trong tay mà không biết bắt đầu từ đâu, không biết kết quả thế nào là đủ để gửi.

| Mục | Trả lời câu hỏi | Viết bao nhiêu |
|---|---|---|
| Mục đích | Hệ thống giải bài toán gì, thay việc nào đang làm tay | 2–3 dòng |
| Ai dùng | Vị trí nào, cần biết gì trước | 2 dòng |
| Quy trình từng bước | Mở gì, gõ gì, làm gì tiếp | Bảng: mỗi bước ghi đầu vào và đầu ra |
| Tiêu chuẩn đầu ra | Thế nào là đạt | Chép từ Skill |
| Ranh giới | Cấm gì, không được tự quyết gì | Chép từ Skill |
| Chỉ số đo | Nhìn vào đâu biết hệ thống có tác dụng | 3 chỉ số quá trình, 2 chỉ số kinh doanh |
| Xử lý khi ra sai | Sai thì làm gì, ai làm | 3 mức: sửa prompt; bổ sung dữ liệu; dừng và báo người phụ trách |

Chỉ số quá trình gồm: thời gian làm 1 đầu ra, số đầu ra mỗi tuần, tỉ lệ bản nháp được duyệt ngay lần đầu. Không hứa doanh thu trong 2 tuần đầu.

## Mẫu dùng ngay

Thay tên file, tên thư mục và điều kiện lọc bằng thông tin thật của bạn trước khi dán.

### Kiểm tra kết nối

Chạy ngay sau khi nối Gmail.

```text title="Kiểm tra đã nối Gmail"
Đọc tiêu đề 3 thư gần nhất trong hộp thư đến. Chỉ đọc, không trả lời, không xóa.
```

### Phân loại thư và soạn nháp

```text title="Gmail · phân loại 20 thư và soạn nháp"
Đọc 20 thư gần nhất trong hộp thư. Xếp vào 4 nhóm: KHẨN / QUAN TRỌNG / CHỜ / BỎ QUA.
Xuất bảng: Người gửi | Nhóm | Lý do (1 câu) | Việc cần làm | Hạn.
Sau đó soạn NHÁP trả lời cho thư khẩn nhất. Không gửi.
Thư nào hỏi về thai kỳ, công dụng chữa bệnh hoặc giá ngoài chính sách thì ghi [CẦN NGƯỜI DUYỆT].
```

### Đọc và ghi file trên Drive

```text title="Google Drive · tổng hợp file đơn hàng"
Trên Drive của tôi có file don-hang-demo.xlsx. Đọc tên các cột và đếm số dòng trước.
Tổng hợp doanh thu theo sản phẩm và theo kênh.
Lưu kết quả thành file mới tên tom-tat-don-hang-thang-7 trong cùng thư mục. Không sửa file gốc.
```

Tập thử: tải [Đơn hàng tháng 7 (Excel)](du-lieu-demo/don-hang-demo.xlsx) lên Drive cá nhân trước. Đạt khi ChatGPT đếm đúng 40 dòng, tổng 147.300.000 đ, và file gốc trên Drive còn nguyên. Số đối chiếu đầy đủ có trong [đáp án](du-lieu-demo/dap-an.docx).

### Bảng luồng tự động

Vẽ bảng này trước khi viết câu lệnh task. Ví dụ với luồng báo cáo tuần:

| Kích hoạt | Xử lý | Đưa ra | Ai duyệt | Ghi log ở đâu |
|---|---|---|---|---|
| 07:00 thứ Hai hằng tuần | Đọc file đơn hàng tuần trên Drive. Kiểm dữ liệu: thiếu cột hoặc thiếu ngày thì dừng và báo. Lập bảng doanh thu theo sản phẩm, đánh dấu cảnh báo | Bản nháp báo cáo tuần lưu trên Drive và thư nháp gửi Trưởng phòng | Trưởng phòng duyệt, rồi mới gửi Ban giám đốc | Sheet "Log báo cáo tuần": ngày chạy, file nguồn, người duyệt, sửa gì |

### Task theo lịch: báo cáo tuần

```text title="Scheduled task · báo cáo doanh thu tuần"
Mỗi thứ Hai lúc 7:00, đọc file đơn hàng tuần mới nhất trong thư mục Báo cáo trên Drive.
Lập bảng doanh thu theo sản phẩm và theo kênh. Đối chiếu tổng với tổng cột Thành tiền.
Đánh dấu [CẢNH BÁO] ở dòng nào có Thành tiền khác Số lượng × Đơn giá.
Nếu file thiếu cột hoặc thiếu ngày: KHÔNG phân tích, chỉ báo cho tôi thiếu gì.
Chỉ tạo thư NHÁP gửi tôi, không gửi cho ai khác.
```

### Task theo sự kiện: thư khách sỉ

Tạo trong ChatGPT Work.

```text title="Task theo sự kiện · thư đặt hàng sỉ"
Khi có thư Gmail mới có tiêu đề chứa "đặt hàng sỉ" hoặc "báo giá":
1. Tóm tắt thư trong 3 dòng: khách muốn gì, sản phẩm và số lượng, việc tôi cần làm.
2. Soạn NHÁP thư trả lời theo bảng chiết khấu sỉ. Khách đòi điều chưa có chính sách
   (độc quyền khu vực, chiết khấu trên 20%, công nợ quá 15 ngày) thì chỉ dùng đúng câu
   xin ý kiến quản lý, không báo số.
3. Không gửi gì ra ngoài. Ghi 1 dòng vào Sheet "Log thư khách sỉ": giờ nhận, người gửi, tóm tắt.
```

### Câu lệnh cho Plugin Creator

```text title="Plugin Creator · tạo plugin Sale Wir"
@plugin-creator Tôi muốn tạo plugin "Sale Wir" cho đội Sale khách sỉ. Tôi không biết code.
Hãy phỏng vấn tôi trước, mỗi lần một nhóm câu, đừng tạo ngay:
1. Việc lặp lại nào plugin sẽ làm, ai dùng, đầu ra gửi cho ai.
2. Các bước và bước nào bắt buộc có người duyệt.
3. Tiêu chuẩn đầu ra: hỏi tôi bằng số. Nếu tôi trả lời bằng tính từ, hỏi ngược "một bản
   KHÔNG đạt trông thế nào?".
4. Ranh giới: từ cấm theo tầng pháp lý sản phẩm, điều chưa có chính sách giá sỉ,
   sản phẩm không được báo giá (Karima).
5. File tôi có sẵn và app cần nối.
Sau khi phỏng vấn: gộp các skill tôi đã có, thêm file tham chiếu và app Drive, Gmail.
Bắt buộc có 3 nguyên tắc chống bịa: chỉ dùng dữ liệu tôi cấp; gắn nhãn [DATA THẬT]/[SUY LUẬN];
mọi thứ gửi khách là nháp, không tự gửi.
Cuối cùng đề xuất 2 yêu cầu thử nằm ngoài những gì tôi đã kể.
```

## Lỗi hay gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Nối nhầm tài khoản công ty | ChatGPT đọc ra địa chỉ email công ty | Dừng ngay. Gỡ quyền trước khi chạy bất kỳ câu lệnh nào |
| Bấm đồng ý mà không đọc quyền | Không biết mình đã cho ChatGPT quyền đọc, soạn và gửi thư | Đọc hết danh sách quyền trước khi bấm |
| Để mức quyền mặc định hoặc bấm "Always allow" | ChatGPT gửi thư hoặc ghi file mà không hỏi | Đặt Gmail ở mức Always ask. Không bấm Always allow khi được hỏi duyệt |
| Nối nhiều tài khoản Google mà không kiểm tra | ChatGPT tìm cả trong hộp thư công ty | Vào Settings → Plugins kiểm tra danh sách tài khoản đã nối, gỡ tài khoản công ty |
| ChatGPT "đọc" ra dữ liệu lạ | Tiêu đề thư hoặc tên cột không có thật | Chưa nối được, ChatGPT đang bịa. Kiểm tra lại kết nối |
| Tự động hóa khi quy trình còn loạn | Luồng chạy ra lỗi hàng loạt | Chuẩn hóa thành skill trước, tự động sau |
| Không có chốt duyệt hoặc không ghi log | Bài đăng hoặc thư đi mà không ai biết | Thêm người duyệt ở đầu lớp đưa ra. Ghi log vào Sheet |
| Plugin thiếu file tham chiếu | Đồng nghiệp chạy thì skill "rỗng", ChatGPT tự bịa giá | Gộp đủ file nguồn sự thật vào plugin |
| Quên gỡ quyền | Kết nối vẫn còn sau nhiều tuần | Gỡ quyền ngay khi xong việc, theo 4 bước ở mục Gỡ quyền |

> **Lưu ý:** Tên và vị trí menu trong ChatGPT thay đổi nhanh. Connectors đã đổi tên thành Apps (12/2025); từ 09/07/2026 App Directory được thay bằng Plugin Directory, và Agent mode được thay bằng ChatGPT Work. Thông tin ở trang này tra cứu ngày 05/10/2026.

## Nâng cao: AI tự thao tác

> **Lưu ý:** Mục này để biết các công cụ đang có, làm được gì và rủi ro ở đâu. Không cài, không dùng cho việc của công ty khi chưa được phép.

Đến Plugin, ChatGPT làm việc trên chữ, trên file và trên dữ liệu bạn nối vào. Bước tiếp theo là ChatGPT tự cầm chuột: tự mở trang web, tự bấm nút trong phần mềm, thậm chí tự theo dõi công việc nhiều ngày liền. Càng tự làm được nhiều thì phanh càng phải chắc.

### Ba công cụ, mức tự chủ tăng dần

| Công cụ | ChatGPT làm gì | Ví như | Mức rủi ro | Nguyên tắc giữ |
|---|---|---|---|---|
| **Browser extension** | Đọc và thao tác trên trang web bạn đang đăng nhập sẵn (Chrome, Edge, Brave, Vivaldi, Opera) | Nhờ đồng nghiệp ngồi cạnh dùng trình duyệt của mình lướt web giúp | Trung bình | Chỉ chọn Allow once hoặc Allow for site. Trang web có thể cài lệnh ẩn |
| **Computer use** | Nhìn màn hình, tự click, tự gõ phím trong phần mềm trên Mac hoặc Windows | Giao chuột và bàn phím cho người khác | Cao | Đóng phần mềm nhạy cảm trước khi dùng. Không bấm Always allow |
| **Dots** | Agent chạy liên tục trên máy tính đám mây riêng, tự theo dõi việc nhiều ngày. Nhận việc qua ChatGPT, Slack, Teams hoặc gọi thoại | Một trợ lý riêng vẫn làm việc khi bạn không ngồi ở máy | Cao nhất, vì tự chủ nhiều nhất | Đặt luật "cho tôi xem nháp trước khi gửi" |

### Browser extension: thao tác trên trình duyệt

#### Làm được gì

- Dùng được các trang web bạn **đang đăng nhập sẵn**, với khung chat mở bên cạnh trang.
- Gọi một tab đang mở vào cuộc chat bằng `@`. Bôi đen đoạn văn để đưa vào chat.
- Tóm tắt video YouTube có phụ đề.
- Thao tác trên trang web theo yêu cầu bằng lời.
- Chạy trong app ChatGPT desktop, dùng trong ChatGPT Work. Đang triển khai dần.

#### Dùng vào việc gì

- Mở 3 trang sản phẩm collagen của đối thủ, nhờ ChatGPT lập bảng so sánh giá và thành phần với Elasten.
- Tóm tắt bài báo ngành dược mỹ phẩm đang mở, tóm tắt video hội thảo có phụ đề.
- Làm việc trên phần mềm chạy trên web chưa có plugin: trang quản trị gian hàng, CRM, hệ thống nội bộ.

#### Điểm cần biết

- **Extension xin quyền rất rộng:** đọc dữ liệu mọi trang, lịch sử duyệt web, bookmark, file tải về.
- **ChatGPT hỏi trước khi vào một trang mới,** với 4 lựa chọn: cho phép một lần, cho phép với trang đó, cho phép mọi trang, hoặc từ chối.
- **Nội dung trang web là nguồn không đáng tin.** Trang web có thể cài sẵn lệnh ẩn để điều khiển ChatGPT, nên người phải kiểm lại kết quả.
- **Máy công ty có thể bị IT chặn cài extension.**

#### Nguyên tắc khi dùng

- Dùng một profile trình duyệt riêng.
- Chọn "Allow once" hoặc "Allow for site". Không chọn "Allow all sites".
- Không dùng trên trang đang đăng nhập tài khoản công ty khi chưa được phép.

### Computer use: điều khiển phần mềm trên máy

ChatGPT chụp màn hình để nhìn, rồi tự click, gõ phím, chuyển cửa sổ trong các phần mềm cài trên máy Mac hoặc Windows. Cần app desktop và plugin Computer Use, dùng trong ChatGPT Work. Trên Mac phải cấp quyền Screen Recording và Accessibility.

#### Dùng vào việc gì

- Thao tác trong phần mềm cài trên máy mà không có plugin, ví dụ Excel bản cài máy, phần mềm kế toán hoặc ERP bản desktop.
- Làm một chuỗi việc qua nhiều phần mềm, ví dụ lấy số liệu từ Excel rồi dán vào báo cáo Word.

#### Điểm cần biết

- **Tài liệu của OpenAI chủ yếu hướng tới lập trình viên,** như kiểm thử ứng dụng hay tái hiện lỗi.
- **ChatGPT hỏi trước khi dùng từng phần mềm.** Có nút "Always allow". Không bấm nút này.
- **Giới hạn có sẵn:** không điều khiển được cửa sổ dòng lệnh (Terminal) và chính ChatGPT; không đăng nhập bằng quyền quản trị; không vượt qua các hộp thoại bảo mật.
- **Trên Windows, ChatGPT chạy trên chính màn hình đang dùng.** Trong lúc nó chạy, bạn không làm việc khác song song được.
- **ChatGPT nhìn thấy mọi thứ đang mở trên màn hình.** Đóng các phần mềm nhạy cảm trước khi dùng.

> **Cảnh báo:** Không giao cho AI tự thao tác: nhập liệu vào hệ thống chính thức của công ty; thanh toán; cài đặt tài khoản, bảo mật, mạng.

### Dots: trợ lý luôn bật

#### Làm được gì

- Một agent "luôn bật", có máy tính và trình duyệt riêng trên đám mây.
- Tự quyết định lúc nào dừng và lúc nào làm tiếp. Có thể giao bớt việc cho ChatGPT Work chạy nền.
- Nhớ các quyết định và sở thích của người dùng qua nhiều phiên làm việc.
- Ở workspace công ty, admin phải bật. Đang triển khai dần.

#### Ví dụ trong tài liệu của OpenAI

- Giữ bản đề xuất bán hàng luôn cập nhật khi khách đổi số lượng hoặc điều khoản, và báo cho bạn những quyết định cần đưa ra tiếp.
- Từ mỗi buổi phỏng vấn, chuẩn bị caption, ghi chú và ý tưởng cắt clip để bạn duyệt.
- Cập nhật bảng so sánh mỗi khi có kết quả mới, và giải thích chỗ kết quả lệch nhau.

#### Điểm cần biết

- **Trước khi Dot làm việc ảnh hưởng tới tài khoản hoặc chia sẻ thông tin ra ngoài,** hệ thống tự kiểm tra và xếp hành động vào 1 trong 3 loại: Dot được tự làm, phải xin duyệt, hoặc phải chuyển cho người làm.
- **Có thể đặt luật riêng,** ví dụ "cho tôi xem bản nháp trước khi gửi".
- **Trình duyệt đám mây của Dot có phiên đăng nhập riêng,** tách khỏi trình duyệt trên máy bạn. Một số trang web chặn trình duyệt đám mây.

Dots là ví dụ rõ nhất của mức "Tác nhân (Agent)": người dùng chuyển vai, từ người giao từng thao tác sang **người đặt mục tiêu và duyệt kết quả**.

### Nguyên tắc vẫn giữ nguyên khi AI tự cầm chuột

- Quyền tăng dần từ đọc, sang ghi, rồi mới tới gửi.
- Duyệt từng trang, từng phần mềm.
- Không bấm "Always allow".
- Người duyệt cuối.
- Không dùng tài khoản công ty khi chưa được phép.

#### Trước khi đề xuất đưa vào dùng, trả lời được 2 câu

1. Trong công việc của bạn, phần mềm nào chạy trên web mà chưa có plugin? Nếu ChatGPT thao tác được trên đó, việc nào muốn giao, việc nào tuyệt đối không giao?
2. Nếu giao cho một trợ lý luôn bật theo dõi báo cáo doanh thu tuần, bạn đặt những điểm duyệt nào? Dùng [bảng luồng tự động](#plugin/plugin-bang-luong-tu-dong) để vẽ.

## Nguồn chính thức

Tính năng ChatGPT thay đổi nhanh. Khi màn hình khác với trang này, đối chiếu lại với nguồn chính thức dưới đây.

- [Plugins in ChatGPT – OpenAI Help](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
- [Mức quyền của app (Permissions) – OpenAI Help](https://help.openai.com/en/articles/20001495)
- [Google Drive trong ChatGPT – OpenAI Help](https://help.openai.com/en/articles/10929079)
- [Scheduled tasks – OpenAI Help](https://help.openai.com/en/articles/10291617)
- [ChatGPT Work – OpenAI Help](https://help.openai.com/en/articles/20001275)
- [Package your plugin – OpenAI Developers](https://developers.openai.com/plugins/build/plugins)
- [Granular OAuth permissions – Google](https://developers.google.com/identity/protocols/oauth2/resources/granular-permissions)
- [Quản lý ứng dụng đã liên kết – Google Account Help](https://support.google.com/accounts/answer/13533235)
- [ChatGPT browser extension – learn.chatgpt.com](https://learn.chatgpt.com/docs/chrome-extension)
- [Computer use – learn.chatgpt.com](https://learn.chatgpt.com/docs/computer-use)
- [Dots – learn.chatgpt.com](https://learn.chatgpt.com/docs/dots)
- [ChatGPT Release Notes – OpenAI Help](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

## Liên quan

- [Skill](#skill): quy trình chuẩn cho một việc. Skill là thành phần chính của plugin tự tạo.
- [Skill template](#skill-template): thư viện bản hướng dẫn viết sẵn; đóng gói thành skill trước, rồi gộp vào plugin của phòng.
- [Instructions](#instructions): luật chung và nguyên tắc chống bịa, áp dụng cả khi ChatGPT đọc dữ liệu qua plugin.
- [Prompt](#prompt): công thức 4 phần cho các câu lệnh dùng plugin.
