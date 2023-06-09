# window_size表示平滑处理的窗口大小是指深度或者宽度吗？

在这个函数中，window_size表示平滑处理的窗口大小是指数据点在水平方向上的窗口大小，即宽度方向。因为在这个函数中，输入的数据data是一个一维的列表，没有对数据进行二维分箱，所以这里的窗口大小是指在输入数据中进行滑动的窗口大小，与分箱的深度无关。

# window_size与宽度等价吗？

不一定等价。Window size是指平滑处理的窗口大小，可以是深度或宽度的值，取决于对哪个方向进行平滑处理。在一些情况下，窗口大小可以等于深度或宽度的大小，但不一定总是相等的。

## （1）分箱方法

在分箱前，一定要先排序数据，再将它们分到等深（等宽）的箱中。
常见的有两种分箱方法：等深分箱和等宽分箱。

### 1.等深分箱：

按记录数进行分箱，每箱具有相同的记录数，每箱的记录数称为箱的权重，也称箱子的深度。

### 2.等宽分箱：

在整个属性值的区间上平均分布，即每个箱的区间范围设定为一个常量，称为箱子的宽度。

## （2）数据平滑

将数据划分到不同的箱子之后，可以运用如下三种策略对每个箱子中的数据进行平滑处理：

### 1.平均值平滑：

箱中的每一个值被箱中数值的平均值替换。

### 2.中值平滑：

箱中的每一个值被箱中数值的中值替换。

### 3.边界平滑：

箱中的最大值和最小值称为箱子的边界，箱中的每一个值被最近的边界值替换。

# Numpy读取数据

## numpy.loadtxt()

可以包括一下参数：

| frame     | 文件、字符串或产生器，可以是gz或者bz2压缩文件                |
| --------- | ------------------------------------------------------------ |
| dtype     | 数据类型。csv的字符串以什么数据类型读入数组中，默认float     |
| delimiter | 分隔字符串的符号，默认是空格                                 |
| skiprows  | 跳过前x行，一般跳过第一行表头                                |
| usecols   | 读取指定列、索引，元组类型                                   |
| unpack    | 如果为True，读入属性将分别写入不同数组变量。如果为False，读入数据只写入一个数组变量。默认为False。 |

# 数据处理函数参数

## 输入参数：

- data:需要被处理的数据，是一个一维列表。
- window_size：平滑处理的窗口大小，是一个整数。

## 输出：

- smoothed_data：经过边界平滑处理后的数据，也是一个列表。

# def width_binning(data, width):

## 具体实现如下：

- 这个函数用于将一个序列按照指定的宽度进行分组，返回一个二维列表，其中每个子列表都包含指定宽度的元素。
- 函数的第一个参数 data 是需要被分组的序列。
- 函数的第二个参数 width 是指定的宽度，即每个子列表包含的元素数量。
- 函数首先定义一个空列表 bins，用于存放最终的结果。
- 然后定义一个变量 start，表示当前分组的起始位置。初始值为 0。
- 循环遍历序列 data，每次取出从 start 开始，长度为 width 的一段子序列，并将其作为一个子列表添加到 bins 中。
- 最后更新 start 的值为 start + width，以便进行下一轮循环，直到遍历完整个序列 data。
- 函数返回分组后的结果 bins。

# def depth_binning(data, depth):

## 具体实现如下：

- 这个函数将一个一维列表 data 进行深度分箱（depth binning），即将其按照一定深度 depth 分成多个子列表。
- 将 data 中的元素按照下标从 0 开始每隔 depth 个元素划分成一组，一共划分出 depth 组
- 然后将每组的元素放到对应的子列表中
- 最终，函数返回一个列表，其中包含 depth 个子列表，每个子列表包含了分到同一组的元素。

# def mean_smooth(data, window_size):

## 具体实现如下：

- 对于第一个窗口大小之前的数据点，直接对前面的数据取平均值。
- 对于最后一个窗口大小之后的数据点，直接对后面的数据取平均值。
- 对于其他数据点，取窗口大小范围内的数据点的平均值。
- 其中，对于第一个和最后一个窗口，由于窗口大小无法取满，需要将其平均值进行修正，即分别除以相应的窗口大小。

比如：

原始数据：[123  68  76 161  52  77 226 350 202 341 260 155 120 163 221 133  45 106 50 125  83  66 131 242 127]
请输入宽度：>? 3

宽度分箱后的数据：[array([123,  68,  76]), array([161,  52,  77]), array([226, 350, 202]), array([341, 260, 155]), array([120, 163, 221]), array([133,  45, 106]), array([ 50, 125,  83]), array([ 66, 131, 242]), array([127])]

深度分箱后的数据：[[123, 52, 202, 120, 45, 83, 127], [68, 77, 341, 163, 106, 66], [76, 226, 260, 221, 50, 131], [161, 350, 155, 133, 125, 242]]

代码：

```python
 for i in range(len(data)):
        if i < window_size // 2 or i >= len(data) - window_size // 2: # 3//2=1, 3-1=2

# 这个其实就是判断数据点位于窗口前还是后，比如窗口大小3，宽度为3就是[1，2]，//就是向下# 取整
# 也就是3个值，数据点小于1，大于等于2都不做处理（下标），窗口大小为3就是不对0，2数据点处理即不对边界# 值处理
# 窗口大小//2就是看数据点在不在中间位置（靠前，靠后），窗口大小为3，宽度为9就是[1,8]就是不对0，8数# # 据点处理即不对边界值处理，对于剩下的取平均数
# 所以窗口大小不能随便选，否则会无意义

            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1])/window_size) # 1-1=0,1+2=3
```

​        这个就是基于python划片，3就是[0:3]区间取值，超过的就按前面的算，比如窗口大小为3，宽度3计算：就是在[a,b,c]里取a,b,c，4超过了界限就取不到只能取前三个。
也就是只处理比1大比2小的，也就是边界值并不做处理，对中间值取平均
第一组就是（123+68+76）/3=89 边界不处理，123，89，76
第二组（161+52+77）/3=96.667，边界不处理，161，96.667，77

深度为4的就是：，注意：每次选3个数据点（窗口大小）。部分：（123+52+202）/3=125.6667,(52+202+120)/3=124.667   。。。。。。

以此类推

宽度分箱后的数据进行均值平滑后的数据：[[123, 89.0, 76], [161, 96.66666666666667, 77], [226, 259.3333333333333, 202], [341, 252.0, 155], [120, 168.0, 221], [133, 94.66666666666667, 106], [50, 86.0, 83], [66, 146.33333333333334, 242], [127]]

深度分箱后的数据进行均值平滑后的数据：[[123, 125.66666666666667, 124.66666666666667, 122.33333333333333, 82.66666666666667, 85.0, 127], [68, 162.0, 193.66666666666666, 203.33333333333334, 111.66666666666667, 66], [76, 187.33333333333334, 235.66666666666666, 177.0, 134.0, 131], [161, 222.0, 212.66666666666666, 137.66666666666666, 166.66666666666666, 242]]

# def mean_smoothing(data, window_size):

## 具体来说

该函数首先创建了一个空列表'smoothed_data

- 函数通过遍历数据并使用窗口大小的一半来确定边界条件。
- 如果当前位置在窗口大小的一半之前或之后，那么该位置的数据不需要平滑处理，直接将该值添加到平滑后的数据中。
- 否则，使用平滑窗口内的数据进行平滑处理，并将结果添加到平滑后的数据中。具体来说，对于每个位置i，平滑窗口为从i-window_size//2到i+window_size//2（向下取整）。
- 平滑后的数据将作为返回值返回。
- 该函数使用了一个简单的平均滤波算法，它将窗口内的数据加起来，并除以窗口大小来计算平均值。因为每个位置需要包含自身的值，所以平均值计算时需要将当前位置的数据也加入到窗口内。最后得到的平均值将作为该位置的平滑值。

比如：

原始数据： [123  68  76 161  52  77 226 350 202 341 260 155 120 163 221 133  45 106 50 125  83  66 131 242 127]
请输入宽度：>? 3

宽度分箱后的数据：[array([123,  68,  76]), array([161,  52,  77]), array([226, 350, 202]), array([341, 260, 155]), array([120, 163, 221]), array([133,  45, 106]), array([ 50, 125,  83]), array([ 66, 131, 242]), array([127])]

深度分箱后的数据：[[123, 52, 202, 120, 45, 83, 127], [68, 77, 341, 163, 106, 66], [76, 226, 260, 221, 50, 131], [161, 350, 155, 133, 125, 242]]

代码：

```python
for i in range(len(data)):
    if i < window_size//2 or i >= len(data)-window_size//2: # 3//2=1, 3-1=2
        smoothed_data.append(data[i])
    else:
    smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1]+[data[i]])/(window_size+1)) # 1-1=0,1+2=3
# 窗口大小为3就是不对0，2数据点处理即不对边界值处理，对于剩下的取平均数
# 并且每次求和取值时要加上data[i],取平均值时2是取的窗口值+1
# 如果不在开头或结尾，则算法将计算以目标为中心的值的平均值。这是通过将目标的左侧和右侧的值相加并包括其# # 自身
```

这个就是基于python划片，3就是[0:3]区间取值，超过的就按前面的算，比如窗口大小为3，宽度3计算：就是在[a,b,c]里取a,b,c，4超过了界限就取不到只能取前三个。

也就是只处理比1大比2小的，也就是边界值并不做处理，对中间值取平均，但是这个算法比上面处理时需要在求和取值时要加上data[i],取平均值时，取的窗口值+1，在第一组就是加68，第二组就是加52

但是在这里数据点不够所以要左边加123+68，右边加76+68，自己加68+68

第一组就是（123+68+68+76）/4 =83.75边界不处理，123，83.75，76

第二组（161+52+52+77）/4=85.5，边界不处理，161，85.5，77

以此类推

然后对于深度为4的话，注意：每次选3个数据点（窗口大小）。第一组部分：

第一个就是不在开头或结尾，则算法将计算以目标为中心的值的平均值。这是通过将目标的左侧和右侧的值相加并包括其自身即：（123+52+202+52）/4=107.25，（52+202+120+202）/4=144 。。。。。。

宽度分箱后的数据进行均值平滑后的数据：[[123, 83.75, 76], [161, 85.5, 77], [226, 282.0, 202], [341, 254.0, 155], [120, 166.75, 221], [133, 82.25, 106], [50, 95.75, 83], [66, 142.5, 242], [127]]

深度分箱后的数据进行均值平滑后的数据：[[123, 107.25, 144.0, 121.75, 73.25, 84.5, 127], [68, 140.75, 230.5, 193.25, 110.25, 66], [76, 197.0, 241.75, 188.0, 113.0, 131], [161, 254.0, 198.25, 136.5, 156.25, 242]]



# def median_smooth(data, window_size):

## 具体实现如下：

- 函数首先创建一个空列表smoothed_data来存储平滑后的数据。
- 然后，遍历原始数据data中的每个数据点。
- 如果当前数据点位于整个数据的前一半或后一半，则不进行平滑处理，直接将其加入到smoothed_data中。
- 否则，以当前数据点为中心，选取包含前后window_size个数据点的范围，对这些数据进行排序并取其中位数作为平滑后的值，将其加入到smoothed_data中。
- 最终，函数返回平滑后的数据列表smoothed_data。

比如：原始数据： [123  68  76 161  52  77 226 350 202 341 260 155 120 163 221 133  45 106 50 125  83  66 131 242 127]
请输入宽度：>? 3

宽度分箱后的数据：[array([123,  68,  76]), array([161,  52,  77]), array([226, 350, 202]), array([341, 260, 155]), array([120, 163, 221]), array([133,  45, 106]), array([ 50, 125,  83]), array([ 66, 131, 242]), array([127])]

深度分箱后的数据：[[123, 52, 202, 120, 45, 83, 127], [68, 77, 341, 163, 106, 66], [76, 226, 260, 221, 50, 131], [161, 350, 155, 133, 125, 242]]

代码：

```python
for i in range(len(data)):
    if i < window_size // 2 or i >= len(data) - window_size // 2:
        smoothed_data.append(data[i])
    else:
        smoothed_data.append(sorted(data[i-window_size//2:i+window_size//2+1])[window_size//2])
# 窗口大小为3就是不对0，2数据点处理即不对边界值处理，对于剩下的排序取中值
```

这个就是基于python划片，3就是[0:3]区间取值，超过的就按前面的算，比如窗口大小为3，宽度3计算：就是在[a,b,c]里取a,b,c，4超过了界限就取不到只能取前三个。
也就是只处理比1大比2小的，也就是边界值并不做处理，对三个数据先进行排序（小-->大），即68，76，123，边界值不处理，中间的即1处的值取中值76，
第一组就是123，76，76
第二组排序：52，77，161，边界值不处理，处理后就是161，77，77
以此类推

深度为4的话：

注意：每次选3个数据点（窗口大小）。第一组：部分：

排序：52，123，202，所以第二个位置是123

再排序：52，120，202，所以第三个位置是120

再排序：45，120，202，所以第四个位置是120

。。。。。。

宽度分箱后的数据进行中值平滑后的数据：[[123, 76, 76], [161, 77, 77], [226, 226, 202], [341, 260, 155], [120, 163, 221], [133, 106, 106], [50, 83, 83], [66, 131, 242], [127]]

深度分箱后的数据进行中值平滑后的数据：[[123, 123, 120, 120, 83, 83, 127], [68, 77, 163, 163, 106, 66], [76, 226, 226, 221, 131, 131], [161, 161, 155, 133, 133, 242]]



# def median_smoothing(data, window_size):

## 具体实现如下：

- 函数遍历待处理的数据，对于每个数据点，如果它是在窗口大小的一半之内或者是在最后一段窗口大小的一半之外的数据点，就不进行平滑，直接将该数据点加入到平滑后的序列中；否则，将该数据点及其窗口大小范围内的数据点取出来，排序后取中间的值，即为平滑后的值。

- 代码中的第一个if语句判断当前数据点是否处于第一个窗口大小的一半之内或者最后一个窗口大小的一半之外
- 如果是的话，则直接将该数据点加入到平滑后的序列中。否则，将该数据点及其窗口大小范围内的数据点（窗口大小一半向前和向后）加入到一个列表中
- 使用Python内置的sorted()函数对这些值进行排序，然后取排序后的中间值，即为平滑后的值。最后将平滑后的值添加到平滑后的序列中，返回平滑后的序列。



比如：

原始数据： [123  68  76 161  52  77 226 350 202 341 260 155 120 163 221 133  45 106 50 125  83  66 131 242 127]
请输入宽度：>? 3

宽度分箱后的数据：[array([123,  68,  76]), array([161,  52,  77]), array([226, 350, 202]), array([341, 260, 155]), array([120, 163, 221]), array([133,  45, 106]), array([ 50, 125,  83]), array([ 66, 131, 242]), array([127])]

深度分箱后的数据：[[123, 52, 202, 120, 45, 83, 127], [68, 77, 341, 163, 106, 66], [76, 226, 260, 221, 50, 131], [161, 350, 155, 133, 125, 242]]

代码：

```python
for i in range(len(data)):
    if i < window_size//2 or i >= len(data)-window_size//2:
        smoothed_data.append(data[i])
    else:
        smoothed_data.append(sorted(data[i-window_size//2:i+window_size//2+1]+[data[i]])[window_size//2])
# 窗口大小为3就是不对0，2数据点处理即不对边界值处理，对于剩下的排序取中值
# 并且最后排序时要对需要处理的数据要加上data[i]，然后乘window_size//2
```

这个就是基于python划片，窗口大小3就是[0:3]区间取值，超过的就按前面的算，比如窗口大小为3，宽度3计算：就是在[a,b,c]里取a,b,c，4超过了界限就取不到只能取前三个。
也就是只处理比1大比2小的，也就是边界值并不做处理，但是这个算法比上面处理时需要在每次取值以后加上data[i]，对三个数据先进行排序（小-->大），即68，76，123，边界值不处理，中间的即1处的值取中值再加上data[1]，68+76=144
第一组就是123，144，76，边界不处理
第二组排序：52，77，161，边界值不处理，处理后就是161，77+52=129，77
以此类推

深度为4：

第一部分：部分：

排序：前两个数据太靠前，不进行处理

排序：52，120，202，所以第三个元素是120，

再排序：45，120，202，所以第四个元素是120

。。。。。。

宽度分箱后的数据进行中值平滑后的数据：[[123, 68, 76], [161, 52, 77], [226, 226, 202], [341, 260, 155], [120, 163, 221], [133, 45, 106], [50, 83, 83], [66, 131, 242], [127]]

深度分箱后的数据进行中值平滑后的数据：[[123, 52, 120, 120, 45, 83, 127], [68, 77, 163, 163, 106, 66], [76, 226, 226, 221, 50, 131], [161, 161, 155, 133, 125, 242]]

# def boundary_smooth(data, window_size):

## 具体实现如下：

- 遍历每一个数据点 i。
- 如果 i 小于窗口大小的一半，即 i < window_size // 2，说明左边没有足够的数据点，此时对前 i+window_size//2+1 个数据点求平均值，并将这个平均值作为 i 处的平滑值。
- 如果 i 大于等于数据总数减去窗口大小的一半，即 i >= len(data) - window_size // 2，说明右边没有足够的数据点，此时对 i-window_size//2 到最后一个数据点求平均值，并将这个平均值作为 i 处的平滑值。
- 否则，即数据点 i 处于中间区域，对 i-window_size//2 到 i+window_size//2+1 个数据点求平均值，并将这个平均值作为 i 处的平滑值。
- 返回经过边界平滑处理后的数据 smoothed_data。

比如：

原始数据： [123  68  76 161  52  77 226 350 202 341 260 155 120 163 221 133  45 106 50 125  83  66 131 242 127]
请输入宽度：>? 3

宽度分箱后的数据：[array([123,  68,  76]), array([161,  52,  77]), array([226, 350, 202]), array([341, 260, 155]), array([120, 163, 221]), array([133,  45, 106]), array([ 50, 125,  83]), array([ 66, 131, 242]), array([127])]

深度分箱后的数据：[[123, 52, 202, 120, 45, 83, 127], [68, 77, 341, 163, 106, 66], [76, 226, 260, 221, 50, 131], [161, 350, 155, 133, 125, 242]]

代码：

```python
for i in range(len(data)):
    if i < window_size // 2: # 1
        smoothed_data.append(sum(data[:i+window_size//2+1])/(i+window_size//2+1))
        # 1+1+1=3 :2/2=:1
    elif i >= len(data) - window_size // 2: # 3-1=2
        smoothed_data.append(sum(data[i-window_size//2:])/(len(data)-i+window_size//2)) # 1/2
    else:
        smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1])/window_size)
        # 2/5
# 如果当前元素的下标小于窗口大小的一半，也就是说当前元素前面不够用来计算滑动平均的数据点，那么将当前元# 素之前的所有数据取平均值，作为当前元素的滑动平均值。
# 如果当前元素的下标大于等于数据序列的长度减去窗口大小的一半，也就是说当前元素后面不够用来计算滑动平均# 的数据点，那么将当前元素之后的所有数据取平均值，作为当前元素的滑动平均值。
# 如果当前元素前后都有足够的数据点用来计算滑动平均，那么将当前元素前后窗口大小个数据取平均值，作为当前# 元素的滑动平均值。
```

第一个元素当前元素前面不够用来计算滑动平均的数据点，那么将当前元素之前的所有数据取平均值，作为当前元素的滑动平均值。所以对于下标0，1的元素取均值，即（123+68）/2=95.5，第二个元素前后都有足够的数据点用来计算滑动平均，所以对0，1，2取均值，即（123+68+76）/3=89，第三个元素当前元素后面不够用来计算滑动平均的数据点，那么将当前元素之后的所有数据取平均值，作为当前元素的滑动平均值。所以（68+76）/2=72，

第一组：95.5，89，72

第二组：（161+52）/2=106.5,(161+52+77)/3=96.667,(52+77)/2=64.5

深度为4：

第一部分：部分：数据点充足（123+52）/2=87.5

(123+52+202)/3=125.667

。。。。。。

宽度分箱后的数据进行边界平滑后的数据：[[95.5, 89.0, 72.0], [106.5, 96.66666666666667, 64.5], [288.0, 259.3333333333333, 276.0], [300.5, 252.0, 207.5], [141.5, 168.0, 192.0], [89.0, 94.66666666666667, 75.5], [87.5, 86.0, 104.0], [98.5, 146.33333333333334, 186.5], [63.5]]

深度分箱后的数据进行边界平滑后的数据：[[87.5, 125.66666666666667, 124.66666666666667, 122.33333333333333, 82.66666666666667, 85.0, 105.0], [72.5, 162.0, 193.66666666666666, 203.33333333333334, 111.66666666666667, 86.0], [151.0, 187.33333333333334, 235.66666666666666, 177.0, 134.0, 90.5], [255.5, 222.0, 212.66666666666666, 137.66666666666666, 166.66666666666666, 183.5]]



# def boundary_smoothing(data, window_size):

## 具体实现如下：

- 该函数通过一个循环遍历所有数据点，并对每个数据点进行处理。
- 如果当前数据点在窗口的左边或右边，即距离数据边界不足窗口大小的一半，就不对该数据点进行平滑处理，直接将其添加到输出列表中。
- 如果当前数据点在窗口内部，就计算它周围窗口大小个数据点的平均值，加上当前数据点的值，再除以窗口大小加1，以得到平滑后的值。
- 最后将平滑处理后的值添加到输出列表中。
- 这种处理方式能够有效避免对边界数据进行过度平滑处理，因为边界数据在计算平均值时只需要考虑窗口内的有效数据点，而不需要进行对称填充等处理。

比如：

原始数据： [123  68  76 161  52  77 226 350 202 341 260 155 120 163 221 133  45 106 50 125  83  66 131 242 127]
请输入宽度：>? 3

宽度分箱后的数据：[array([123,  68,  76]), array([161,  52,  77]), array([226, 350, 202]), array([341, 260, 155]), array([120, 163, 221]), array([133,  45, 106]), array([ 50, 125,  83]), array([ 66, 131, 242]), array([127])]

深度分箱后的数据：[[123, 52, 202, 120, 45, 83, 127], [68, 77, 341, 163, 106, 66], [76, 226, 260, 221, 50, 131], [161, 350, 155, 133, 125, 242]]

代码：

```python
for i in range(len(data)):
    if i < window_size//2 or i >= len(data)-window_size//2:
        smoothed_data.append(data[i])
    else:
        smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1]+[data[i]])/(window_size+1))
# 1 2 
# 0:3 + /4
```

只处理比大于等于1比2小的，也就是边界值并不做处理，但是这个算法比上面处理时需要在每次取值以后加上data[i]，在第一组就是加68，第二组就是加52
第一组就是（123+68+68++76）/4 =83.75边界不处理，123，83.75，76
第二组（161+52+52+77）/4=85.5，边界不处理，161，85.5，77
以此类推

深度为4：

第一部分：部分：数据点充足

注意：每次选3个数据点（窗口大小）。第一组部分：

第一个就是不在开头或结尾，则算法将计算以目标为中心的值的平均值。这是通过将目标的左侧和右侧的值相加并包括其自身即：（123+52+202+52）/4=107.25，（52+202+120+202）/4=144 。。。。。。



宽度分箱后的数据进行边界平滑后的数据：[[123, 83.75, 76], [161, 85.5, 77], [226, 282.0, 202], [341, 254.0, 155], [120, 166.75, 221], [133, 82.25, 106], [50, 95.75, 83], [66, 142.5, 242], [127]]

深度分箱后的数据进行边界平滑后的数据：[[123, 107.25, 144.0, 121.75, 73.25, 84.5, 127], [68, 140.75, 230.5, 193.25, 110.25, 66], [76, 197.0, 241.75, 188.0, 113.0, 131], [161, 254.0, 198.25, 136.5, 156.25, 242]]

# def normalize(data):

## 具体实现如下：

- 这个代码定义了一个normalize函数，它用于将给定的一组数据进行归一化处理。
- 函数接受一个参数data，表示需要进行归一化处理的数据。
- 函数首先通过调用min()和max()函数来计算数据中的最小值和最大值，然后对于数据中的每个元素x，将其减去最小值并除以最大值减去最小值，即 (x-min_val)/(max_val-min_val)，得到其在0和1之间的归一化值
- 最后将所有的归一化值构成的列表返回给调用者。

代码：

```python
def normalize(data):
    min_val = min(data) # 45
    max_val = max(data) # 350
    normalized_data = [(x-min_val)/(max_val-min_val) for x in data]
    return normalized_data
```

# 仓库地址：

[cai-04/python-learning: python，数据仓库实验代码 (github.com)](https://github.com/cai-04/python-learning)
