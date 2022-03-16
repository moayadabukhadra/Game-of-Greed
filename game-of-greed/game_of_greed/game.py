from game_of_greed.game_banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:
    def __init__(self, roller=None):
        self.roller = roller
        self.banker = Banker()
        self.banker.bank

    def play(self):
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            banked = self.banker
            round = 1

            while round:
                score = 0
                shelved = banked.shelf(score)
                # print(shelved)
                # shelf = 0
                print(f"Starting round {round}")
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(",".join(nums))
                count = 0
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                result = banked.bank()[1]
                if decision == "q":

                    break
                else:
                    count = 1
                    new_list = []
                    selected_dice = tuple(decision)
                    for elem in selected_dice:
                        new_list.append(int(elem))
                    # print(new_list)
                    new_tuple = tuple(new_list)
                    # print(new_tuple)
                    score = GameLogic.calculate_score(new_tuple)
                    shelved = banked.shelf(score)
                    # print(score)

                    rem_dice = 6 - len(selected_dice)
                    print(
                        f"You have {shelved} unbanked points and {rem_dice} dice remaining"
                    )

                    choice = input("(r)oll again, (b)ank your points or (q)uit ")
                    # choice = input("(r)oll again, (b)ank your points or (q)uit: ")
                    if choice == "q" and count == 1:
                        print("hi")
                        print(f"Total score is {result} points")
                        print(f"Thanks for playing. You earned {result} points")
                        break
                    round += 1

                    print(f"You banked {shelved} points in round {(round-1)}")
                    print(f"Total score is {shelved} points")

            print(f"Thanks for playing. You earned {result} points")


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
