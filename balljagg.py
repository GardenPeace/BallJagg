from random import randint
from time import sleep

JAGGLING_SPEED = 0.03


class BallJagg:
    def __init__(self):
        self.ball_position = [0, 0, 0]

    def __ball_replace(self):
        self.ball_position = [0, 0, 0]
        self.ball_position[randint(0, len(self.ball_position) - 1)] = 1

    def __jaggling(self):
        for _ in range(100):
            self.__ball_replace()
            print(self.ball_position)

        for _ in range(20):
            sleep(JAGGLING_SPEED)
            print('')

    def __ball_position_expect(self):
        position_expect = int(input('1だった場所は位置は左:0, 真ん中:1, 右:2のどれですか？数字で解答してください'))
        if self.ball_position[position_expect] == 1:
            print('正解です')
        else:
            print('×です。')

    def game_start(self):
        self.__jaggling()
        self.__ball_position_expect()


def main():
    BallJagg().game_start()


if __name__ == '__main__':
    main()
