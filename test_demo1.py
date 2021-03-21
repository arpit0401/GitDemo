
import pytest

from pytestdemo.BaseClass import Baseclass


@pytest.mark.usefixtures("dataload")
class Testdemo2(Baseclass):

      def test_demo1(self, dataload):
            print("hello")
            print(dataload)
            assert 9 == 9
            log = self.test_loggingDemo()
            log.info(dataload)



def test_demo6(paramdata):
      print(paramdata)
