from Calculator import Operation
#pip install pytest
def test_Calculator():
  #given 
  a=1
  b=2
  ope1 = Operation(a,b)
  
  #When
  expected_sum=a+b
  expected_rest=a-b
  expected_mult=a*b
  expected_div=a/b


  #Then
  assert ope1.sum() == expected_sum
  assert ope1.rest() == expected_rest
  assert ope1.mult() == expected_mult
  assert ope1.div() == expected_div

#python -m pytest