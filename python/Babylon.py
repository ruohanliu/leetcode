class Solution:
    def babylon(self) -> bool:
        @cache
        def game(state):
            """
                #google #game

                represent game state using 12*4 = 48bit

                2^(nlogn)*(color + n)
            """
            # total 12 stacks
            for i in range(0,12):
                a = (state>>i*4)&15
                if a:
                    # option 1,merge stacks with same top color
                    for j in range(i+1,3*(i//3+1)):
                        b = (state>>j*4)&15
                        if b and not game(state-(a<<i*4)+(a<<j*4)):
                            return True
                                    
                    # option 2,merge stacks with same height
                    # consider stacks after i
                    for j in range(3*(i//3+1),12):
                        b = (state>>j*4)&15
                        if a == b and (not game(state-(a<<i*4)+(a<<j*4)) or not game(state-(b<<j*4)+(b<<i*4))):
                            return True
            return False

        state=sum(1<<(4*i) for i in range(12))
        return [2,1][game(state)]