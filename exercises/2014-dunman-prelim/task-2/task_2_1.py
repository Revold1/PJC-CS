Pastry = [["", 0, 0] for _ in range(11)]

Pastry[1][0] = "Cranberry"
Pastry[1][1] = 1.10
Pastry[1][2] = 1
Pastry[2][0] = "Blueberry"
Pastry[2][1] = 1.10
Pastry[2][2] = 6
Pastry[3][0] = "Sweet Potato"
Pastry[3][1] = 1.20
Pastry[3][2] = 4
Pastry[4][0] = "Pumpkin Toast"
Pastry[4][1] = 1.30
Pastry[4][2] = 8
Pastry[5][0] = "Coconut Kaya"
Pastry[5][1] = 1.60
Pastry[5][2] = 0
Pastry[6][0] = "Red Bean"
Pastry[6][1] = 0.80
Pastry[6][2] = 1
Pastry[7][0] = "Peanut Butter"
Pastry[7][1] = 0.90
Pastry[7][2] = 7
Pastry[8][0] = "Pineapple Longan"
Pastry[8][1] = 1.40
Pastry[8][2] = 0
Pastry[9][0] = "Apple Strudel"
Pastry[9][1] = 1.50
Pastry[9][2] = 6
Pastry[10][0] = "Spicy Floss"
Pastry[10][1] = 1.90
Pastry[10][2] = 5


def check_availability():
    name = input("Enter pastry name: ").title()

    for item in Pastry:
        if item[0] == name:
            if item[2] == 0:
                print("Sold out!")
            else:
                print("Available.")
            return

    print("Pastry does not exist.")


# check_availability()
