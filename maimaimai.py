class Buy(object):

    def __init__(self, budget, goods_price_list):
        '''
        设置预算, 和物品的价格
        '''
        self.budget = budget
        self.goods_price_list = goods_price_list

    def process_goods(self):
        self.goods_price_list.pop()

    def analize(self):
        '''
        处理分析
        '''
        cost = sum(self.goods_price_list)

        if cost <= self.budget:
            print(cost)

        else:
            cost = self.process_goods()
            self.analize()


def main():
    budget = int(input('请输入预算: '))
    goods_price = input('请输入要买物品的价格,用空格分开: ')
    goods_price_list = sorted([int(i) for i in goods_price.split()])
    goods = Buy(budget, goods_price_list)
    goods.analize()

if __name__ == '__main__':
    main()