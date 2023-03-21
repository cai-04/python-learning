# 导入需要的库
import numpy as np

# 定义函数：宽度分箱函数
def width_binning(data, width):
    bins = []
    start = 0
    while start < len(data):
        bins.append(data[start:start+width])
        start += width
    return bins

# 定义函数：深度分箱函数
def depth_binning(data, depth):
    bins = []
    for i in range(depth):
        bins.append([data[j] for j in range(i, len(data), depth)])
    return bins

# 定义函数：均值平滑函数（边界处理不够好）
def mean_smooth(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size // 2 or i >= len(data) - window_size // 2: # 3//2=1, 3-1=2
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1])/window_size) # 1-1=0,1+2=3
    return smoothed_data

# 定义函数：均值平滑函数（边界处理更好）
def mean_smoothing(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size//2 or i >= len(data)-window_size//2: # 3//2=1, 3-1=2
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1]+[data[i]])/(window_size+1)) # 1-1=0,1+2=3
    return smoothed_data

# 定义函数：中值平滑函数(边界处理不够好)
def median_smooth(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size // 2 or i >= len(data) - window_size // 2:
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sorted(data[i-window_size//2:i+window_size//2+1])[window_size//2])
    return smoothed_data

# 定义函数：中值平滑函数(边界处理更好)
def median_smoothing(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size//2 or i >= len(data)-window_size//2:
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sorted(data[i-window_size//2:i+window_size//2+1]+[data[i]])[window_size//2])
    return smoothed_data

# 定义函数：边界平滑函数1(边界处理不够好)
def boundary_smooth(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size // 2:
            smoothed_data.append(sum(data[:i+window_size//2+1])/(i+window_size//2+1))
        elif i >= len(data) - window_size // 2:
            smoothed_data.append(sum(data[i-window_size//2:])/(len(data)-i+window_size//2))
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1])/window_size)
    return smoothed_data

# 定义函数：边界平滑函数2(边界处理更好)
def boundary_smoothing(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size//2 or i >= len(data)-window_size//2:
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1]+[data[i]])/(window_size+1))
    return smoothed_data

# 定义函数：数据规范化到【0，1】
def normalize(data):
    min_val = min(data) # 45
    max_val = max(data) # 350
    normalized_data = [(x-min_val)/(max_val-min_val) for x in data]
    return normalized_data

# 输入数据
# data = [123,68,76,161,52,77,226,350,202,341,260,155,120,163,221,133,45,106,50,125,83,66,131,242,127]
# 读入数据
file_name = '1.txt'
data = np.loadtxt(file_name, dtype= 'int32', delimiter=',')
print("原始数据：", data)

# 输入数据
#input_data = input("请输入数据：")
#data = [int(x) for x in input_data.split(',')]
#print("输入的数据：", data)
# 输入宽度、深度
bin_width = int(input("请输入宽度："))
bin_depth = int(input("请输入深度："))

# 对宽度分箱、深度分箱后的数据分别进行均值平滑、中值平滑、边界平滑
width_binned_data = width_binning(data, bin_width)
print("宽度分箱后的数据："+str(width_binned_data))
depth_binned_data = depth_binning(data, bin_depth)
print("深度分箱后的数据："+str(depth_binned_data))
# width_mean_smoothed_data = [mean_smooth(bin, 3) for bin in width_binned_data]
# print("宽度分箱后的数据进行均值平滑后的数据："+str(width_mean_smoothed_data))
width_mean_smoothed_data = [mean_smoothing(bin, 3) for bin in width_binned_data]
print("宽度分箱后的数据进行均值平滑后的数据："+str(width_mean_smoothed_data))
# depth_mean_smoothed_data = [mean_smooth(bin, 3) for bin in depth_binned_data]
# print("深度分箱后的数据进行均值平滑后的数据："+str(depth_mean_smoothed_data))
depth_mean_smoothed_data = [mean_smoothing(bin, 3) for bin in depth_binned_data]
print("深度分箱后的数据进行均值平滑后的数据："+str(depth_mean_smoothed_data))
# width_median_smoothed_data = [median_smooth(bin, 3) for bin in width_binned_data]
# print("宽度分箱后的数据进行中值平滑后的数据："+str(width_median_smoothed_data))
width_median_smoothed_data = [median_smoothing(bin, 3) for bin in width_binned_data]
print("宽度分箱后的数据进行中值平滑后的数据："+str(width_median_smoothed_data))
depth_median_smoothed_data = [median_smooth(bin, 3) for bin in depth_binned_data]
print("深度分箱后的数据进行中值平滑后的数据："+str(depth_median_smoothed_data))
depth_median_smoothed_data = [median_smoothing(bin, 3) for bin in depth_binned_data]
print("深度分箱后的数据进行中值平滑后的数据："+str(depth_median_smoothed_data))
# width_boundary_smoothed_data = [boundary_smooth(bin, 3) for bin in width_binned_data]
# print("宽度分箱后的数据进行边界平滑后的数据："+str(width_boundary_smoothed_data))
width_boundary_smoothed_data = [boundary_smoothing(bin, 3) for bin in width_binned_data]
print("宽度分箱后的数据进行边界平滑后的数据："+str(width_boundary_smoothed_data))
# depth_boundary_smoothed_data = [boundary_smooth(bin, 3) for bin in depth_binned_data]
# print("深度分箱后的数据进行边界平滑后的数据："+str(depth_boundary_smoothed_data))
depth_boundary_smoothed_data = [boundary_smoothing(bin, 3) for bin in depth_binned_data]
print("深度分箱后的数据进行边界平滑后的数据："+str(depth_boundary_smoothed_data))


# 规范化
normalized_data = normalize(data)
print("规范化结果：", normalized_data)
