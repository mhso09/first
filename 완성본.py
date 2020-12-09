menuList = ["1", "2", "3", "4", "5", "6"]
Menu_names = ["입력", "출력", "수정", "삭제", "검색", "종료"]

class books(object):
    Names = []
    Ages = []
    Phones = []
    Addresis = []
    Mails = []
    Groups = []
    def update(self):
        name = input("수정할 이름을 입력해주세요.")
        name = name.strip().upper()
        if name in books.Names:
            idx = books.Names.index(name)
            name = input("이름을 바꿔주세요.")
            name = name.strip().upper()
            phone = input("번호를 바꿔주세요.")
            phone = phone.strip().upper()
            books.Names[idx] = name
            books.Phones[idx] = phone
            print("수정 되었습니다.")
        else:
            print("없는 사람입니다.")
            return
    def nEmpty(self):
        n = len(books.Names)
        if n == 0:
            return True
        else:
            return False
    def list_All(self):
        print("     목록")
        print("-----------------")
        bEmpty = books.nEmpty(self)
        if bEmpty == True:
            print("비어있습니다.")
            return
        for i, name in enumerate(books.Names):
            phone = books.Phones[i]
            age = books.Ages[i]
            address = books.Addresis[i]
            mail = books.Mails[i]
            group = books.Groups[i]
            print("{0}번째 멤버 \nname : {1}{2} \nphone : {3} \nage : {4} \naddress : {5} \nmail : {6} \ngroup : {7} \n-----------------"
                .format(i+1, name[0], name[1:].lower(), phone, age, address, mail, group))
        print("Total : {} 명".format(len(books.Names)))
    def search(self):
        choice = input("사람 그룹 (P / G)")
        choice = choice.strip().upper()
        if choice == "P":
            name = input("이름을 입력해주세요.")
            name = name.strip().upper()
            if name in books.Names:
                idx = books.Names .index(name)
                phone = books.Phones[idx]
                print("이름 : {0}{1} \n번호 :{2}".format(
                    name[0], name[1:].lower(), phone))
                return idx
        elif choice == "G":
            group = input("그룹을 입력해주세요.")
            group = group.strip().upper()
            print("ㅡㅡGROUP(    NUM    )ㅡㅡㅡㅡㅡㅡㅡ")
            if group in books.Groups:
                i = 0
                idx = books.Groups.index(group)
                name = books.Names[idx]
                phone = books.Phones[idx]
                address = books.Addresis[idx]
                print("{0}번째 멤버\n이름 : {1}{2} \n번호 : {3} \n주소 : {4}".format(
                    i+1, name[0], name[1:], phone, address))
        else:
            print("없습니다.")
            return None
    def delete(self):
        name = input("삭제할 이름을 입력해주세요.")
        name = name.strip().upper()
        if name in books.Names:
            idx = books.Names.index(name)
            del books.Names[idx]
            del books.Phones[idx]
            print("{0}{1}님의 정보가 삭제되었습니다.".format(name[0].upper(), name[1:]))
        else:
            print("없습니다.")
            return
    def insert(self):
        print("입력해주세요")
        name = input("새로운 이름을 입력해주세요.")
        name = name.strip().upper()
        phone = input("폰 번호를 입력해주세요.")
        phone = phone.strip().upper()
        age = input("나이를 입력해주세요.")
        age = age.strip()
        address = input("주소를 입력해주세요.")
        address = address.upper()
        mail = input("메일을 입력해주세요.")
        mail = mail.upper()
        group = input("그룹을 입력해주세요.")
        group = group.strip().upper()

        books.Names.append(name)
        books.Ages.append(age)
        books.Phones.append(phone)
        books.Addresis.append(address)
        books.Mails.append(mail)
        books.Groups.append(group)

        print("등록되었습니다.")
        ins = input("계속 입력하시겠습니까?  y / n")
        if ins == "y":
            books.insert(self)
        elif ins == "n":
            return
        elif ins != "y" or "n":
            while True:
                ins = input("다시 입력해주세요.")
                if ins == "y":
                    books.insert(self)
                elif ins == "n":
                    break
        elif ins == "n":
            return

import 로그인
_id = input("ID : ")
_pwd = input("PASSWORD : ")
book1 = books()
bFinish = False
if 로그인.login(_id, _pwd):
    print("로그인 성공")

    while not bFinish:
        print("-----------------\n menu")
        for a, k in enumerate(Menu_names):
            print(a+1, k)
        print("-----------------")
        menu = ""
        while True:
            menu = input("무엇을 선택하시겠습니까?  ")
            menu = menu.strip().upper()
            print()
            if menu in menuList:
                break
        if menu == "1":
            book1.insert()
        elif menu == "2":
            print("모든 멤버를 출력합니다.")
            book1.list_All()
        elif menu == "3":
            book1.update()
        elif menu == "4":
            book1.delete()
        elif menu == "5":
            book1.search()
        elif menu == "6":
            print("종료합니다.")
            bFinish = True
else:
    print('로그인 실패')
