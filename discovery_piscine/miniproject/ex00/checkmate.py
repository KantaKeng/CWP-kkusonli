def checkmate(board):
    rows = board.split("\n") #เอากระดาน แบ่งเป็นแถว
    king_row = None
    king_column = None

    for index, row in enumerate(rows): #ลูบจนกว่าจะเจอ King แล้วบอกตำแหน่ง
        for column, cell in enumerate(row):
            if cell == "K":
                king_row = index
                king_column = column
                print(f"Found K at row {index}, column {column}")

    #จะตรวจเดินขึ้นก่อน
    check_row = king_row - 1 
    check_column = king_column

    while check_row >= 0 and check_row < len(rows): #ถ้าแถวที่ตรวจยังอยู่ในกระดานก็ตรวจต่อ
        cell = rows[check_row][check_column] #ไปหยิบ ตัวหมาก จาก [check_row][check_column] เก้บไว้ใน cell

        if cell == "R" or cell == "Q":
            print("Success")
            return
        elif cell != ".":   #ถ้าเจออะไรก็ตามที่ไม่ใช่ช่องว่าง หยุดตรวจ
            break

        check_row = check_row - 1 #ตรวจเสร็จแล้วขยับอีกช่อง บน

    #ตรวจล่างต่อ
    check_row = king_row + 1
    check_column = king_column

    while check_row >= 0 and check_row < len(rows):
        cell = rows[check_row][check_column]

        if cell == "R" or cell == "Q":
            print("Success")
            return
        elif cell != ".":   #ถ้าเจออะไรก็ตามที่ไม่ใช่ช่องว่าง หยุดตรวจ
            break

        check_row = check_row + 1 #เช็คแถวด่านล่าง เดินลงนั้นแหละ

    #ตรวจด้านซ้ายต่อ
    check_row = king_row
    check_column = king_column - 1

    while check_column >= 0 and check_column < len(rows):
        cell = rows[check_row][check_column]

        if cell == "R" or cell == "Q":
            print("Success")
            return

        elif cell != ".":   #ถ้าเจออะไรก็ตามที่ไม่ใช่ช่องว่าง หยุดตรวจ
            break

        check_column = check_column - 1

    # ตรวจด้านขวาต่อ
    check_row = king_row
    check_column = king_column + 1

    while check_column >= 0 and check_column < len(rows):
        cell = rows[check_row][check_column]

        if cell == "R" or cell == "Q":
            print("Success")
            return

        elif cell != ".": #ถ้าเจออะไรก็ตามที่ไม่ใช่ช่องว่าง หยุดตรวจ
            break

        check_column = check_column + 1