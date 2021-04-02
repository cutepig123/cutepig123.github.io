---
categories: tools
---
backtrader的indices實現分析：表達式模板

# 如何理解如下策略中的self.sma1，self.crossover之類的變量？他們是如何求值的？

```python


class SmaCross(bt.SignalStrategy):
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.sma1, self.sma2 = bt.ind.SMA(period=Shortperiod), bt.ind.SMA(period=Longperiod)

        # TODO: 這些變量其實不是真正的數字，那麽他們的比較，加減是怎麽做的呢？
        self.crossover = bt.ind.CrossOver(self.sma1, self.sma2)
        #self.signal_add(bt.SIGNAL_LONG, self.crossover)

    def next(self):
        sma1_slope = self.sma1[0] - self.sma1[-1]
        if not self.position:
            if self.crossover > 0 and sma1_slope>sma1_slope_threshold:
                self.buy()

        elif self.crossover < 0:
            self.close()
```

# 分析

`self.sma1, self.sma2 = bt.ind.SMA(period=Shortperiod), bt.ind.SMA(period=Longperiod)`

`self.sma1`為一個class變量，（可以理解為表達式模板）而不是具體數字

`sma1_slope = self.sma1[0] - self.sma1[-1]`

`self.sma1[0]`調用`[]`函數，計算數字.debug發現，他會調用LineSeries的

```python
	def __getitem__(self, key):
        return self.lines[0][key]
```

而`self.lines`類型為`<backtrader.lineseries.Lines_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageBase_MovingAverageSimple_SMA object at 0x061BB8B0>	`

所以繼續debug會看到嗲用Lines的

`    def __getitem__(self, line):
        '''
        Proxy line operation
        '''
        return self.lines[line]`

再繼續LineBuffer的
`    def __getitem__(self, ago):
        return self.array[self.idx + ago]	`

這個用C++的表達式模板就是如下寫法

```cpp
template <class InputDataExpression>
class SMAExpression{
	InputDataExpression input_data_exp_;
	
	SMAExpression(InputDataExpression input_data_exp):input_data_exp_(input_data_exp)
	{}
	
	double get(int index) const {
		me = mean(input_data_exp_.get(index-5), input_data_exp_.get(index-4), ...input_data_exp_.get(index-1))
		return me
	}
}

template <class InputDataExpression1, class InputDataExpression2>
class SubExpression{
	InputDataExpression1 input_data_exp1_;
	InputDataExpression2 input_data_exp2_;
	
	SubExpression(InputDataExpression1 input_data_exp1, InputDataExpression2 input_data_exp2)
	:input_data_exp1_(input_data_exp1), input_data_exp2_(input_data_exp2)
	{}
	
	double get(int index) const {
		me = input_data_exp1_(index) - input_data_exp2_(index)
		return me
	}
}

```

總結：大概原理我猜到了，但是還是沒找到移動平均這個函數的代碼實現在哪裏

