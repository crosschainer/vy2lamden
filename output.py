name: public(string[64]) # TODO: is this an acceptable size?
symbol: public(string[32]) # TODO: is this an acceptable size?
decimals: public(uint256)
totalSupply: public(uint256)
balanceOf: public(map(address, uint256))
approvedFunds: map(address, map(address, uint256))
@construct
def seed(_name: string[64], _symbol: string[32], _decimals: uint256, _totalSupply: uint256):
    self.name = _name
    self.symbol = _symbol
    self.decimals = _decimals
    self.totalSupply = _totalSupply
    self.balanceOf[msg.sender] = self.totalSupply
@export
def transfer(_to: address, _value: uint256) -> bool:
    self.balanceOf[msg.sender] -= _value
    self.balanceOf[_to] += _value
    return True
@export
def transferFrom(_from: address, _to: address, _value: uint256) -> bool:
    self.approvedFunds[_from][msg.sender] -= _value
    self.balanceOf[_from] -= _value
    self.balanceOf[_to] += _value
    return True
@export
def approve(_spender: address, _value: uint256) -> bool:
    self.approvedFunds[msg.sender][_spender] = _value
    return True
@export
def allowance(_owner: address, _spender: address) -> uint256:
    return self.approvedFunds[_owner][_spender]