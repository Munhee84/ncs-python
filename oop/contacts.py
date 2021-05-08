'''
이름, 전호번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램 작성
'''
class Contacts:

    name = ''
    phone = ''
    email = ''
    address = ''

    def __str__(self):
        return f'이름 : {self.name} \n' \
               f'전화번호 : {self.phone}\n' \
               f'e-mail : {self.email}\n' \
               f'주소 : {self.address}'


class ContactsService:

    def set_contact(self):
        obj = Contacts()
        obj.name = input("이름 : ")
        obj.phone = input("전화번호 : ")
        obj.email = input("e-mail : ")
        obj.address = input("주소 ")
        return obj

    def get_contact(self, ls):
        for i in ls:
            print(i)

    def del_contact(self, ls, name):
        for i, j in enumerate(ls):  # i=index, j =element 리스트내부의 주소
            if j.name == name:
                del ls[i]

    def print_menu(self):
        print("1.연락처 입력 \n 2.연락처 출력 \n 3.연락처 삭제 \n 4.종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        service =  ContactsService()

        while 1:
            menu = service.print_menu()
            if menu == 1:
                t= service.set_contact()
                ls.append(t)
            elif menu == 2:
                t= service.get_contact(ls)
            elif menu == 3:
                name = input("삭제할 입름 :")
                service.del_contact(ls, name)
            elif menu ==4:
                break

if __name__ == '__main__':
    ContactsService.main()