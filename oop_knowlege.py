Để khai báo 1 class sử dụng keyword để định nghĩa "Class"
	class cha:
Mỗi Class sẽ có funtion khởi tạo có cú pháp bằng __init__ ,mỗi hàm đối số đầu tiên sẽ luôn là seft:
	def __init__(selt,x,y)
Sử dụng seft để gán giá trị cho các thuộc tính:
	selt.x=x
	selt.y=y
Trong mỗi class sẽ có các function riêng đựợc định nghĩa:
	def funct()
Với mỗi lớp con khi thừa kế thì sẽ phải thừa kế luôn từ hàm khỏi tạo, đầy đủ hàm khởi tạo cha rồi thêm các biến vào hàm khởi tạo cho con
- Để thừa kế, cú pháp là: 
		class con(cha): # tên class cha
			def __init__(selt,x,y,z) với z là biến của class con #hàm khởi tạo riêng của class con
			 kế thừa hàm khởi tạo cha bằng cú pháp: con.__init__(selt,x,y)
				Gán giá trị cho biến bằng selt: self.z=z

Với 1 function OOP có 3 phương thức: public, private,protected
- sau function muốn nó private thì dùng : __tên function = name
Với 1 function nằm ngoài class, có thể gọi vào class bằng cách gán function đó vào trong biến của class
Đê kiểm tra instance type dùng : isinstance(obj, int) kết quả sẽ trả về true, false
Để kiểm tra kế thừa hay không, dùng : issubclass(bool, int)

Hàm print được đinh nghĩa bởi function :
	def __str__()

=>Để sử dụng được file class, cần phải import file đó vào file thực thi:
	import file
	Gán biến để gọi class trong file: var1=file.con()
	Để gọi được function trong class con(): var1.funct()