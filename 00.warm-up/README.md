# Warm Up

## 環境設定

輸入以下指令到 Terminal 來安裝 IPython Notebook 環境

``` bash
sudo apt-get install ipython3-notebook -y
```

把下面的檔案存成 `run.py`

``` python
import os

ip = os.getenv("IP", "0.0.0.0")
port = os.getenv("PORT", "0.0.0.0")

print("Bind on %s:%s" % (ip, port))
os.system("ipython3 notebook --ip %s --port %s" % (ip, port))
```

## 其他資源

- [Sublime Text](http://www.sublimetext.com/)
- [IPython](https://ipython.org/)
- [IDLE](http://ez2learn.com/install/idle.html)
