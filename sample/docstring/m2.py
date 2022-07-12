import pytest

@pytest.mark.daily
@pytest.mark.nightly
def test_oth():
   """:reqs: abcd-4,abdc-2

   to jest test

   :suite: nightly
   :init: tutu

   :passcrit: działa

   :desc: jakoś

   :step: krok 1
   :step: krok 2
   :step: krok 3
   """
   assert 1

def test_nothing():
   """
   :reqs: abcd-3

   to jest test

   :init: tutu

   :passcrit: działa

   :desc: jakoś

   :step: krok 1
   :step: krok 2
   :step: krok 3
   """
   assert 2 > 1
