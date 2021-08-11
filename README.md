如果你不知道该怎么用的话，就把gerber文件放到`dist/gerbers`里面，然后运行`dist/gerber2png.exe`就可以了，运行结束后在`dist/output`里面会生成对应的PNG文件

gerber文件测试了，eagle自带的CAM和嘉立创的CAM

# 2021年8月11日 UPDATE:
  我发现我的另外一个电脑上那个exe文件会报毒。如果不放心的话可以自己用python跑也行。
  
---

If you don't know how to use it, just copy gerber files into `dist/gerbers`,then run `dist/gerber2png.exe`. You will find PNG files in `dis/output`
# 2021.08.11 UPDATE:
  It seemed that windows defender will identified the exe file as virus, you can run the `gerber2png.py` to gererate the png files.
