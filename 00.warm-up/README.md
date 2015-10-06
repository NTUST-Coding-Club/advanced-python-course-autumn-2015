# Warm Up

## 環境設定

輸入以下指令到 Terminal 來安裝 IPython Notebook 環境

``` bash
sudo apt-get install python3 python3-dev python3-pip ipython3-notebook -y
sudo -H pip3 install -U 'ipython[notebook]'
```

輸入以下指令讓你打 `python` 的時候預設執行 `python3`

``` bash
echo 'alias python=python3' >> ~/.bashrc
echo 'alias ipython=ipython3' >> ~/.bashrc
echo 'alias pip=pip3' >> ~/.bashrc
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

# Shell

- `ls` -- 列出這個資料夾的內容
- `cd` -- 切換到別的資料夾
- `cd ..` -- 切換到上一層資料夾
- `python3 file.py` -- 執行某個檔案 
