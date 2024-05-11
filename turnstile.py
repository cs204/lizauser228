import sm
class Turnstile(sm.SM):
    startState = 'locked'
    def getNextValues(self, state, inp):
        if state == 'locked':
            if inp == 'coin':
                return('unlocked','enter')
            else:
                return('locked','pay')
        else:
            if inp == 'turn':
                return('locked','pay')
            else:
                return('unlocked','enter')

if __name__ == "__main__":
    t = Turnstile()
    print(t.transduce(['turn', 'coin', 'turn', 'coin']))