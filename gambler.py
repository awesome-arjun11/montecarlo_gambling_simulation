__author__ = "Arjun Singh"
__email__ = "awesome.arjun11@gmail.com"


import random
import matplotlib.pyplot as plt
import argparse


class Gamble:

    def __init__(self,funds,initial_wager,wager_count, win_percent):
        self.funds = funds
        self.initial_wager = initial_wager
        self.wager_count = wager_count
        self.win_percent = win_percent

    def randomEventResult(self):
        """
        Returns win or lose according to winning chance
        :param win_percent: chance of winning (simulated)
        :return: True or False
        """
        ran_num = random.randint(1, 100)
        if ran_num <= self.win_percent:
            return True
        else:
            return False

    def linear_betting(self):
        worth = self.funds
        wager = self.initial_wager
        wX = []

        wY = []
        currentWager = 1

        while currentWager <= self.wager_count:
            if self.randomEventResult():
                worth += wager
                wY.append(worth)
            else:
                worth -= wager
                wY.append(worth)

            wX.append(currentWager)
            currentWager += 1

        plt.plot(wX, wY)

    def martingale_betting(self):
        worth = self.funds
        wager = self.initial_wager
        wX = []
        wY = []
        currentWager = 1

        # since we'll be betting based on previous bet outcome
        previousWager = 'win'

        # since we'll be doubling
        previousWagerAmount = self.initial_wager

        while currentWager <= self.wager_count:
            if previousWager == 'win':
                if self.randomEventResult():
                    worth += wager
                    wX.append(currentWager)
                    wY.append(worth)
                else:
                    worth -= wager
                    previousWager = 'loss'
                    previousWagerAmount = wager
                    wX.append(currentWager)
                    wY.append(worth)
                    if worth < 0:
                        break
            elif previousWager == 'loss':
                if self.randomEventResult():
                    wager = previousWagerAmount * 2
                    worth += wager
                    wager = self.initial_wager
                    previousWager = 'win'
                    wX.append(currentWager)
                    wY.append(worth)
                else:
                    wager = previousWagerAmount * 2
                    worth -= wager
                    if worth < 0:
                        break

                    previousWager = 'loss'
                    previousWagerAmount = wager
                    wX.append(currentWager)
                    wY.append(worth)


            currentWager += 1

        plt.plot(wX, wY)

    def run(self,num_sim,mart = False):
        if mart:
            for _ in range(num_sim):
                self.martingale_betting()
        else:
             for _ in range(num_sim):
                self.linear_betting()
            
        plt.show()  
        


def main():
    parser = argparse.ArgumentParser("Arguments to run a Monte Carlo Simulation")
    parser.add_argument('funds', help='Total Initial Funds', type=int)
    parser.add_argument('init_wager', help='Initial bet amount', type=int)
    parser.add_argument('wager_count', help='Total number of bets', type=int)
    parser.add_argument('-p','--win_chance', help='Chance of winning(in %)', default=50,type=int)
    parser.add_argument('-ns','--num_sim', help='Path to the file or directory',type=int,default=1)
    parser.add_argument('-mart','--mstrategy',help='Martingale Gambling strategy',action='store_true')
    args = parser.parse_args()

    gamble = Gamble(args.funds,args.init_wager,args.wager_count,args.win_chance)
    gamble.run(args.num_sim,args.mstrategy)

    


if __name__ == '__main__':
    main()