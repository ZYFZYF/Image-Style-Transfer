# Image-Style-Transfer
    《数字媒体(2)：多媒体》课程中视频小课堂大作业-图像风格迁移任务
    
## TODO
 - 论文复现
     - [Gatys](https://arxiv.org/abs/1508.06576)方法复现 完成
        - 基本效果 √
        - 修改loss（增加光滑项）√
        - 用Chen中的style swap操作来计算loss ×（没有意义  不做了）
     - [Johnson](https://arxiv.org/abs/1603.08155)方法复现 完成
        - 训了6个小时还是和白训了一样？怎么办？
        - 破案了，算loss的时候千万不能.item()，这样就从tensor变成scalar了，更不要谈backward()了，浪费我这么久。。。。。。
        - 每个style需要的参数是不一样的，需要每张分别作
     - [Shen](https://arxiv.org/abs/1709.04111)方法复现 ×
        - 目前打算放弃这个，直接开发实施转换的应用了
     - [Chen](https://arxiv.org/abs/1612.04337)方法复现 完成
        - 训练过程中出现的奇妙现象：generate出来的图片底色随着训练轮数的变化大幅度改变？（好像是学习率设大了？）
        - 为什么训练到后面transfer以及画loss的速度越来越慢？甚至到了两分钟以上
        - 颜色还可以，但效果比较模糊，每张256x256要0.8s，正常大小的（500左右的）也是2s左右
 - 工作集成
     - 同步进行中
 - 实时风格转换demo 完成
     - 从文件选择图片并显示 完成
        - 用了QImage和PIL的Image，前者拿不到用后者加载并强转，目前没有发现反例
        - [PIL Image to QPixmap conversion issue](https://stackoverflow.com/questions/34697559/pil-image-to-qpixmap-conversion-issue)
     - 显示摄像头内容 完成
     - 图片风格转换 
        - 算法层面 完成
        - 显示进度 不打算做
     - 视频风格转换 部分完成
        - 支持从摄像头实时转换
        - 速度慢，每秒2帧
            - mac上每秒1.5帧
            - win上每秒3帧
        - UI更新速度更不上显示速度 完成
            - 新开线程
            - win上1280x720视频每帧0.27秒 mac上0.58秒
            - win上640x480摄像头每帧0.11秒
            - win上1920x1080视频每帧0.35秒
     - 还有一个从图像风格转换界面点返回就会挂掉的奇怪bug 修复
     - mac上经常选择文件选不了（感觉是系统bug，不打算解决）解决
        - 原来是因为焦点丢了
## Dataset

 - Content 
    MSCOCO 2017 Val images [5K/1GB] and Test images [41K/6GB] 共45670张
 - Style
    Kaggle https:// www.kaggle.com/c/painter-by-numbers test9 共8491张

## References

 - https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/03-advanced/neural_style_transfer/main.py#L84-L94
 - https://github.com/irasin/Pytorch_Style_Swap