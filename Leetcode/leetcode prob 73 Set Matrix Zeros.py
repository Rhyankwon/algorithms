class Solution:
    def setZeroes(self, matrix):
        # 1번 방식. 0인 매트릭스 인덱스 모두 저장 후 해당 열/행 하나라도 해당되면 전부 0으로 만들기
        # First solution. Save every index that contains 0 and make components of each row and column zero
        # zeros = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
                    # zeros.append([i, j])
        # for i in zeros:
        #     a, b = i
        #     for j in range(len(matrix[a])):
        #         matrix[a][j] = 0
        #     for j in range(len(matrix)):
        #         matrix[j][b] = 0
        # return matrix
        # 2번 방식. 1번과 똑같지만 크기가 커지면 중복되는 열/행 많아짐. 중복되는것들 삭제!
        # second solution. Delete repeated indices from first solution. it will be effective when more zeroes.
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # zeros.append([i, j])
                    rows.append[i]
                    cols.append[j]
        rows = list(set(rows))
        cols = list(set(cols))
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        for i in cols:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        return matrix
