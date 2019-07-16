# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:38:10 2019

@author: 705family
"""
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
#from sklearn.model_selection import train_test_split,StratifiedKFold
# import matplotlib as plt

def DataCombine():
    path = 'F:/课题/数据处理/开始时间数据配对/'
    data = pd.read_excel(path + '1月.xlsx')
    for i in range(2,7):
        name = path + str(i) + '月.xlsx'
        data2 = pd.read_excel(name)
        data = pd.concat([data,data2],axis=0)
    data = data.dropna()
    data = data.drop(['时间','生产日期','焦炭负荷','总焦','总球','总块'],axis=1)
    return data

class LRModel(object):
    def __init__(self,feature_num,output_num,num_examples,
                 learning_rate=0.01,training_epochs=25,
                 batch_size=100,display_step=1):
        #训练参数
        self.learning_rate = learning_rate
        self.training_epochs = training_epochs
        self.batch_size = batch_size
        self.display_step = display_step
        self.num_examples = num_examples
        self.total_batch = int(num_examples/batch_size)
        #网络结构参数
        self.feature_num = feature_num
        self.output_num = output_num
        
    def build_model(self):
        # 从输入到输出的网络结构,定义到计算损失的层
        X = tf.placeholder(tf.float32,[None,self.feature_num])
        Y = tf.placeholder(tf.float32,[None,self.output_num])
        W = tf.Variable(tf.zeros([self.feature_num,self.output_num]))
        b = tf.Variable(tf.zeros([self.output_num]))
        pred = tf.nn.softmax(tf.matmul(X,W)+b)
        loss = tf.reduce_mean(tf.square(pred-Y))
        # 优化器
        optimizer = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(loss)
        # 初始化
        init = tf.global_variables_initializer()
        return X,Y,pred,loss,optimizer,init
        
    def train(self,x,y,xt,yt):
        X,Y,pred,loss,optimizer,init = self.build_model()
        with tf.Session() as sess:
            sess.run(init)
            for epoch in range(self.training_epochs):
                avg_loss = 0.
#                skf = StratifiedKFold(n_splits=self.total_batch, random_state=42, shuffle=True)
#                for k, (batch_x, batch_y) in enumerate(skf.split(x, y)):
                for k in range(self.total_batch):
                    batch_x = x[k*self.batch_size:(k+1)*self.batch_size-1,:]
                    batch_y = y[k*self.batch_size:(k+1)*self.batch_size-1,:]
                    _,l = sess.run([optimizer,loss],feed_dict={X:batch_x,Y:batch_y})
                    avg_loss += l/self.total_batch
                
                if (epoch+1)%self.display_step == 0:
                    print("Epoch:{},loss={}".format(epoch+1,avg_loss))
            
            print("optimization finished")
            print("Accuracy:",loss.eval({X:xt,Y:yt}))
                

if __name__ == "__main__":
    data = DataCombine()
    ys = ['Mn','P','S','Si','Ti','铁水温度','铁水重量']
    x = data[[x for x in data.columns if x not in ys]]
    y = data[['Si','铁水温度']]
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x.values)
    y = scaler.fit_transform(y.values)
    X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=2019)
    
    lr = LRModel(np.size(X_train,1),np.size(y_train,1),len(X_train))
    lr.train(X_train,y_train,X_test,y_test)
    