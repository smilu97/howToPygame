### Class
class는 데이터를 묶어서 한번에 처리하거나 편하게 처리하기 위한 것.
객체 지향 프로그래밍이란 프로그램을 이 class로 잘 묶고 캡슐화라는 것을 하는 것을 의미함.
프로그램 흐름을 순서대로 표시하는 절차 지향과는 다르게, 프로그램 흐름을 많은 조각으로 나누어서 각 객체들이 그 조각들을 처리하는
모양으로 만들 수 있음

### python에서 Class정의
--------------------------------
```python
class TestClass :
  def __init__(self) :
      self.value = 0
      self.name = 'Default Name'
  def printer(self) :
      print 'value : ' + str(self.value)
      print 'name  : ' + self.name
```
class안의 Attribute에 접근하려면 클래스 이름이나 변수 이름 뒤에 .(점)을 붙여서 하위 항목을 가리킬 수 있다.
이 경우 self가 자기 자신을 가리키게 되서. self.value는 자신안의 value라는 Attribute를 가리키는 것을 알 수 있다.
우선 클래스의 이름의 경우 보통 첫 글자를 대문자로 하고, 변수의 경우 첫 글자는 소문자로 하는 경우가 많다.
저 TestClass는 생성되는 순간 자동으로 __init__함수를 호출한다. 그래서 자신(self) 안에 value와 name이라는 변수 Attribute를 새로
정의하게 된다.
TestClass는 __init__, printer 2개의 함수를 '가지고'있다. 각 함수에서 self는 자기 자신을 가리키며, 항상 함수 인자의 첫 번째이게 된다.

### Class의 사용
--------------------------------
우리가 정의한 TestClass를 '생성'하는 방법은 이러하다
```python
test = TestClass()
test.name = 'YoungJin'
test.value = 3
test.otherValue = 4
test.printer()
print test.otherValue
```
위 코드는 TestClass를 하나 생성해서 test변수가 가리치게 된다.
TestClass안에서 self.name이라고 가리켰던 변수는 여기에서는 test.name이라고 접근 할 수 있고 test.value의 경우도 마찬가지이다.
이 때, TestClass안에서 정의한 변수가 아니더라도 test.otherValue=4 처럼 새로운 Attribute를 정의하고 사용할 수도 있다.
test.printer()는 TestClass.printer(test)와 같다

### 상속
--------------------------------
```python
class SecondClass(TestClass) :
  def __init__(self) :
    TestClass.__init__(self)
    self.moreValue = 0
  def printer(self) :
    print 'value     : ' + str(self.value)
    print 'moreValue : ' + str(self.moreValue)
    print 'name      : ' + self.name
  def moreFunction(self) :
    print 'Hello I'm Child'
```
위의 SecondClass는 TestClass를 '상속'하고 있다. 이 때 SecondClass를 TestClass의 Child라고 하고, TestClass는 SecondClass의
부모라고 한다.
SecondClass.__init__에서는 TestClass.__init__을 따로 호출해주는 것이 보통이다.
SecondClass는 TestClass의 함수들을 가지고 있다.
이 경우, TestClass와 SecondClass모두 printer라는 함수를 가지고 있는데, 우선적으로 가장 Child한 함수를 호출하게 된다. 즉,
```python
second = SecondClass()
second.printer()
```
와 같은 코드에서 second.printer()는 SecondClass.printer(second)가 된다.
만약, SecondClass가 printer()를 가지고 있지 않았다면, second.printer()는 TestClass.printer(second)가 되었을 것이다.

