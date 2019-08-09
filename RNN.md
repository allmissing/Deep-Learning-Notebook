# RNN

## 矩阵求导术
向量对矩阵求导https://zhuanlan.zhihu.com/p/24709748
矩阵对矩阵求导https://zhuanlan.zhihu.com/p/24863977

## BPTT推导
https://zhuanlan.zhihu.com/p/26892413

## Tensorflow与LSTM

1. dynamic_rnn: https://blog.csdn.net/u013230189/article/details/82814235  

2. BasicLSTMCell： https://blog.csdn.net/u013230189/article/details/82808362

3. bias_add与普通add的区别: https://www.jianshu.com/p/018c0d5c26ff  

4. dropout: https://www.jianshu.com/p/c752d405a4d7  

5. tf.concat: https://blog.csdn.net/neil3611244/article/details/81487596  


## Seq2Seq

### 1.Seq2Seq的基本思想
使用一个循环神经网络读取输入句子，将整个句子的信息压缩到一个固定维度的编码中；再使用另一个循环神经网络读取这个编码，将其“解压”为目标语言的一个句子。

