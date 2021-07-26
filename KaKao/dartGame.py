 
def Solution(dartResult):
    nums = []
    for j, s in enumerate(dartResult):
        if s == 'S':
            nums[-1] **= 1
        elif s == 'D':
            nums[-1] **= 2
        elif s == 'T':
            nums[-1] **= 3
        elif s == '*':
            nums[-1] *= 2
            if len(nums) > 1:
                nums[-2] *= 2
        elif s == '#':
            nums[-1] *= -1
        else:
            if dartResult[j-1].isdigit():
                nums[-1] = nums[-1] * 10 + int(s)
            else :
                nums.append(int(s))
    return sum(nums)
    # 파이썬 알고리즘 인터뷰 풀이. solution of a textbook
    # nums = [0]
    # for s in dartResult:
    #     if s == 'S':
    #         nums[-1] **= 1
    #         nums.append(0)
    #     elif s == 'D':
    #         nums[-1] **= 2
    #         nums.append(0)
    #     elif s == 'T':
    #         nums[-1] **= 3
    #         nums.append(0)
    #     elif s == '*':
    #         nums[-2] *= 2
    #         if len(nums) > 2:
    #             nums[-3] *= 2
    #     elif s == '#':
    #         nums[-2] *= -1
    #     else:
    #         # 자릿수 올리기 위해서 미리 0선언
    #         # Define 0 first to handle double digits
    #         nums[-1] = nums[-1] * 10 + int(s)
    # return sum(nums)

scores1 = '1S2D*3T'
scores2 = '1T2D3D#'
print(Solution(scores1))
print(Solution(scores2))