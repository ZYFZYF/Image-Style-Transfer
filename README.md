# Image-Style-Transfer
    《数字媒体(2)：多媒体》课程中视频小课堂大作业-图像风格迁移任务
    
## TODO
 - 论文复现
     - [Gatys](https://arxiv.org/abs/1508.06576)方法复现 部分完成
        - 基本效果 √
        - 修改loss（增加光滑项）√
        - 用Chen中的style swap操作来计算loss ×
     - [Johnson](https://arxiv.org/abs/1603.08155)方法复现 ×
        - 训了6个小时还是和白训了一样？怎么办？
        - 破案了，算loss的时候千万不能.item()，这样就从tensor变成scalar了，更不要谈backward()了，浪费我这么久。。。。。。
        - 每个style需要的参数是不一样的，需要每张分别作
     - [Shen](https://arxiv.org/abs/1709.04111)方法复现 ×
        - 目前打算放弃这个，直接开发实施转换的应用了
     - [Chen](https://arxiv.org/abs/1612.04337)方法复现 部分完成
        - 训练过程中出现的奇妙现象：generate出来的图片底色随着训练轮数的变化大幅度改变？（好像是学习率设大了？）
        - 为什么训练到后面transfer以及画loss的速度越来越慢？甚至到了两分钟以上
        - 颜色还可以，但效果比较模糊，每张256x256要0.8s，正常大小的（500左右的）也是2s左右
 - 工作集成
     - 同步进行中
 - 实时风格转换demo ×

## Dataset

 - Content 
    MSCOCO 2017 Val images [5K/1GB] and Test images [41K/6GB] 共45670张
 - Style
    Kaggle https:// www.kaggle.com/c/painter-by-numbers test9 共8491张

## References

 - https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/03-advanced/neural_style_transfer/main.py#L84-L94
 - https://github.com/irasin/Pytorch_Style_Swap