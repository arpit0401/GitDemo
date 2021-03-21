import pytest



@pytest.fixture(scope = "class")
def setup():
      print("i'll be runnign first")
      yield

      print("end")

@pytest.fixture()
def dataload():
      print("this is data loading ")
      return ["name","last name", "email"]

@pytest.fixture(params = [(1,2),(3,4)])
def paramdata(request):
      return request.param