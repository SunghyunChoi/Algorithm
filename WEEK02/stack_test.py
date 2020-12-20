from stack_make import FixedStack

stk = FixedStack(10)

##데이터를 넣는다.

for i in range(10):
    stk.push(i)

print(stk.is_full())

stk.dump()

print(stk.peek())

print(f"{stk.pop()}을 pop했습니다.")

stk.dump()