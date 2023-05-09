# 编码规范

&emsp;  为保证项目编码风格一致，本项目全部采用[Google 开源项目风格](https://zh-google-styleguide.readthedocs.io/en/latest/)，为了更好地规范代码仓库，此处根据Google 开源项目风格汇总了一些常用规范。

## Python 编码风格

### 命名规范

&emsp;  函数名、变量名和文件名应该是描述性的, 避免缩写. 特别要避免那些对于项目之外的人有歧义或不熟悉的缩写, 也不要通过省略单词中的字母来进行缩写.

- 模块名: `module_name`; 

- 包名: `package_name`;
-  类名: `ClassName`; 
- 方法名: `method_name`; 
- 异常名: `ExceptionName`; 
- 函数名: `function_name`, `query_proper_noun_for_thing`, `send_acronym_via_https`; 
- 全局常量名: `GLOBAL_CONSTANT_NAME` ; 
- 全局变量名: `global_var_name`;
- 实例名: `instance_var_name`; 
- 函数参数名: `function_parameter_name`; 
- 局部变量名: `local_var_name`.

**需要避免的名称**

1. 只有单个字符的名称, 除了以下特别批准的情况:
   1. 计数器和迭代器 (例如, `i`, `j`, `k`, `v` 等等).
   2. 在 `try/except` 语句中代表异常的 `e`.
   3. 在 `with` 语句中代表文件句柄的 `f`.
   4. 私有的、没有约束 (constrain) 的类型变量 (type variable, 例如 `_T = TypeVar("_T")`, `_P = ParamSpec("_P")`).
2. 包含连字符(`-`) 的包名/模块名.
3. 首尾均为双下划线的名称, 例如 `__double_leading_and_trailing_underscore__` (此类名称是 Python 的保留名称).
4. 包含冒犯性词语的名称.
5. 在不必要的情况下包含变量类型的名称 (例如 `id_to_name_dict`).

**命名规范**

1. “内部(Internal)”这个词表示仅在模块内可用, 或者在类内是保护/私有的.
2. 在一定程度上, 在名称前加单下划线 (`_`) 可以保护模块变量和函数 (格式检查器会对受保护的成员访问操作发出警告).
3. 在实例的变量或方法名称前加双下划线 (`__`, 又名为 dunder) 可以有效地把变量或方法变成类的私有成员 (基于名称修饰 name mangling 机制). 我们不鼓励这种用法, 因为这会严重影响可读性和可测试性, 而且没有 **真正** 实现私有. 建议使用单下划线.

| 类型              | 公有                 | 私有                  |
| ----------------- | -------------------- | --------------------- |
| 包                | `lower_with_under`   |                       |
| 模块              | `lower_with_under`   | `_lower_with_under`   |
| 类                | `CapWords`           | `_CapWords`           |
| 异常              | `CapWords`           |                       |
| 函数              | `lower_with_under()` | `_lower_with_under()` |
| 全局常量/类常量   | `CAPS_WITH_UNDER`    | `_CAPS_WITH_UNDER`    |
| 全局变量/类变量   | `lower_with_under`   | `_lower_with_under`   |
| 实例变量          | `lower_with_under`   | `_lower_with_under`   |
| 方法名            | `lower_with_under()` | `_lower_with_under()` |
| 函数参数/方法参数 | `lower_with_under`   |                       |
| 局部变量          | `lower_with_under`   |                       |

### 主程序

> 使用 Python 时, 提供给 `pydoc` 和单元测试的模块必须是可导入的. 如果一个文件是可执行文件, 该文件的主要功能应该位于 `main()` 函数中. 你的代码必须在执行主程序前检查 `if __name__ == '__main__'` , 这样导入模块时不会执行主程序.

```python
def main():
    ...

if __name__ == '__main__':
    main()
```

## 函数长度

> 函数应该小巧且专一.

我们承认有时长函数也是合理的, 所以不硬性限制函数长度. 若一个函数超过 40 行, 应该考虑在不破坏程序结构的前提下拆分这个函数.