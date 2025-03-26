from ListByClass import ArrayList

list = ArrayList()
while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")

    if command == "i":
        pos = int(input(" 입력행 번호: "))
        content = input(" 입력행 내용: ")
        list.insert(pos, content)

    elif command == "d":
        pos = int(input(" 삭제행 번호: "))
        list.delete(pos)
    
    elif command == "r":
        pos = int(input(" 변경행 번호: "))
        content = input(" 변경행 내용: ")
        list.delete(pos)
        list.insert(pos, content)
    
    elif command == "p":
        for i in range(list.size):
            print("[%d] %s" % (i, list.array[i]), end='\n')
        
    elif command == "l":
        # filename = r"C:\Users\...\LineEditorText.txt"

        filename = 'LineEditorText.txt'
        f = open(filename, 'r') # r은 파일읽기 모드를 준비한다
        
        # lines = f.read() # read() 파일의 텍스트 전체를 하나의 문자열로 출력 
        # print(lines)
        lines = f.readlines() # readlines()는 각 줄을 원소로 하는 리스트를 반환
        for line in lines:
            line = line.strip() # 각 요소의 빈 줄을 없애줌
            print(line)

    elif command == "s":
        filename = 'LineEditorText.txt'
        w = open(filename, 'w') 

        for i in range(list.size):
            # 문자형이 아닌 경우 문자형 변환
            if not isinstance(list.array[i], str):
                list.array[i] = str(list.array[i])
            w.write(list.array[i] + '\n')
        
        w.close() # close() 해야 값이 저장됨

    elif command == "q":
        break
    
    
    
    
