for i in `adb devices|grep 'device$'|awk '{print $1}'`
do
    udid=$i pytest test_xueqiu.py &
done