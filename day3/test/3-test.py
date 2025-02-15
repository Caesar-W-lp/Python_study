# 作者:李一安
# 2024年12月30日14时16分21秒
# 1713450722@qq.com

# print输出格式控制
# print()输出字符串时会自动换行，如果要在同一行输出多个字符串，可以用end参数指定输出的结尾符，默认是换行符。

for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}\t", end="")

    print("")

