import pytest
@pytest.mark.usefixtures("setup")
class Testclass:
      def test_demo2(self):
            print("demo2")
            assert 0 == 2

      def test_demo3(self):
            assert 23 == 23
            print("demo3")