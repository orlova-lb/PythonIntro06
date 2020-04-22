# Operator
# арифметические операторы
"""
    +   A + B, 5 + 7, 4.6 + 7.2, 'Hello' + 'World!' = HelloWorld!
    -   A - B, 5 - 7, 4.6 - 7.2
    *   A * B, 5 * 7,   'A' * 5 = 'AAAAA'
    /   10 / 2 = 5, 10 / 3 = 3.33333333333
    //  10 / 2 = 5, 10 / 3 = 3.0
    %   10 % 3 = 1, 3 % 54679856749 = 3, 12345 % 10 = 5
    **  2 ** 3 = 8, 2 ** 3 ** 4 = 2417851639229258349412352
"""

# сравнение
"""
    >       True, False
    <
    >=
    <=
    !=
    ==
"""

# присваивание
"""
    a = 5
    a = a + 5   <===>   a += 5
    a = a - 5   <===>   a -= 5
    a = a * 5   <===>   a *= 5
    a = a / 5   <===>   a /= 5
    a = a // 5   <===>   a //= 5
    a = a % 5   <===>   a %= 5
    a = a ** 5   <===>   a **= 5
    a = a & b  <===> a &= b
    a = a | b  <===> a |= b
    a = a ^ b  <===> a ^= b
    a = a >> b  <===> a >>= b
    a = a << b  <===> a <<= b
"""

# логические
"""
    and     И
    or      ИЛИ
    not     НЕ
    
    A       B       and     or      not A
    True    True    True    True    False
    True    False   False   True    False
    False   True    False   True    True
    False   Fasle   False   False   True
"""

# битовые
"""
    &       И
    |       ИЛИ
    ^       исключающее ИЛИ
    ~       НЕ
    
    A       B       ^
    True    True    False
    True    False   True
    False   True    True
    False   False   False
    
                &       |
    5 = 0101
    7 = 0111
        0101    5       
        0111            7
"""

# сдвиг
"""
    >>
    <<
    
    2 << 2
    0010  ==>  0100  ==> 1000
    
                &
    11010010    
    10000000    00000010 = 2
"""

status = 210    # 11010010
for i in range(8):
    print(status & (1 << i))


# 4 + (6 - 3) * 2 // 4
