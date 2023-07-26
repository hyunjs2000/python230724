# DemoRE.py
import re

#숫자가 0에서 N번 th
#함정을 추가
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#선택 블록 : ctrl + /
result = re.match("[0-9]*th", "  35th")
print(result)
# print(result.group())

result = re.search("apple", "빅테크에서 apple의 위상")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")
print(result.group())
result = re.search("\d{5}", "우리 동네는 42300")
print(result.group())

print("---대소문자---")
data = "Apple is big company and apple is very delicious"
c = re.compile("apple", re.IGNORECASE)
print(c.findall(data))

print("---다중라인검색---")
data2 = """파이썬을
배워서

누구나 사용"""
#글자가 하나라도 있을 때 => 빈 줄 제외함
c = re.compile("^.+",re.MULTILINE)
print(c.findall(data2))

telChecker = re.compile("(\d{2,3})-(\d{3,4})-(\d{4})")
m = telChecker.match("02-3429-5000")
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
print(m)
