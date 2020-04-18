from Suits import Suits
from Runners import Runner

def start():
    ts = Suits.TestSuits()

    #to change test suits just select ts.*****
    tests = ts.all_tests()
    Runner.Runner(tests)


if __name__ == '__main__':
    start()
