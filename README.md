# FFT 计算脚本

## 开发背景
Maxwell 导出的csv格式数据文件，直接计算出`FFT分解`的模和角度。

## 环境配置
 - 安装 Python2，配置 Python 环境
 - 安装依赖，在代码目录下（cmd / terminal）执行 `pip install -r requirements.txt`

## 文件安排
``` shell
➜  fft-calc tree -L 1
.
├── README.md # 本说明文件
├── abs.png # 输出结果模的点图
├── data.csv # csv数据源文件
├── deg.png # 输出结果角度的点图
├── main.py # 代码文件
└── requeriments.txt # 依赖信息
```

## 使用教程
**注： 案例中使用了`venv`，所以命令为`./venv/bin/python`，如果不选择使用`venv`，可以直接使用`python`。**
### 帮助信息
``` shell
➜  fft-calc ./venv/bin/python main.py -h
usage: main.py [-h] [-i INDEX] [-f FILE]

Process FFT calculation from csv file.

optional arguments:
  -h, --help  show this help message and exit
  -i INDEX    FFT result index
  -f FILE     csv file position
```

### 输入输出
csv文件格式：
第一行为值的标题，第二行开始为对应的值。
第一列为时间，第二列开始为每一组数据。  
例如：
```
"Time [ms]","InducedVoltage(A) [V] - Cmax='0mm'","InducedVoltage(A) [V] - Cmax='0.05mm'","InducedVoltage(A) [V] - Cmax='0.1mm'","InducedVoltage(A) [V] - Cmax='0.15mm'","InducedVoltage(A) [V] - Cmax='0.2mm'","InducedVoltage(A) [V] - Cmax='0.25mm'","InducedVoltage(A) [V] - Cmax='0.3mm'"
0,-32.3140627749798,-33.7762828932894,-35.6153337490804,-37.2582997744644,-39.3954921803522,-41.1402818992027,-42.9023575704048
0.043,-32.3140627749798,-33.7762828932894,-35.6153337490804,-37.2582997744644,-39.3954921803522,-41.1402818992027,-42.9023575704048
```

在代码目录下执行 `python main.py -i [次数] -f [文件位置]`。
**参数说明 ：**
- `-h` 帮助信息（如上）
- `-i` 分解的第i次值
- `-f` csv 数据文件位置

输出：
```
abs: [FFT分解第i次值的模]
deg: [FFT分解第i次值的角度]
```
且在目录下生成两个文件，`abs.png`和`deg.png`，分别为上面输出数据对应的点图。

### 例子

读取目录下`data.csv`文件，取`FFT分解`的第2次值
``` shell
➜  fft-calc ./venv/bin/python main.py -i 2 -f data.csv
abs: [96.65678352170129, 97.04985593504676, 97.19889131260092, 97.73349092734544, 98.34556572822059, 99.12159518772086, 99.43738614457523]
deg: [110.83101429031922, 110.75258971018361, 110.79728341989707, 110.81272902230863, 110.84119522264129, 110.88773297016189, 110.91663616180655]
```