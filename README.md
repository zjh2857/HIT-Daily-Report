# HIT-Daily-Report
## 1.本地安装
```
git clone https://github.com/zjh2857/HIT-Daily-Report.git
cd HIT-Daily-Report
pip install selenium
pip install webdriver_manager
sudo dpkg -i google-chrome-stable_current_amd64.deb
export USER=yourusername
export PASSWORD=yourpassword
export LOCATION='yourlocation'
python main.py
```
location可以在https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/edit 处获取，获取方式为上报前按下F12，上报后查看save项，info的值即为location，如为url编码则需要解码。
为了实现定时上报，可以输入`crontab -e`输入如下指令实现每日自动上报
```
0 8 * * * python main.py
```

## 2.Github Actions

您也可以直接fork本项目，点击Setting，点击secret添加secret `USER` `PASSWORD` `LOCATION`,在Action栏中，可以看到每日上报的情况。
