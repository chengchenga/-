class test(object):
    def __init__(self, data_time, list):
        self.data_time = data_time
        self.list = list
        self.code_list = ['ABCDEFGHI', 'JKLMNOPQR', 'STUVWXYZ*']

    def month(self):
        month = self.data_time[0] - 1
        move = month % len(self.code_list)
        if move != 0:
            for i in range(move):
                add = self.code_list.pop(0)
                self.code_list.append(add)

    def day(self):
        day = self.data_time[1] - 1
        move = day % 9
        if move != 0:
            for i in range(len(self.code_list)):
                self.code_list[i] = self.code_list[i][move:] + self.code_list[i][0:move]
        print(self.code_list)

    def jiami(self):
        jm_code_list = []
        print(self.list)
        for j in self.list:
            if j in self.list:
                for i in self.code_list:
                    a = str(self.code_list.index(i) + 1)
                    try:
                        c = str(i.index(j) + 1)
                    except Exception:
                        pass
                    else:
                        jm_code_list.append(a + c)

        print(' '.join(jm_code_list))

def main():
    data_time = [int(i) for i in input('输入日期，用空格分开： ').split()]
    print(data_time)
    con = input('输入要加密的，注意大写,空格用*代替： ')
    list = [i for i in con]
    te = test(data_time, list)
    te.month()
    te.day()
    te.jiami()

if __name__ == '__main__':
    main()



