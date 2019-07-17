# Tensorflow编程流程

### 利用tensorboard监测神经网络中的某些变量
1. 在定义网络结构变量时添加summary变量，写法：tf.summary.scaler(起个名字,变量)  
2. 在session对话前用merged = tf.summary.merge_all()将所有监测变量整理到一起
3. 定义一个writer，用于写summary日志: summary_writer = tf.summary.FileWriter(日志存放目录,sess.graph)
4. session运行时返回summary变量,并写入日志：

    summary,_ = sess.run([merged,train_step],feed_dict={x:xs,y_:ys})
    summary_writer.add_summary(summary,训练step)
    
5. session运行结束后summary_writer.close()


