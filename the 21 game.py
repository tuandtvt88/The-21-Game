#The 21 Game - Compucademy

import random


while True: #Dùng while để khởi tạo vòng lặp, điều kiện kiểm tra sẽ là True =>
            # trò chơi sẽ luôn được tiếp tục lại cho đến khi người dùng nhập giá trị để kết thúc.
    
    print(r"""
      _______ _            ___  __    _____                      
     |__   __| |          |__ \/_ |  / ____|                     
        | |  | |__   ___     ) || | | |  __  __ _ _ __ ___   ___ 
        | |  | '_ \ / _ \   / / | | | | |_ |/ _` | '_ ` _ \ / _ \
        | |  | | | |  __/  / /_ | | | |__| | (_| | | | | | |  __/
        |_|  |_| |_|\___| |____||_|  \_____|\__,_|_| |_| |_|\___|

    """)
    
    current_number = 1 # Khai báo biến tổng số đếm với giá trị khởi tạo = 0 (tạm gọi là current_number)

    if random.randint(0, 1) == 0: # Dùng randint(0, 1) lấy ra một con số ngẫu nhiên để quyết định ai sẽ 
                                #là người chơi hiện tại. (tạm gọi biến là current_player)
        current_player = "human"
    else:
        current_player = "computer"

    while current_number <= 21: #Dùng while để tạo vòng lặp đếm số, điều kiện kiểm tra sẽ là current_number <= 21
      
        print("The current number is " + str(current_number) + ".")
        print

        if current_player == "human":

            print("Add 1, 2, or 3. Do not pass 21. The player who lands on 21 loses.")

            player_choice = ""
            while player_choice not in ["1", "2", "3"]:
                player_choice = input("What will you add? ")

            player_choice = int(player_choice)
            current_number = current_number + player_choice
            print

            if current_number >= 21:
                print("The current number is " + str(current_number) + ".")
                print()
                print("Sorry, you lose.")
                break
            current_player = "computer"

        else:

            computer_choice = random.randint(1, 3)
            current_number = current_number + computer_choice
            print("Computer turn. The computer choses " + str(computer_choice) + ".")
            print

            if current_number >= 21:
                print("The current number is " + str(current_number) + ".")
                print()
                print("Well done, you won!")
                break
            current_player = "human"

    print
    play_again = input("Do you want to play again? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Goodbye")
        break
