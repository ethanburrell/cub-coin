# Proof of Rhythm (01/13/2020)
### Ethan Burrell

------

Proof of Rhythm is a blockchain consensus algorithm under development for the
purpose of leader selection in a network of untrusted nodes. It builds on two
powerful examples of "leader election", the Proof of Work (PoW) model presented in Bitcoin's
white paper and Proof of Elapsed Time, a lesser known mechanism proposed by Intel.

PoW as presented in Bitcoin was extremely powerful at the time, it allowed new and easily
validated blocks to be added to a decentralized ledger. However, the process which elected these
blocks was extremely wasteful in terms of resources. As time progressed and the difficulty to discovering
new blocks increased, mining Bitcoin needed a large investment and expensive GPU or ASIC based
machines.

Proof of Elapsed Time (PoET) solves the same problem as the classic Bitcoin puzzle, but
in a much smarter way. Instead of having a complicated hash-puzzle for miners to solve,
it uses Intel CPU's special instructions to prove that a node was the first one to awake
from sleep, electing a new leader to propose new blocks. This is better than generic PoW
in two ways: it greatly reduces the power consumption of a miner, and reduces the price
for a new miner to join the pool and effectively mine. However, there is a downside to
PoET, it requires specialized hardware for a miner to enter. Although the hardware is becoming
more common on consumer and enterprise motherboards, it still is [difficult to set up](https://software.intel.com/en-us/forums/intel-software-guard-extensions-intel-sgx/topic/671285).

Proof of Rhythm is a proposed consensus algorithm that builds on both Proof of Work and
Proof of Elapsed Time, while overcoming the hardware limitations of PoET. Proof of Rhythm
is another way to create a random time waiting algorithm that is verifiable by the block chain.
In PoET this is done by a signing key by the sandboxed. [verify this]. This allows for simple
cryptographic function calls to verify if the miner waited the correct amount of time.

Proof of Rhythm uses a mathematical series to create long periods of the process being asleep,
with small moments of the process becoming awake. There are several tradeoffs here, and some
cryptonomics in play. There are some guarantees that this process must give:
1. The elected node must have actually waited using its function as a rule.
2. The winning node must be selected at random with regards to the period of its series.

Both of these points must be ensured to have this be a secure way to discover new blocks.
If (1) is violated, then malicious actors can fake their waiting times and always win the race.
The second is a way to encourage participation in the network. Unlike normal PoW, the overall cost
of setting up a mining system is extremely small, so there is not major incentive to send the new block to
one user. 

#### Why build upon Proof of Elapsed Time
