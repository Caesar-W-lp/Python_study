# 作者:李一安
# 2025年02月10日14时54分59秒
# 1713450722@qq.com

import first_package

# 包中都有一个init文件，这个init文件用于外界访问的权限管理，
# 当外界要调用这个包中的模块时，需要在init文件中写明对外界开放的模块列表

first_package.send_message.send()

txt = first_package.receive_message.receive()

print(txt)