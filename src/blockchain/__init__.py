class Blockchain:
    def __init__(self, genesis, first):
        self.chain = [genesis, first]
        self.length = len(self.chain)

    def add(self, new_block):
        assert new_block.validate_new_block(self.chain[-1]) == True, "New Block is not valid"
        self.chain.append(new_block)
        self.length += 1

    def set_chain(self, new_chain):
        self.chain = new_chain
        self.length = len(new_chain)

    def validate_chain(self):
        if len(self.chain) <= 2:
            return self.chain[1].validate_new_block(self.chain[0])

        last_block = self.chain[0]
        for block in self.chain[1:]:
            if block.validate_new_block(last_block) == False:
                return False
            last_block = block

        return True


    def chain_conflicts(self, other_blockchain):
        """
        return the winning block chain
        """
        #return self.resolve_via_length(other_blockchain)
        new_chain = self.resolve_via_length(other_blockchain)
        if len(new_chain) != self.length:
            self.set_chain(new_chain)

    def resolve_via_length(self, other_blockchain):
        curr_chain_valid = self.validate_chain()
        other_chain_valid = other_blockchain.validate_chain()

        if other_chain_valid and not curr_chain_valid:
            return other_chain_valid
        elif not other_chain_valid and curr_chain_valid:
            return curr_chain_valid
        elif curr_chain_valid and other_chain_valid:
            # both valid, now just select the longest one
            if self.length > other_blockchain.length:
                return self
            else:
                return other_blockchain
