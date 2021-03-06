import pytest

@pytest.mark.nightly
def test_sth():
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

@pytest.mark.daily
def test_anything():
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

@pytest.mark.nightly
def test_sth_bad():
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
