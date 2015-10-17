一、目标

对js escape加密的字符串进行解密

二、使用方法

(1)参数

-e      对输入的字符进行加密
-d      对输入的字符进行解密
-f      以文件的形式打开一个源字符
-o      将结果输出到文件
-h      显示帮助信息

(2)手动输入

当不指定 -f 时为手动输入模式

(3)结果输出

当不指定 -o时，将结果输入到终端

(4)命令格式

python unescape.py -e
python unescape.py -d
python unescape.py -[e|d] -f <file> -o <file>

三、代码说明

代码还有些问题，比如加密时无法完成js escape加密
时间比较紧，以后再更新，因为当下只用到解密而已。

