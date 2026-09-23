def checkmate(board):
    rows = board.split("\n")  # เอากระดาน แบ่งเป็นแถว

    # เช็คว่ากระดานเป็นสี่เหลี่ยมไหม
    size = len(rows)

    for row in rows:
        if len(row) != size:
            print("Error")
            return

    # ตัวแปรเอาไว้เก็บตำแหน่ง King
    king_row = None
    king_column = None
    king_count = 0

    # ลูบทุกช่องจนกว่าจะเจอ King แล้วบอกตำแหน่ง
    for index, row in enumerate(rows):
        for column, cell in enumerate(row):
            if cell == "K":
                king_row = index
                king_column = column
                king_count += 1

    # ต้องมี King แค่ตัวเดียว
    if king_count != 1:
        print("Error")
        return

    # =========================
    # ตรวจ Rook / Queen ด้านบน
    # =========================

    check_row = king_row - 1  # จะตรวจเดินขึ้นก่อน
    check_column = king_column  # column ไม่เปลี่ยน เพราะเดินตรงขึ้น

    while check_row >= 0 and check_row < len(rows):
        cell = rows[check_row][check_column]  # ไปหยิบตัวหมากจากตำแหน่งที่กำลังตรวจ

        if cell == "R" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_row = check_row - 1  # ตรวจเสร็จแล้วขยับขึ้นอีกช่อง

    # =========================
    # ตรวจ Rook / Queen ด้านล่าง
    # =========================

    check_row = king_row + 1  # เริ่มตรวจด้านล่าง
    check_column = king_column  # column ไม่เปลี่ยน

    while check_row >= 0 and check_row < len(rows):
        cell = rows[check_row][check_column]

        if cell == "R" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_row = check_row + 1  # ขยับลงอีกช่อง

    # =========================
    # ตรวจ Rook / Queen ด้านซ้าย
    # =========================

    check_row = king_row  # row ไม่เปลี่ยน เพราะเดินตรงซ้าย
    check_column = king_column - 1  # เริ่มจากช่องซ้ายของ King

    while check_column >= 0 and check_column < len(rows):
        cell = rows[check_row][check_column]

        if cell == "R" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_column = check_column - 1  # ขยับไปทางซ้ายอีกช่อง

    # =========================
    # ตรวจ Rook / Queen ด้านขวา
    # =========================

    check_row = king_row  # row ไม่เปลี่ยน
    check_column = king_column + 1  # เริ่มจากช่องขวาของ King

    while check_column >= 0 and check_column < len(rows):
        cell = rows[check_row][check_column]

        if cell == "R" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_column = check_column + 1  # ขยับไปทางขวาอีกช่อง

    # =========================
    # ตรวจ Bishop / Queen เฉียงขึ้นซ้าย
    # =========================

    check_row = king_row - 1  # ขยับขึ้น
    check_column = king_column - 1  # ขยับซ้าย

    while check_row >= 0 and check_column >= 0:
        cell = rows[check_row][check_column]

        if cell == "B" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_row = check_row - 1
        check_column = check_column - 1

    # =========================
    # ตรวจ Bishop / Queen เฉียงขึ้นขวา
    # =========================

    check_row = king_row - 1  # ขยับขึ้น
    check_column = king_column + 1  # ขยับขวา

    while check_row >= 0 and check_column < len(rows):
        cell = rows[check_row][check_column]

        if cell == "B" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_row = check_row - 1
        check_column = check_column + 1

    # =========================
    # ตรวจ Bishop / Queen เฉียงลงซ้าย
    # =========================

    check_row = king_row + 1  # ขยับลง
    check_column = king_column - 1  # ขยับซ้าย

    while check_row < len(rows) and check_column >= 0:
        cell = rows[check_row][check_column]

        if cell == "B" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_row = check_row + 1
        check_column = check_column - 1

    # =========================
    # ตรวจ Bishop / Queen เฉียงลงขวา
    # =========================

    check_row = king_row + 1  # ขยับลง
    check_column = king_column + 1  # ขยับขวา

    while check_row < len(rows) and check_column < len(rows):
        cell = rows[check_row][check_column]

        if cell == "B" or cell == "Q":
            print("Success")
            return

        elif cell != ".":
            break  # เจอตัวอื่นบัง ก็หยุดทางนี้

        check_row = check_row + 1
        check_column = check_column + 1

    # =========================
    # ตรวจ Pawn
    # =========================

    # Pawn ในรูปโจทย์จะโจมตีเฉียงขึ้น 2 ช่อง
    pawn_row = king_row + 1

    if pawn_row < len(rows):

        # เช็ค Pawn ทางซ้ายบน
        if king_column - 1 >= 0:
            cell = rows[pawn_row][king_column - 1]

            if cell == "P":
                print("Success")
                return

        # เช็ค Pawn ทางขวาบน
        if king_column + 1 < len(rows):
            cell = rows[pawn_row][king_column + 1]

            if cell == "P":
                print("Success")
                return

    # ถ้าตรวจทุกทางแล้วไม่เจอหมากที่โจมตี King
    print("Fail")